import tkinter
import time
from PIL import ImageTk
from simpleimage import SimpleImage
import random
import math

MEHRAN = 'images/Ourplayers/mehran.png'
MEHRANLARGE = 'images/Ourplayers/mehransquare.png'
CHRIS = 'images/Ourplayers/chrisP.png'
KAREL = 'images/Ourplayers/karel.png'
PYTHON = 'images/Ourplayers/python.jpg'
BEEPER = 'images/ThisnThat/beeper.png'
TATOO = 'images/Tatooine/vista.jpg'
TATOO2 = 'images/Tatooine/desert.jpg'
TATSAM = 'images/Tatooine/tatsample.png'
DESTAT = 'images/Tatooine/desertat.png'
DESTAT1 = 'images/Tatooine/desertatsam.png'
BAGS = 'images/ThisnThat/luggage.png'
SPACE1 = 'images/Space/purplespace.jpg'
SPACE = 'images/Space/bluespace.jpg'
HYPER = 'images/Hyperspace/whitesace.jpg'
FALCON = 'images/Falcon/lfalcon.jpg'
FALCONGO = 'images/Falcon/falcongo.png'
FALCONB = 'images/Falcon/falconside.png'
HYPERFAL = 'images/Hyperspace/falconspace.jpg'
EARTH = 'images/Earth/earth.jpg'
KENYA = 'images/Earth/kenya1.jpg'
STANFORD = 'images/Earth/quad.jpg'
STANFORD1= 'images/Earth/stanford1.jpg'
STANFORD2 ='images/Earth/stanford2.jpg'
STAN = 'images/Earth/stanback.png'
STAN1 = 'images/Earth/stanback1.png'
RICH = 'images/Ourplayers/karelcreator.png'
GUIDO = 'images/Ourplayers/guido.jpg'
MTRAIN = 'images/Earth/mt-rainier.jpg'
XWING = 'images/XWing/frontleftx.jpg'
RXWING = 'images/XWing/xwinglft.png'
LXWING = 'images/XWing/xwingrt.png'
FXWING = 'images/XWing/xwingfront.png'
CLOUD = 'images/Earth/cloudx.png'
CLOUDR = 'images/Earth/cloudrx.png'
MTRAINRG = 'images/Earth/mtrainrt.png'
MTRAINLF = 'images/Earth/mtrainleft.png'
MTRAINCLR = 'images/Earth/mtrainleftcl.png'
MTRAINCEN = 'images/Earth/mtraincen.png'
MEHSTAN = 'images/Earth/mehlarge.png'
SIMBA = 'images/Our players/simba-sq.png'
BURRITO = 'images/ThisnThat/burrito.png'
SABER = 'images/ThisnThat/lightsaber.png'
CHALK = 'images/Earth/chalkboard.jpeg'
BBACK = 'images/Earth/blackback.png'
BLACKB = 'images/Earth/blackboard.jpg'
MASK = 'images/Masks/mask.jpg'
N_ROWS = 3
N_COLS = 5
BURR_SIZE = 200
WIDTH = N_COLS * BURR_SIZE
HEIGHT = N_ROWS * BURR_SIZE
TATOOCLOSE= 'images/Tatooine/tatooclose.jpg'
CLOSE = 'images/Tatooine/closefal2.png'

CLW = 160
MLH = 155
MLW = 140
MHEI = 129
MMW = 125
MWID = 115
KLH = 100
KLW = 90
KWID = 70
KHEI = 80

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
SQUARE_SIZE = 120


def main():
    action_list = []

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Karel's Unexpected Journey")
    open_phimage = create(TATOOCLOSE, CANVAS_WIDTH, CANVAS_HEIGHT)
    opening = canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=open_phimage)
    m1 = canvas.create_text(60, 240, anchor='w', font='Papyrus 50', fill='yellow',  text="Karel's Unexpected Journey")
    m2 = canvas.create_line(60, 280, 700, 280, fill='yellow')
    m3 = canvas.create_text(980, 580, anchor='e', font='Papyrus 20', fill= 'purple', text='Final Project . Code in Place . Sp 2020 . Jacquelynne Fontaine')
    canvas.update()
    time.sleep(4)

    m4 = canvas.create_text(60, 340, anchor='w', font='Papyrus 32', fill='yellow', text='A semi-choose-your-own-adventure ')
    m5 = canvas.create_text(60, 390, anchor='w', font='Papyrus 32', fill='yellow', text='short film')
    canvas.update()
    time.sleep(7)

    beeper_phimage= create(BEEPER, 22, 20)
    beeper = canvas.create_image(-15, 560, image=beeper_phimage)
    canvas.update()
    for i in range(4):
        for i in range(10):
            canvas.move(beeper, 3, -2)
            canvas.update()
            time.sleep(1/70)
        for i in range(10):
            canvas.move(beeper, 3, 2)
            canvas.update()
            time.sleep(1/70)
    time.sleep(3)

    canvas.itemconfigure(m1, state='hidden')
    canvas.itemconfigure(m2, state='hidden')
    canvas.itemconfigure(m3, state='hidden')
    canvas.itemconfigure(m4, state='hidden')
    canvas.itemconfigure(m5, state='hidden')
    canvas.update()
    time.sleep(3)


