from redis_connection import RedisConnection
from settings import REDIS_PORT


class Routes ():

    def __init__(self):
        self.redis = RedisConnection(port=REDIS_PORT)
        self.root_key_name= 'route'


    def insert_new_route(self, route_name, nodes, times):
        self.redis.redis_connection.hmset(self.root_key_name+':'+str(route_name),
                                          {
                                              'node':nodes,
                                              'times':times
                                  }
                              )


rout = Routes()
rout.insert_new_route('lala', ['hello', 'asdas', 'dassd'], ['11/13/18', '15/12/18'])