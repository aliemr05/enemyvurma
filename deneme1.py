from ursina import *

app = Ursina()

# Temel nesneler
cube = Entity(model="cube", position=(0,0,0))
sphere1 = Entity(model="sphere", color=color.red, position=(5,0,0))
sphere2 = Entity(model="sphere", color=color.green, position=(-5,0,0))

# Tuğla blokları
brick1 = Entity(model="cube", texture="brick", position=(0,1,0))
brick2 = Entity(model="cube", texture="brick", position=(0,1,1))

# Kamera ve ortam
EditorCamera()
Sky()

# Duvar gibi tuğla dizilimi (5x3 blok)
for x in range(5):
    for y in range(3):
        Entity(model="cube", texture="brick", position=(x, y, -2))

# Z yönünde merdiven (4 basamaklı)
for step in range(4):
    Entity(model="cube", texture="brick", position=(7, step, step))

app.run()
