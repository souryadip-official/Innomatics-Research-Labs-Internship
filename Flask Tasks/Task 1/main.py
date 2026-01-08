from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def welcome():
    query = request.args.get('username')
    if query is None:
        return ("Hey, welcome!\n"
            "We couldn't find your name in the query parameter!\n"
            "Pass your name using ?username=<yourname> in the URL\n")
    else:
        hr = datetime.now().hour
        greet = ""
        if hr < 12:
            greet = "Good Morning"
        elif hr < 18:
            greet = "Good Afternoon"
        else:
            greet = "Good Evening"
        return f"{greet} {query.upper()}"


if __name__ == '__main__':
    app.run(debug = True)