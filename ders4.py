from ursina import *

class Particle(Entity): 
    def __init__(self, position, color = color.red):
        super().__init__(
            model = "cube", 
            color = color, 
            position = position, 
            scale = random.uniform(0.1, 0.5) #uniform da ondalik sayilar
        )
        #rastgele yön ve yasam süresi 
        self.velocity = Vec3(random.uniform(-3,3), random.uniform(-3,3 ), random.uniform(-3,3))
        self.lifetime = random.uniform(0.5, 1.5)

    def update(self): 
        self.position += self.velocity * time.dt
        self.lifetime -= time.dt
        if self.lifetime < 0: 
            destroy(self)
#MARK:input
def input(key):
    global timeractive 
    if key == "r": 
        for coin in coinlist:
            coin.x = random.randint(-30, 30)
            coin.z = random.randint(-30, 30)
    if key == "x":
        coin_topla()

  
    if key == "r": 
         invoke(coinler_yerlestirme, delay = 5)
    
    
    if key == "b": 
        bomb.isactive = True
        invoke(enemy_hit, delay = 5)
        kalpsesi.play()

    if key == "m": 
       invoke(merkeze_git, delay = 1)

    if key == "g": 
        bomba_koy()

    if key == "z":
        timeractive = not timeractive  


    if key == "left mouse down" and oyuncu.gun: 
        oyuncu.gun.blink(color.orange)
        bullet = Entity(parent = oyuncu.gun, model = "cube", scale = 0.5, color = color.black)
        mermilist.append(bullet)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position + bullet.forward * 100, duration = 1, curve = curve.linear)
        invoke(bullet_cikar, bullet, delay = 1.9)
        destroy(bullet, 2) #yok etmek

    if key == "t" and distance(oyuncu, gun) < 3:
        get_gun()
    if key == "t" and distance(oyuncu, gun2) < 3:
        get_gun2()
    if key == "t" and distance(oyuncu, gun3) < 3:
        get_gun3()

def düsmani_vurma():
    global puan, giftlist #funksiyondaki degisken degisimi !, disinda tanimlaninca 
    for enemy in enemylist:
        for mermi in mermilist: 
            if distance(mermi, enemy) < 1: 
                puan += 1
                puan_text.text = "puan: " + str(puan)
 #               mermilist.remove(mermi)
                enemy.x = random.randint(-50, 50)
                enemy.z = random.randint(-50, 50)
                for i in range(20):
                        Particle(position = mermi.position, color = color.yellow)
                if enemy.gift == 0:
                    newgift = Entity(model = "Heart", position = mermi.position, color = color.red, tip = "kalp")
                    giftlist.append(newgift)
                if enemy.gift == 1:
                    newgift = Entity(model = "Shield", position = mermi.position, color = color.gray, tip = "kalkan", scale = 0.5)
                    giftlist.append(newgift)

def collect_gift():
    global can, shield_active
    for gift in giftlist: 
        if distance(gift, oyuncu) < 2 and gift.tip == "kalp":
            can += 1
            can_text.text = "can: " + str(can)  
            giftlist.remove(gift)
            destroy(gift)
            return
        elif distance(gift, oyuncu) < 2 and gift.tip == "kalkan": 
            shield_active = True
            giftlist.remove(gift)
            destroy(gift)
            return

def bullet_cikar(bullet):
    mermilist.remove(bullet)

def enemy_hit():                         
    for enemy in enemylist: 
        if distance(enemy, bomb) < 10:
            enemy.position -= enemy.forward * 50
    bomb.isactive = False

def bomba_koy(): 
    bomb.isactive = True #bombayi aktif etmek
timer = 0
timeractive = True 
def handle_timer(): 
    global timer, timeractive
    if timeractive: 
        timer += 1
    invoke(handle_timer, delay = 1) 
    timer_text.text = "time:" + str(timer)
