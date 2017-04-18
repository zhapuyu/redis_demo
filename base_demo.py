import redis

# parameter password is optional.
conn = redis.Redis(host='localhost', port=6379, db=0)

print('dbsize: {size}'.format(size=conn.dbsize()))
print('ping: {ping}'.format(ping=conn.ping()))

info = conn.info()
print(type(info))
for info_key in info:
    print("key is {key}, value is {value}".format(key=info_key, value=info[info_key]))