############################################

    tatoo_phimage = create(TATOO, CANVAS_WIDTH, CANVAS_HEIGHT)
    tatoo = canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=tatoo_phimage)
    canvas.update()
    time.sleep(2)

    a = canvas.create_text(960, 50, anchor='e', font='Papyrus 40', text='Early morning,  Tatooine')
    a54 = canvas.create_line(520, 60, 960, 60)
    canvas.update()
    time.sleep(3)

    # Mehran and Karel appear, walking
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2

    end_y = start_y + SQUARE_SIZE
    a1 = canvas.create_text(960, 140, anchor='e', font='Papyrus 34', text="Jedi Master Mehran walks with his apprentice, Karel.")
    canvas.update()

    mehran = greenscreen(MEHRAN, TATSAM, 0, 0)
    mehran_phimage = create_greened(mehran, MWID, MHEI)
    mehran = canvas.create_image(-45, 400, image=mehran_phimage)
    canvas.update()

    karel_phimage = create(KAREL, 70, 80)
    karel = canvas.create_image(-65, 500, image=karel_phimage)
    canvas.update()

    for i in range(20):
        canvas.move(mehran, 5, 0)
        canvas.update()
        canvas.move(karel, 5, 0)
        canvas.update()
        time.sleep(1/40)

    time.sleep(2)

    #Karel runs forward
    a2 = canvas.create_text(960, 190, anchor='e', font='Papyrus 34', text="But Karel spots something approaching!")
    while not is_past_middle(canvas, karel):
        canvas.move(karel, 3, 0)
        canvas.update()
        time.sleep(1/65)  # parameter is seconds to pause.
    for i in range(3):
        canvas.move(karel, 3, 0)
        time.sleep(1/65)

    #Mehran follows
    a3= canvas.create_text(960, 240, anchor='e', font='Papyrus 34', text='"What is it?" Master Mehran asks.')
    for i in range (135):
        canvas.move(mehran, 3, 0)
        #always_green_dark(canvas, mehran, MEHRAN, TATOO)
        canvas.update()
        time.sleep(1/68)  # parameter is seconds to pause.

    mehran = greenscreen(MEHRAN, 'images/Tatooine/back.png', 0, 2)
    mehran_phimage = create_greened(mehran, MWID, MHEI)
    mehran = canvas.create_image(458, 400, image=mehran_phimage)

    karel_phimage = create(KAREL, 70, 80)
    karel = canvas.create_image(get_left_x(canvas, karel)-1, 500, image=karel_phimage)

    a4 = canvas.create_text(960, 290, anchor='e', font='Papyrus 34', text='"Wait, I can use the Force..."')
    canvas.update()
    time.sleep(2)

    python = greenscreen_python(PYTHON, TATSAM, 0, 0)
    python_phimage = create_greened(python, 100, 100)
    python = canvas.create_image(900, 470, image= python_phimage)
    canvas.update()
    time.sleep(1)

    beeper_phimage = create(BEEPER, 40, 30)
    beeper = canvas.create_image(460, 555, image=beeper_phimage)
    canvas.update()
    time.sleep(1/30)

    canvas.itemconfigure(a, state='hidden')
    canvas.itemconfigure(a1, state='hidden')
    canvas.itemconfigure(a2, state='hidden')
    canvas.itemconfigure(a3, state='hidden')
    canvas.itemconfigure(a4, state='hidden')
    canvas.itemconfigure(a54, state='hidden')

    for i in range(130):
        canvas.move(python, -2, 0)
        #always_green(canvas, python, TATOO)
        canvas.update()
        time.sleep(1/50)

    time.sleep(1/33)

    for i in range (12):
        canvas.move(beeper, 3, -2)
        canvas.update()
        time.sleep(1/50)
    for i in range (11):
        canvas.move(beeper, -1, -2)
        canvas.update()
        time.sleep(1/50)

    canvas.itemconfigure(beeper, state='hidden')
    canvas.update()

    a5= canvas.create_text(970, 140, anchor='e', font='Papyrus 34', text='"Are you Master Mehran?"')
    a32 = canvas.create_text(970, 190, anchor='e', font='Papyrus 34', text='asks the creature, panting.')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(a5, state='hidden')
    canvas.itemconfigure(a32, state='hidden')
    canvas.update()

    a6 = canvas.create_text(240, 90, anchor='w', font='Papyrus 34', text='"Why yes, that is me," the Master replies,')
    canvas.update()
    time.sleep(2)
    a7 = canvas.create_text(240, 145, anchor='w', font='Papyrus 34', text='"and the Force tells me ...')
    canvas.update()
    time.sleep(2)
    a16 = canvas.create_text(240, 195, anchor='w', font='Papyrus 34', text='you may need my help on your planet."')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(a6, state='hidden')
    canvas.itemconfigure(a7, state='hidden')
    canvas.itemconfigure(a16, state='hidden')
    canvas.update()
    time.sleep(1/3)

    a8 = canvas.create_text(970, 90, anchor='e', font='Papyrus 34', text='"My creator was right! You do understand me!')
    canvas.update()
    time.sleep(2)
    a9 = canvas.create_text(970, 140, anchor='e', font='Papyrus 34', text='Yes, our planet is in peril.')
    canvas.update()
    time.sleep(2)
    a10 = canvas.create_text(970, 190, anchor='e', font='Papyrus 34', text='We are in a global shutdown," explains the creature,')
    canvas.update()
    time.sleep(2)
    a17 = canvas.create_text(970, 240, anchor='e', font='Papyrus 34', text='"and need tools to navigate the future."')
    canvas.update()
    time.sleep(2)
    canvas.itemconfigure(a8, state='hidden')
    canvas.itemconfigure(a9, state='hidden')
    canvas.itemconfigure(a10, state='hidden')
    canvas.itemconfigure(a17, state='hidden')
    canvas.update()
    a11 = canvas.create_text(980, 90, anchor='e', font='Papyrus 34', text='"My creator said you might be able to help us...')
    a20 = canvas.create_text(980, 140, anchor='e', font='Papyrus 34', text= 'Is that true?"')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(a11, state='hidden')
    canvas.itemconfigure(a20, state='hidden')
    canvas.update()
    time.sleep(1/2)

    a18 = canvas.create_text(240, 90, anchor='w', font='Papyrus 34',text='"Of course!" the Master replies.')
    canvas.update()
    time.sleep(2)
    a12 = canvas.create_text(240, 145, anchor='w', font='Papyrus 34', text='"I will do what I can to help your planet,')
    canvas.update()
    time.sleep(2)
    a13 = canvas.create_text(240, 200, anchor='w', font='Papyrus 34', text='and I will bring my apprentice, Karel, with me!')
    canvas.update()
    time.sleep(2)
    a14 = canvas.create_text(350, 255, anchor='w', font='Papyrus 34', text='Karel, would you like that?"')
    canvas.update()
    time.sleep(2)
    canvas.itemconfigure(a12, state='hidden')
    canvas.itemconfigure(a13, state='hidden')
    canvas.itemconfigure(a14, state='hidden')
    canvas.itemconfigure(a18, state='hidden')
    canvas.update()

    a21 = canvas.create_text(340, 90, anchor='w', font='Papyrus 34', text='Help Karel decide...')
    canvas.update()
    time.sleep(2)
    a22 = canvas.create_text(340, 140, anchor='w', font='Papyrus 34', text='Enter 1 in the terminal to help,')
    canvas.update()
    time.sleep(1)
    a23 = canvas.create_text(340, 190, anchor='w', font='Papyrus 34', text='or 0 to stay behind.')
    canvas.update()
    choice = int(input(str("Would you like to stay or go? 1 or 0? ")))
    canvas.itemconfigure(a21, state='hidden')
    canvas.itemconfigure(a22, state='hidden')
    canvas.itemconfigure(a23, state='hidden')
    if choice == 0:
        a24 = canvas.create_text(240, 90, anchor='w', font='Papyrus 34', text='"But Karel," Master Mehran pauses,')
        canvas.update()
        time.sleep(2)
        a25 = canvas.create_text(240, 140, anchor='w', font='Papyrus 34', text='"Something in the Force tells me...')
        canvas.update()
        time.sleep(2)
        a26 = canvas.create_text(240, 190, anchor='w', font='Papyrus 34', text='...that you will play a big part in this journey.')
        canvas.update()
        time.sleep(2)
        a27 = canvas.create_text(440, 240, anchor='w', font='Papyrus 34', text='Please reconsider..."')
        canvas.update()
        time.sleep(1/2)
        choice = int(input("Would you like to stay or go? 1 or 0? "))
        canvas.itemconfigure(a24, state='hidden')
        canvas.itemconfigure(a25, state='hidden')
        canvas.itemconfigure(a26, state='hidden')
        canvas.itemconfigure(a27, state='hidden')
        time.sleep(1)
        if choice == 0:
            a29 = canvas.create_text(240, 140, anchor='w', font='Papyrus 34', text='"Ok, field trip, you are coming with me."')
            canvas.update()
            time.sleep(3)
            canvas.itemconfigure(a29, state='hidden')
            a30 = canvas.create_text(140, 140, anchor='w', font='Papyrus 34', text='"The force tells me that bringing you is the right choice!"')
            canvas.update()
            time.sleep(2)
            canvas.itemconfigure(a30, state='hidden')
            canvas.update()
            time.sleep(1/2)
        else:
            jump(canvas, karel)
    else:
        a30 = canvas.create_text(140, 140, anchor='w', font='Papyrus 34', text='"The force tells me that bringing you is the right choice!"')
        canvas.update()
        time.sleep(2)
        jump(canvas, karel)
        canvas.itemconfigure(a30, state='hidden')

    time.sleep(1/2)

    a15 = canvas.create_text(970, 140, anchor='e', font='Papyrus 34', text='"Oh, thank you so much!')
    a19 = canvas.create_text(970, 190, anchor='e', font='Papyrus 34', text='Come, there is no time to lose!')
    canvas.update()
    time.sleep(2)
    a20 = canvas.create_text(970, 240, anchor='e', font='Papyrus 34', text='I will race ahead and meet you on my planet."')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(a15, state='hidden')
    canvas.itemconfigure(a19, state='hidden')
    canvas.itemconfigure(a20, state='hidden')
    canvas.update()
    time.sleep(1)

    jump(canvas, karel)

    time.sleep(1/2)

    ############################################



    tatoo2_phimage = create_landscape(TATOO2, CANVAS_WIDTH, CANVAS_HEIGHT)
    tatoo = canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=tatoo2_phimage)
    c =canvas.create_text(150, 150, anchor='w', font='Papyrus 44', text="Let's choose how to get there!")
    canvas.update()
    #tatoo = adjust(TATOO2)
    falcon = greenscreen(FALCON, DESTAT1, 0, 0)
    xwing = greenscreen(XWING, DESTAT, 0, 0)

    falcon_phimage = create_greened(falcon, 400, 250)
    falcon = canvas.create_image(170, 450, image=falcon_phimage)

    tiefight_phimage = create_greened(xwing, 250, 250)
    xwing = canvas.create_image(835, 470, image=tiefight_phimage)
    canvas.update()
    time.sleep(2)

    mehran = greenscreen(MEHRAN, 'images/Tatooine/destatsam1.png', 0, 0)
    mehran_phimage = create_greened(mehran, MWID, MHEI)
    mehran = canvas.create_image(560, 490, image=mehran_phimage)
    karel_phimage = create(KAREL, KWID, KHEI)
    karel = canvas.create_image(460, 540, image=karel_phimage)

    canvas.update()
    time.sleep(1/30)

    canvas.itemconfigure(c, state='hidden')
    canvas.update()
    c1= canvas.create_text(45, 90, anchor='w', font='Papyrus 40', text='"What ship should we take, Karel?" asks Mehran.')
    canvas.update()
    time.sleep(2)

    c2= canvas.create_text(150, 150, anchor='w', font='Papyrus 40', text="Help Karel decide...")
    canvas.update()
    time.sleep(1)

    c3= canvas.create_text (150, 210, anchor='w', font='Papyrus 40', text="Enter 1 in the terminal for the Millenium Falcon")
    canvas.update()
    time.sleep(1)

    c4= canvas.create_text(150, 270, anchor='w', font='Papyrus 40', text="Enter 0 in the terminal for the X-Wing.")
    canvas.update()
    time.sleep(1)

    ship = int(input("Enter 1 for the Falcon, or 0 for the X-Wing: "))
    if ship == 0:
        canvas.itemconfigure(c1, state='hidden')
        canvas.itemconfigure(c2, state='hidden')
        canvas.itemconfigure(c3, state='hidden')
        canvas.itemconfigure(c4, state='hidden')
        canvas.update()
        c5 = canvas.create_text(350, 150, anchor='w', font='Papyrus 50', text="The X-Wing it is!")
        canvas.update()
        time.sleep(1/2)
        for i in range(10):
            canvas.move(mehran, 25, 2)
            canvas.update()
            time.sleep(1/12)
        for i in range(4):
            canvas.move(mehran, 22, -2)
            canvas.update()
            time.sleep(1 / 12)
        canvas.itemconfigure(c5, state='hidden')
        c6 = canvas.create_text(40, 75, anchor='w', font='Papyrus 40', text='"Oh no!" Exclaims Mehran,')
        c9 = canvas.create_text(40, 170, anchor='w', font='Papyrus 40',text='as he notices the empty fuel tank...')
        c7 = canvas.create_text(40, 270, anchor='w', font='Papyrus 40', text='"Better take the Falcon, she never will let us down!"')
        canvas.update()
        time.sleep(3)
        for i in range(14):
            canvas.move(mehran, -27, 0)
            canvas.update()
            time.sleep(1 / 10)
        canvas.itemconfigure(c6, state='hidden')
        canvas.itemconfigure(c7, state='hidden')
        canvas.itemconfigure(c9, state='hidden')
        time.sleep(1)
    else:
        canvas.itemconfigure(c1, state='hidden')
        canvas.itemconfigure(c2, state='hidden')
        canvas.itemconfigure(c3, state='hidden')
        canvas.itemconfigure(c4, state='hidden')

    canvas.create_text(150, 150, anchor='w', font='Papyrus 50', text="We are taking the Falcon, friends!")
    time.sleep(1/2)
    jump(canvas, karel)
    for i in range (8):
        canvas.move(karel, -23, -1)
        canvas.update()
        time.sleep(1/6)
    for i in range(14):
        canvas.move(mehran, -27, 0)
        canvas.update()
        time.sleep(1 / 10)
    for i in range(6):
        canvas.move(mehran, -5, -5)
        canvas.update()
        time.sleep(1 / 10)
    time.sleep(1)

    bag_phimage = create(BAGS, 55, 40)
    bag = canvas.create_image(220, 565, image=bag_phimage)

    bag1_phimage = create(BAGS, 55, 40)
    bag1 = canvas.create_image(170, 535, image=bag1_phimage)
    canvas.update()
    time.sleep(2)



    ############################################



    space_phimage = create_landscape(SPACE, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=space_phimage)
    d = canvas.create_text(70, 150, anchor='w', font='Papyrus 50', fill= 'white', text="Our heroes begin their journey...")
    canvas.update()
    time.sleep(1/2)

    falcon = greenscreen('images/Falcon/falcongo1.png', SPACE, 800, 150)
    falcongo_phimage = create_greened(falcon, 150, 110)
    falcongo = canvas.create_image(20, 580, image=falcongo_phimage)
    canvas.update()
    time.sleep(1/30)

    for i in range(140):
        canvas.move(falcongo, 5, -2)
        canvas.update()
        time.sleep(1/70)
    for i in range(100):
        canvas.move(falcongo, 4, -4)
        canvas.update()
        time.sleep(1/70)

    canvas.itemconfigure(falcongo, state='hidden')

    d1 = canvas.create_text(70, 250, anchor='w', font='Papyrus 46', fill='white', text="And soon find that their destination ...")
    canvas.update()
    time.sleep(2)
    d2 = canvas.create_text(70, 340, anchor='w', font='Papyrus 46', fill='white', text="Is much farther than they expected.")
    canvas.update()
    time.sleep(2)

    d3 = canvas.create_text(70, 430, anchor='w', font='Papyrus 46', fill='white', text="They'll need to access lightspeed!")
    canvas.update()
    time.sleep(2)

    d4 = canvas.create_text(70, 520, anchor='w', font='Papyrus 46', fill='white', text="But the Hyperdrive is broken again! ")
    canvas.update()
    time.sleep(1)

    canvas.itemconfigure(d, state='hidden')
    canvas.itemconfigure(d1, state='hidden')
    canvas.itemconfigure(d2, state='hidden')
    canvas.itemconfigure(d3, state='hidden')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(d4, state='hidden')
    canvas.update()
    time.sleep(1/50)



    ############################################



    add_list = []

    space1_phimage = create(SPACE1, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=space1_phimage)
    b = canvas.create_text(100, 110, anchor='w', font='Papyrus 44', fill= 'white', text= "Answer three questions correctly in a row")
    b1 = canvas.create_text(200, 175, anchor='w', font='Papyrus 44', fill= 'white', text= "to help Karel fix the Hyperdrive!")
    canvas.update()
    time.sleep(4)
    canvas.update()
    while len(add_list) < 3:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        e = canvas.create_text(50, 400, anchor='w', font='Papyrus 50', fill= 'white', text= "What is " + str(num1) + " + " + str(num2) + "?")
        canvas.update()
        time.sleep(1)
        print(str("What is " + str(num1) + " + " + str(num2) + "?"))
        e1 = canvas.create_text(50, 500, anchor='w', font='Papyrus 35', fill= 'white', state= 'normal', text="Answer in the terminal...")
        canvas.update()
        num3 = int(input("Your answer: "))
        canvas.itemconfigure(e1, state='hidden')
        canvas.update()
        sum = num1 + num2
        if sum == num3:
            add_list.append(1)
            left = 3 - len(add_list)
            if left == 0:
                canvas.itemconfigure(e, state='hidden')
                canvas.itemconfigure(b, state='hidden')
                canvas.itemconfigure(b1, state='hidden')
                canvas.create_text(200, 330, anchor='w', font='Papyrus 70', fill='white', text="Lightspeed ahead!")
                canvas.update()
                time.sleep(2)
                falcon = greenscreen_dark(FALCONB, SPACE1, 0 ,0)
                falcon_phimage = create_greened(falcon, 200, 80)
                falcon = canvas.create_image(100, 220, image=falcon_phimage)
                canvas.update()
                while not is_past_middle(canvas, falcon):
                    canvas.move(falcon, 5, 3)
                    canvas.update()
                    time.sleep(1/50)
                for i in range (75):
                    canvas.move(falcon, 9, 0)
                    canvas.update()
                    time.sleep(1/60)
                print("Lightspeed granted!")
                time.sleep(1/2)
            else:
                e2 = canvas.create_text(50, 500, anchor='w', font='Papyrus 35', fill= 'white', text="Nice work young padawan!")
                e3 =canvas.create_text(50, 560, anchor='w', font='Papyrus 35', fill= 'white', text="Answer " + str(left) + " more correctly to fix the Hyperdrive!")
                canvas.update()
                time.sleep(3)
                canvas.itemconfigure(e, state='hidden')
                canvas.itemconfigure(e2, state='hidden')
                canvas.itemconfigure(e3, state='hidden')
                canvas.update()
                time.sleep(1/2)
                print(str("Nice work! Answer " + str(left) + " more correctly to access hyperspeed to Earth!"))

        else:
            e2 =canvas.create_text(50, 500, anchor='w', font='Papyrus 35', fill= 'white', text="Incorrect. The expected answer is: " + (str(sum)))
            canvas.update()
            time.sleep(3)
            canvas.itemconfigure(c2, state='hidden')
            canvas.update()
            time.sleep(1/5)
            print(str("Incorrect. The expected answer is: " + (str(sum))))
            canvas.itemconfigure(e, state='hidden')
            canvas.itemconfigure(e2, state='hidden')
            add_list.clear()



    ############################################



    hyper_phimage = create_landscape(HYPERFAL, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=hyper_phimage)
    karel_phimage = create(KAREL, 110, 130)
    karel = canvas.create_image(850, 480, image=karel_phimage)


    mehran = greenscreen(MEHRAN, 'images/Hyperspace/mehhyper.png', 0,0)
    mehran_phimage = create_greened(mehran, 185, 200)
    mehran = canvas.create_image(230, 480, image=mehran_phimage)
    canvas.update()
    time.sleep(2)

    f = canvas.create_text(70, 38, anchor='w', font='Papyrus 36', fill='yellow', text='"There are some Jedi Masters on Earth, I recall,"')
    canvas.update()
    time.sleep(4)
    canvas.itemconfigure(f, state='hidden')
    f1 = canvas.create_text(70, 38, anchor='w', font='Papyrus 36', fill='yellow', text='Master Mehran says, glancing at Karel.')
    canvas.update()
    time.sleep(3)

    the_shakes(canvas, karel)

    canvas.itemconfigure(f1, state='hidden')
    f2 = canvas.create_text(70, 38, anchor='w', font='Papyrus 36', fill='yellow', text='"Shall we have one join us?"')
    canvas.update()
    time.sleep(2)
    f3 = canvas.create_text(350, 580, anchor='w', font='Papyrus 36', fill='yellow', text='Help Karel decide: 1 for Yes, 0 for No')
    canvas.update()
    time.sleep(1/2)

    the_shakes(canvas, karel)

    pick_up = int(input("Shall we pick the other Master up? 1 for Yes, 0 for No: "))
    if pick_up == 0:
        canvas.itemconfigure(f2, state='hidden')
        canvas.itemconfigure(f3, state='hidden')
        f4 = canvas.create_text(70, 45, anchor='w', font='Papyrus 45', fill='yellow', text='"So be it! No friends this trip!"')
        canvas.update()
        time.sleep(3)

    else:
        action_list.append('Chris')
        canvas.itemconfigure(f2, state='hidden')
        canvas.itemconfigure(f3, state='hidden')
        f4 = canvas.create_text(70, 45, anchor='w', font='Papyrus 40', fill='yellow', text='"So be it! I am happy to see my old friend again!"')
        canvas.update()
        time.sleep(3)


    ###########################################



    earth_phimage = create_landscape(EARTH, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=earth_phimage)
    canvas.update()
    time.sleep(1/2)

    falcon = greenscreen_dark(FALCONB, 'images/Falcon/earthfal.png', 0, 0)
    falcon_phimage= create_greened(falcon, 190, 120)
    falcon = canvas.create_image(10, -10, image=falcon_phimage)
    canvas.update()

    for i in range(40):
        canvas.move(falcon, 3, 3)
        canvas.update()
        time.sleep(1/65)

    time.sleep(2)
    g = canvas.create_text(360, 110, anchor='w', font='Verdana 50', fill='yellow', text="Welcome to Earth!")
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(g, state='hidden')
    canvas.update()
    time.sleep(1/10)

    g1 = canvas.create_text(910, 100, anchor='e', font='Verdana 30', fill='yellow', text='"We made it!" exclaims Master Mehran.')
    canvas.update()
    time.sleep(2)
    g2 = canvas.create_text(910, 150, anchor='e', font='Verdana 30', fill='yellow', text='Then he notices a rather green Karel.')
    canvas.update()
    time.sleep(2)
    g3 = canvas.create_text(910, 200, anchor='e', font='Verdana 30', fill='yellow', text='"Ah, your first time in Hyperspace?" he chuckles.')
    canvas.update()
    time.sleep(2)
    g4= canvas.create_text(910, 250, anchor='e', font='Verdana 30', fill='yellow', text='"I am glad we are close to the right man who can help!"')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(g1, state='hidden')
    canvas.itemconfigure(g2, state='hidden')
    canvas.itemconfigure(g3, state='hidden')
    canvas.itemconfigure(g4, state='hidden')

    if 'Chris' in action_list:
        g5 =canvas.create_text(910, 270, anchor='e', font='Verdana 30', fill='yellow', text='"Good thing we were already on our way there!"')
        canvas.update()
        time.sleep(3)
    else:
        g5 =canvas.create_text(910, 270, anchor='e', font='Verdana 30', fill='yellow',text='"Seems we needed to visit my friend anyway, ')
        g6 =canvas.create_text(910, 320, anchor='e', font='Verdana 30', fill='yellow',text='young padawan!"')
        canvas.update()
        time.sleep(3)
        canvas.itemconfigure(g6, state='hidden')
    canvas.itemconfigure(g5, state='hidden')
    canvas.create_text(650, 200, anchor='e', font='Verdana 60', fill='yellow', text='Next Stop:')
    canvas.update()
    time.sleep(2)


    ###########################################


    kenya_phimage = create_landscape(KENYA, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=kenya_phimage)
    canvas.update()


    falcon = greenscreen_dark(FALCONB, KENYA, 0, 820)
    falcon_phimage = create_greened(falcon, 310, 145)
    falcon = canvas.create_image(20, 520, image=falcon_phimage)
    canvas.update()

    for i in range(15):
        canvas.move(falcon, 10, 0)
        canvas.update()
        time.sleep(1/65)
    time.sleep(1/2)
    h = canvas.create_text(400, 100, anchor='w', font='Garamond 80', fill='yellow', text="Kenya!")
    canvas.update()
    time.sleep(2)


    karel = make_sick(KAREL)
    karel_phimage = create_greened(karel, KWID, KHEI)
    karel = canvas.create_image(350, 520, image=karel_phimage)

    mehran = greenscreen(MEHRAN, KENYA, 850, 790)
    mehran_phimage = create_greened(mehran, MWID, MHEI)
    mehran = canvas.create_image(450, 530, image=mehran_phimage)
    canvas.update()
    time.sleep(1/2)

    canvas.itemconfigure(h, state='hidden')
    canvas.update()

    the_shakes(canvas, karel)

    h1 = canvas.create_text(15, 100, anchor='w', font='Garamond 38', fill='yellow', text='"I think I already see my friend,' )
    h2 = canvas.create_text(15, 150, anchor='w', font='Garamond 38', fill='yellow', text='poor Karel!" says Mehran squinting.')
    canvas.update()
    time.sleep(2)

    canvas.update()

    chris = greenscreen(CHRIS, 'images/Earth/chrisback.png', 0, 0)
    chris_phimage = create_greened(chris, 130, 130)
    chris = canvas.create_image(945, 530, image=chris_phimage)
    canvas.update()

    for i in range(50):
        canvas.move(chris, -5, 0)
        canvas.update()
        time.sleep(1/65)

    h3= canvas.create_text(990, 90, anchor='e', font='Garamond 38', fill='yellow', text='"Master Mehran!" calls the Jedi.')
    canvas.update()
    time.sleep(1/2)

    canvas.itemconfigure(h1, state='hidden')
    canvas.itemconfigure(h2, state='hidden')
    canvas.update()
    time.sleep(2)

    the_shakes(canvas, karel)

    canvas.itemconfigure(h3, state='hidden')
    h4 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='"Master Chris! I am so happy to see you,')
    h5 = canvas.create_text(15, 110, anchor='w', font='Garamond 38', fill='yellow', text='for several reasons!"')

    canvas.update()
    time.sleep(2)

    the_shakes(canvas, karel)

    time.sleep(1)
    h25= canvas.create_text(990, 60, anchor='e', font='Garamond 38', fill='yellow', text='"And I, you, old friend!')
    canvas.update()
    time.sleep(2)
    canvas.itemconfigure(h4, state='hidden')
    canvas.itemconfigure(h5, state='hidden')
    h6 = canvas.create_text(990, 110, anchor='e', font='Garamond 38', fill='yellow', text='How can I help?"')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(h6, state='hidden')
    canvas.itemconfigure(h25, state='hidden')

    h7 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='"As you see, my young apprentice')
    h8 = canvas.create_text(15, 110, anchor='w', font='Garamond 38', fill='yellow', text='is not used to lightspeed yet...')
    h9 = canvas.create_text(15, 160, anchor='w', font='Garamond 38', fill='yellow', text='Do you have anything to ease his sickness?"')

    canvas.update()
    time.sleep(3)

    the_shakes(canvas, karel)
    time.sleep(1)

    canvas.itemconfigure(h7, state='hidden')
    canvas.itemconfigure(h8, state='hidden')
    canvas.itemconfigure(h9, state='hidden')
    h10 = canvas.create_text(990, 60, anchor='e', font ='Garamond 38', fill='yellow', text= '"Of course! My friend Jedi Bright')
    h11 = canvas.create_text(990, 110, anchor='e', font ='Garamond 38', fill='yellow', text = 'made special pills just for this condition!"')
    canvas.update()
    time.sleep(2)

    beeper_phimage = create(BEEPER, 35, 30)
    beeper = canvas.create_image(get_left_x(canvas, chris)+30, get_top_y(canvas, chris)+30, image=beeper_phimage)
    canvas.update()
    time.sleep(1/30)

    the_shakes(canvas, karel)

    toss_item(canvas, beeper)

    the_shakes(canvas, karel)

    canvas.itemconfigure(beeper, state='hidden')
    canvas.update()
    time.sleep(1)
    canvas.itemconfigure(h10, state='hidden')
    canvas.itemconfigure(h11, state='hidden')
    time.sleep(1)

    karel_phimage = create(KAREL, KWID, KHEI)
    karel = canvas.create_image(350, 520, image=karel_phimage)
    canvas.update()
    time.sleep(1/2)

    jump(canvas, karel)

    h12 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='"Fantastic! As good as new!')
    canvas.update()
    time.sleep(2)
    h13 = canvas.create_text(15, 110, anchor='w', font='Garamond 38', fill='yellow', text='Thank you, Master Chris,')
    canvas.update()
    time.sleep(2)
    h20 = canvas.create_text(15, 160, anchor='w', font='Garamond 38', fill='yellow',text='and to your friend, as well!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(h12, state='hidden')
    canvas.itemconfigure(h13, state='hidden')
    canvas.itemconfigure(h20, state='hidden')
    canvas.update()
    time.sleep(1 / 2)

    h14 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='The reason we are here, my friend,')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(h14, state='hidden')
    canvas.update()
    time.sleep(1/2)

    h15 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='...a blue and yellow creature came to visit us today,')
    canvas.update()
    time.sleep(2)
    h16 = canvas.create_text(15, 110, anchor='w', font='Garamond 38', fill='yellow', text='and said this planet was in peril, needing help...')
    canvas.update()
    time.sleep(2)
    h17 = canvas.create_text(15, 160, anchor='w', font='Garamond 38', fill='yellow', text='What can we do?"')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(h15, state='hidden')
    canvas.itemconfigure(h16, state='hidden')
    canvas.itemconfigure(h17, state='hidden')
    canvas.update()
    time.sleep(1/2)

    h18 = canvas.create_text(990, 60, anchor='e', font='Garamond 38', fill='yellow', text='"Yes, our planet needs help - in medicine and information.')
    canvas.update()
    time.sleep(2)
    h19 = canvas.create_text(990, 110, anchor='e', font='Garamond 38', fill='yellow', text='The creature sounds familiar... ')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(h18, state='hidden')
    canvas.itemconfigure(h19, state='hidden')
    h24 = canvas.create_text(990, 60, anchor='e', font='Garamond 38', fill='yellow', text='but he might not be what you think he is...')
    canvas.update()
    time.sleep(2)
    h20 = canvas.create_text(990, 110, anchor='e', font='Garamond 38', fill='yellow', text='I will join you, as I would love to help!"')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(h20, state='hidden')
    canvas.itemconfigure(h24, state='hidden')
    canvas.update()

    h21 = canvas.create_text(15, 60, anchor='w', font='Garamond 38', fill='yellow', text='"Wonderful news!')
    canvas.update()
    time.sleep(1)
    h22 = canvas.create_text(15, 110, anchor='w', font='Garamond 38', fill='yellow', text='I was hoping you would join us."')
    canvas.update()
    time.sleep(1)
    h23 = canvas.create_text(45, 180, anchor='w', font='Garamond 48', fill='yellow', text='Next stop...')
    canvas.update()
    time.sleep(1)

    jump(canvas, karel)
    time.sleep(1)


    ############################################



    stanford_phimage = create(STANFORD, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=stanford_phimage)
    i = canvas.create_text(310, 150, anchor='w', font='Verdana 80', text="Stanford!")
    canvas.update()
    time.sleep(1/60)

    image = stanford_filer(STANFORD)
    stanford_phimage = create_greened(image, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=stanford_phimage)
    i = canvas.create_text(310, 150, anchor='w', font='Verdana 80', text="Stanford!")
    canvas.update()
    time.sleep(1/2)

    stanford_phimage = create(STANFORD, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=stanford_phimage)
    i = canvas.create_text(310, 150, anchor='w', font='Verdana 80', text="Stanford!")
    canvas.update()
    time.sleep(1)


    falcon = greenscreen_dark(FALCONB, STANFORD, 350, 0)
    falcon_phimage = create_greened(falcon, 310, 145)
    falcon = canvas.create_image(20, 300, image=falcon_phimage)
    canvas.update()

    for i in range(47):
        canvas.move(falcon, 10, 0)
        canvas.update()
        time.sleep(1/65)
    time.sleep(2)


    ############################################


    stanford_phimage = create(STANFORD1, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=stanford_phimage)

    python = greenscreen_python(PYTHON, 'images/Earth/pythonback.png', 10, 0)
    python_phimage = create_greened(python, 120, 130)
    python = canvas.create_image(740, 410, image=python_phimage)
    canvas.update()
    time.sleep(1)
    time.sleep(1/2)

    k4 = canvas.create_text(15, 570, anchor='w', font='Courier 32',text='Our heroes find their guide waiting for them...')
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(k4, state='hidden')

    mehran = greenscreen(MEHRAN,'images/Earth/back.png', 0, 0)
    mehran_phimage = create_greened(mehran, MWID, MHEI)
    mehran = canvas.create_image(-300, 530, image=mehran_phimage)

    chris = greenscreen(CHRIS, 'images/Earth/chrisback1.png' , 0, 0)
    chris_phimage = create_greened(chris, 130, 130)
    chris = canvas.create_image(-320, 527, image=chris_phimage)
    canvas.update()

    karel_phimage = create(KAREL, KWID, KHEI)
    karel = canvas.create_image(-320, 560, image=karel_phimage)
    canvas.update()
    time.sleep(1/2)

    forward(canvas, mehran, chris, karel)
    move_into_space(canvas, mehran, karel, chris)
    canvas.itemconfigure(k4, state='hidden')
    time.sleep(1)

    for i in range (2):
        jump(canvas, karel)

    k = canvas.create_oval(750, 200, 990, 370, fill='white', outline='black')
    k1 = canvas.create_text(get_left_x(canvas, k) + 35, get_top_y(canvas, k) + 80, anchor='w', font='Courier 30', text='Welcome!\nAnd\nthank you!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(k1, state='hidden')
    k2 = canvas.create_text(get_left_x(canvas, k) + 30, get_top_y(canvas, k) + 80, anchor='w', font='Courier 30',text="I'll take\n you to\nmy creator,")
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(k2, state='hidden')
    k3 = canvas.create_text(get_left_x(canvas, k) + 30, get_top_y(canvas, k) + 85, anchor='w', font='Courier 30', text="please\nfollow me!")
    canvas.update()
    time.sleep(3)
    canvas.itemconfigure(k, state='hidden')
    canvas.itemconfigure(k3, state='hidden')
    canvas.update()
    time.sleep(1/2)

    mehran_oval= canvas.create_oval(get_left_x(canvas, mehran)-50, get_top_y(canvas, mehran)- 200, get_left_x(canvas, mehran)+150, get_top_y(canvas, mehran)- 50, fill='white', outline='black')
    k4= canvas.create_text(get_left_x(canvas, mehran_oval)+10, get_top_y(canvas, mehran_oval)+70, anchor='w', font='Courier 22', text=' Oh we get\n text boxes\n at Stanford!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(mehran_oval, state='hidden')
    canvas.itemconfigure(k4, state='hidden')

    for i in range(3):
        canvas.move(python, 3, -2)
        canvas.update()
        time.sleep(1/50)
    for i in range(70):
        canvas.move(python, 5, 0)
        canvas.update()
        time.sleep(1/60)


    jump(canvas, mehran)

    forward(canvas, mehran, chris, karel)

    for i in range(15):
        canvas.move(mehran, 8, -4)
        canvas.move(chris, 8, -4)
        canvas.move(karel, 8, -3)
        canvas.update()
        time.sleep(1 / 65)
    for i in range(35):
        canvas.move(mehran, 9, 0)
        canvas.move(chris, 10, 0)
        canvas.move(karel, 14, -2)
        canvas.update()
        time.sleep(1 / 60)



    ############################################



    classroom_phimage = create(CHALK, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=classroom_phimage)


    rich = greenscreen(RICH, BBACK, 0,0)
    rich_phimage = create_greened(rich, MMW, MLW-5)
    rich = canvas.create_image(820, 400, image=rich_phimage)

    guido = greenscreen_python(GUIDO, BBACK,  0,0)
    guido_phimage = create_greened(guido, 173, MLH)
    guido = canvas.create_image(630, 370, image=guido_phimage)

    python = greenscreen_python(PYTHON, BBACK,  0,0)
    python_phimage = create_greened(python, KLW, KLH)
    python = canvas.create_image(500, 470, image=python_phimage)

    mehran = greenscreen(MEHRAN, BBACK,  0,0)
    mehran_phimage = create_greened(mehran, MLW, MLH)
    mehran = canvas.create_image(-110, 370, image=mehran_phimage)

    chris = greenscreen(CHRIS, BBACK,  0,0)
    chris_phimage = create_greened(chris, CLW, CLW)
    chris = canvas.create_image(-140, 399, image=chris_phimage)

    karel_phimage = create(KAREL, KHEI, KLW)
    karel = canvas.create_image(-215, 530, image=karel_phimage)
    canvas.update()
    time.sleep(1)


    for i in range (30):
        canvas.move(mehran, 5, 0)
        canvas.update()
        time.sleep(1/65)

    forward(canvas, mehran, chris, karel)
    time.sleep(1/2)
    jump(canvas, python)
    time.sleep(1)
    j= canvas.create_oval(5, 200, 200, 300, fill ='white', outline='black')
    j1=canvas.create_text(get_left_x(canvas, j), get_top_y(canvas, j)+50, anchor= 'w', font ='Courier 50', text= ' Dad!?')
    canvas.update()


    for i in range (2):
        jump(canvas, karel)
    time.sleep(1)
    for i in range(62):
        canvas.move(karel, 10,0)
        canvas.update()
        time.sleep(1 / 50)

    canvas.itemconfigure(j, state='hidden')
    canvas.itemconfigure(j1, state='hidden')
    canvas.update()

    jump(canvas, karel)
    jump(canvas, karel)

    rich_oval= canvas.create_oval(750, 150, 990, 310, fill ='white', outline='black')
    j3 = canvas.create_text(get_left_x(canvas, rich_oval)+ 30, get_top_y(canvas, rich_oval)+ 79, anchor= 'w', font ='Courier 36', text= 'Yes,\nKarel...')
    canvas.update()
    time.sleep(1/2)

    canvas.itemconfigure(j3, state='hidden')
    j4 = canvas.create_text(get_left_x(canvas, rich_oval) + 6, get_top_y(canvas, rich_oval) + 80, anchor='w', font='Courier 36', text= ' I am your\n father. ')
    time.sleep(2)

    for i in range(2):
        jump(canvas, karel)

    happy_dance(canvas, karel)

    for i in range(17):
        canvas.move(karel, 10, 0)
        canvas.update()
        time.sleep(1 / 50)

    jump(canvas, karel)

    time.sleep(1)
    canvas.itemconfigure(j4, state='hidden')
    j5 = canvas.create_text(get_left_x(canvas, rich_oval) + 10, get_top_y(canvas, rich_oval) + 79, anchor='w', font='Courier 26', text= " (I've always\n   wanted\n to say that!)")
    canvas.update()
    time.sleep(1)
    jump(canvas, rich)
    time.sleep(1/2)

    canvas.itemconfigure(j5, state='hidden')
    canvas.itemconfigure(rich_oval, state='hidden')
    chris_oval = canvas.create_oval(30, 150, 270, 300, fill='white', outline='black')
    j7 = canvas.create_text(get_left_x(canvas, chris_oval)+37, get_top_y(canvas, chris_oval) + 68, anchor='w', font='Courier 28', text= 'How can\nwe help?')
    canvas.update()
    time.sleep(2)

    mehran_oval = canvas.create_oval(300, 130, 570, 280, fill='white', outline='black')
    j9 = canvas.create_text(get_left_x(canvas, mehran_oval)+37, get_top_y(canvas, mehran_oval) + 68, anchor='w', font='Courier 28', text='Yes, who\ndo we fight?')
    canvas.update()
    time.sleep(1)
    saber = greenscreen_dark(SABER,BBACK, 0 ,0)
    saber_phimage = create_greened(saber, 100, 100)
    saber = canvas.create_image(get_left_x(canvas, mehran)+ 120, get_top_y(canvas, mehran), image= saber_phimage)
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(mehran_oval, state ='hidden')
    canvas.itemconfigure(chris_oval, state='hidden')
    canvas.itemconfigure(j7, state='hidden')
    canvas.itemconfigure(j9, state='hidden')

    guido_oval = canvas.create_oval(400, 110, 700, 300, fill='white', outline='black')
    j10 = canvas.create_text(get_left_x(canvas, guido_oval)+11, get_top_y(canvas, guido_oval)+93, anchor ='w',font='Courier 24', text= 'Not fight like that,\nwe fight with these: ')
    canvas.update()
    time.sleep(1/30)

    mask = greenscreen_python(MASK, BBACK, 0,0)
    mask_phimage = create_greened(mask, 60, 60)
    mask = canvas.create_image(get_left_x(canvas, guido)+ 80, get_top_y(canvas, guido)+ 65, image= mask_phimage)
    canvas. update()
    time.sleep(1/2)

    toss_item(canvas, mask)

    mask1 = greenscreen_python(MASK, BBACK, 0, 0)
    mask1_phimage = create_greened(mask1, 60, 60)
    mask1 = canvas.create_image(get_left_x(canvas, guido), get_top_y(canvas, guido) +60, image=mask1_phimage)
    canvas.update()
    time.sleep(1/40)

    for i in range (36):
        canvas.move(mask, -7, 0)
        canvas.update()
        time.sleep(1/60)

    toss_item(canvas, mask1)
    canvas.itemconfigure(saber, state='hidden')
    canvas.itemconfigure(j10, state='hidden')
    j11 = canvas.create_text(get_left_x(canvas, guido_oval) + 40, get_top_y(canvas, guido_oval) + 95, anchor='w',font='Courier 22', text='Our battle \nis silent.\nWe need knowledge\nand strength \nof character.')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j11, state='hidden')
    j12 = canvas.create_text(get_left_x(canvas, guido_oval) + 40, get_top_y(canvas, guido_oval) + 95, anchor='w', font='Courier 22', text=' I created\n Python,\n(as in, Monty,)\n in the hope to\n simplify and\n unite.')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j12, state='hidden')
    j13 = canvas.create_text(get_left_x(canvas, guido_oval) + 35, get_top_y(canvas, guido_oval) + 95, anchor='w',font='Courier 22', text='In this time\nof peril, I know\nPython could help\nothers.')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j13, state='hidden')
    j23 = canvas.create_text(get_left_x(canvas, guido_oval) + 35, get_top_y(canvas, guido_oval) + 95, anchor='w', font='Courier 22', text='To a novice\nthe language\nis difficult.')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j23, state='hidden')
    j24 = canvas.create_text(get_left_x(canvas, guido_oval) + 45, get_top_y(canvas, guido_oval) + 95, anchor='w', font='Courier 22', text='I ask, how\ncan we reach\nas many people\nas possible?')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(chris_oval, state='normal')
    j14 = canvas.create_text(get_left_x(canvas, chris_oval) + 20, get_top_y(canvas, chris_oval) + 75, anchor='w', font='Courier 22', text='Leave it to us!\nWe will educate\nthe planet!')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j24, state='hidden')
    j15 = canvas.create_text(get_left_x(canvas, guido_oval) + 70, get_top_y(canvas, guido_oval) + 90, anchor='w', font='Courier 28', text='Huzzah!')
    canvas.update()
    jump(canvas, guido)
    time.sleep(2)

    canvas.itemconfigure(j15, state='hidden')
    canvas.itemconfigure(guido_oval, state='hidden')
    canvas.itemconfigure(j14, state='hidden')
    j20 = canvas.create_text(get_left_x(canvas, chris_oval) + 25, get_top_y(canvas, chris_oval) + 75, anchor='w', font='Courier 22', text="We are familiar\nwith this \ncreature's\nlanguage!")
    canvas.update()
    time.sleep(4)


    canvas.itemconfigure(mehran_oval, state='normal')
    j16 = canvas.create_text(get_left_x(canvas, mehran_oval) + 30, get_top_y(canvas, mehran_oval) + 75, anchor='w',font='Courier 22', text='And our friend\nKarel is trained\nto be a gateway!')
    canvas.update()
    time.sleep(2)
    canvas.move(beeper, 980, 590)
    canvas.itemconfigure(beeper, state='normal')
    time.sleep(2)
    jump(canvas, karel)

    canvas.itemconfigure(j20, state='hidden')
    canvas.itemconfigure(j16, state='hidden')
    canvas.itemconfigure(mehran_oval, state='hidden')
    j17 = canvas.create_text(get_left_x(canvas, chris_oval) + 25, get_top_y(canvas, chris_oval) + 75, anchor='w', font='Courier 22', text='We will need \nto call\non our fellow')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(j17, state='hidden')
    j22 = canvas.create_text(get_left_x(canvas, chris_oval) + 21, get_top_y(canvas, chris_oval) + 75, anchor='w', font='Courier 22', text='Jedi Masters\nto fulfill \nthis great task!')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(mehran_oval, state='normal')
    j18 = canvas.create_text(get_left_x(canvas, mehran_oval) + 35, get_top_y(canvas, mehran_oval) + 75, anchor='w', font='Courier 22', text='If we both\nuse the Force\nwe could reach\nhundreds!')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(j22, state='hidden')
    canvas.itemconfigure(j18, state='hidden')
    canvas.itemconfigure(mehran_oval, state='hidden')
    canvas.itemconfigure(chris_oval, state='hidden')
    canvas.itemconfigure(guido_oval, state='normal')
    j19 = canvas.create_text(get_left_x(canvas, guido_oval) + 31, get_top_y(canvas, guido_oval) + 95, anchor='w', font='Courier 26', text='Do you think\nthey will come?')
    canvas.update()
    time.sleep(3)

    for i in range(5):
        the_shakes_for_two(canvas, mehran, chris)



    ############################################




    mtrain_phimage = create(MTRAIN, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=mtrain_phimage)
    canvas.update()
    time.sleep(1/2)
    xwing5 = greenscreen(XWING, MTRAINCEN, 0, 0)
    xwing5_phimage = create_greened(xwing5, 150, 130)
    xwing5 = canvas.create_image(500, -200, image=xwing5_phimage)
    canvas.update()
    time.sleep(1 / 30)
    for i in range(26):
        canvas.move(xwing5, 0, 10)
        canvas.update()
        time.sleep(1/65)

    time.sleep(2)

    xwing_phimage = rx_wing_sky(canvas, RXWING)
    xwing = canvas.create_image(700,130, image= xwing_phimage)
    canvas.update()
    time.sleep(1)
    #canvas.coords(xwing)
    # if canvas.find_overlapping(xwing) < 0:
    #     canvas.move(xwing, 1, 1)
    #     canvas.update()
    #     time.sleep(1/60)

    xwing1_phimage = lx_wing_sky(canvas, LXWING)
    xwing1 = canvas.create_image(200, 100, image= xwing1_phimage)
    #not_covering(canvas, xwing1)
    canvas.update()
    time.sleep(1/30)

    time.sleep(1)

    xwing37_phimage = r2x_wing_sky(canvas, RXWING)
    xwing37 = canvas.create_image(870, 40, image = xwing37_phimage)
    #not_covering(canvas, xwing37)
    canvas.update()
    time.sleep(1/3)

    xwing3_phimage = l1x_wing_cloud(canvas, LXWING)
    xwing3 = canvas.create_image(150, 240, image=xwing3_phimage)
    #not_covering(canvas, xwing3)
    canvas.update()
    time.sleep(1 / 3)

    xwing2_phimage = r1x_wing_sky(canvas, RXWING)
    xwing2 = canvas.create_image(800, 100, image=xwing2_phimage)
    #not_covering(canvas, xwing2)
    canvas.update()
    time.sleep(1 / 5)

    xwing6_phimage = l2x_wing_sky(canvas, LXWING)
    xwing6 = canvas.create_image(80, 170, image=xwing6_phimage)
    #not_covering(canvas, xwing6)
    canvas.update()
    time.sleep(1 / 5)

    xwing7_phimage = rx_wing_sky(canvas, RXWING)
    xwing7 = canvas.create_image(640, 150, image=xwing7_phimage)
    canvas.update()
    time.sleep(1 / 10)


    xwing8_phimage = l1x_wing_clear(canvas, LXWING)
    xwing8 = canvas.create_image(400, 40, image=xwing8_phimage)
    canvas.update()
    time.sleep(1 / 10)


    xwing9_phimage = l1x_wing_clear(canvas, LXWING)
    xwing9 = canvas.create_image(220, 30, image=xwing9_phimage)
    canvas.update()
    time.sleep(1 / 30)


    xwing10_phimage = r2x_wing_sky(canvas, RXWING)
    xwing10 = canvas.create_image(950, 120, image=xwing10_phimage)
    canvas.update()
    time.sleep(1 / 30)


    xwing11_phimage = lx_wing_sky(canvas, LXWING)
    xwing11 = canvas.create_image(372, 170, image=xwing11_phimage)
    canvas.update()
    time.sleep(1 / 30)


    xwing12_phimage = r1x_wing_sky(canvas, RXWING)
    xwing12 = canvas.create_image(680, 40, image=xwing12_phimage)
    canvas.update()
    time.sleep(1 / 30)


    xwing13_phimage = l1x_wing_clear(canvas, LXWING)
    xwing13 = canvas.create_image(120, 120, image=xwing13_phimage)
    canvas.update()
    time.sleep(1 / 50)

    xwing14_phimage = rx_wing_sky(canvas, RXWING)
    xwing14 = canvas.create_image(780, 20, image=xwing14_phimage)
    canvas.update()
    time.sleep(1 / 50)


    xwing15_phimage = l2x_wing_sky(canvas, LXWING)
    xwing15 = canvas.create_image(290, 100, image=xwing15_phimage)
    canvas.update()
    time.sleep(1 / 50)


    xwing16_phimage = r2x_wing_sky(canvas, RXWING)
    xwing16 = canvas.create_image(855, 155, image=xwing16_phimage)
    canvas.update()
    time.sleep(1 / 60)


    xwing17_phimage = lx_wing_sky(canvas, LXWING)
    xwing17 = canvas.create_image(190, 180, image=xwing17_phimage)
    canvas.update()
    time.sleep(1 / 60)


    xwing18_phimage = rx_wing_cloud(canvas, RXWING)
    xwing18 = canvas.create_image(950, 250, image=xwing18_phimage)
    canvas.update()
    time.sleep(1 / 60)


    xwing19_phimage = l2x_wing_sky(canvas, LXWING)
    xwing19 = canvas.create_image(50, 50, image=xwing19_phimage)
    canvas.update()
    time.sleep(1 / 70)


    xwing20_phimage = r1x_wing_sky(canvas, RXWING)
    xwing20 = canvas.create_image(700, 100, image=xwing20_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing21_phimage = lx_wing_clear(canvas, LXWING)
    xwing21 = canvas.create_image(260, 40, image=xwing21_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing22_phimage = r1x_wing_cloud(canvas, RXWING)
    xwing22 = canvas.create_image(850, 220, image=xwing22_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing23_phimage = lx_wing_clear(canvas, LXWING)
    xwing23 = canvas.create_image(350, 30, image=xwing23_phimage)
    canvas.update()
    time.sleep(1 / 60)

    xwing24_phimage = rx_wing_cloud(canvas, RXWING)
    xwing24 = canvas.create_image(700, 190, image=xwing24_phimage)
    canvas.update()
    time.sleep(1 / 60)

    xwing25_phimage = lx_wing_clear(canvas, LXWING)
    xwing25 = canvas.create_image(175, 45, image=xwing25_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing26_phimage = r1x_wing_sky(canvas, RXWING)
    xwing26 = canvas.create_image(599, 48, image=xwing26_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing27_phimage = lx_wing_clear(canvas, LXWING)
    xwing27 = canvas.create_image(130, 65, image=xwing27_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing28_phimage = rx_wing_sky(canvas, RXWING)
    xwing28 = canvas.create_image(790, 170, image=xwing28_phimage)
    canvas.update()
    time.sleep(1 / 70)

    xwing29_phimage = l1x_wing_clear(canvas, LXWING)
    xwing29 = canvas.create_image(180, 140, image=xwing29_phimage)
    canvas.update()
    time.sleep(1 / 80)

    xwing30_phimage = rx_wing_sky(canvas, RXWING)
    xwing30 = canvas.create_image(720, 150, image=xwing30_phimage)
    canvas.update()
    time.sleep(1 / 80)

    xwing38_phimage = r1x_wing_sky(canvas, RXWING)
    xwing38 = canvas.create_image(750, 50, image=xwing38_phimage)
    canvas.update()
    time.sleep(1 / 90)

    xwing31_phimage = l1x_wing_clear(canvas, LXWING)
    xwing31 = canvas.create_image(400, 70, image=xwing31_phimage)
    canvas.update()
    time.sleep(1 / 90)

    xwing32_phimage = rx_wing_cloud(canvas, RXWING)
    xwing32 = canvas.create_image(740, 220, image=xwing32_phimage)
    canvas.update()
    time.sleep(1 / 90)

    xwing33_phimage = lx_wing_cloud(canvas, LXWING)
    xwing33 = canvas.create_image(100, 250, image=xwing33_phimage)
    canvas.update()
    time.sleep(1 / 90)

    xwing34_phimage = r1x_wing_sky(canvas, RXWING)
    xwing34 = canvas.create_image(630, 85, image=xwing34_phimage)
    canvas.update()
    time.sleep(1 / 90)

    xwing35_phimage = lx_wing_cloud(canvas, LXWING)
    xwing35 = canvas.create_image(278, 200, image=xwing35_phimage)
    canvas.update()
    time.sleep(1/40)


    xwing36= greenscreen(FXWING, MTRAIN, 0, 10)
    xwing36_phimage = create_greened(xwing36, 1000, 517)
    xwing36 = canvas.create_image(500, 20, image = xwing36_phimage)
    canvas.update()
    time.sleep(1/65)

    for i in range(33):
        canvas.move(xwing36, 0, 10)
        canvas.update()
        time.sleep(1/65)

    time.sleep(2)

    john = greenscreen_python('images/Ourplayers/john.png', 'images/ThisnThat/heroback.png', 30, 50)
    john_phimage = create_greened(john, 83, 85)
    john = canvas.create_image(505, 232, image = john_phimage)
    canvas.update()
    time.sleep(2)

    jump(canvas, john)

    time.sleep(2)
    canvas.itemconfigure(xwing36, state='hidden')




    ############################################




    stanford_phimage = create(STANFORD2, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=stanford_phimage)


    rich = greenscreen(RICH, STAN1, 0, 0)
    rich_phimage = create_greened(rich, MWID, MMW)
    rich = canvas.create_image(770, 530, image=rich_phimage)

    guido = greenscreen_python(GUIDO, STAN, 0, 0)
    guido_phimage = create_greened(guido, MLH, MLW)
    guido = canvas.create_image(610, 520, image=guido_phimage)

    mehran = greenscreen(MEHRAN, STAN1, 0, 0)
    mehran_phimage = create_greened(mehran, MMW, MLW)
    mehran = canvas.create_image(360, 520, image=mehran_phimage)

    chris = greenscreen(CHRIS, STAN1, 0, 0)
    chris_phimage = create_greened(chris, MLW, MLW)
    chris = canvas.create_image(180, 523, image=chris_phimage)

    karel_phimage = create(KAREL, KHEI, KLW)
    karel = canvas.create_image(890, 550, image=karel_phimage)

    python = greenscreen_python(PYTHON, STAN, 0,0)
    python_phimage = create_greened(python, KHEI, KLW)
    python = canvas.create_image(490, 530, image= python_phimage)
    canvas.update()
    time.sleep(1/2)

    for i in range(17):
        canvas.move(rich, 0, -3)
        canvas.move(chris, 0, -5)
        canvas.move(mehran, 0, -6)
        canvas.move(guido, 0, -3)
        canvas.update()
        time.sleep(1 / 50)
    time.sleep(1/7)
    for i in range(17):
        canvas.move(rich, 0, 3)
        canvas.move(chris, 0, 5)
        canvas.move(mehran, 0, 6)
        canvas.move(guido, 0, 3)
        canvas.update()
        time.sleep(1 / 50)

    guido_oval = canvas.create_oval(490, 220, 760, 430, fill='white', outline='black', state= 'hidden')
    rich_oval = canvas.create_oval(720, 290, 996, 460, fill='white', outline='black')
    chris_oval = canvas.create_oval(20, 210, 295, 440, fill='white', outline='black', state= 'hidden')
    mehran_oval = canvas.create_oval(260, 170, 555, 380, fill='white', outline='black', state='hidden')
    rich_text = get_left_x(canvas, rich_oval)+35, get_top_y(canvas, rich_oval)+ 80
    guido_text = get_left_x(canvas, guido_oval)+12, get_top_y(canvas, guido_oval)+ 100
    mehran_text = get_left_x(canvas, mehran_oval)+15, get_top_y(canvas, mehran_oval)+ 105
    chris_text = get_left_x(canvas, chris_oval)+20, get_top_y(canvas, chris_oval)+ 112

    w = canvas.create_text(rich_text, anchor ='w', font ='Courier 26', text= 'This is\nincredible!')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(w, state='hidden')
    canvas.itemconfigure(rich_oval, state='hidden')
    canvas.itemconfigure(guido_oval, state='normal')
    w1 = canvas.create_text(guido_text, anchor='w', font='Courier 22', text='The people of Earth\nwill be so grateful\nfor the knowledge!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(w1, state='hidden')
    w2 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text='We are indebted\nto you all!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(rich_oval, state='normal')
    w3 = canvas.create_text(rich_text, anchor='w', font='Courier 26', text='How can we\nrepay you?')
    canvas.update()
    time.sleep(2)

    jump(canvas, karel)
    time.sleep(1)

    canvas.itemconfigure(chris_oval, state='normal')
    canvas.itemconfigure(guido_oval, state='hidden')
    canvas.itemconfigure(rich_oval, state='hidden')
    canvas.itemconfigure(w2, state='hidden')
    canvas.itemconfigure(w3, state='hidden')
    w11 = canvas.create_text(chris_text, anchor='w', font='Courier 26', text=' There is no\n need to repay.\n We teach\n out of love!')
    canvas.update()
    time.sleep(4)
    canvas.itemconfigure(w11, state='hidden')
    w11 = canvas.create_text(chris_text, anchor='w', font='Courier 26', text='... However,\nif you are\nasking...')
    canvas.update()
    time.sleep(2)
    canvas.itemconfigure(w11, state='hidden')
    w4 = canvas.create_text(chris_text, anchor='w', font='Courier 26', text='During my time\nas a Jedi\nI feel I am\nmissing...')
    canvas.update()
    time.sleep(4)
    canvas.itemconfigure(w4, state='hidden')
    w5 = canvas.create_text(chris_text, anchor='w', font='Courier 26', text="... something.\nBut I don't know\nwhat that\ncould be...")
    canvas.update()
    time.sleep(4)
    canvas.update()

    canvas.itemconfigure(chris_oval, state='hidden')
    canvas.itemconfigure(guido_oval, state='normal')
    canvas.itemconfigure(w5, state='hidden')
    w6 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text='I have an idea!')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(w6, state='hidden')
    w7 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' In my travels\n I came across\n a prized\n specimen...')
    canvas.update()
    time.sleep(4)

    simba = greenscreen(SIMBA, STAN1, 0,0)
    simba_phimage = create_greened(simba, KLW, KLW)
    simba = canvas.create_image(70, -100, image=simba_phimage)
    canvas.update()
    time.sleep(1/65)
    for i in range(65):
        canvas.move(simba, 0, 10)
        canvas.update()
        time.sleep(1/30)
    time.sleep(1/2)
    jump(canvas, simba)
    time.sleep(1)
    canvas.itemconfigure(w7, state='hidden')
    w8 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' Considered the\n "goodest boy"\n in the land..')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(w8, state='hidden')
    w9 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' And revered\n in many\n cultures:')
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(w9, state='hidden')
    w10 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' Master Chris,\n please accept\n     Simba!')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(guido_oval, state='hidden')
    canvas.itemconfigure(w10, state='hidden')

    simba1 = warhol(SIMBA)
    simba1_phimage = create_greened(simba1, CANVAS_WIDTH, CANVAS_HEIGHT)
    simba1 = canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=simba1_phimage)
    canvas.update()
    time.sleep(2)

    simba2_phimage = create(SIMBA, 200, 200)
    simba2 = canvas.create_image(500, 300, image=simba2_phimage)
    canvas.update()
    time.sleep(1 / 65)
    jump(canvas, simba2)
    jump(canvas, simba2)
    time.sleep(2)

    canvas.itemconfigure(simba1, state='hidden')
    canvas.itemconfigure(simba2, state='hidden')

    jump(canvas, chris)
    happy_dance(canvas, chris)
    jump(canvas, simba)

    time.sleep(1/5)

    canvas.itemconfigure(guido_oval, state='normal')
    w11 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' Master Mehran,\n what might\n you want?')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(guido_oval, state='hidden')
    canvas.itemconfigure(w11, state='hidden')
    canvas.itemconfigure(mehran_oval, state='normal')
    w12 = canvas.create_text(mehran_text, anchor='w', font='Courier 26', text='\nTo be honest..\n')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(w12, state='hidden')
    w13 = canvas.create_text(mehran_text, anchor='w', font='Courier 26', text="  I've been\n  dreaming of\n  a food...")
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(w13, state='hidden')
    w14 = canvas.create_text(mehran_text, anchor='w', font='Courier 26', text=" That's wrapped\n in itself...")
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(w14, state='hidden')
    w15 = canvas.create_text(mehran_text, anchor='w', font='Courier 26', text="  but better\n  than a taco...")
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(mehran_oval, state='hidden')
    canvas.itemconfigure(w15, state='hidden')
    canvas.itemconfigure(guido_oval, state='normal')
    w16 = canvas.create_text(guido_text, anchor='w', font='Courier 26', text=' Say no more!\n We have exactly\n the thing!')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(w16, state='hidden')
    w17 = canvas.create_text(guido_text, anchor='w', font='Courier 26',text=' How many\n would you like?')
    canvas.update()
    time.sleep(3)

    canvas.itemconfigure(guido_oval, state='hidden')
    canvas.itemconfigure(w17, state='hidden')
    canvas.itemconfigure(mehran_oval, state='normal')
    w18 = canvas.create_text(mehran_text, anchor='w', font='Courier 26',text=" I don't know!\n How many would I\n like?")
    canvas.update()
    time.sleep(1)


    mehran1 = greenscreen(MEHRANLARGE, MEHSTAN, 0, 0)
    mehran1_phimage = create_greened(mehran1, MMW*4, MMW*4)
    mehran1 = canvas.create_image(430, 390, image=mehran1_phimage)
    canvas.update()
    time.sleep(1/2)

    mehran2 = greenscreen(MEHRANLARGE, MEHSTAN, 0, 0)
    mehran2_phimage = create_greened(mehran2, MMW * 9, MMW *9)
    mehran2 = canvas.create_image(500, 440, image=mehran2_phimage)
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(mehran2, state='hidden')
    canvas.itemconfigure(mehran1, state='hidden')
    w19= canvas.create_text(37, 50, anchor ='w', font= 'Courier 40', text= "How many burritos shall we give Mehran?\n     Answer in the terminal!")
    canvas.update()
    time.sleep(1/2)

    num_burr = int(input("How many burritos should Mehran get? Don't be shy, interspace travel builds an appetite! "))


    burrito = warhol(BURRITO)
    burrito_phimage = create_greened(burrito, CANVAS_WIDTH, CANVAS_HEIGHT)
    burrito = canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=burrito_phimage)
    canvas.update()
    time.sleep(1)

    canvas.create_text(450, 240, anchor='w', font='Verdana 60', text= str(num_burr))
    canvas.create_text(450, 330, anchor='w', font='Verdana 60', text= 'BURRITOS!!')
    canvas.update()
    time.sleep(1)

    mehran = greenscreen(MEHRAN, 'images/This n That/red_burr.png', 5, 0)
    mehran_phimage = create_greened(mehran, 180, 190)
    mehran = canvas.create_image(310, 305, image= mehran_phimage)
    canvas.update()
    time.sleep(1)

    for i in range(2):
        jump(canvas, mehran)
    happy_dance(canvas, mehran)

    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(burrito, state='hidden')



    ############################################



    earthclose_phimage = create('images/Space/earthscape.png', CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH, CANVAS_HEIGHT, anchor=tkinter.SE, image=earthclose_phimage)
    canvas.update()
    time.sleep(2)

    z10 = canvas.create_text(450, 220, anchor='w', font="Verdana 36", fill='yellow', text='Six weeks later...')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(z10, state='hidden')
    canvas.update()
    time.sleep(1)

    z11= canvas.create_text(50, 120, anchor='w', font= "Verdana 36", fill ='yellow', text="Our Masters journeyed home!")
    canvas.update()
    time.sleep(2)

    z12 = canvas.create_text(50, 170, anchor='w', font="Verdana 36", fill='yellow', text="Master Chris with his new companion,")
    canvas.update()
    time.sleep(2)

    z13 = canvas.create_text(50, 220, anchor='w', font="Verdana 36", fill='yellow', text="and Master Mehran with " + str(num_burr))
    z25 = canvas.create_text(50, 270, anchor='w', font="Verdana 36", fill='yellow', text="burritos to tie him over.")
    canvas.update()
    time.sleep(4)

    canvas.itemconfigure(z11, state='hidden')
    canvas.itemconfigure(z12, state='hidden')
    canvas.itemconfigure(z13, state='hidden')
    canvas.itemconfigure(z25, state='hidden')
    canvas.update()
    time.sleep(1/2)

    z18 = canvas.create_text(50, 120, anchor='w', font="Verdana 36", fill='yellow', text="Karel remained on Earth...")
    canvas.update()
    time.sleep(2)

    z19 = canvas.create_text(50, 170, anchor='w', font="Verdana 36", fill='yellow', text="reunited with its creator,")
    canvas.update()
    time.sleep(2)

    z20 = canvas.create_text(50, 220, anchor='w', font="Verdana 36", fill='yellow', text="and aiding generations to come.")
    canvas.update()
    time.sleep(2)

    z9 = canvas.create_text(450, 300, anchor='w', font="Verdana 33", fill='yellow',text='And so...')
    canvas.update()
    time.sleep(2)

    canvas.itemconfigure(z18, state='hidden')
    canvas.itemconfigure(z19, state='hidden')
    canvas.itemconfigure(z20, state='hidden')
    canvas.update()
    time.sleep(2)
    canvas.itemconfigure(z9, state='hidden')
    canvas.update()
    time.sleep(1 / 2)

    z1 = canvas.create_text(50, 170, anchor='w', font="Verdana 36", fill='yellow', text= "Karel's unexpected journey comes to a close!")
    canvas.update()
    time.sleep(3)

    z = canvas.create_text(50, 240, anchor='w', font="Verdana 36", fill='yellow', text="Thank you, gentle participant!")
    canvas.update()
    time.sleep(5)
    canvas.itemconfigure(z, state='hidden')
    canvas.itemconfigure(z1, state='hidden')
    canvas.update()
    time.sleep(1/2)

    z30= canvas.create_line(30, 30, 30, 400, fill='yellow')
    z31= canvas.create_line(30, 30, 900, 30, fill='yellow')
    z2 = canvas.create_text(60, 150, anchor='w', font= "Verdana 33", fill = 'yellow', text="Because of the efforts of Prof. Mehran,\nProf. Chris, and hundreds others,\nover 10,000 people joined together\nas one student body, and began the study\nof an invaluable tool.")
    canvas.update()
    time.sleep(10)

    canvas.itemconfigure(z2, state='hidden')
    canvas.update()
    time.sleep(1/2)

    z14 = canvas.create_text(60, 150, anchor='w', font="Verdana 33", fill='yellow', text='In this small way, our planet united.\nDuring a time of uncertainty, we crossed oceans,\nlanguages, and cultures to humbly learn\na new skill, and in turn,\nstrengthen our humanity.')
    canvas.update()
    time.sleep(11)
    canvas.itemconfigure(z14, state='hidden')
    canvas.update()
    time.sleep(1)

    z7 = canvas.create_text(70, 120, anchor='w', font="Verdana 33", fill= 'yellow', text='Thank you Prof. Mehran, Prof. Chris,\nand the 800 + Volunteers that selflessly\n"flew to the rescue".')
    canvas.update()
    time.sleep(4)

    falcon = greenscreen_dark(FALCONB, 'images/Space/earthscape.png', 0, 0)
    falcon_phimage = create_greened(falcon, 100, 40)
    falcon = canvas.create_image(-100, 330, image=falcon_phimage)
    canvas.update()
    while not is_past_middle(canvas, falcon):
        canvas.move(falcon, 5,0)
        canvas.update()
        time.sleep(1/50)
    for i in range (70):
        canvas.move(falcon, 10, 0)
        canvas.update()
        time.sleep(1/50)
    time.sleep(1)

    canvas.create_text(980, 585, anchor='e', font='Papyrus 20', fill='black', text='Final Project . Code in Place . Sp 2020 . Jacquelynne Fontaine')
    print('')
    print('')
    print("Thank you for participating! Karel's unexpected journey is now finished.")
    print("Have a lovely day!")
    canvas.update()
    time.sleep(7)

    canvas.itemconfigure(z30, state='hidden')
    canvas.itemconfigure(z31, state='hidden')
    canvas.itemconfigure(z7, state='hidden')
    canvas.update()
    time.sleep(1/2)

    time.sleep(2)

    canvas.mainloop()






