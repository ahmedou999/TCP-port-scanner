import socket,threading,json,random,time
from colorama import Fore,Style,init

services_ports = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
}
ip = input("Entrez l'adresse IP ou le nom de domaine à scanner : ").strip()
try:
    ip = socket.gethostbyname(ip)  # Convertir un domaine en IP
except socket.gaierror:
    print("⚠ Erreur : Impossible de résoudre l'adresse IP. Vérifiez l'orthographe.")
    exit()

portL={}
lock =threading.Lock()
def scannerV2(ip,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((ip,port))==0:
        with lock:
            portL[port]=services_ports.get(port,"Inconnu")
    sock.close()


threads=[]
def scanRapide(ip):
    threads=[]

    while True :
        try :
            min_port = int(input("Entrez le port minimum à scanner (entre 1 et 65535) :"))
            if 1 <= min_port <= 65535:
                print(f"✅ Vous avez choisi {min_port} comme port minimum.")
                break
            else:
                print("⚠ Le port doit être entre 1 et 65535.")
        except ValueError:
            print("⚠ Entrée invalide. Veuillez entrer un nombre.")
    while True:
        try :
            max_port = int(input("Veuillez le port maximum à scanner (il doit être supérieur au port minimum):"))
            if min_port <= max_port <= 65535:
                print(f"✅ Vous avez choisi {max_port} comme port maximum.")
                break
            else:
                print("⚠ Le port doit être entre le port minimum et 65535.")
        except ValueError:
            print("⚠ Entrée invalide. Veuillez entrer un nombre.")
    
    L=list(range(min_port,max_port+1))
    random.shuffle(L)

    for p in L:
        time.sleep(random.uniform(0.1,0.6))
        thread = threading.Thread(target=scannerV2,args=(ip,p))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()


def sauvegarde(dict):
    res= input("voulez-vous sauvegarder le scan (oui/non)").lower().strip()
    while res not in ["oui", "non"] :
        res= input("OUI ou NON").lower().strip()
    if res == "non":
        print("❌ Sauvegarde annulée.")
        return
    if res == "oui":
        format=input("En quelle format (json/txt)").lower().strip()
        while format not in ["json", "txt", "exit"]:
            format= input("JSON ou TXT ou EXIT").lower().strip()
        if format == "exit":
            print("❌ Sauvegarde annulée. Aucun fichier n'a été créé.")
            return
        else:
            if format =="txt":
                with open("resultat_scan.txt","w") as f:
                    for port,service  in dict.items():
                        f.write(f"{port} : {service}\n")
                print("sauvegarde terminée")
                return
            else:
                with open("resultat_scan.json","w") as f:
                        json.dump(dict,f,indent=4)
                print("sauvegarde terminée")
                return

scanRapide(ip)
for port , v in portL.items():
    if v == "Inconnu":
        print(Fore.YELLOW + f"Le port {port} est associé a la valeur:{v}"+ Style.RESET_ALL)
    else :
        print(Fore.GREEN + f"Le port {port} est associé a la valeur:{v}"+ Style.RESET_ALL)
print(sauvegarde(portL))
