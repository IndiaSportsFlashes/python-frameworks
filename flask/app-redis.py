from flask import Flask
import redis
import json
app = Flask(__name__)
app.debug = True
db = redis.Redis('localhost')

redis_host = "localhost"
redis_port = 6379
redis_password = ""

@app.route('/')
@app.route('/live')
def home():
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    pipe = r.pipeline()
    post_list =  r.lrange("english:homepage",0,-1)
    # homepage_body="<html><body><ol>"
    for post_id in post_list:
        pipe.get("english:json:post:"+post_id)
    post_slug_list = pipe.execute()
    for post_slug in post_slug_list:
        pipe.get("english:json:post:"+post_slug)
        pipe.get("english:json:post:"+post_slug+":meta")
    post_contents = pipe.execute()
    data=[]
    count=0
    for post_content in post_contents:
        if not count%2 == 0:
            data.append(json.loads(post_content))
        else :
            data.append(post_content)
        count=count+1
    return data

@app.route('/about')
def about():
    return db.get('about') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)