# MARK: UPDATE
def update():

    move = (held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s'])
    if move != (0,0,0): # != anlami esit degildir!
        oyuncu.rotation_y = math.degrees(math.atan2(move[0], move[2]))
    oyuncu.position += Vec3(*move) * time.dt * oyuncu.speed/2
    camera.position = oyuncu.position + Vec3(0, 20, -40)
    camera.look_at(oyuncu.position)

    carpisma() 
    enemy_move()
    coin_topla()
    düsmani_vurma()
    collect_gift()

    if bomb.isactive == False:
        bomb.position = oyuncu.position
        menzil.visible = False
    if bomb.isactive == True: 
        menzil.visible = True 
    if mouse.world_point:
        oyuncu.look_at_xz(mouse.world_point)


def coinler_yerlestirme(): 
    for coin in coinlist: 
        coin.x = random.randint(-30, 30)
        coin.z = random.randint(-30, 30)

def coin_topla(): 
    for coin in coinlist: 
        if distance(coin, oyuncu) < 1:
            coinsesi.play()
            coin.x = random.randint(-30, 30)
            coin.z = random.randint(-30, 30)

def coinleri_mavi_yap():
    for coin in coinlist: 
        coin.color = color.blue 

def merkeze_git(): 
    oyuncu.position = Vec3(0)
    

def boya(): 
    for enemy in enemylist: 
        enemy.color = color.lime 

def carpisma(): 
    global can
    for enemy in enemylist: 
        if distance(enemy, oyuncu) < 1:
            can -= 1
            can_text.text = "can: " + str(can)
            enemy.color = color.random_color()
            enemy.x = random.randint(-9, 10) 
            oyuncu.position = Vec3(0)  

def enemy_move(): 
    for enemy in enemylist:
        enemy.position += enemy.forward * 10 * time.dt
        if distance(enemy, oyuncu) > 100: 
            
            enemy.look_at(oyuncu) 

def bomba_koy():
    yeni_bomba = Entity(
        model="sphere",
        color=color.black,
        scale=0.5,
        position=oyuncu.position + Vec3(0, 1, 0), 
        collider="box"
    )
    yeni_bomba.world_parent = scene
    yeni_bomba.animate_position(yeni_bomba.position + oyuncu.forward * 10, duration=1)
    destroy(yeni_bomba, delay = 1.1)

def enemy_hit_bomba(bomba):
    for enemy in enemylist:
        if distance(enemy, bomba) < 5:
            enemy.position -= enemy.forward * 20


#MARK: APP
app = Ursina()
ground = Entity(model = "plane", scale = 200, texture = "grass", collider = "box")
oyuncu = Entity(model = "cube", color = color.azure, x = -2, origin_y = -0.5, z = -8, scale_y = 2, speed = 8)
bomb = Entity(model = "sphere",color = color.black, x = -2, origin_y = -0.5, z = -8, isactive = False )
menzil = Entity(parent = bomb, model = Circle(64,  mode = "line", radius = 10, thickness = 4), color = color.red, rotation_x = 90, visible = False) 
coinlist = []
for i in range(1):
    coin = Entity(model = "sphere", color = color.gold, scale = (0.5, 0.5, 0.1) , origin_y = -0.5, x = i *2, y = 0, z = 20+i)
    coinlist.append(coin)
    print(i)
enemylist = []
for i in range(10):
    enemy = Entity(model = "cube", color = color.red, origin_y = -0.5, x = random.randint(-100, 100), z = random.randint(-100, 100))
    enemy.gift = random.randint(0, 3)
    enemylist.append(enemy)
mermilist = []


sahne_küpü = Entity(model = "cube", texture = "brick", scale = (2, 10, 2), x=5, y=5, z=5)
menzil2 = Entity(parent = bomb, model = Circle(64, mode = "line", radius = 10, thickness = 4), color = color.red, rotation_x = 90, visible = False)

# sesler = 
kalpsesi = Audio("heart.wav", autoplay = False, loop = True)
patlamasesi = Audio("explosion.wav", autoplay = False, loop = False)
coinsesi = Audio("coin.wav", autoplay = False, loop = False )
giftlist = []

#EditorCamera() 
Sky()

#silah 
oyuncu.gun = None
gun = Button(parent = scene, model = "cube", color = color.black, origin_y = -0.5, z = 10, collider = "box", scale = (.2,.2,0.5))
gun2 = duplicate(gun, x = 10, z = 10, color = color.gray)
gun3 = duplicate(gun, x = 15, z = 15, color = color.black)


def get_gun(): 
    if oyuncu.gun != None:
        oyuncu.gun.parent = scene
        oyuncu.gun.position = oyuncu.forward * 5
    
    gun.parent = oyuncu
    gun.position = Vec3(0, 0.3, .7)
    oyuncu.gun = gun

def get_gun2(): 
    if oyuncu.gun != None:
        oyuncu.gun.parent = scene
        oyuncu.gun.position = oyuncu.forward * 5
        
    gun2.parent = oyuncu
    gun2.position = Vec3(0, 0.3, .7)
    oyuncu.gun = gun2

def get_gun3():
    if oyuncu.gun != None:
        oyuncu.gun.parent = scene 
        oyuncu.gun.position = oyuncu.forward * 5

    gun3.parent = oyuncu
    gun3.position = Vec3(0, 0.3, .7)
    oyuncu.gun = gun3

gun._on_click = get_gun
gun2._on_click = get_gun2
gun3._on_click = get_gun3

puan = 0 
puan_text = Text("puan: " + str(puan), position = (-0.8, 0.45), color = color.black)
can = 10 
can_text = Text("can : " + str(can), position = (-0.8, 0.40), color = color.black)
timer_text = Text("timer : " + str(timer), position = (-0.4, 0.40), color = color.black)
handle_timer()
app.run() 


#kordinatlar .5, 0, .5
 #coinler gecikmeli 5 saniye bir sekilde random yerlere gidicekler tusa bastigimda
 #toplanan coin 3 saniye sonra maviye dönsün 
 # #ayarladigimiz tus oyuncuyu 10 saniye sonra merkeze getirsin x = 0, y = 0
 #sahneye küp koyalim texture brick olsun 10 yari capinda bir menzil ! (boyutu uzun), parent ile yapalim 
 #haftaya bomba sesi !
 #coin i topladigimizda collect sesi yapalim unutma digerleri gibi önce ekleyelim ondan sonra da sesler yerine ekliyelim (derste yaptiklarini tekrarla!)
 #haftaya ki konumuz silah toplamak !
 #gun ile oynayalim daha iyi pozisyona getirelim!
 #yeni gun3 yapalim kendimiz pekistirmek icin forward i degitirip backward veya up yapalriiz pratik yapalim !
 #g harfini basinca bomba atalim (oyuncuyu kullanalim), bullet mantigini kullanalim !
 #tuslari güncellemek haftaya yapilcak! (hatirlatma)
 #enemy patlatma hatirlatma !
 #kamera acisi ayarlama !!
 #ödev ! shield ekleme if enemygift = 1 
 #github hesabi acmak ve git yükleme !
 #zaman jokeri indirelim ödev! (poly pizza)
 