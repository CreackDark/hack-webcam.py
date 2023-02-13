
import re

import os

import time

import sys

#Counrty example  :  US , JP

def banner():

    print ('\t         \033[1;34m   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')

    print ('\t         \033[1;34m   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')

    print ('\t         \033[1;34m   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')

    print ('\t         \033[1;34m   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')

    print ('\t         \033[1;34m   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇\033[2;32m  Code By :\033[2;31m Dark ')

    print ('\t         \033[1;34m   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')

    print ('\t         \033[1;34m   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')

    print ('\t         \033[1;34m   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')

    print('''\n\t\033[1;33m         https://t.me/CreackDark

\t       https://github.com/CreackDark/\n''')

def cam():

    os.system('clear')

    banner()

    try:

        co = input('\033[1;37m [ + ]\033[1;32m Enter Country : \033[1;37m').upper()

        headers = {"User-Agent": "mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68>

        res = requests.get(f"http://www.insecam.org/en/bycountry/{co}", headers=headers).text

        page = re.findall(r'pagenavigator\("\?page=", (\d+)', res)[0]

    except:

        sys.exit("\033[1;37m [ ✘ ] \033[1;31m Error .........!!   ")

        cam()

    for dead in range(int(page)):

        req = requests.get(f"http://www.insecam.org/en/bycountry/{co}/?page={page}" ,headers=heade>

        ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", req)

        for i in ip:
        print("\n\033[1;37m [ ✓ ] \033[1;31m",i)

        input("\n \033[1;37m Welcome In Creack_Dark Code Is Thank You \n")

        cam()

#--------------------------------

if __name__ == '__main__':
cam()
