import redis

# parameter password is optional.
conn = redis.Redis(host='localhost', port=6379, db=0)

conn.set('foo', 'bar')
ret = conn.get('foo')
print(ret)
print(type(ret))
