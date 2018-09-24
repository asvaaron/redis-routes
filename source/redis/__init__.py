from redis_connection import RedisConnection
from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

# Set my port connection
redis = RedisConnection(
    port=REDIS_PORT,
    host=REDIS_HOST
)
redis.redis_connection.set('foo', 'bar')
print(redis.redis_connection.get('foo'))

redis.redis_connection.hmset("route:lele", {
                                    'hello':['sdas', 'dasdda', 12],
                                    'lala':15,
                                    'caca':18
                                 }
                             )
