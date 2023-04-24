from flask import Flask, url_for, render_template, redirect, request
from flask_oauthlib.client import OAuth
from data import db_session
from data.user import User

application = Flask(__name__)
application.config['SECRET_KEY'] = 'your-secret-key-here'

oauth = OAuth(application)

google = oauth.remote_app(
    'google',
    consumer_key='908445130025-c6evvsigi79m501vgstb6nt4862jkfbu.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email profile'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


def update_db(email, time, speed):
    user = User()
    user.email = email
    user.time = time
    user.speed_of_time = speed
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


@application.route('/<index>/', methods=['POST'])
def save(index):
    print(index)
    return redirect('../game')


@application.route('/')
def start():
    param = {}
    param['title'] = 'clicker'
    '''if oidc.user_loggedin:
        return 'Welcome %s' % oidc.user_getfield('email')'''
    return render_template('start-window.html', **param)


@application.route('/login')
def login():
    '''param = {}
    param['title'] = 'Login'
    param['email'] = oidc.user_getfield('email')
    param['email'] = 'email'
    return render_template('login.html', **param)'''
    return google.authorize(callback=url_for('authorized', _external=True))


@application.route('/game')
def game():
    param = {}
    param['title'] = 'clicker'
    param['products'] = ['fertilizer tier 1', 'fertilizer tier 2', 'fertilizer tier 3', 'over fertilizer']
    return render_template('game.html', **param)


@application.route('/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(request.args['error_reason'],
                                                            request.args['error_description'])
    param = {}
    param['title'] = 'Authorized'
    return render_template('logged-start.html')


@application.route('/rules')
def rules():
    return '''You can WAIT and buy fertilazers to increase speed of time.'''


if __name__ == '__main__':
    db_session.global_init("db/users.db")
    application.run(port=8080, host='127.0.0.1')

