from flask import Flask

app = Flask(__name__)

@app.route('/helloFlask')
def helloFlask():
    return '<h1>Hello Flask!</h1>'

@app.route('/hello/Allen')
def hello1():
    return 'Hello Allen'

@app.route('/hello/Jack')
def hello2():
    return 'Hello Jack'


@app.route('/hello/<username>')
def hello(username):
    return 'Hello {}'.format(username)

@app.route('/add/<x>/<y>')
def add(x, y):
    return '{}'.format(int(x) + int(y))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)