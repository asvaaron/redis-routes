from redis_connection import RedisConnection
from settings import REDIS_PORT


class Routes ():

    def __init__(self):
        self.redis = RedisConnection(port=REDIS_PORT)
        self.root_key_name = 'route'


    def route_hash_name(self, route_name):
        """
        Return string with the route name using prefix
        :param route_name: name of the route
        :return: route name parsed
        """
        return self.root_key_name+':'+str(route_name)


    def insert_new_route(self, route_name, places, times):
        """
        Insert new hash route in redis database
        :param route_name: name of the new route
        :param places: all available places
        :param times: departure time for each place
        """
        self.redis.redis_connection.hmset(
            self.route_hash_name(route_name),
            {
                'places': places,
                'times': times
            }
        )


    def routes_keys_list(self, route_name):
        """
        Return all the key values from a route
        :param route_name:
        :return: key values
        """
        return self.redis.redis_connection.hkeys(
            self.route_hash_name(route_name)
        )


    def get_route(self,route_name):
        """
        Return an python dic with all the key-values
        :param route_name:
        :return: array
        """
        return self.redis.redis_connection.hgetall(
            self.route_hash_name(route_name),
        )

rout = Routes()
rout.insert_new_route('lala', ['hello', 'asdas', 'dassd'], ['11/13/18', '15/12/18'])
print(rout.get_route('lala'))