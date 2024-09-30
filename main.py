import RPi.GPIO as GPIO
from time import sleep, time 
from multiprocessing import Process, Lock

from menu import PrintMenu, PrintGraph, PrintTable, dyInit
from utils_ import InputValidator, InputTextValidator, generarAleatorio
from puntos_ import getPuntos, addScore
from buzzer_melodys.mario import init as mario
from buzzer_melodys.coundDown import init as cundDown
from buzzer_melodys.bip import init as bip
from buzzer_melodys.bip2 import init as bip2
from buzzer_melodys.game import init as gameMusic_

PUNTOS_DIR = 'puntos.txt'
Puntos, nPuntos = getPuntos(PUNTOS_DIR)


def marioMusic(l, n):
    l.acquire()
    try:
        while True:
            mario()
    finally:
        l.release()
def gameMusic(l, n):
    l.acquire()
    try:
        while True:
            gameMusic_()
    finally:
        l.release()
def cundDownMusic(l, n):
    l.acquire()
    try:
        cundDown()
    finally:
        l.release()
def BIP(l, n):
    l.acquire()
    try:
        bip()
    finally:
        l.release()
def BIP2(l, n):
    l.acquire()
    try:
        bip2()
    finally:
        l.release()
musicProcess = {} 
dy = dyInit()

# Configuración de pines
BUTTON_PINS = [26, 19, 13, 6, 5]
LED_PINS_GREEN = [4]
LED_PINS_AMBER = [21, 20, 24, 16, 1]
LED_PINS_RED = [17, 23, 25,27, 22]
TIME_GAME = 5

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configura los pines de LEDs y Buttons
for pin in LED_PINS_GREEN + LED_PINS_AMBER + LED_PINS_RED:
    GPIO.setup(pin, GPIO.OUT)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

# Función para apagar todos los LEDs
def all_leds_off():
    for pin in LED_PINS_GREEN + LED_PINS_AMBER + LED_PINS_RED:
        GPIO.output(pin, GPIO.LOW)
def Led_on(arr):
    for pin in arr:
        GPIO.output(pin, GPIO.HIGH)
def Led_off(arr):
    for pin in arr:
        GPIO.output(pin, GPIO.LOW)
def detectButtons():
    return [
        GPIO.input(BUTTON_PINS[0]) != GPIO.HIGH,
        GPIO.input(BUTTON_PINS[1]) != GPIO.HIGH,
        GPIO.input(BUTTON_PINS[2]) != GPIO.HIGH,
        GPIO.input(BUTTON_PINS[3]) != GPIO.HIGH,
        GPIO.input(BUTTON_PINS[4]) != GPIO.HIGH
        ]

def Game(rondas, play):
    # buzzer hace bip
    puntos = 0
    currentTime = time()
    times = []
    promedio = 0
    for ronda in range(rondas):
        PrintMenu([f'Ronda {ronda +1} ','',f'Puntos {puntos:29}', f'Tiempo promedio {promedio:20}s'], 0, f'Es el turno de {play}', dy)
        GA = generarAleatorio()
        GA2 = [i for i in GA]
        for pin in range(5):
            GPIO.output(LED_PINS_AMBER[pin] if GA[pin] else LED_PINS_RED[pin], GPIO.HIGH)
        time_ = TIME_GAME
        startTime = time()
        while (round(time()-startTime,2) <= time_):
            if 1 in GA2: 
                db = detectButtons()
                for b in range(5):
                    if db[b] :
                        if GA[b] == 1 and GA2[b] ==1:
                            GA2[b] = -1
                            puntos = puntos+1
                            lock_ = Lock()
                            sound = Process(target=BIP,args=(lock_, 1))
                            sound.start()
                            times.append(round(time()-currentTime,2))
                            currentTime = time()
                            promedio = round(sum(times) / len(times), 3)
                            #print('+1')
                            PrintMenu([f'Ronda {ronda +1} ','',f'Puntos {puntos:29}', f'Tiempo promedio {promedio:20}s'], 0, f'Es el turno de {play}', dy)
                            GPIO.output(LED_PINS_AMBER[b], GPIO.LOW)
                        elif GA2[b] == 0:
                            GA2[b] = -1
                            lock_ = Lock()
                            sound = Process(target=BIP2,args=(lock_, 1))
                            sound.start()
                            #print(GA2)
                            puntos = puntos-1
                            PrintMenu([f'Ronda {ronda +1} ','',f'Puntos {puntos:29}', f'Tiempo promedio {promedio:20}s'], 0, f'Es el turno de {play}', dy)
                            GPIO.output(LED_PINS_RED[b], GPIO.LOW)
            else:
                break
            sleep(0.01)
        if (round(time()-startTime,2) >= time_):
            print('time')
        all_leds_off()
        GPIO.output(LED_PINS_GREEN[0], GPIO.HIGH)
        #Led_on(LED_PINS_RED+LED_PINS_AMBER)
        sleep(0.5)
        all_leds_off()
    return [puntos, promedio]    

