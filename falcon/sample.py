import falcon
#import redis

#redis_host = "localhost"
#redis_port = 6379
#redis_password = ""



class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        #r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        #r.set("msg:hello", "Hello Redis!!!")
        #msg = r.get("msg:hello")
        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())