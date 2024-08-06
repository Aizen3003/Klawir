import pygame as pg
import random
import nastroi

class Nota :
    def __init__(self, koorx, koory, nasswu, dlitswu, nome):
        self.dlit = dlitswu
        if dlitswu == 1:
            self.kart = pg.image.load("short_tile.png")
        elif dlitswu == 2:
            self.kart = pg.image.load("long_tile.png")
        self.nasswu = nasswu
        self.nome = nome
        self.swuk = pg.mixer.Sound("Sounds/" + self.nasswu + ".ogg")
        self.swuk.set_volume(0.01)
        self.ras1 = self.kart.get_width() 
        self.ras2 = self.kart.get_height() 
        self.rect = pg.rect.Rect([koorx, koory], [self.ras1, self.ras2])
        self.spid = 2
        self.nasch = 0

    def otris(self, okn):
        okn.blit(self.kart, self.rect)
    
    def upraw(self):
        self.rect.y += self.spid

    def klik(self):
        self.nasch += 1
        if self.dlit == 1:
            self.kart = pg.image.load("short_tile_pressed.png")
        elif self.dlit == 2:
            self.kart = pg.image.load("long_tile_pressed.png")
        kanswobod = pg.mixer.find_channel()
        if kanswobod != None:
            kanswobod.queue(self.swuk)
        else :
            pg.mixer.stop()
        self.swuk.play()

class Melodi :
    def __init__(self, noti, dlit):
        self.naswan = noti
        self.prodli = dlit
        self.timpost = 0
        self.timsosd = 0
        self.noti = []
        self.notia = 0
        
    def sosidanie(self):
        self.timpost = pg.time.get_ticks()
        if self.timpost - self.timsosd >= 1000 and self.notia < len(self.naswan):
            nom = random.randint(0, nastroi.POLOS - 1)
            koorx = nom * nastroi.SCHIRPOLOS
            nota = Nota(koorx, 0, self.naswan[self.notia], self.prodli[self.notia], self.notia)
            self.notia += 1
            self.timsosd = pg.time.get_ticks()
            self.noti.append(nota)

    def otris (self, okn):
        for pesn in self.noti:
            pesn.otris(okn)

    def upraw(self):
        for dwih in self.noti:
            dwih.upraw()