########################################################################################################################



def create(image, width, length):
    image1 = SimpleImage(image)
    image1.pil_image = image1.pil_image.resize((width, length))
    image2 = ImageTk.PhotoImage(image1.pil_image)
    return image2

def create_landscape(image, width, length):
    image1 = SimpleImage(image)
    image1.pil_image = image1.pil_image.resize((width, length))
    image2 = ImageTk.PhotoImage(image1.pil_image)
    return image2

def create_greened(image, width, length):
    image1 = image
    image1.pil_image = image1.pil_image.resize((width, length))
    image2 = ImageTk.PhotoImage(image1.pil_image)
    return image2

def greenscreen(image1, image2, x1, y1):
    image = SimpleImage(image1)
    image2 = SimpleImage(image2)
    for y in range(image.height):
        for x in range (image.width):
            pixel =image.get_pixel(x, y)
            if pixel.red >= 245 and pixel.blue >=245 and pixel.green >= 245:
                pixel = image2.get_pixel(x1+ x, y1+ y)
                image.set_pixel(x, y, pixel)
    return image

def the_shakes(canvas, image):
    for i in range(8):
        canvas.move(image, 3, 0)
        canvas.update()
        time.sleep(1 / 40)
        canvas.move(image, -3, 0)
        canvas.update()
        time.sleep(1 / 40)

