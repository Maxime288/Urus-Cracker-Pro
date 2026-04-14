# 🔨 Urus-Cracker Pro

> **Hash Cracking & Password Recovery Tool**
> Un utilitaire performant de récupération de mots de passe par force brute et attaque par dictionnaire, inspiré par John The Ripper.
> Python 3 · Cryptography · SHA-256.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Cryptography-red)
![Algorithm](https://img.shields.io/badge/Algorithm-Brute--Force-orange)

---

## 📋 Présentation

**Urus-Cracker Pro** est un outil de cybersécurité conçu pour tester la robustesse des politiques de mots de passe en tentant de casser des empreintes numériques (hashes). Dans un audit, cet outil permet de démontrer qu'un mot de passe simple, même haché, reste vulnérable aux attaques par dictionnaire.

### Fonctionnalités principales

- **Déchiffrement SHA-256** : Supporte l'algorithme de hachage standard moderne.
- **Optimisation de lecture** : Lecture de wordlist en streaming pour gérer des fichiers massifs (comme RockYou.txt) sans saturer la RAM.
- **Feedback en temps réel** : Compteur de mots testés et calcul de la vitesse d'exécution.
- **Interface intuitive** : Gestion via arguments CLI pour une intégration facile dans des scripts automatisés.

---

## ⚙️ Fonctionnement Technique

Le script repose sur le principe de l'**attaque par dictionnaire** :

1. Il ne déchiffre pas le hash (impossible par définition).
2. Il parcourt chaque mot d'une liste (wordlist).
3. Il calcule le hash SHA-256 de ce mot.
4. Il compare le résultat avec le hash cible. S'ils sont identiques, le mot de passe est trouvé.

---

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Maxime288/Urus-Cracker-Pro
cd Urus-Cracker-Pro
```

### 2. Vérifier Python

```bash
python3 --version
```

> Python 3.10 ou supérieur est requis. Aucune dépendance externe n'est nécessaire — le script repose uniquement sur `hashlib`, `argparse`, `sys` et `time`, tous inclus dans la bibliothèque standard Python.

---

## 🚀 Utilisation

### Syntaxe

```bash
python3 urus_cracker.py -t <VOTRE_HASH> -w <WORDLIST>
```

### Exemple SHA-256

Pour casser le mot de passe `password123` :

```bash
python3 urus_cracker.py -t ef92b778ba715867219a6bc011652561c04e330e59dd0b62e40e21936954274d -w passwords.txt
```

### Exemple MD5

```bash
python3 urus_cracker.py -t 33796ec8787f71936c50756306c9a331 -w passwords.txt -f md5
```

---

## 🛠️ Wordlists recommandées

Pour des tests efficaces, il est recommandé d'utiliser des dictionnaires réels :

- **RockYou** : `/usr/share/wordlists/rockyou.txt` (Standard Kali Linux)
- **SecLists** : Une collection complète pour tous types de services.

---

## ⚠️ Avertissement Légal

Cet outil est destiné **exclusivement** à un usage éducatif et à des tests de pénétration autorisés. L'utilisation de ce script pour tenter d'accéder à des comptes dont vous n'êtes pas le propriétaire ou sans autorisation explicite est **illégale**.

---

## 🔗 Liens

- **Dépôt GitHub** : [https://github.com/Maxime288/Urus-Cracker-Pro](https://github.com/Maxime288/Urus-Cracker-Pro)
