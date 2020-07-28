import time
import random
import pygame
import sys
import sqlite3
from tkinter import *
import tkinter.messagebox

baglanti=sqlite3.connect("meydanMuho.db")
imlec=baglanti.cursor()
imlec.execute("create table if not exists meydanMuho (Ad TEXT,Zaman INT)")

pygame.init()

ekran_en=1200
ekran_boy=700
boyut=(ekran_en,ekran_boy)
pencere=pygame.display.set_mode(boyut)

pygame.display.set_caption("SuperWarrior")
ekran=Tk()

ekran_en2 = 1200
ekran_boy2 = 700
boyut2 = (ekran_en2, ekran_boy2)
pencere2 = pygame.display.set_mode(boyut2)

black=(0,0,0)
chocalate=(210,105,30)
white=(255,255,255)
green=(0,128,0)
red=(255,0,0)
blue=(0,0,255)
aqua=(0,255,255)
yellow=(255,255,0)
purple=(255,0,255)
orange=(255,165,0)
lime=(0,255,0)
gold=(255,215,0)
salmon=(250,128,114)
deepPink=(255,0,127)
brown=(204,102,0)

icon=pygame.image.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\icon.png')
pygame.display.set_icon(icon)

class yazilar():
    size =50
    message="Mesaj"
    color=white
    x=0
    y=0
    def introYazisi(self,message,color,x,y,size):
        self.message=message
        self.color=color
        self.x=x
        self.y=y
        self.size = size
        fontIntro = pygame.font.SysFont(None, size)
        yazi=fontIntro.render(message,True,color)
        pencere.blit(yazi,[x,y])
    def butonYazisi(self,msg,color,x,y,size):
        self.message=msg
        self.color=color
        self.x=x
        self.y=y
        self.size=size
        fontButton=pygame.font.SysFont(None,size)
        butonYazisi=fontButton.render(msg,True,color)
        pencere.blit(butonYazisi,[x,y])
    def oyunYazilari(self,msg,color,x,y,size):
        self.message = msg
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        fontOyun = pygame.font.SysFont(None, size)
        oyunYazisi = fontOyun.render(msg, True, color)
        pencere2.blit(oyunYazisi, [x, y])


