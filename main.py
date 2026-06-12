import os
import random
import time
import requests
from colorama import Fore, Style, init
from tqdm import tqdm

os.system("title Nitro Generator by guns.lol/9cu")

init(autoreset=True)

webhook_url = None

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
  _   _ _                      _____                           _             
 | \ | (_)                    / ____|                         | |            
 |  \| |_  __ _  __ _  __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | . ` | |/ _` |/ _` |/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |\  | | (_| | (_| | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_| \_|_|\__, |\__, |\__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
           __/ | __/ |                                                       
          |___/ |___/                                                          
    """)

    print(Fore.YELLOW + "[1] Nitro Generator")
    print(Fore.YELLOW + "[2] Nitro Checker")
    print(Fore.YELLOW + "[3] Utiliser un Webhook")
    print(Fore.YELLOW + "[4] Crédits")
    print(Fore.YELLOW + "[0] Fermer\n")

def nitrocode():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choices(caracteres, k=16))

def checknitro(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

def sendwebhook(code):
    if webhook_url:
        payload = {
            "content": f"Code Nitro valide trouvé : {code}"
        }
        requests.post(webhook_url, json=payload)

def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "Ce tool a été créé par yoannchvl")
    print(Fore.YELLOW + "https://guns.lol/9cu")
    print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
    input()

def enterwebhook():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "Entrez l'URL du webhook Discord que vous souhaitez utiliser :")
    global webhook_url
    webhook_url = input(Fore.CYAN + "[->] URL du webhook : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Webhook configuré avec succès !\n")
    print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
    input()

def main():
    while True:
        menu()
        choix = input(Fore.CYAN + "[->] Choisissez une option : ")
        
        if choix == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + "Combien de nitro voulez-vous générer ?")
            try:
                nombre = int(input(Fore.CYAN + "[->] Entrez un nombre : "))
                os.system('cls' if os.name == 'nt' else 'clear')

                fichier = open("nitro.txt", "w")
                print(Fore.RED + "Génération des nitro en cours...")
                for _ in tqdm(range(nombre), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Style.RESET_ALL)):
                    code = f"https://discord.gift/{nitrocode()}"
                    fichier.write(code + "\n")
                    time.sleep(0.01)
                fichier.close()

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Les nitro ont été stockés dans le fichier nitro.txt")
                print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
                input()
            
            except ValueError:
                print(Fore.RED + "[Erreur] Veuillez entrer un nombre valide.")
                time.sleep(2)
        
        elif choix == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + "Le Nitro Checker va checker les codes nitro de 'nitro.txt'...")
            try:
                with open("nitro.txt", "r") as fichier:
                    lignes = fichier.readlines()

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.YELLOW + "Lancement du Nitro Checker...\n")
                valid_codes = []

                for ligne in tqdm(lignes, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Style.RESET_ALL)):
                    code = ligne.strip().split('/')[-1]
                    if checknitro(code):
                        valid_codes.append(ligne.strip())
                        sendwebhook(ligne.strip())

                os.system('cls' if os.name == 'nt' else 'clear')
                if valid_codes:
                    with open("validnitro.txt", "w") as valid_fichier:
                        for valid_code in valid_codes:
                            valid_fichier.write(valid_code + "\n")
                    print(Fore.GREEN + "\nLes codes valides ont été stockés dans 'validnitro.txt'.")
                else:
                    print(Fore.RED + "\nAucun code valide trouvé.")

                print(Fore.MAGENTA + "[->] Faites entrer pour revenir au menu")
                input()
            except FileNotFoundError:
                print(Fore.RED + "[Erreur] Le fichier 'nitro.txt' n'a pas été trouvé.")
                time.sleep(2)

        elif choix == "3":
            enterwebhook()

        elif choix == "4":
            credits()

        elif choix == "0":
            print(Fore.RED + ":(")
            break

        else:
            print(Fore.RED + "[Erreur] Choix invalide. Veuillez réessayer.")
            time.sleep(2)

if __name__ == "__main__":
    main()
