from ursina import *

app = Ursina()
cube = Entity(model = "cube")
sphere = Entity(model = "sphere", color = color.red, x = 5)
sphere2 = Entity(model = "sphere", color = color.green, x = -5)
brick = Entity(model = "cube", texture = "brick", y = 1)
brick = Entity(model = "cube", texture = "brick", y = 1, z = 1)
EditorCamera() 
Sky()

for x in range(5):
    for y in range(3):
        Entity(model="cube", texture="brick", position=(x, y, -2))

# 4 basamaklı merdiven - z yönünde ilerliyor
for step in range(4):
    Entity(model="cube", texture="brick", position=(7, step, step))



app.run()