def the_shakes_for_two(canvas, item, item1):
    for i in range(8):
        canvas.move(item, 3, 0)
        canvas.move(item1, -3, 0)
        canvas.update()
        time.sleep(1 / 40)
        canvas.move(item, -3, 0)
        canvas.move(item1, 3, 0)
        canvas.update()
        time.sleep(1 / 40)

def jump(canvas, image):
    for i in range(9):
        canvas.move(image, 0, -3)
        canvas.update()
        time.sleep(1 / 50)
    for i in range(9):
        canvas.move(image, 0, 3)
        canvas.update()
        time.sleep(1 / 50)
    return image

def happy_dance(canvas, image):
    for i in range(2):
        for i in range(9):
            canvas.move(image, -2, -3)
            canvas.update()
            time.sleep(1 / 50)
        for i in range(9):
            canvas.move(image, -2, 3)
            canvas.update()
            time.sleep(1 / 50)
        for i in range(9):
            canvas.move(image, 2, -3)
            canvas.update()
            time.sleep(1 / 50)
        for i in range(9):
            canvas.move(image, 2, 3)
            canvas.update()
            time.sleep(1 / 50)

def greenscreen_python(image1, image2, x1, y1):
    image= SimpleImage(image1)
    image2 = SimpleImage(image2)
    for y in range(image.height):
        for x in range (image.width):
            pixel =image.get_pixel(x, y)
            if pixel.red >= 230 and pixel.blue >=230 and pixel.green >= 230:
                pixel = image2.get_pixel(x1+ x, y1+ y)
                image.set_pixel(x, y, pixel)
    return image

