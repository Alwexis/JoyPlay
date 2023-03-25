#? Liberías Internas
import time
from datetime import datetime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#? Librerías Externas
import pygame
from pynput.keyboard import Controller
from util.KeysLibrary import keyDictionary
from colorama import Fore, Back, Style
from Main import config

dir_path = os.path.dirname(os.path.abspath(__file__))

keyboard = Controller()

#? Handler
def init():
    pygame.init()
    # os.system('cls')
    print(Fore.BLUE + Style.BRIGHT + "Iniciando detección de Teclas" + Fore.RESET + Style.RESET_ALL)
    print(Fore.CYAN + "Detectando un Joystick...")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(Fore.GREEN + "Detección de Joystick completa!" + Fore.RESET)
    print(Fore.CYAN + "Iniciando detección de Teclas 😺" + Fore.RESET)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN and event.button in config:
                key = None
                if len(config[event.button]) == 1:
                    key = str(config[event.button]).lower()
                else:
                    key = keyDictionary[config[event.button].lower()]
                print(Fore.GREEN + ' LOG ' + Back.RESET + Fore.RESET + ' | ' + Back.WHITE+ Style.BRIGHT + f" {datetime.now().strftime('%H:%M:%S')} " + Back.RESET + Fore.RESET + ' | ' + Fore.RESET + Back.RESET + Style.RESET_ALL + Fore.CYAN + f"Presionó la tecla {event.button} " + Fore.YELLOW + Style.BRIGHT + "(Joystick)" + Style.RESET_ALL + Fore.BLUE + f" --> {key} " + Fore.YELLOW + Style.BRIGHT + "(Teclado)" + Fore.RESET + Style.RESET_ALL)
                keyboard.press(key)
                if isReleasable(config[event.button]) == False:
                    time.sleep(0.1)
                    keyboard.release(key)
            elif event.type == pygame.JOYBUTTONUP and event.button in config:
                if isReleasable(config[event.button]):
                    key = None
                    if len(config[event.button]) == 1:
                        key = config[event.button]
                    else:
                        key = keyDictionary[config[event.button].lower()]
                    keyboard.release(key)

def isReleasable(key):
    return key in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'ALT']