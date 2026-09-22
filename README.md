# Scanner de Ports TCP Multi-threaded

Script Python simple permettant de scanner les ports réseau TCP sur une adresse IP cible en utilisant le multi-threading.

## Utilisation

1. Exécutez le script dans votre terminal :
   ```bash
   python3 scanner.py
   ```

2. Entrez l'adresse IP cible lorsqu'elle vous est demandée :
   ```text
   Entrer l'adresse IP de la cible : 192.168.1.1
   ```

3. **Exemple de sortie :**
   ```text
   Entrer l'adresse IP de la cible : 192.168.1.1
   Le port 80 est ouvert
   Le port 443 est ouvert

   Les ports ouverts sont : [80, 443]
   Durée du programme : 1.45 secondes
   ```

## Fonctionnement technique

1. **`port_scan(port)`** : Tente d'établir une connexion TCP (`socket.SOCK_STREAM`) vers la cible et le port spécifié.
2. **`fill_queue(port_list)`** : Remplit la file d'attente thread-safe (`queue.Queue`) avec la liste des ports à tester.
3. **`executor()`** : Fonction exécutée par chaque thread. Elle dépile un port, le teste et enregistre le résultat s'il est ouvert.
4. **Gestion des threads** : 100 threads sont démarrés simultanément et synchronisés avec `join()` pour garantir la fin de tous les tests avant d'afficher le résumé.
