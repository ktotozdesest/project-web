from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sec-key'


@app.route('/')
def start():
    param = {}
    param['title'] = 'clicker'
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