class Rules():
    def rules(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pencere.fill(white)
            # Buttons:
            pygame.draw.rect(pencere, green, (200, 550, 210, 80))
            pygame.draw.rect(pencere,black,(550,550,210,80))
            pygame.draw.rect(pencere, red, (850, 550, 210, 80))

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 200 + 210 > mousePosition[0] > 200 and 550 + 80 > mousePosition[1] > 550:
                pygame.draw.rect(pencere, lime, (200, 550, 210, 80))
                if click[0] == 1:
                    game = oyun()
                    game.oyun()
            else:
                pygame.draw.rect(pencere, green, (200, 550, 210, 80))

            if 850 + 210 > mousePosition[0] > 850 and 550 + 80 > mousePosition[1] > 550:
                pygame.draw.rect(pencere, salmon, (850, 550, 210, 80))
                if click[0] == 1:
                    quit()
            else:
                pygame.draw.rect(pencere, red, (850, 550, 210, 80))

            if 550 + 210 > mousePosition[0] > 550 and 550 + 80 > mousePosition[1] > 550:
                pygame.draw.rect(pencere, chocalate, (550, 550, 210, 80))
                if click[0] == 1:
                    intro = Intro()
                    intro.giris_ekrani()
            else:
                pygame.draw.rect(pencere, black, (550, 550, 210, 80))

            yazi_yaz=yazilar()
            yazi_yaz.butonYazisi("BAŞLA", black, 245, 575, 50)
            yazi_yaz.butonYazisi("ÇIKIŞ", black, 910, 575, 50)
            yazi_yaz.butonYazisi("MENÜ",white,600,575,50)

            baslik="KURALLAR"
            kural1="1- SEÇİLEN KARAKTERİMİZ DÜŞMAN ÜSSÜNE KADAR GELEN CANAVARLARLA SAVAŞIR"
            kural1_1="HER ÖLDÜRDÜĞÜ DÜŞMAN ASKERİNDEN BELİRLİ BİR MİKTAR PARA KAZANIR."
            kural2="2- KAZANILAN PARA İLE KAHRAMINIMIZIN ÖZELLİKLERİ GELİŞTİRİLEBİLİR."
            kural3="3- DÜŞMANLARIN ELİNDEN PRENSESİ KURTARDIĞIMIZ DA OYUN SONLANIR."
            kural4="Tuşlar: W-A-S-D-SPACE"

            text=yazilar()
            text.introYazisi(baslik,red,400,20,100)
            text.introYazisi(kural1,purple,10,170,35)
            text.introYazisi(kural1_1,purple,10,210,35)
            text.introYazisi(kural2,purple,10,290,35)
            text.introYazisi(kural3,purple,10,370,35)
            text.introYazisi(kural4,orange,350,440,50)
            pygame.display.update()


class scores():
    def kayit(self,Ad,Zaman):
        imlec.execute("insert into meydanMuho values (?,?)",(Ad,Zaman))
        baglanti.commit()
    def score(self):
        imlec.execute("select * From meydanMuho")
        veriler = imlec.fetchall()
        for i in veriler:
            veri=Label(text=i)
            veri.pack()
            ekran.geometry("200x500")
        ekran.mainloop()
class Intro():
    giris_muzigi=""
    giris_resmi=""
    user_text=""
    def giris_ekrani(self,user_text=""):
        self.user_text=user_text
        input_rect=pygame.Rect(440,610,400,32)
        font=pygame.font.SysFont(None,30)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        user_text=user_text[:-1]
                    else:
                        user_text+=event.unicode

            pencere.fill(black)

            self.giris_muzigi = pygame.mixer.music.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Müzikler\avengers_music.mp3')
            pygame.mixer.music.play(0)

            textSurface = font.render(user_text, True, aqua)
            pencere.blit(textSurface, [444, 618])
            yazi_yaz = yazilar()
            text="B10 İYİ OYUNLAR DİLER..."
            yazi_yaz.introYazisi(text,yellow,285,50,70)
            yazi_yaz.introYazisi("Nickname: ",white,280,610,40)

            #Buttons:
            pygame.draw.rect(pencere,green,(40,200,210,80))
            pygame.draw.rect(pencere, orange, (40, 400, 210, 80))
            pygame.draw.rect(pencere, blue, (970, 200, 210, 80))
            pygame.draw.rect(pencere, yellow, (970, 400, 210, 80))
            pygame.draw.rect(pencere, red, (1050, 640, 170, 60))
            pygame.draw.rect(pencere,white,input_rect,2)

            mousePosition = pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            #print(mousePosition)
            if 40 + 210 > mousePosition[0] > 40 and 200 + 80 > mousePosition[1] > 200:
                pygame.draw.rect(pencere, lime, (40, 200, 210, 80))
                if click[0]==1:
                    #print("Başla")
                    game=oyun()
                    game.oyun()
            else:
                pygame.draw.rect(pencere, green, (40, 200, 210, 80))
            if 40+210>mousePosition[0]>40 and 400+80 >mousePosition[1] >400:
                pygame.draw.rect(pencere, gold, (40, 400, 210, 80))
                if click[0]==1:
                    #print("Kurallar")
                    rule=Rules()
                    rule.rules()
            else:
                pygame.draw.rect(pencere, orange, (40, 400, 210, 80))
            if 970+210 > mousePosition[0] >970 and 200+80>mousePosition[1]>200:
                pygame.draw.rect(pencere, aqua, (970, 200, 210, 80))
                if click[0]==1:
                    score=scores()
                    score.score()
            else:
                pygame.draw.rect(pencere, blue, (970, 200, 210, 80))
            if 1050+170 >mousePosition[0]>1050 and 640+60>mousePosition[1]>640:
                pygame.draw.rect(pencere, salmon, (1050, 640, 170, 60))
                if click[0]==1:
                    quit()
            else:
                pygame.draw.rect(pencere, red, (1050, 640, 170, 60))

            if 970 + 210 > mousePosition[0] > 970 and 400 + 80 > mousePosition[1] > 400:
                pygame.draw.rect(pencere,white, (970, 400, 210, 80))
                if click[0] == 1:
                    tkinter.messagebox.showinfo("HAKKINDA","BU OYUNUN YAZILIMI VE TASARIMI BERTUĞ İLK TARAFINDAN YAPILMIŞTIR...")
                    ekran.mainloop()
            else:
                pygame.draw.rect(pencere, yellow, (970, 400, 210, 80))

            yazi_yaz.butonYazisi("BAŞLA",white,87,225,50)
            yazi_yaz.butonYazisi("KURALLAR",black,45,425,50)
            yazi_yaz.butonYazisi("SKORLAR",white,990,225,50)
            yazi_yaz.butonYazisi("ÇIKIŞ", black, 1080, 650, 50)
            yazi_yaz.butonYazisi("HAKKINDA",black,980,430,50)
            self.giris_resmi=pygame.image.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\war1.jpg')
            pencere.blit(self.giris_resmi,(280,160))
            pygame.display.update()

#------------------------------------ KARAKTER HAREKETLERİ ------------------------------------:
class WalkSprite(pygame.sprite.Sprite):
    def __init__(self,characterX,characterY):

        super(WalkSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\wlk\Walk10.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(characterX, characterY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0
                self.is_move=False
            self.image = self.images[self.index]


class RunSprite(pygame.sprite.Sprite):
    def __init__(self,characterX,characterY):

        super(RunSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Run\Run10.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(characterX, characterY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index +=0.5

            if self.index >= len(self.images):
                self.index = 0
                self.is_move=False
            self.image = self.images[int(self.index)]


class AttackSprite(pygame.sprite.Sprite):
    def __init__(self,characterX,characterY):

        super(AttackSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Attack\Attack10.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(characterX, characterY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 0.5

            if self.index >= len(self.images):
                self.index = 0
                self.is_move=False
            self.image = self.images[int(self.index)]

class IdleSprite(pygame.sprite.Sprite):
    def __init__(self,characterX,characterY):

        super(IdleSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Idle\Idle10.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(characterX, characterY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]


class deadSprite(pygame.sprite.Sprite):
    def __init__(self,characterX,characterY):

        super(deadSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Dead\Dead10.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(characterX, characterY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]

# ------------------------------ ZOMBİ HAREKETLERİ ----------------------------------:
class ZombiWalkRSprite(pygame.sprite.Sprite):
    def __init__(self,zombiX,zombiY):

        super(ZombiWalkRSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walkR\walk10.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(zombiX,zombiY, 150, 198)

    def moving(self):
        self.is_move=True
        self.rect.x+=3
    def update(self):
        if self.is_move==True:
            self.index += 0.7

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[int(self.index)]


class ZombiWalkSprite(pygame.sprite.Sprite):
    def __init__(self,zombiX,zombiY):

        super(ZombiWalkSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\walk\walk10.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(zombiX,zombiY, 150, 198)

    def moving(self):
        self.is_move=True
        self.rect.x-=3
    def update(self):
        if self.is_move==True:
            self.index += 0.7

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[int(self.index)]


class ZombiAttackSprite(pygame.sprite.Sprite):
    def __init__(self,zombiX,zombiY):

        super(ZombiAttackSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\attack\Attack8.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(zombiX,zombiY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[int(self.index)]


class ZombiDeadSprite(pygame.sprite.Sprite):
    def __init__(self,zombiX,zombiY):

        super(ZombiDeadSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead10.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead11.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Zombi\dead\Dead12.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(zombiX,zombiY, 150, 198)

    def moving(self):
        self.is_move=True
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[int(self.index)]


class PrensesSprite(pygame.sprite.Sprite):
    def __init__(self,zombiX,zombiY):

        super(PrensesSprite, self).__init__()
        self.images = []
        self.is_move=False
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run1.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run2.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run3.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run4.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run5.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run6.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run7.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run8.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run9.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run10.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run11.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run12.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run13.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run14.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run15.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run16.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run17.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run18.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run19.png"))
        self.images.append(pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\Prenses\Run20.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(zombiX,zombiY, 150, 198)

    def moving(self):
        self.is_move=True
        self.rect.x-=5
    def update(self):
        if self.is_move==True:
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[int(self.index)]


class Background(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\background_Images\arkaplan6.jpg").convert()
        self.rect = self.image.get_rect()
        self._layer = -10
        pygame.sprite.Sprite.__init__(self, *args)
        self.moved = 0
        self.number = number
        self.rect.x = self.rect.width * self.number

    def update(self):
        self.rect.move_ip(-1, 0)
        self.moved += 1

        if self.moved >= self.rect.width:
            self.rect.x = self.rect.width * self.number
            self.moved = 0

class Background2(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\background_Images\arkaplan3.jpg").convert()
        self.rect = self.image.get_rect()
        self._layer = -10
        pygame.sprite.Sprite.__init__(self, *args)
        self.moved = 0
        self.number = number
        self.rect.x = self.rect.width * self.number

    def update(self):
        self.rect.move_ip(-1, 0)
        self.moved += 1

        if self.moved >= self.rect.width:
            self.rect.x = self.rect.width * self.number
            self.moved = 0


class Background3(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\background_Images\arkaplan4.jpg").convert()
        self.rect = self.image.get_rect()
        self._layer = -10
        pygame.sprite.Sprite.__init__(self, *args)
        self.moved = 0
        self.number = number
        self.rect.x = self.rect.width * self.number

    def update(self):
        self.rect.move_ip(-1, 0)
        self.moved += 1

        if self.moved >= self.rect.width:
            self.rect.x = self.rect.width * self.number
            self.moved = 0

#group = pygame.sprite.LayeredUpdates()
#Background(0, group)
#Background(1, group)
#group.update()
#group.draw(pencere)
#pygame.display.flip()

class oyun():
    def pause(self):
        Time=pygame.time.Clock()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key==pygame.K_m:
                        intro.giris_ekrani()
            pencere2.fill(black)
            txt = yazilar()
            txt.oyunYazilari("- PAUSE -", deepPink, 280, 100, 200)
            txt.oyunYazilari(". SPACE TO CONTINUE", red, 300, 350, 70)
            txt.oyunYazilari(". M TO MENU", red, 300, 450, 70)
            txt.oyunYazilari(". Q TO EXIT", red, 300, 550, 70)
            pygame.display.update()
            Time.tick(5)

    def oyun(self):

        fps=15
        skor=0
        money=0
        level=1
        ekran_en2 = 1100
        ekran_boy2 = 700
        boyut2 = (ekran_en2, ekran_boy2)
        pencere2 = pygame.display.set_mode(boyut2)
        pygame.display.set_caption("SUPER WARRIOR")

        self.Zaman=100
        score=scores()
        intro=Intro()
        Ad=intro.user_text
        Zaman=100
        score.kayit(Ad,Zaman)

        #character animation:
        karakterX=100
        karakterY=580

        walk_sprite = WalkSprite(karakterX, karakterY)
        walk_group = pygame.sprite.Group(walk_sprite)

        run_sprite = RunSprite(karakterX, karakterY)
        run_group = pygame.sprite.Group(run_sprite)

        attack_sprite = AttackSprite(karakterX, karakterY)
        attack_group = pygame.sprite.Group(attack_sprite)

        dead_sprite = deadSprite(karakterX, karakterY)
        dead_group = pygame.sprite.Group(dead_sprite)

        idle_sprite = IdleSprite(karakterX, karakterY)
        idle_group = pygame.sprite.Group(idle_sprite)

        prenses_sprite=PrensesSprite(900,580)
        prenses_group=pygame.sprite.Group(prenses_sprite)

        zombiX=random.randrange(950,1100)
        zombiY=580

        zombiWalk_sprite=ZombiWalkSprite(zombiX,zombiY)
        zombiWalk_group=pygame.sprite.Group(zombiWalk_sprite)

        zombiWalk_spriteR=ZombiWalkRSprite(0,zombiY)
        zombiWalk_groupR=pygame.sprite.Group(zombiWalk_spriteR)

        zombiAttack_sprite=ZombiAttackSprite(karakterX+20,zombiY)
        zombiAttack_group=pygame.sprite.Group(zombiAttack_sprite)

        zombiDead_sprite=ZombiDeadSprite(karakterX+20,zombiY)
        zombiDead_group=pygame.sprite.Group(zombiDead_sprite)


        group = pygame.sprite.LayeredUpdates()
        group2=pygame.sprite.LayeredUpdates()
        group3 = pygame.sprite.LayeredUpdates()
        Background(0, group)
        Background(1, group)
        Background2(0,group2)
        Background2(1,group2)
        Background3(0, group3)
        Background3(1, group3)

        ekran1=True
        ekran2=False
        ekran3=False

        #karakter:
        idle=True
        walk = False
        run=False
        attack=False
        dead=False
        move = True
        # zombi:
        zombiWalk=False
        zombiWalkR=False
        zombiAttack=False
        zombiDead=False
        goster = False

        zombiSayisi=50

        coinX = random.randrange(400,1000)
        coinY=600
        Time = pygame.time.Clock()

        okX=karakterX+30
        okY=600
        ok=pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\ok.png")

        health=100
        zombiHealth = 60

        caniksirSayisi=0
        hiziksirSayisi=0
        saldiriiksirSayisi=0
        oksayisi=0

        saldiriGucu=False
        okAt=False

        prensesRun = False

        pygame.key.set_repeat(1,500)
        while move:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_s:
                        fps=20
                        idle = False
                        walk=True
                        run=False
                        attack=False
                        dead = False
                        if walk == True:
                            walk_sprite.moving()
                    if event.key == pygame.K_d:
                        fps=60
                        idle = False
                        walk=False
                        attack=False
                        run=True
                        dead = False
                        if run == True:
                            pygame.display.update()
                            run_sprite.moving()
                    if event.key==pygame.K_SPACE:
                        fps=40
                        idle = False
                        walk=False
                        run=False
                        attack=True
                        dead = False
                        if attack==True:
                            attack_sprite.moving()
                    if event.key==pygame.K_p:
                        self.pause()

                    if event.key==pygame.K_F1 and caniksirSayisi>=1 and health<=100:
                        caniksirSayisi-=1
                        health+=10
                        if health>=90:
                            health=100
                    if event.key == pygame.K_F2 and hiziksirSayisi >= 1:
                        hiziksirSayisi -= 1
                        fps+=5
                    if event.key==pygame.K_F3 and saldiriiksirSayisi>=1:
                        saldiriiksirSayisi-=1
                        saldiriGucu=True
                    if event.key==pygame.K_a and oksayisi>=1:
                        oksayisi-=1
                        okAt=True
                else:
                    fps=20
                    walk = False
                    run = False
                    attack = False
                    dead = False
                    idle=True
                    zombiWalk=True

            coin = pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\dollar.png")
            step = 5

            skor_yaz = yazilar()

            if zombiSayisi==0:
                zombiSayisi=0
                zombiWalk=False
                zombiAttack=False
                zombiDead=False
                prensesRun=True

            if walk==True or run==True and ekran1==True:
                group.update()
                coinX -= step
            group.draw(pencere2)
            if skor>=30:
                level=2
                ekran1=False
                ekran2=True
                if walk==True or run==True and ekran2==True:
                    group2.update()
                    coinX-=step
                group2.draw(pencere2)
            if skor >= 60:
                level=3
                ekran1 = False
                ekran2 = False
                ekran3=True
                if walk == True or run == True and ekran3 == True:
                    group3.update()
                    coinX-=step
                group3.draw(pencere2)

            if karakterX >= zombiWalk_sprite.rect.x - 30 and karakterY<=zombiWalk_sprite.rect.y:
                zombiWalk = False
                zombiAttack=True
                if zombiAttack==True:
                    walk=False
                    run=False
                    if walk==False and run==False and attack==False:
                        idle=True
                if health<=0:
                    zombiAttack=False
                if zombiHealth<=0:
                    zombiAttack=False

            if zombiWalkR==True:
                zombiWalk_spriteR.moving()
                zombiWalk_groupR.update()
                zombiWalk_groupR.draw(pencere2)

            if zombiWalk == True:
                zombiWalk_sprite.moving()
                zombiWalk_group.update()
                zombiWalk_group.draw(pencere2)

            if zombiAttack==True:
                zombiAttack_sprite.moving()
                zombiAttack_group.update()
                zombiAttack_group.draw(pencere2)
                health-=0.08

            if karakterX>=coinX-30 and karakterY<=coinY:
                coinX=random.randrange(400,1000)
                coinY = 600
                money+=1
            elif coinX<=0:
                coinX = random.randrange(400, 1000)
                coinY = 600

            if idle==True:
                idle_sprite.moving()
                idle_group.update()
                idle_group.draw(pencere2)
            if walk==True:
                idle=False
                walk_group.update()
                walk_group.draw(pencere2)
            elif run==True:
                run_group.update()
                run_group.draw(pencere2)
            elif attack==True:
                attack_group.update()
                attack_group.draw(pencere2)
                if karakterX >= zombiWalk_sprite.rect.x - 30 and karakterY <= zombiWalk_sprite.rect.y:
                    zombiHealth -= 0.4
                    if saldiriGucu==True:
                        zombiHealth-=0.8
                    if zombiHealth<=0:
                        saldiriGucu=False
                        zombiHealth=0
                        zombiWalk = False
                        zombiAttack = False
                        zombiDead=True
            if zombiDead == True:
                money+=2
                skor+=10
                zombiSayisi-=1
                zombiAttack=False
                zombiWalk=False
                goster=True
                if goster==True:
                    zombiDead_sprite.moving()
                    zombiDead_group.update()
                    zombiDead_group.draw(pencere2)
                    fps=2
                    goster=False

            if zombiDead==True and goster==False:
                zombiDead=False
                zombiAttack=False
                zombiHealth=60
                zombiWalk_sprite.rect.x=random.randrange(950,1100)
                zombiY=580

            if health == 0:
                fps = 8
                idle = False
                walk = False
                run = False
                attack = False
                zombiWalk = False
                zombiAttack = False
                zombiWalkR = False
                dead = True
                health = 0

            if dead == True:
                fps = 5
                dead_sprite.moving()
                dead_group.update()
                dead_group.draw(pencere2)

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            can=pygame.image.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\iksirler\can.png')
            pygame.draw.rect(pencere2,green,(380,10,80,70))

            hiz = pygame.image.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\iksirler\hız.png')
            pygame.draw.rect(pencere2, green, (500, 10, 80, 70))

            saldiriHizi = pygame.image.load(r'C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\iksirler\saldırıhızı.png')
            pygame.draw.rect(pencere2, green, (620, 10, 80, 70))

            okicon = pygame.image.load(r"C:\Users\bertug\PycharmProjects\SuperWarrior\Resimler\okicon.png")
            pygame.draw.rect(pencere2,green,(740,10,80,70))

            if 380 + 80 > mousePosition[0] > 380 and 10 + 70 > mousePosition[1] > 10:
                pygame.draw.rect(pencere2, green, (380, 10, 80, 70))
                if click[0] == 1 and money>=10:
                   caniksirSayisi+=1
                   money-=10
            else:
                pygame.draw.rect(pencere2, green, (380, 10, 80, 70))

            if 500 + 80 > mousePosition[0] > 500 and 10 + 70 > mousePosition[1] > 10:
                pygame.draw.rect(pencere2, green, (500, 10, 80, 70))
                if click[0] == 1 and money >= 12:
                    hiziksirSayisi += 1
                    money -= 12
            else:
                pygame.draw.rect(pencere2, green, (500, 10, 80, 70))

            if 620 + 80 > mousePosition[0] > 620 and 10 + 70 > mousePosition[1] > 10:
                pygame.draw.rect(pencere2, green, (620, 10, 80, 70))
                if click[0] == 1 and money >= 15:
                    saldiriiksirSayisi += 1
                    money -= 15
            else:
                pygame.draw.rect(pencere2, green, (620, 10, 80, 70))


            if 740 + 80 > mousePosition[0] > 740 and 10 + 70 > mousePosition[1] > 10:
                pygame.draw.rect(pencere2, green, (740, 10, 80, 70))
                if click[0] == 1 and money >= 5:
                    oksayisi += 1
                    money -= 5
            else:
                pygame.draw.rect(pencere2, green, (740, 10, 80, 70))


            if okAt == True:
                okX += 10
                pencere2.blit(ok, (okX, okY))
                if okX >= zombiWalk_sprite.rect.x or okX <= zombiAttack_sprite.rect.x and okAt == True:
                    zombiHealth -= 10
                    if zombiHealth == 0:
                        zombiDead = True
                    okX = karakterX + 30
                    okAt = False

            if prensesRun==True:
                prenses_sprite.moving()
                prenses_group.update()
                prenses_group.draw(pencere2)
                if prenses_sprite.rect.x<=karakterX+30:
                    prenses_sprite.rect.x=karakterX+30
                    skor_yaz.oyunYazilari("TEBRİKLER",red,250,ekran_boy/2,150)
                    time.sleep(2)

            pencere2.blit(can, (380, 40))
            pencere2.blit(hiz, (505, 40))
            pencere2.blit(saldiriHizi, (625, 40))
            pencere2.blit(okicon,(740,40))

            pygame.draw.rect(pencere2,red,(walk_sprite.rect.x-15,karakterY-3,100,8))
            pygame.draw.rect(pencere2, lime, (walk_sprite.rect.x-15, karakterY-3, health, 8))
            if prensesRun!=True:
                pygame.draw.rect(pencere2, red, (zombiWalk_sprite.rect.x + 5, zombiY - 5, 60, 8))
                pygame.draw.rect(pencere2, lime, (zombiWalk_sprite.rect.x + 5, zombiY - 5, zombiHealth, 8))

            pygame.draw.rect(pencere2,brown,(0,90,1200,35))

            skor_yaz.oyunYazilari("Kalan Zombi Sayısı =",white,400,100,30)
            skor_yaz.oyunYazilari(str(zombiSayisi),white,615,100,30)
            skor_yaz.oyunYazilari("10$",yellow,405,10,40)
            skor_yaz.oyunYazilari(str(caniksirSayisi),white,440,50,25)
            skor_yaz.oyunYazilari("12$",yellow,525,10,40)
            skor_yaz.oyunYazilari(str(hiziksirSayisi), white, 560, 50, 25)
            skor_yaz.oyunYazilari("15$", yellow, 645, 10, 40)
            skor_yaz.oyunYazilari(str(saldiriiksirSayisi), white, 680, 50, 25)
            skor_yaz.oyunYazilari("5$", yellow, 765, 10, 40)
            skor_yaz.oyunYazilari(str(oksayisi),white,800,50,25)

            skor_yaz.oyunYazilari("SCORE:",purple,950,10,40)
            skor_yaz.oyunYazilari(str(skor),purple,1060,10,40)
            skor_yaz.oyunYazilari("COIN:",gold,10,50,40)
            skor_yaz.oyunYazilari(str(money),gold,100,50,40)
            skor_yaz.oyunYazilari("HEALTH: %", aqua, 10, 10, 40)
            skor_yaz.oyunYazilari(str(int(health)),aqua,170,10,40)
            skor_yaz.oyunYazilari("LEVEL: ",white,950,55,40)
            skor_yaz.oyunYazilari(str(level),white,1060,55,40)

            pencere2.blit(coin, (coinX,coinY))

            pygame.display.flip()
            pygame.display.update()
            Time.tick(fps)

intro=Intro()
intro.giris_ekrani()
