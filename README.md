# TCP Port Scanner 🔍

Ce projet est un **scanner de ports TCP** en ligne de commande écrit en Python.  
Il permet de scanner une plage de ports sur une adresse IP ou un nom de domaine, et d’identifier les ports ouverts, associés à leur service.

---

## ⚙️ Fonctionnalités

- 📥 Saisie interactive de l’IP/domaine
- 🔢 Définition personnalisée de la plage de ports (entre 1 et 65535)
- 🧵 Utilisation de threads pour accélérer le scan
- 🟢 Affichage des ports ouverts avec code couleur (colorama)
- 💾 Option de **sauvegarde des résultats** (`.txt` ou `.json`)
- 🧠 Détection de certains services courants (SSH, HTTP, DNS, etc.)

---

## 💡 Recommandation

> Pour de meilleures performances, il est conseillé de scanner des plages de ports **raisonnables** (par exemple 100 à 200 ports).  
Un scan complet de 1000+ ports peut être plus long selon votre machine.

---

## 📁 Fichiers créés

- `resultat_scan.txt` ou `resultat_scan.json` : sauvegarde des résultats du scan

---

## 💻 Exécution

```bash
python scanneurCLI.py

