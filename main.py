import pygame as pg
import nastroi
import spreit
import pygame.freetype as freet
import menu as man

pg.init()
pg.mixer.init(channels=6)

# константы
# здесь записан порядок нот и их длительность для каждой песни

class Spiele:
    def __init__(self):
        self.menu = man.Menu(self)
        self.okno = pg.display.set_mode(nastroi.SIZE)
        self.a = 0
        self.melodi = spreit.Melodi(nastroi.CHRISTMAS_TREE_NOTES, nastroi.CHRISTMAS_TREE_DURATION)
        self.time = pg.time.Clock()
        self.pism = freet.Font(None, 20)
        self.aktiwemu = 0
        self.numernotia = 0
        self.geymover = 0

    def otris(self):
        self.okno.fill([255, 255, 255])
        chertilo = 0
        for cherch in range(nastroi.POLOS):
            chertilo += nastroi.SCHIRPOLOS
            pg.draw.line(self.okno, [0, 0, 0], [chertilo, 0], [chertilo, 600])
        if self.geymover == 0:
            self.melodi.otris(self.okno)
        else :
            self.pism.render_to(self.okno, [170, 300], "Game Over")
        if self.melodi.notia == len(nastroi.CHRISTMAS_TREE_NOTES) and self.melodi.noti[self.melodi.notia - 1].rect.y > 650 :
            self.pism.render_to(self.okno, [170, 300], "The End")
        pg.display.flip()

    def sobitia(self):
        sobitia = pg.event.get()
        for sobi in sobitia:
            if sobi.type == pg.QUIT:
                self.a += 1
            if sobi.type == pg.MOUSEBUTTONDOWN:
                for pian in self.melodi.noti:
                    if pian.rect.collidepoint(sobi.pos):
                        # print("Клик")
                        pian.klik()
                        if pian.nome == self.numernotia:
                            pass
                        else :
                            self.geymover = 1
                            print("NO")
                        self.numernotia += 1
            if sobi.type == pg.KEYDOWN:
                if sobi.key == pg.K_RETURN:
                    self.aktiwemu = 0
                    self.geymover = 0
                    self.numernotia = 0

    def logika(self):
        if self.geymover == 0:
            for notianto in self.melodi.noti:
                if notianto.rect.y > 600 and notianto.nasch == 0:
                    self.geymover = 1
            self.melodi.sosidanie()
            self.melodi.upraw()

    def sbor(self):
        while self.a < 1:
            if self.aktiwemu == 1:
                self.otris()
                self.sobitia()
                self.logika()
            elif self.aktiwemu == 0:
                self.menu.otris()
                self.menu.sobitia()
                self.menu.logika()
            self.time.tick(100)

pal = Spiele()
pal.sbor()
