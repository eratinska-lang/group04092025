from redis_service.base import reddis_client
import time

while True:
    reddis_client.publish("school", "Нагадування: завтра контрольна робота з фізики")
    time.sleep(10)