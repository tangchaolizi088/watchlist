from flask import Flask
from flask import escape,url_for
app = Flask(__name__)

@app.route('/user/<name>')
@app.route('/')
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % escape(name)



@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name = 'greyLi'))
    return 'Test Page'




if __name__ == '__main__':
    app.run()