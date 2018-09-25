from redis_connection import RedisConnection
from settings import REDIS_PORT


class Routes ():

    def __init__(self):
        self.redis = RedisConnection(port=REDIS_PORT)
        self.root_key_name= 'route'


    def route_hash_name(self, route_name):
        return self.root_key_name+':'+str(route_name)


    def insert_new_route(self, route_name, places, times):
        self.redis.redis_connection.hmset(
            self.route_hash_name(route_name),
            {
                'places': places,
                'times': times
            }
        )


    def routes_keys_list(self, route_name):
        return self.redis.redis_connection.hkeys(
            self.route_hash_name(route_name)
        )


    def get_route(self,route_name):
        return self.redis.redis_connection.hmget(
            self.route_hash_name(route_name),
            [
                'places',
                'times'
            ]
        )

rout = Routes()
rout.insert_new_route('lala', ['hello', 'asdas', 'dassd'], ['11/13/18', '15/12/18'])
print(rout.routes_keys_list('lala'))