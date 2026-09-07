import pygame
from pygame import *
from random import randint


# ==========================================
# INITIALIZATION
# ==========================================

pygame.init()
mixer.init()


# ==========================================
# GAME WINDOW
# ==========================================

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze Game")

clock = time.Clock()
FPS = 60


# ==========================================
# CLASS GAME SPRITE
# ==========================================

class GameSprite(sprite.Sprite):

    def __init__(
        self,
        play_img,
        lose_img,
        win_img,
        player_x,
        player_y,
        player_speed
    ):
        super().__init__()

        # ----------------------------------
        # Load gambar kondisi awal
        # ----------------------------------

        self.play_img = transform.scale(
            image.load(play_img).convert_alpha(),
            (55, 55)
        )

        # ----------------------------------
        # Load gambar kondisi kalah
        # ----------------------------------

        self.lose_img = transform.scale(
            image.load(lose_img).convert_alpha(),
            (55, 55)
        )

        # ----------------------------------
        # Load gambar kondisi menang
        # ----------------------------------

        self.win_img = transform.scale(
            image.load(win_img).convert_alpha(),
            (55, 55)
        )

        # ----------------------------------
        # Gambar yang digunakan pertama kali
        # ----------------------------------

        self.image = self.play_img

        # Kecepatan karakter
        self.speed = player_speed

        # Rectangle karakter
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y


    # ======================================
    # DRAW SPRITE
    # ======================================

    def reset(self):
        window.blit(
            self.image,
            self.rect
        )


    # ======================================
    # KONDISI AWAL
    # ======================================

    def set_play(self):
        self.image = self.play_img


    # ======================================
    # KONDISI KALAH
    # ======================================

    def set_lose(self):
        self.image = self.lose_img


    # ======================================
    # KONDISI MENANG
    # ======================================

    def set_win(self):
        self.image = self.win_img


# ==========================================
# CLASS PLAYER
# ==========================================

class Player(GameSprite):

    def update(self):

        keys = key.get_pressed()


        # ----------------------------------
        # Bergerak ke kiri - A
        # ----------------------------------

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


        # ----------------------------------
        # Bergerak ke kanan - D
        # ----------------------------------

        if keys[K_d] and self.rect.x < win_width - 60:
            self.rect.x += self.speed


        # ----------------------------------
        # Bergerak ke atas - W
        # ----------------------------------

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed


        # ----------------------------------
        # Bergerak ke bawah - S
        # ----------------------------------

        if keys[K_s] and self.rect.y < win_height - 60:
            self.rect.y += self.speed


# ==========================================
# CLASS ENEMY
# ==========================================

class Enemy(GameSprite):

    def __init__(
        self,
        play_img,
        lose_img,
        win_img,
        player_x,
        player_y,
        player_speed
    ):

        super().__init__(
            play_img,
            lose_img,
            win_img,
            player_x,
            player_y,
            player_speed
        )

        # Arah gerakan enemy
        self.side = "left"


    def update(self):

        # ----------------------------------
        # Jika mencapai batas kiri
        # ----------------------------------

        if self.rect.x <= 470:
            self.side = "right"


        # ----------------------------------
        # Jika mencapai batas kanan
        # ----------------------------------

        if self.rect.x >= win_width - 60:
            self.side = "left"


        # ----------------------------------
        # Gerakkan enemy
        # ----------------------------------

        if self.side == "left":
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed


# ==========================================
# CLASS WALL
# ==========================================

class Wall(sprite.Sprite):

    def __init__(
        self,
        color_1,
        color_2,
        color_3,
        wall_x,
        wall_y,
        wall_width,
        wall_height
    ):
        super().__init__()

        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

        self.width = wall_width
        self.height = wall_height


        # ----------------------------------
        # Membuat surface wall
        # ----------------------------------

        self.image = Surface(
            [self.width, self.height]
        )

        self.image.fill(
            (
                self.color_1,
                self.color_2,
                self.color_3
            )
        )


        # ----------------------------------
        # Rectangle wall
        # ----------------------------------

        self.rect = self.image.get_rect()

        self.rect.x = wall_x
        self.rect.y = wall_y


    # ======================================
    # DRAW WALL
    # ======================================

    def draw_wall(self):

        draw.rect(
            window,
            (
                self.color_1,
                self.color_2,
                self.color_3
            ),
            self.rect
        )


# ==========================================
# BACKGROUND
# ==========================================

background = transform.scale(
    image.load("background1.jpg").convert(),
    (win_width, win_height)
)


# ==========================================
# CREATE WALLS
# ==========================================

w1 = Wall(
    200, 184, 117,
    100, 20,
    450, 10
)

w2 = Wall(
    200, 184, 117,
    100, 480,
    350, 10
)

w3 = Wall(
    200, 184, 117,
    100, 20,
    10, 380
)

w4 = Wall(
    200, 184, 117,
    200, 130,
    10, 350
)

w5 = Wall(
    200, 184, 117,
    450, 130,
    10, 360
)

w6 = Wall(
    200, 184, 117,
    300, 20,
    10, 350
)

w7 = Wall(
    200, 184, 117,
    390, 120,
    130, 10
)


walls = [
    w1,
    w2,
    w3,
    w4,
    w5,
    w6,
    w7
]


