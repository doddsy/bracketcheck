from flask import Flask, render_template, request

app = Flask(__name__)

def bracket_check(input):
    opening = tuple('{')
    closing = tuple('}')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in input:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return render_template('page.html', output=bracket_check(request.form['content']))
    elif request.method == 'GET':
        return render_template('page.html')
if __name__ == '__main__':
    app.run()
