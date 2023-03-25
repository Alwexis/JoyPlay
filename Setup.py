import os
from colorama import Fore, Back, Style
import re

__actual_path__ = os.path.dirname(os.path.abspath(__file__))

def main():
    os.system('cls')
    print(Style.BRIGHT + Fore.BLUE + 'Bienvenido a JoyPlay Profile Setup v0.1'.center(100) + Style.RESET_ALL)
    print(Fore.BLUE + 'Estás a punto de crear un nuevo perfil. Por favor contesta las preguntas'.center(100))
    nombrePerfilRaw = input(Fore.GREEN + '\nNombre del Perfil: ' + Fore.WHITE)
    nombrePerfil = normalizeString(nombrePerfilRaw)
    while os.path.isfile(f'{__actual_path__}/Profiles/{nombrePerfil}.txt'):
        print(Fore.RED + 'Ya existe un perfil con ese nombre, por favor elija otro.')
        nombrePerfilRaw = input(Fore.GREEN + '\nNombre del Perfil: ' + Fore.WHITE)
        nombrePerfil = nombrePerfilRaw
        #nombrePerfil = normalizeString(nombrePerfilRaw)

    os.system('cls')
    print(Style.BRIGHT + Fore.BLUE + 'Bienvenido a JoyPlay Profile Setup v0.1'.center(100) + Style.RESET_ALL)
    print(Fore.WHITE + f'Creando perfil {nombrePerfil}...\n'.center(100))
    print(Fore.BLUE + 'Seleccione un tipo de Control de los siguientes:'.center(100))
    print(Fore.GREEN + '1. Switch PRO Controller'.center(100))
    print(Fore.GREEN + '2. Xbox 360 Controller'.center(100))
    print(Fore.GREEN + '3. PS4 Controller'.center(100))
    tipoControl = input(Fore.BLUE + '\nEscriba el número del control que desea usar: ' + Fore.WHITE)
    while tipoControl not in ['1', '2', '3']:
        tipoControl = input(Fore.RED + 'Escriba el número del control que desea usar: ' + Fore.WHITE)

    os.system('cls')
    print(Style.BRIGHT + Fore.BLUE + 'Bienvenido a JoyPlay Profile Setup v0.1'.center(100) + Style.RESET_ALL)
    print(Fore.WHITE + f'Creando perfil {nombrePerfil}...'.center(100))
    print(f'Control seleccionado: {tipoControl}\n'.center(100))
    print(Fore.BLUE + 'Indíquenos el nombre del Programa a utilizar, escribe "-" para configurar más tarde.'.center(100))
    nombrePrograma = input(Fore.GREEN + '\nNombre del Programa: ' + Fore.WHITE)
    
    os.system('cls')
    print(Style.BRIGHT + Fore.BLUE + 'Bienvenido a JoyPlay Profile Setup v0.1'.center(100) + Style.RESET_ALL)
    print(Fore.WHITE + f'Nombre del perfil {nombrePerfil}'.center(100))
    print(f'Control seleccionado: {tipoControl}'.center(100))
    print(f'Nombre del Programa: {nombrePrograma}\n'.center(100))
    print(Fore.BLUE + Style.BRIGHT + 'CREANDO PERFIL...'.center(100))
    createProfile(nombrePerfil, tipoControl, nombrePrograma)
    print(Fore.GREEN + Style.BRIGHT + 'PERFIL CREADO CON ÉXITO!'.center(100))

def normalizeString(stringToNormalize):
    stringNormalized = stringToNormalize
    stringNormalized = re.sub(r'[áàäâÁÀÄÂ]', 'a', stringNormalized)
    stringNormalized = re.sub(r'[éèëêÉÈËÊ]', 'e', stringNormalized)
    stringNormalized = re.sub(r'[íìïîÍÌÏÎ]', 'i', stringNormalized)
    stringNormalized = re.sub(r'[óòöôÓÒÖÔ]', 'o', stringNormalized)
    stringNormalized = re.sub(r'[úùüûÚÙÜÛ]', 'u', stringNormalized)
    stringNormalized = re.sub(r'[ñÑ]', 'n', stringNormalized)
    stringNormalized = re.sub(r'[çÇ]', 'c', stringNormalized)
    return stringNormalized

def createProfile(nombrePerfil, tipoControl, nombrePrograma):
    template = ''
    if tipoControl == '1':
        tipoControl = 'Switch PRO Controller'
        template = open(f'{__actual_path__}/profiles/templates/Switch.txt', 'r').read()
    elif tipoControl == '2':
        tipoControl = 'Xbox 360 Controller'
        template = open(f'{__actual_path__}/profiles/templates/Xbox.txt', 'r').read()
    elif tipoControl == '3':
        tipoControl = 'PS4 Controller'
        template = open(f'{__actual_path__}/profiles/templates/PS4.txt', 'r').read()

    game = nombrePrograma if nombrePrograma != '-' else 'None'
    with open(f'{__actual_path__}/Profiles/{nombrePerfil}.txt', 'w') as profile:
        profile.write(f'# Perfil {nombrePerfil} #\n')
        profile.write(f'\n# Nombre del Programa a utilizar #\n')
        profile.write(f'programa={game}\n')
        profile.write(f'\n{template}')

if __name__ == '__main__':
    main()