def greenscreen_dark(image1, image2, x1, y1):
    image= SimpleImage(image1)
    image2 = SimpleImage(image2)
    for y in range(image.height):
        for x in range (image.width):
            pixel =image.get_pixel(x, y)
            if pixel.red <= 0 and pixel.blue <= 0 and pixel.green <= 0:
                pixel = image2.get_pixel(x1+ x, y1+ y)
                image.set_pixel(x, y, pixel)
    return image

def forward(canvas, item, item1, item2):
    for i in range(40):
        canvas.move(item, 8, 0)
        canvas.move(item1, 8, 0)
        canvas.move(item2, 8, 0)
        canvas.update()
        time.sleep(1/65)

def move_into_space(canvas, item, item1, item2):
    for i in range(20):
        canvas.move(item, 4, 0)
        canvas.move(item1, 4, 0)
        canvas.move(item2, 4, 0)
        canvas.update()
        time.sleep(1 / 80)

    for i in range(50):
        canvas.move(item, 5, -1)
        canvas.move(item1, 1, 0)
        canvas.move(item2, 3, 0)
        canvas.update()
        time.sleep(1 / 60)

    for i in range(10):
        canvas.move(item, 5, 0)
        canvas.move(item1, 2, -1)
        canvas.move(item2, 5, -1)
        canvas.update()
        time.sleep(1 / 60)

