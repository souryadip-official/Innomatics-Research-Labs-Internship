from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["GET","POST"]) # we need to allow both GET and POST
def index():
    if request.method == 'POST':
        note = request.form.get("note") # We are getting data from form and not from query params
        if note and note.strip(): # So, that empty notes cannot be added
            notes.append(note.strip())
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)