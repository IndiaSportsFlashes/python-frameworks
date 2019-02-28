from flask import Flask
import redis
app = Flask(__name__)
app.debug = True
db = redis.Redis('localhost')


@app.route('/')
@app.route('/live')
def home():
    return db.get('home')

@app.route('/about')
def about():
    return db.get('about') 

if __name__ == '__main__':
    app.run()