import json

import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

with open('sfpost.json', 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data)

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
r.set("english:homepage:count",0)
for i in data:
    if i["ln"]==1:
        post_slug=str(i["title"]).replace(" ", "_")
        r.set("english:json:post:"+str(i["id"]), post_slug)
        r.set("english:json:post:"+post_slug, i["dis"])
        r.set("english:json:post:"+post_slug+":meta",'{"id":"'+str(i["id"])+'","slug":"'+post_slug+'","title":"'+i["title"]+'","type":"text","meta_description":"'+i["meta_description"]+'","social_feature_img" :"'+i["img_path"]+'"}')
        r.lpush("english:homepage",str(i["id"]))
        r.incr("english:homepage:count")

msg = r.lrange("english:homepage",0,-1)
print(msg)

