import os
import threading
from WindowHandler import get_active_window_process_name, init as initWindowHandler
from colorama import Fore, Back, Style

profiles = {}
config = {}

def loadConfig():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    if len(profiles.keys()) == 0:
        for nombre_archivo in os.listdir(dir_path + '/profiles'):
            if os.path.isfile(dir_path + '/profiles/' + nombre_archivo):
                game = None
                with open(dir_path + '/profiles/' + nombre_archivo, "r") as configFile:
                    for linea in configFile:
                        if linea.startswith("#") == False and linea.startswith('programa'):
                            game = linea.replace('programa=', '')
                            break
                if game != None:
                    # profiles.append({
                    #     'path': dir_path + '/profiles/' + nombre_archivo,
                    #     'name': game
                    # })
                    game = game.replace('\n', '')
                    profiles[game] = dir_path + '/profiles/' + nombre_archivo
                else:
                    print(Fore.RED + Style.BRIGHT + "No se encontró el nombre del juego en " + Fore.RESET + Style.RESET_ALL + Fore.CYAN + f"{nombre_archivo}" + Fore.RESET + Style.RESET_ALL)
    processData = get_active_window_process_name()
    nombre = processData['window_title']
    if nombre in profiles:
        profilePath = profiles[nombre]
        print(Fore.BLUE + Style.BRIGHT + "\nCargando configuración de " + Fore.RESET + Style.RESET_ALL + Fore.CYAN + f"{nombre}" + Fore.RESET + Style.RESET_ALL)
        with open(profilePath, "r") as configFile:
            for linea in configFile:
                if linea.startswith("#") == False and linea.startswith('programa') == False:
                    parsedLinea = linea.replace(' ', '').replace('\n', '')
                    valores = parsedLinea.split("=")
                    if len(valores) > 1:
                        config[int(valores[1])] = valores[0]
        print(Fore.GREEN + Style.BRIGHT + "Configuración cargada correctamente!\n" + Fore.RESET + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "\n⚠️  No se encontró una configuración para " + Fore.RESET + Style.RESET_ALL + Fore.YELLOW + f"{nombre}" + Fore.RESET + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + 'Crea una configuración para este juego o aplicación abriendo el archivo ' + Back.GREEN + Fore.BLACK + Style.BRIGHT + ' Setup.py ' + Style.RESET_ALL + Back.RESET)
        print(Fore.BLUE + '🔃 Cambia de ventana al juego o aplicación la cual quieras aplicar la configuración.\n')

def init():
    os.system('cls')
    __WindowsHandlerThread__ = None
    while True:
        loadConfig()
        # Hilo para detectar cambios de ventana
        __WindowsHandlerThread__ = threading.Thread(target=initWindowHandler)
        __WindowsHandlerThread__.daemon = True
        __WindowsHandlerThread__.start()
        from InputHandler import init as initInputHandler
        initInputHandler()
        # if __WindowsHandlerThread__ != None:
        #     __WindowsHandlerThread__.join(0)

if __name__ == "__main__":
    init()