# ==========================================
# CREATE PLAYER - ODY
# ==========================================

ody = Player(
    "ody1.png",       # Kondisi awal
    "ody2.png",       # Kondisi kalah
    "ody3.png",       # Kondisi menang
    5,
    win_height - 80,
    4
)


# ==========================================
# CREATE ENEMY - ANTI
# ==========================================

anti = Enemy(
    "anti1.png",      # Kondisi awal
    "anti2.png",      # Kondisi kalah
    "anti3.png",      # Kondisi menang
    win_width - 80,
    280,
    2
)


# ==========================================
# CREATE GOAL - PENELOPE
# ==========================================

penelope = GameSprite(
    "penelope1.png",  # Kondisi awal
    "penelope2.png",  # Kondisi kalah
    "penelope3.png",  # Kondisi menang
    win_width - 120,
    win_height - 80,
    0
)


# ==========================================
# FONT
# ==========================================

game_font = font.Font(
    None,
    70
)


win_text = game_font.render(
    "YAYYY!",
    True,
    (255, 215, 0)
)


lose_text = game_font.render(
    "NOOOO!",
    True,
    (180, 0, 0)
)


# ==========================================
# BACKSOUND
# ==========================================

mixer.music.load(
    "backsoundmusic.ogg"
)

# -1 = musik diulang terus-menerus
mixer.music.play(-1)


# ==========================================
# SOUND EFFECT
# ==========================================

money = mixer.Sound(
    "goalbacksound.ogg"
)

kick = mixer.Sound(
    "losesoundeffect.ogg"
)


# ==========================================
# GAME VARIABLES
# ==========================================

game = True
finish = False


# ==========================================
# GAME LOOP
# ==========================================

while game:


    # ======================================
    # EVENTS
    # ======================================

    for e in event.get():

        if e.type == QUIT:
            game = False


    # ======================================
    # GAME STILL RUNNING
    # ======================================

    if not finish:


        # ----------------------------------
        # Background
        # ----------------------------------

        window.blit(
            background,
            (0, 0)
        )


        # ----------------------------------
        # Update characters
        # ----------------------------------

        ody.update()
        anti.update()


        # ----------------------------------
        # Draw characters
        # ----------------------------------

        ody.reset()
        anti.reset()
        penelope.reset()


        # ----------------------------------
        # Draw walls
        # ----------------------------------

        for wall in walls:
            wall.draw_wall()


        # ==================================
        # COLLISION WITH ENEMY
        # ==================================

        if sprite.collide_rect(ody, anti):

            # Game selesai
            finish = True


            # --------------------------------
            # HENTIKAN BACKSOUND
            # --------------------------------

            mixer.music.stop()


            # --------------------------------
            # Ubah SEMUA karakter ke gambar
            # kondisi KALAH
            # --------------------------------

            ody.set_lose()
            anti.set_lose()
            penelope.set_lose()


            # --------------------------------
            # Tampilkan semua gambar kalah
            # --------------------------------

            ody.reset()
            anti.reset()
            penelope.reset()


            # --------------------------------
            # Tampilkan tulisan OOF!
            # --------------------------------

            window.blit(
                lose_text,
                (200, 200)
            )


            # --------------------------------
            # Putar suara kalah
            # --------------------------------

            kick.play()


        # ==================================
        # COLLISION WITH WALL
        # ==================================

        for wall in walls:

            if sprite.collide_rect(ody, wall):

                # Game selesai
                finish = True


                # --------------------------------
                # HENTIKAN BACKSOUND
                # --------------------------------

                mixer.music.stop()


                # --------------------------------
                # Ubah SEMUA karakter ke gambar
                # kondisi KALAH
                # --------------------------------

                ody.set_lose()
                anti.set_lose()
                penelope.set_lose()


                # --------------------------------
                # Tampilkan semua gambar kalah
                # --------------------------------

                ody.reset()
                anti.reset()
                penelope.reset()


                # --------------------------------
                # Tampilkan tulisan OOF!
                # --------------------------------

                window.blit(
                    lose_text,
                    (200, 200)
                )


                # --------------------------------
                # Putar suara kalah
                # --------------------------------

                kick.play()


                break


        # ==================================
        # WIN CONDITION
        # ==================================

        if sprite.collide_rect(ody, penelope):

            # Game selesai
            finish = True


            # --------------------------------
            # HENTIKAN BACKSOUND
            # --------------------------------

            mixer.music.stop()


            # --------------------------------
            # Ubah SEMUA karakter ke gambar
            # kondisi MENANG
            # --------------------------------

            ody.set_win()
            anti.set_win()
            penelope.set_win()


            # --------------------------------
            # Tampilkan semua gambar menang
            # --------------------------------

            ody.reset()
            anti.reset()
            penelope.reset()


            # --------------------------------
            # Tampilkan tulisan YAY!
            # --------------------------------

            window.blit(
                win_text,
                (200, 200)
            )


            # --------------------------------
            # Putar suara menang
            # --------------------------------

            money.play()


    # ======================================
    # UPDATE DISPLAY
    # ======================================

    display.update()


    # ======================================
    # FPS
    # ======================================

    clock.tick(FPS)


# ==========================================
# QUIT GAME
# ==========================================

pygame.quit()