def greenscreen_medium(image1, image2, x1, y1):
    image= SimpleImage(image1)
    image2 = SimpleImage(image2)
    for y in range(image.height):
        for x in range (image.width):
            pixel =image.get_pixel(x, y)
            if pixel.red >= 245 and pixel.blue >=245 and pixel.green >= 245:
                pixel = image2.get_pixel(x1, y1)
                image.set_pixel(x, y, pixel)
    return image

def make_sick(image):
    image = SimpleImage(image)
    for pixel in image:
        pixel.red *= .5
        pixel.green == 255
        pixel.blue *=.5
    return image

def toss_item(canvas, image):
    for i in range (25):
        canvas.move(image, -6, -6)
        canvas.update()
        time.sleep(1/65)

    for i in range (20):
        canvas.move(image, -5, 0)
        canvas.update()
        time.sleep(1/65)

    for i in range (18):
        canvas.move(image, -6, 6)
        canvas.update()
        time.sleep(1/65)

def rx_wing_sky(canvas, image):
    xwing = greenscreen(image, MTRAINRG, 0, 0)
    image = create_greened(xwing, 30, 20)
    return image

def rx_wing_cloud(canvas, image):
    xwing = greenscreen(image, CLOUDR, 0, 0)
    image = create_greened(xwing, 30, 20)
    return image

