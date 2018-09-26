import redis


class RedisConnection:

    # Default port: 6378
    # Default host: localhost
    # Default db: 0
    def __init__(self, host='127.0.0.1', db=0, port=6378):
        """
        Create an Redis Connection and prints any possible exception

        :param host: Redis host
        :param db: Redis database namespace
        :param port: Redis port
        """
        """Configure Redis database connection """
        try:
            self.redis_connection = redis.StrictRedis(
                host=host,
                port=port,
                db=db,
                charset="utf-8",
                decode_responses=True
            )
        except IOError as e:
            print
            "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ConnectionError:
            print
            "Could not convert data to an integer."


# # Set my port connection
# redis = RedisConnection(port=6379)
# redis.redis_connection.set('foo', 'bar')
# print(redis.redis_connection.get('foo'))
#
# redis.redis_connection.hmset("route:lele", {
#                                     'hello':['sdas','dasdda'],
#                                     'lala':15,
#                                     'caca':18
#                                  }
#                              )
# #
#
# # Block  List
# for i in range(0, 10):
#     print(redis.redis_connection.brpop({'comments'}, timeout=100))