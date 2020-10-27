#!/usr/bin/env python3
from luxand import luxand

client = luxand("560e70ecf705457196e9c80d3d0ff67f")

client.add_person(name = "Angelina Jolie", photos = ["https://dashboard.luxand.cloud/img/angelina-jolie.jpg"])
client.add_person(name = "Brad Pitt", photos = ["https://dashboard.luxand.cloud/img/brad-pitt.jpg"])

result = client.recognize(photo = "https://dashboard.luxand.cloud/img/angelina-and-brad.jpg")

print(result)