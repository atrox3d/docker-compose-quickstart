import time

from flask import Flask
import redis
import redis.exceptions

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379)

def get_hit_count(retries=5):
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as ce:
            if retries == 0:
                raise ce
            retries -= 1
            print('redis connection error, waiting .5 secs...')
            time.sleep(0.5)
            print('retrying')

@app.route('/')
def hello():
    count = get_hit_count()
    return f'{count = }'