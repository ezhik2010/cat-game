#pgzero

WIDTH = 1000
HEIGHT = 500

TITLE = "Cat's home"
FPS = 30
fon = Actor('LivingRoom1')
sofa = Actor('sofa1', (280,300))
miska = Actor('miska1',(500,350))
Inmenu = Actor('bonus1', (80,450))
kot = Actor('kotik1)',(600,450))
knopka1 = Actor('bonus', (130,450))
knopka2 = Actor('bonus', (500,450))
knopka3 = Actor('bonus', (870,450))
fon_menu = Actor('menu')
fon_shop = Actor('polka')
rastenie = Actor('rastenie2', (200,180))
rastenie_for_home = Actor('rastenie2', (450,220), size = (70,85))
akvarium = Actor('akvarium', (600,300))
akvarium_for_home = Actor('akvarium', (550,225), size = (100,70))
kogtetochka = Actor('koggtetochka1', (800,150))
kogtetochka_for_home = Actor('koggtetochka1',(700,280))
price1 = Actor('price1', (220,190))
price2 = Actor('price1', (620,310))
price3 = Actor('price1', (820,160))
petshop = Actor('petshop')
kot2 = Actor('kotik2',(820,350))
kot3 = Actor('kotik3',(380,200))
kot4 = Actor('kotik4',(100,20))
kot_for_home2 = Actor('kotik2',(640,300))
kot_for_home3 = Actor('kotik3',(280,300))
kot_for_home4 = Actor('kotik4',(555,170))
sale_kot = Actor('sale1', (100,20))
sale_kot1 = Actor('sale1', (380,200))
sale_kot2 = Actor('sale1', (820,350))
sale1 = Actor('sale1', (200,180))
sale2 = Actor('sale1', (600,300))
sale3 = Actor('sale1', (800,150))
count = 0
purchase = 0
purchase1 = 0
purchase2 = 0
purchase_kot = 0
purchase_kot1 = 0
purchase_kot2 = 0
countstart = 0
countstart1 = 0
mode = 'menu'
def draw():
    if mode == 'game':
        fon.draw()
        kot.draw()
        sofa.draw()
        miska.draw()
        Inmenu.draw()
        screen.draw.text('Меню', center=(80, 450), color="black", fontsize = 20)
        if purchase == 1:
            rastenie_for_home.draw()
        if purchase1 == 1:
            akvarium_for_home.draw()
        if purchase2 == 1:
            kogtetochka_for_home.draw()
        if purchase_kot == 1:
            kot_for_home4.draw()
        if purchase_kot1 == 1:
            kot_for_home3.draw()
        if purchase_kot2 == 1:
            kot_for_home2.draw()
    elif mode == 'menu':
        fon_menu.draw()
        knopka1.draw()
        screen.draw.text('Магазин', center=(130, 450), color="black", fontsize = 26)
        knopka2.draw()
        screen.draw.text('Квартира', center=(500, 450), color="black", fontsize = 26)
        knopka3.draw()
        screen.draw.text('Зоомагазин', center=(870, 450), color="black", fontsize = 26)
    elif  mode == 'shop':
        fon_shop.draw()
        rastenie.draw()
        akvarium.draw()
        kogtetochka.draw()
        price1.draw()
        screen.draw.text('500', center=(225,197), color="black", fontsize = 18)
        screen.draw.text('2 монеты за клик', center=(225,120), color="black", fontsize = 22, background="#FFE4B5")
        price2.draw()
        screen.draw.text('2000', center=(625,317), color="black", fontsize = 16)
        screen.draw.text('5 монет в 2 секунды', center=(625,240), color="black", fontsize = 22, background="#FFE4B5")
        price3.draw()
        screen.draw.text('5000', center=(825,167), color="black", fontsize = 16)
        screen.draw.text('7 монет за клик', center=(825,80), color="black", fontsize = 22, background="#FFE4B5")
        Inmenu.draw()
        screen.draw.text('Меню', center=(80, 450), color="black", fontsize = 20)
        if purchase == 1:
            sale1.draw()
        if purchase1 == 1: 
            sale2.draw()
        if purchase2 == 1: 
            sale3.draw()
    elif mode == 'petshop':
        petshop.draw()
        Inmenu.draw()
        screen.draw.text('Меню', center=(80, 450), color="black", fontsize = 20)
        kot2.draw()
        screen.draw.text('Котик-Единорожек', center=(820,410), color="black", fontsize = 22, background="#F19CBB")
        screen.draw.text('Цена - 29999', center=(820,432), color="black", fontsize = 22, background="#F19CBB")
        kot3.draw()
        screen.draw.text('Котик-Пончик', center=(380,250), color="black", fontsize = 22, background="#BDECB6")
        screen.draw.text('Цена - 19999', center=(380,272), color="black", fontsize = 22, background="#BDECB6")
        kot4.draw()
        screen.draw.text('Котик-Нутелла', center=(100,70), color="black", fontsize = 22, background="#755C48")
        screen.draw.text('Цена - 9999', center=(100,92), color="black", fontsize = 22, background="#755C48")
        if purchase_kot == 1:
            sale_kot.draw()
        if purchase_kot1 == 1: 
            sale_kot1.draw()
        if purchase_kot2 == 1: 
            sale_kot2.draw()
    screen.draw.text(count, center=(950, 30), color="black", fontsize = 20, background = '#F08A5D')    
    
