import redis
import os
import time

#r = redis.StrictRedis( host=os.environ['REDIS_HOST'], port=6379, db=0)
#r = redis.StrictRedis( host='localhost', port=6379, db=0)
r = redis.StrictRedis( host='localhost', decode_responses=True, port=6379, db=0)

redis_ready = False

#intenta hasta que este listo el contenedor
while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)

print("setup: redis alive")


while True:

    _,color=r.brpop('cola_mayusculas')
    print(color.upper()) 
    r.lpush('upper--cola', color.upper())
    time.sleep(1)