from ursina import *
def input(key): 
    if key == "w": 
        cube.z += 1

    if key == "s":
        cube.z -= 1 

    if key == "a": 
        cube.x -= 1

    if key == "d": 
        cube.x += 1

def update():
    if held_keys["up arrow"]:
        cube.z += 0.1

    if held_keys["down arrow"]:
        cube.z -= 0.1

    if held_keys["right arrow"]:
        cube.x += 0.1

    if held_keys["left arrow"]:
        cube.x -= 0.1
    
    
    carpisma() 

def carpisma(): 
    if distance(cube, oyuncu) < 10: 
        cube.color = color.random_color()
        cube.x = random.randint(-10, 10)
    if distance(cube2, oyuncu) < 10: 
        cube2.color = color.random_color()
        cube2.x = random.randint(-9, 10)
    if distance(cube3, oyuncu) < 10: 
        cube3.color = color.random_color()
        cube3.x = random.randint(-8, 10)    
    if distance(cube4, oyuncu) < 10: 
        cube4.color = color.random_color()
        cube4.x = random.randint(-7, 10)
app = Ursina()
cube = Entity(model = "cube", color = color.brown,  origin_y = -0.5)
ground = Entity(model = "plane", scale = 200, texture = "grass")
sphere = Entity(model = "sphere", color = color.red, origin_x = -2, origin_y = -0.5, origin_z = -8)
cube2 = Entity(model = "cube", color = color.yellow,  origin_x = -3, origin_y = -0.5, origin_z = -2)
cube3 = Entity(model = "cube", color = color.green, origin_x = -6, origin_y = -0.5, origin_z = -4)
cube4 = Entity(model = "cube", color = color.black, origin_x =-8, origin_y = -0.5, origin_z = -6  )
oyuncu = Entity(model = "cube", color = color.blue, origin_x = -10, origin_y = -0.5, origin_z = -12) #oyuncu mavi (player!)
EditorCamera() 
Sky()


app.run()


#3 adet küp 2 3 blok yakin rengi degistir ve baska random bir yere gitsinler 

#mesela ; cube1.x = random.randint(-43) or cube.y or cube.z /ist eig egal!)
