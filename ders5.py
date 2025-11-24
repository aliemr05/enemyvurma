from ursina import *

app = Ursina()
ground = Entity(model = "plane", scale = "200", texture = "grass")
oyuncu = Entity(model = "cube", color = color.azure, x = -2, origin_y = -0.5, z = -8, scale = 2)
bomb = Entity(model = "sphere", color = color.black, x = -2, origin_y = -0.5, z = -8, isactive = False)
menzil = Entity(parent = bomb, model = Circle(64, mode = "lime", radius = 10, thickness = 4), color = color.red, rotation_x = 90, visible = False)
coinlist = []
for i in range(10):
    coin = Entity(model = "sphere", color = color.gold, scale = (0.5, 0.5, 0.1), origin_y = -0.5, x = i *2, y = 0, z = 10+i)
    coinlist.append(coin)
    print(i)
enemylist = []
for i in range(400): 
    enemy = Entity(model = "cube", color = color.red, origin_y = )





EditorCamera() 
Sky()









app.run()

