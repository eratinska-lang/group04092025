import requests

url = "https://cdn.royalcanin-weshare-online.io/hz9p43oBRYZmsWpcq7ap/v1/bp-lot-1-labrador-couleur-outdoor"

response = requests.get(url=url)
print(response.content)

with open("cute_dogs.jpeg", mode="wb") as f:
     content = response.content
     f.write(response.content)
     f.write(response.content)
     f.write(b' hello from Zhenya')

with open("cute_dogs.jpeg", mode="rb") as file:
    file_content = file.read()
    print(file_content)