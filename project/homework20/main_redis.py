from redis_service.base import reddis_client

reddis_client.set("my_favorite_car", "Audi Q7")

reddis_client.setex("my_pet", 2 * 60 * 60, "собака Макс")

products = ["молоко", "яйця", "мука", "цукор"]
reddis_client.rpush("products_list", *products)
reddis_client.expire("products_list", 7 * 24 * 60 * 60)

cake_ingredients = {"flour": 250, "milk": 500}
reddis_client.hset("cake_ingredients", mapping=cake_ingredients)
reddis_client.hset("cake_ingredients", "sugar", 300)
reddis_client.hset("cake_ingredients", "sugar", 500)
reddis_client.delete("cake_ingredients")