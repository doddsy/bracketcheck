from flask import Flask, render_template, request

app = Flask(__name__)

def bracket_check(input):
    brackets = ['{}']
    while any(x in input for x in brackets):
        for br in brackets:
            input = input.replace(br, '')
    return not input

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return render_template('page.html', output=bracket_check(request.form['content']))
    elif request.method == 'GET':
        return render_template('page.html')
if __name__ == '__main__':
    app.run()
