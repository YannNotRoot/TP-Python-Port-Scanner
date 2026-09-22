import time
import socket
import threading
from queue import Queue

# Début du timer
start = time.time()

# Demande à l'utilisateur
target = input("Entrer l'adresse IP de la cible : ").strip()
# Création de la queue
queue = Queue()
# Liste des ports ouverts
open_ports = []

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
        
def executor():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Le port {} est ouvert".format(port))
            open_ports.append(port)


# Ports de 1 à 1024 inclus
port_list = range(1, 1025)
fill_queue(port_list)

thread_list = []


for t in range(100):
    thread = threading.Thread(target=executor)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

print("\nLes ports ouverts sont :", open_ports)


duree = time.time() - start
print(f"Durée du programme : {duree} secondes")


# 172.16.193.254