def lx_wing_sky(canvas, image):
    xwing = greenscreen_dark(image, MTRAINLF, 0, 0)
    image = create_greened(xwing, 50, 24)
    return image

def lx_wing_cloud(canvas, image):
    xwing = greenscreen_dark(image, CLOUD, 0, 0)
    image = create_greened(xwing, 50, 24)
    return image

def lx_wing_clear(canvas, image):
    xwing = greenscreen_dark(image, MTRAINCLR, 0, 0)
    image = create_greened(xwing, 50, 24)
    return image

def l1x_wing_sky(canvas, image):
    xwing = greenscreen_dark(image, MTRAINLF, 0, 0)
    image = create_greened(xwing, 30, 15)
    return image

def l1x_wing_cloud(canvas, image):
    xwing = greenscreen_dark(image, CLOUD, 0, 0)
    image = create_greened(xwing, 30, 15)
    return image

def l1x_wing_clear(canvas, image):
    xwing = greenscreen_dark(image, MTRAINCLR, 0, 0)
    image = create_greened(xwing, 30, 15)
    return image

def r1x_wing_sky(canvas, image):
    xwing = greenscreen(image, MTRAINRG, 0, 0)
    image = create_greened(xwing, 50, 33)
    return image

def r1x_wing_cloud(canvas, image):
    xwing = greenscreen(image, CLOUDR, 0, 0)
    image = create_greened(xwing, 50, 33)
    return image

