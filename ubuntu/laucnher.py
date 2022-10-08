import os
from time import sleep
from click import style
from colorama import Fore, Back, Style

os.system('sudo apt install python3-pip')
os.system('pip install colorama ')
os.system('sudo pip install colorama')
os.system('sudo apt install figlet')
os.system('clear')
os.system('figlet Zombie Travel')
sleep(4)
print(Back.BLACK + 'Вас приветствует установщик Zombie Travel!' + Style.RESET_ALL)
sleep(3)
print(Back.BLACK + 'Пожалуйста выберите нужную вам версию из списка:' + Style.RESET_ALL)
sleep(2)
print(Back.GREEN + 'ZombieTravel v1.1' + Style.RESET_ALL)
print('web - https://1samson1.github.io/ZombieTravel/index.html')
print('github - https://github.com/1samson1/ZombieTravel')
sleep(5)
print(Back.GREEN + 'ZombieTravel v2' + Style.RESET_ALL)
print('web - https://1dilordos1.github.io/ZombieTravel/index.html')
print('github - https://github.com/1dilordos1/ZombieTravel')
sleep(1000)