def Menu():
    pos = 0
    level = [
        [
            'GAME',
            ['play', 0, 2],
            ['stats', 0, 1, ['stats', Puntos, ['name ', 'score '], True]],
            ['config', 2],
            ['exit', -1]
        ],
        [
            'CONFIG',
            ['rondas [20]', 2, 20],
            ['tiempo [5]', 2, 5],
            ['atrás', 1]
        ],
        [
            'PLAYER',
            ['name player', 2],
            ['atrás', 2]
        ],
        [
            'STATS',
            ['stats', 2],
            ['atrás', 1]
        ]
    ]
    m = 1
    fn = [0, 0]
    while True:
        if m == -1:
            break
        elif m == 0:
            if level[fn[0]-1][fn[1]+1][2] == 1:
                t, it, l, e = [a for a in level[fn[0]-1][fn[1]+1][3]] 
                PrintTable(t,it,l,e, dy)
                while True:
                    sleep(0.5)
                    btn = detectButtons()
                    if True in btn:
                        fn = [0, 0]
                        m = 1 
                        pos = 0
                        break
            elif level[fn[0]-1][fn[1]+1][2] == 2:
                PrintMenu(['Cantidad de jugadores','',''], 0, 'GAME', dy)
                cj = InputValidator('Cantidad de jugadores', 1, 5)
                player = [f"player {o+1}" for o in range(cj)]
                for i in range(cj):
                    PrintMenu([f'{player[l]}' for l in range(cj)], i, 'GAME', dy)
                    player[i] = InputTextValidator(f'name player {i+1}', 5)
                musicProcess.terminate()
                for play in player:
                    PrintMenu(['star','',''], 0, f'Es el turno de {play}', dy)
                    sleep(1)
                    while True:
                        sleep(0.05)
                        btn = detectButtons()
                        if True in btn:
                            lock_ = Lock()
                            sound = Process(target=cundDownMusic,args=(lock_, 1))
                            sound.start()
                            Led_on([LED_PINS_RED[0], LED_PINS_RED[-1]])
                            PrintGraph('\t_____\n\t|___ /\n\t  |_ \ \n\t ___) |\n\t|____/\n', 6, dy)
                            sleep(1)
                            Led_on([LED_PINS_RED[1], LED_PINS_RED[-2]])
                            PrintGraph('\t ___ \n\t|___ \ \n\t  __) |\n\t / __/\n\t|_____|', 5, dy)
                            sleep(1)
                            Led_on([LED_PINS_RED[2]])
                            PrintGraph('\t   _\n\t  / |\n\t  | |\n\t  | |\n\t  |_|', 5, dy)
                            sleep(1)
                            Led_off(LED_PINS_RED)
                            PrintGraph('      __ _    ___\n     / _` |  / _ \ \n    | (_| | | (_) |\n     \__, |  \___/\n     |___/', 5, dy)
                            Led_on(LED_PINS_GREEN)
                            sleep(1)
                            Led_off(LED_PINS_GREEN)
                            break
                    lock__ = Lock()
                    gameMusic__ = Process(target=gameMusic,args=(lock__, 1))
                    gameMusic__.start()
                    stats__ = Game(level[1][1][2], play)
                    gameMusic__.terminate()
                    PrintMenu([f'','',f'Puntos {stats__[0]:29}', f'Tiempo promedio {stats__[1]:20}s'], -1, f'Estadísticas de {play}', dy)
                    scoreSave = addScore(play, f'{stats__[1]}s', PUNTOS_DIR)
                    while True:
                        sleep(0.5)
                        btn = detectButtons()
                        if True in btn:
                            fn = [0, 0]
                            m = 1 
                            pos = 0
                            break
                    #t, it, l, e = [a for a in level[fn[0]-1][fn[1]+1][
                    PrintTable('stats', scoreSave, ['name ', 'score '], True, dy)
                    while True:
                        sleep(0.5)
                        btn = detectButtons()
                        if True in btn:
                            fn = [0, 0]
                            m = 1 
                            pos = 0
                            break
                m=1
                pos=0
                break
        else: 
            PrintMenu([t[0] for t in level[m-1]][1:], pos, level[m-1][0], dy)
        
            while True:
                sleep(0.5)
                btn = detectButtons()
                if btn[0]:
                    pos = (len(level[m-1])-2) if pos == 0 else pos -1
                    break
                elif btn[1]:
                    pos = 0 if pos == (len(level[m-1])-2) else pos +1
                    break
                elif btn[4]:
                    if level[m-1][pos+1][1] != m:
                      fn = [m,pos]
                      m = level[m-1][pos+1][1] 
                      pos = 0
                      break
                    else:
                      change = InputValidator(f'{level[m-1][pos+1][0]} :', 0, 100)
                      level[m-1][pos+1][0] = f"{level[m-1][pos+1][0].split(' ')[0]} [{change}]"
                      level[m-1][pos+1][2] = change
                      break


try:
    while True:
        lock = Lock()
        musicProcess = Process(target=marioMusic,args=(lock, 1))
        musicProcess.start()
        Menu()
        musicProcess.terminate()
except KeyboardInterrupt:
    musicProcess.terminate()
    all_leds_off()
    GPIO.cleanup()
    pass

finally:
    musicProcess.terminate()
    all_leds_off()
    GPIO.cleanup()