def l2x_wing_sky(canvas, image):
    xwing = greenscreen_dark(image, MTRAINLF, 0, 0)
    image = create_greened(xwing, 90, 75)
    return image

def r2x_wing_sky(canvas, image):
    xwing = greenscreen(image, MTRAINRG, 0, 0)
    image = create_greened(xwing, 90, 70)
    return image

def not_covering(canvas, image):
#does not work yet
    if canvas.find_overlapping(image) > 0:
        canvas.move(image, 1, 1)
        canvas.update()
        time.sleep(1/60)
    return image

def stanford_filer(image):
    image = SimpleImage(image)
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= 0.7
        pixel.blue *= 1.5
    return image

def warhol(image):
    """
    This function creates the separate adjusted images from the original,
    adjusting the colors based on the values given, then combines them
    to create a warhol effect.
    """
    og_image = SimpleImage(image)
    pink = make_recolored(image, 1.2, 0, 1.2)
    green = make_recolored(image, .5, 1.2, .5)
    blue = make_recolored(image, .5, 1, 2.2)
    yellow = make_recolored(image, 2, 2, .4)
    brighter = make_recolored(image, 1.5, 1.5, 1.5)
    darker = make_recolored(image, .5, .5, .5)
    red = make_recolored(image, 1.6, .3, .3)
    purple = make_recolored(image, 1.4, .3, 1.4)
    orange = make_recolored(image, 1.1, 1.2, 0)
    image = make_warhol(pink, brighter, blue, og_image, green, yellow, red, darker, purple, orange)
    return image

def make_recolored(image, red_scale, green_scale, blue_scale):
    """
    This function uses the parameters given to adjust the image accordingly;
    multiplying the pixels by the parameter, then returning the new image.
    """
    image = SimpleImage(image)
    for pixel in image:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return image

def make_warhol(pink, brighter, blue, og_burrito, green, yellow, red, darker, purple, orange):
    """
    This function combines the colored images, including the original,
    into a Warhol grid pattern- adjusting the placement of the image
    based on the width and height of the original image.
    """
    image = SimpleImage.blank(WIDTH, HEIGHT)
    for y in range(BURR_SIZE):
        for x in range(BURR_SIZE):
            image.set_pixel(x, y, pink.get_pixel(x, y))
            image.set_pixel(x + BURR_SIZE, y, brighter.get_pixel(x, y))
            image.set_pixel(x + 2 * BURR_SIZE, y, blue.get_pixel(x, y))
            image.set_pixel(x + 3 * BURR_SIZE, y, darker.get_pixel(x, y))
            image.set_pixel(x + 4 * BURR_SIZE, y, green.get_pixel(x, y))
            image.set_pixel(x, y + BURR_SIZE, yellow.get_pixel(x, y))
            image.set_pixel(x + BURR_SIZE, y + BURR_SIZE, red.get_pixel(x, y))
            image.set_pixel(x + 2 * BURR_SIZE, y + BURR_SIZE, og_burrito.get_pixel(x, y))
            image.set_pixel(x + 3 * BURR_SIZE, y + BURR_SIZE, purple.get_pixel(x, y))
            image.set_pixel(x + 4 * BURR_SIZE, y + BURR_SIZE, orange.get_pixel(x, y))
            image.set_pixel(x, y + 2 * BURR_SIZE, green.get_pixel(x, y))
            image.set_pixel(x + BURR_SIZE, y + 2 * BURR_SIZE, og_burrito.get_pixel(x, y))
            image.set_pixel(x + 2 * BURR_SIZE, y + 2 * BURR_SIZE, blue.get_pixel(x, y))
            image.set_pixel(x + 3 * BURR_SIZE, y + 2 * BURR_SIZE, red.get_pixel(x, y))
            image.set_pixel(x + 4 * BURR_SIZE, y + 2 * BURR_SIZE, pink.get_pixel(x, y))
    return image

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

def always_green_screen(canvas, image, image1, image2):
# wish this would work
    curr_x = get_left_x(canvas, image)
    curr_y = get_top_y(canvas, image)
    greenscreen(image1, image2, curr_x, curr_y)
    image_phimage = create_greened(image, MWID, MHEI)
    image = canvas.create_image(curr_x, curr_y, image=image_phimage)
    return image

def always_green_dark(canvas, image, image1, image2):
#not working  - says doesn't work within create greened
    curr_x = get_left_x(canvas, image)
    curr_y = get_top_y(canvas, image)
    greenscreen_dark(image1, image2, curr_x, curr_y)
    image_phimage = create_greened(image, MWID, MHEI)
    image = canvas.create_image(curr_x, curr_y, image=image_phimage)
    return image

def is_past_middle(canvas, image):
    max_x = CANVAS_WIDTH / 2 - SQUARE_SIZE / 2 + 30
    curr_x = get_left_x(canvas, image)
    return curr_x > max_x

def left_the_screen(canvas, image):
    max_x = CANVAS_WIDTH -1
    curr_x = get_left_x(canvas, image)
    return curr_x > max_x

def right_the_screen(canvas, image):
    max_x = 0
    curr_x = get_left_x(canvas, image)
    return curr_x > max_x

def get_left_x(canvas, shape):
    # returns the x location of the shape
    return canvas.coords(shape)[0]

def get_top_y(canvas, shape):
    # returns the y location of the shape
    return canvas.coords(shape)[1]

# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
