from flask import Flask, render_template, redirect, request, flash, session
import pyshorteners
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

# Models
class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable = False)

class URLHistory(db.Model):
    username = db.Column(db.String, db.ForeignKey('user.username'), primary_key = True)
    timestamp = db.Column(db.DateTime, primary_key = True)
    original_url = db.Column(db.String, nullable = False)
    shortened_url = db.Column(db.String, nullable = False)

@app.route('/', methods=['GET'])
def home():
    try:
        if (session['username']):
            return redirect(f'/dashboard/{session['username']}')
    except:
        return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
        return render_template("login.html")
    # Post handling
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    
    user = User.query.filter_by(username = username).first()
    if (not user):
        flash("Invalid credentials!", "danger")
        return redirect('/login')
    if (user.password == password):
        session['username'] = username
        return redirect(f'/dashboard/{username}')
    else:
        flash("Invalid credentials!", "danger")
        return redirect('/login')
    
@app.route('/signup', methods=["GET","POST"])
def signup():
    if (request.method == "GET"):
        return render_template("signup.html")
    # Post handling
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    
    if (len(password) < 8 or len(password) > 16):
        flash("Password must be between 8-16 characters", "info")
        return redirect("/signup")
    
    if (len(username) < 7 or len(username) > 20): # 5-9 would be too short for an username
        flash("Password must be between 8-16 characters", "info")
        return redirect("/signup")
    
    user = User.query.filter_by(username=username).first()
    if user:
        flash("Username already exists", "danger")
        return redirect("/signup")
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    flash("Signup successful! Please login to use our services.", "success")
    return redirect('/login')
    
@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    if 'username' not in session or session['username'] != username:
        flash('Unauthenticated or unauthorized access!', "danger")
        return redirect('/login')
    user = User.query.filter_by(username=username).first()
    if (not user):
        flash('Unauthenticated or unauthorized access!', "danger")
        return redirect('/login')
    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']
        obj = pyshorteners.Shortener()
        short_url = obj.tinyurl.short(original_url)
        new_url = URLHistory(username=username, timestamp = datetime.now(), original_url = original_url, shortened_url = short_url)
        db.session.add(new_url)
        db.session.commit()
        
    return render_template("dashboard.html", username=username, short_url=short_url)

@app.route('/history/<username>', methods=['GET'])
def history(username):
    if 'username' not in session or session['username'] != username:
        flash('Unauthenticated or unauthorized access!', "danger")
        return redirect('/login')
    user = User.query.filter_by(username=username).first()
    if (not user):
        flash('Unauthenticated or unauthorized access!', "danger")
        return redirect('/login')
    urls = URLHistory.query.filter_by(username=username).order_by(URLHistory.timestamp.desc()).all()
    return render_template("history.html", username=username, urls=urls)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect('/login')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)