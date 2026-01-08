from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def root():
    if request.method.upper() == 'GET':
        return render_template('home.html')
    else:
        results = None
        string = ''
        pattern = ''
        string = request.form.get('string')
        pattern = request.form.get('pattern')
        try:
            if string.strip() == "" or pattern.strip() == "":
                raise re.error('Empty')
            results = re.findall(pattern, string)
        except re.error:
            results = []
        return render_template('home.html', results=results, string=string, pattern=pattern)


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5001)