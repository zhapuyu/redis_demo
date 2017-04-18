import redis

# parameter password is optional.
conn = redis.Redis(host='localhost', port=6379, db=0)
conn.sadd('set_key_0', 'a')




