"""Basic connection example.
"""

import redis
import config

reddis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

success = reddis_client.set('foo', 'bar')
# True

result = reddis_client.get('foo')
print(result)
# >>> bar


