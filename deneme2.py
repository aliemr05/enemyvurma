from ursina import *
def input(key): 
    if key == "w": 
        oyuncu.z += 1

    if key == "s":
        oyuncu.z -= 1 

    if key == "a": 
        oyuncu.x -= 1

    if key == "d": 
        oyuncu.x += 1

    if key == "r": 
        for coin in coinlist:
            coin.x = random.randint(-30, 30)
            coin.z = random.randint(-30, 30)


def update():
    if held_keys["up arrow"]:
        oyuncu.z += 0.1

    if held_keys["down arrow"]:
        oyuncu.z -= 0.1

    if held_keys["right arrow"]:
        oyuncu.x += 0.1

    if held_keys["left arrow"]:
        oyuncu.x -= 0.1 

    carpisma() 
   
def carpisma(): 
   
    if distance(cube, oyuncu) < 2:
        cube.color = color.random_color()
        cube.x = random.randint(-9, 10)   
    if distance(cube2, oyuncu) < 2:
        cube2.color = color.random_color()
        cube2.x = random.randint(-9, 10)
    if distance(cube3, oyuncu) < 2: 
        cube3.color = color.random_color()
        cube3.x = random.randint(-8, 10)    
    if distance(cube4, oyuncu) < 2: 
        cube4.color = color.random_color()
        cube4.x = random.randint(-7, 10)



app = Ursina()
cube = Entity(model = "cube", color = color.brown,  origin_y = -0.5)
ground = Entity(model = "plane", scale = 200, texture = "grass")
oyuncu = Entity(model = "sphere", color = color.red, x = -2, origin_y = -0.5, z = -8)
cube2 = Entity(model = "cube", color = color.yellow,  x = -3, origin_y = -0.5, z = -2)
cube3 = Entity(model = "cube", color = color.green, x = -6, origin_y = -0.5, z = -4)
cube4 = Entity(model = "cube", color = color.black, x =-8, origin_y = -0.5, z = -6  )

coinlist = []
for i in range(10):
    coin = Entity(model = "sphere", color = color.gold, scale = (0.5, 0.5, 0.1) , origin_y = -0.5, x = i *2, y = 0, z = 10+i)
    coinlist.append(coin)
    print(i)
EditorCamera() 
Sky()


app.run()

#coin toplama ve küt listesi r ye bastiginda da küpler random yerlere gitsinler !! ödev 







            

   





