from redis_connection import RedisConnection
from settings import REDIS_PORT
from plot import Plot
import json
import numpy as np

class Routes ():

    def __init__(self):
        self.redis = RedisConnection(port=REDIS_PORT)
        self.redis_conn=self.redis.redis_connection
        self.root_key_name = 'route'
        self.ploter = Plot()


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
        bloom = ''.join([str(x) for x in places])+''.join([str(x) for x in times])
        bloom = bloom.replace(" ", "")
        print(bloom)
        if self.bloom_filter(bloom):

            self.redis_conn.hmset(
                self.route_hash_name(route_name),
                {
                    'places': places,
                    'times': times
                }
            )
            return True
        else:
            return False

    def convert_to_list(self, string_array):
        """
        Convert type string array ['A','B'] to list type
        :param string_array: string in array format
        :return: list type
        """
        string_array = string_array.replace("'", "\"")
        return json.loads(string_array)

    def plot_graph_route(self, route_name):

        places=self.get_route_dic(route_name)['places']
        lala=self.convert_to_list(places)
        print(type(['Amsterdam', 'Paris', 'Londres', 'Mexico DF']))
        self.ploter.plot_routes(name=route_name, routes=lala)

    def plot_cities_route(self, route_name):
        places = self.get_route_dic(route_name)['places']
        lala = self.convert_to_list(places)
        self.ploter.plot_city_in_map(name=route_name, routes=lala)

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
        dic = self.redis_conn.hgetall(
            self.route_hash_name(route_name),
        )
        return  dic
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

    def bloom_filter(self, name_string):
        """
        Inserts in a bloom filter new string if it does not exists
        :param name_string: string name
        :return: boolean false (exists) true (not exists)
        """
        commad1 = "BF.EXISTS bloom %s" % name_string
        commad2 = "BF.ADD bloom %s" % name_string
        exists = int(self.redis_conn.execute_command(commad1))
        if not exists:
            self.redis_conn.execute_command(commad2)
        return not exists


rout = Routes()
# rout.insert_new_route('perro', ['San Jose', 'Managua', 'New York'], ['11/13/18', '15/12/18'])
# #print(rout.get_route('lala'))
# # rout.get_all_routes()
# rout.plot_graph_route('perro')
# rout.plot_cities_route('perro')
print(rout.bloom_filter('Hello2222'))