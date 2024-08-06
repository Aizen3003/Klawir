import pygame as pg
import nastroi
import spreit
import pygame.freetype as freet

class Menu :
    def __init__(self, spiele):
        self.kart = pg.image.load("menu.png")
        self.spiele = spiele
        self.nezrimklin = freet.Font(None, 30)
        self.einspesn = nastroi.RED
        self.zweipesn = nastroi.VIOL
        self.driepesn = nastroi.VIOL
        self.numerpesn = 1

    def otris(self):
        self.spiele.okno.blit(self.kart, [0, 0])
        self.nezrimklin.render_to(self.spiele.okno, [30, 250], "В лесу родилась ёлкчка", self.einspesn)
        self.nezrimklin.render_to(self.spiele.okno, [60, 350], "Визуальные мечи", self.zweipesn)
        self.nezrimklin.render_to(self.spiele.okno, [150, 450], "Утро", self.driepesn)
        pg.display.flip()

    def sobitia(self):
        sobitia = pg.event.get()
        for sobi in sobitia:
            if sobi.type == pg.KEYDOWN:
                if sobi.key == pg.K_RETURN:
                    self.spiele.aktiwemu = 1
                    if self.numerpesn == 1:
                        self.spiele.melodi = spreit.Melodi(nastroi.CHRISTMAS_TREE_NOTES, nastroi.CHRISTMAS_TREE_DURATION)
                    elif self.numerpesn == 2:
                        self.spiele.melodi = spreit.Melodi(nastroi.BIRCH_NOTES, nastroi.BIRCH_DURATION)
                    elif self.numerpesn == 3:
                        self.spiele.melodi = spreit.Melodi(nastroi.MORNING_NOTES, nastroi.MORNING_DURATION)
                if sobi.key == pg.K_DOWN:
                    if self.numerpesn == 1:
                        self.einspesn = nastroi.VIOL
                        self.zweipesn = nastroi.RED
                        self.numerpesn = 2
                    elif self.numerpesn == 2:
                        self.zweipesn = nastroi.VIOL
                        self.driepesn = nastroi.RED
                        self.numerpesn = 3
                    elif self.numerpesn == 3:
                        self.driepesn = nastroi.VIOL
                        self.einspesn = nastroi.RED
                        self.numerpesn = 1
                elif sobi.key == pg.K_UP:
                    if self.numerpesn == 1:
                        self.einspesn = nastroi.VIOL
                        self.driepesn = nastroi.RED
                        self.numerpesn = 3
                    elif self.numerpesn == 2:
                        self.zweipesn = nastroi.VIOL
                        self.einspesn = nastroi.RED
                        self.numerpesn = 1
                    elif self.numerpesn == 3:
                        self.driepesn = nastroi.VIOL
                        self.zweipesn = nastroi.RED
                        self.numerpesn = 2

            if sobi.type == pg.QUIT:
                self.a += 1
                
    def logika(self):
        pass