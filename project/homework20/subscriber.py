from redis_service.base import reddis_client

pubsub = reddis_client.pubsub()
pubsub.subscribe("school")


with open("messages.txt", "a", encoding="utf-8") as f:
    for message in pubsub.listen():
        if message["type"] == "message":
            text = message["data"]
            if "контрольна робота" in text:
                f.write(text + "\n")