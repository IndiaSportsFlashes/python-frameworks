import falcon
import json
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""



class HomePage:
    def on_get(self, req, resp):
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        pipe = r.pipeline()
        post_list =  r.lrange("english:homepage",0,-1)
        homepage_body="<html><body><ol>"
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
        resp.media = data

api = falcon.API()
api.add_route('/home', HomePage())