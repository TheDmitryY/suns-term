from colorama import Fore
from settings.options import options_menu, ssh_menu_text, ip_menu_text, project_menu_text, tacleapi_menu_text, scan_menu_text, scan_udp_menu,scan_tcp_text,scan_sites_menu
import os

os.system("clear")

text = """
     ,---.
    '   .-' ,--.,--.,--,--,  ,---.
    `.  `-. |  ||  ||      \(  .-'
    .-'    |'  ''  '|  ||  |.-'  `)
    `-----'  `----' `--''--'`----'
         Author: @trustes       \n"""

caption = "\nWelcome to me custom Termux terminal script \nHe help fast manage termux console menu with fast option to you.\n"

def init_app():
    os.system("clear")
    print(Fore.LIGHTRED_EX + text)
    print(Fore.LIGHTRED_EX + caption)
    print(Fore.LIGHTRED_EX + options_menu)
    option = int(input(Fore.LIGHTGREEN_EX + " > "))
    if option == 1:
        ssh_menu()
    elif option == 2:
        ip_menu()
    elif option == 3:
        project_menu()
    elif option == 4:
        tacleapi_menu()


def ssh_menu():
    os.system("clear")
    print(Fore.LIGHTBLUE_EX + text)
    print(Fore.LIGHTBLUE_EX + caption)
    print(Fore.LIGHTBLUE_EX + ssh_menu_text)
    option_ssh = int(input(Fore.LIGHTGREEN_EX + " > "))
    if option_ssh == 1:
        os.system("ssh suns")
    elif option_ssh == 2:
        os.system("ssh pc")
    elif option_ssh == 3:
        pass
    elif option_ssh == 4:
        init_app()
    elif option_ssh == 5:
        exit
    else:
        print(Fore.LIGHTBLUE_EX + "[ERROR] - Input error!")

def ip_menu():
    os.system("clear")
    print(Fore.LIGHTMAGENTA_EX + text)
    print(Fore.LIGHTMAGENTA_EX + caption)
    print(Fore.LIGHTMAGENTA_EX + ip_menu_text)
    option_ip = int(input(Fore.LIGHTGREEN_EX + " > "))
    if option_ip == 1:
        os.system("ifconfig")
    elif option_ip == 2:
        scan_menu()
    elif option_ip == 3:
        init_app()
    elif option_ip == 4:
        exit

def project_menu():
    os.system("clear")
    print(Fore.LIGHTYELLOW_EX + text)
    print(Fore.LIGHTYELLOW_EX + caption)
    print(Fore.LIGHTYELLOW_EX + project_menu_text)
    option_pj = int(input(Fore.LIGHTMAGENTA_EX + " > "))
    if option_pj == 1:
        os.system(Fore.LIGHTRED_EX + "ls /data/data/com.termux/files/home/scripts")
    elif option_pj == 2:
        pass
    elif option_pj == 3:
        pass
def tacleapi_menu():
    os.system("clear")
    print(Fore.LIGHTYELLOW_EX + text)
    print(Fore.LIGHTYELLOW_EX + caption)
    print(Fore.LIGHTYELLOW_EX + tacleapi_menu_text)
    option_api = int(input(Fore.LIGHTYELLOW_EX + " > "))
    if option_api == 1:
        os.system("curl 192.168.0.110:14358/shutdown") 
    elif option_api == 2:
        os.system("curl 192.168.0.110:14358/sleepmode")
    elif option_api == 3:
        os.system("curl 192.168.0.110:14358/reboot")
    elif option_api == 4:
        command_api = input(Fore.LIGHTYELLOW_EX + " Enter command > ")
        os.system(f"curl 192.168.0.110:14358/command/{command_api}")
    elif option_api == 5:
        init_app()
    elif option_api == 6:
        exit

def scan_menu() -> None:
    os.system("clear")
    print(Fore.LIGHTCYAN_EX + text)
    print(Fore.LIGHTCYAN_EX + caption)
    print(Fore.LIGHTCYAN_EX + scan_menu_text)
    option_scan = int(input(Fore.LIGHTCYAN_EX + " > "))
    if option_scan == 1:
        scan_tcp()
    elif option_scan == 2:
        pass
    elif option_scan == 3:
        pass
    else:
        init_app()

def scan_udp() -> None:
    os.system("clear")
    print(Fore.LIGHTCYAN_EX + text)
    print(Fore.LIGHTCYAN_EX + caption)
    print(Fore.LIGHTCYAN_EX + scan_udp_menu)
    option_udp = int(input(Fore.LIGHTCYAN_EX + " > "))
    if option_udp == 1:
        pass
    elif option_udp == 2:
        pass
    elif option_udp == 3:
        pass

def scan_tcp() -> None:
    os.system("clear")
    print(Fore.LIGHTCYAN_EX + text)
    print(Fore.LIGHTCYAN_EX + caption)
    print(Fore.LIGHTCYAN_EX + scan_tcp_text)
    option_tcp = int(input(Fore.LIGHTCYAN_EX + " > "))
    if option_tcp == 1:
        ip = input(Fore.LIGHTCYAN_EX + "Enter IP > ")
        os.system(f"nmap -sS {ip}")
    elif option_tcp == 2:
        ip = input(Fore.LIGHTCYAN_EX + "Enter IP > ")
        os.system(f"nmap -sT {ip}")
    elif option_tcp == 3:
        ip = input(Fore.LIGHTCYAN_EX + "Enter IP > ")
        os.system(f"nmap -sA {ip}")
    elif option_tcp == 4:
        ip = input(Fore.LIGHTCYAN_EX + "Enter IP > ")
        os.system(f"nmap -sW {ip}")
    elif option_tcp == 5:
        ip = input(Fore.LIGHTCYAN_EX + "Enter IP > ")
        os.system(f"nmap -sM {ip}")