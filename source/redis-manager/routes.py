from redis_connection import RedisConnection
from settings import REDIS_PORT


class Routes ():

    def __init__(self):
        self.redis = RedisConnection(port=REDIS_PORT)
        self.redis_conn=self.redis.redis_connection
        self.root_key_name = 'route'


    def route_hash_name(self, route_name):
        """
        Return string with the route name using prefix
        :param route_name: string name of the route
        :return: string route name parsed
        """
        return self.root_key_name+':'+str(route_name)


    def insert_new_route(self, route_name, places, times):
        """
        Insert new hash route in redis database
        :param route_name: string name of the new route
        :param places: array strings all available places
        :param times: array strings  departure time for each place
        """
        self.redis_conn.hmset(
            self.route_hash_name(route_name),
            {
                'places': places,
                'times': times
            }
        )


    def routes_keys_list(self, route_name):
        """
        Return all the key values from a route
        :param route_name: string route name
        :return: string array key values
        """
        return self.redis_conn.hkeys(
            self.route_hash_name(route_name)
        )


    def get_route_dic(self,route_name):
        """
        Return an python dic with all the key-values
        :param route_name: string route name
        :return: python route dictionary
        """
        return self.redis_conn.hgetall(
            self.route_hash_name(route_name),
        )

    def get_all_routes(self, filter=None,count=None):
        """
        Return an array with all the routes available
        <p>
        If not filter parameter return all routes
        :param filter:  string route name
        :param count: integer count of returned elements
        :return: keys array
        """
        array = []
        search = None
        if filter is not None:
            search = self.route_hash_name(filter)
        else:
            search = self.route_hash_name('*')
        for key in self.redis_conn.scan_iter(search):
            print(key)
            array.append(key)
        return array


rout = Routes()
#rout.insert_new_route('lala', ['hello', 'asdas', 'dassd'], ['11/13/18', '15/12/18'])
#print(rout.get_route('lala'))
rout.get_all_routes()