def for_sofa():
    global count
    count += 1 
    
def for_akvarium():
    global count
    count += 5
    
def on_mouse_down(button, pos):
    global mode, count, purchase, purchase1, purchase2, countstart, countstart1,purchase_kot, purchase_kot1, purchase_kot2 
    if mode == 'menu':
        if knopka1.collidepoint(pos):
            mode = 'shop'
        elif knopka2.collidepoint(pos):
            mode = 'game'
        elif knopka3.collidepoint(pos):
            mode = 'petshop' 
    elif mode == 'game':
        if button == mouse.LEFT:
            if sofa.collidepoint(pos) and countstart == 0:
                schedule_interval(for_sofa, 2)
                countstart = 1
            if akvarium_for_home.collidepoint(pos) and countstart1 == 0:
                schedule_interval(for_akvarium, 2)
                countstart1 = 1    
            if miska.collidepoint(pos):
                count += 1
            if purchase == 1 and rastenie_for_home.collidepoint(pos):
                count += 2
            if purchase2 == 1 and kogtetochka_for_home.collidepoint(pos):
                count += 7    
            if Inmenu.collidepoint(pos):
                mode = 'menu'
    elif mode == 'shop':     
            if button == mouse.LEFT:
                if kogtetochka.collidepoint(pos):
                    if count >= 5000:
                        if purchase2 == 0:
                            count -= 5000
                            purchase2 = 1
                if akvarium.collidepoint(pos):
                    if count >= 2000:
                        if purchase1 == 0:
                            count -= 2000
                            purchase1 = 1 
                if rastenie.collidepoint(pos):
                    if count >= 500:
                        if purchase == 0:
                            count -= 500
                            purchase = 1    
                if Inmenu.collidepoint(pos):
                    mode = 'menu'            
    elif mode == 'petshop':  
        if button == mouse.LEFT:
            if kot2.collidepoint(pos):
                if count >= 29999:
                    if purchase_kot2 == 0:
                        count -= 29999
                        purchase_kot2 = 1
            if kot3.collidepoint(pos):
                if count >= 19999:
                    if purchase_kot1 == 0:
                        count -= 19999
                        purchase_kot1 = 1 
            if kot4.collidepoint(pos):
                if count >= 9999:
                    if purchase_kot == 0:
                        count -= 9999
                        purchase_kot = 1    
            if Inmenu.collidepoint(pos):
                mode = 'menu'