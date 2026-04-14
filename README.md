# 🔨 Urus-Cracker Pro

> **Hash Cracking & Password Recovery Tool**
> Un utilitaire performant de récupération de mots de passe par attaque par dictionnaire avec mutations, inspiré par John The Ripper.
> Python 3 · Cryptography · Multi-Format · Rules Engine.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Cryptography-red)
![Version](https://img.shields.io/badge/Version-1.5-orange)
![Algorithm](https://img.shields.io/badge/Algorithm-Dictionary--Attack-yellow)

---

## 📋 Présentation

**Urus-Cracker Pro** est un outil de cybersécurité conçu pour tester la robustesse des politiques de mots de passe en tentant de casser des empreintes numériques (hashes). Dans un audit, cet outil permet de démontrer qu'un mot de passe simple, même haché, reste vulnérable aux attaques par dictionnaire.

### Fonctionnalités principales

- **Multi-format** : Supporte tous les algorithmes compatibles `hashlib` (MD5, SHA-1, SHA-256, SHA-512…).
- **Rules Engine** : Génère automatiquement 6 mutations par mot (majuscules, leet speak, suffixes classiques…).
- **Optimisation de lecture** : Lecture de la wordlist en streaming pour gérer des fichiers massifs (comme RockYou.txt) sans saturer la RAM.
- **Feedback en temps réel** : Compteur de mots testés et calcul du temps d'exécution.
- **Interface intuitive** : Gestion via arguments CLI pour une intégration facile dans des scripts automatisés.

---

## ⚙️ Fonctionnement Technique

Le script repose sur le principe de l'**attaque par dictionnaire avec mutations** :

1. Il parcourt chaque mot d'une wordlist ligne par ligne.
2. Pour chaque mot, il génère 6 variantes via le moteur de règles (`get_mutations`).
3. Il calcule le hash de chaque variante selon le format choisi.
4. Il compare le résultat avec le hash cible. S'ils sont identiques, le mot de passe est trouvé.

### Mutations appliquées (Rules Engine)

| Règle | Exemple (base : `urus`) |
|---|---|
| Original | `urus` |
| Capitalize | `Urus` |
| Uppercase | `URUS` |
| Suffixe `123` | `urus123` |
| Suffixe `!` | `urus!` |
| Leet speak | `urus` → `uru5` |

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

> Python 3.10 ou supérieur est requis.

### 3. Rendre le script exécutable (Linux / macOS)

```bash
chmod +x urus_cracker.py
```

### 4. Dépendances

Aucune installation externe n'est requise. Le script utilise uniquement des modules de la **bibliothèque standard Python** :

| Module | Rôle |
|---|---|
| `hashlib` | Calcul des hashes (MD5, SHA-256, SHA-512…) |
| `argparse` | Gestion des arguments CLI (`-t`, `-w`, `-f`) |
| `sys` | Affichage dynamique dans le terminal |
| `time` | Mesure du temps d'exécution |
| `datetime` | Horodatage |

---

## 🚀 Utilisation

### Syntaxe

```bash
python3 urus_cracker.py -t <HASH> -w <WORDLIST> [-f <FORMAT>]
```

### Arguments

| Argument | Description | Défaut |
|---|---|---|
| `-t`, `--target` | Hash à casser | requis |
| `-w`, `--wordlist` | Chemin vers la wordlist | requis |
| `-f`, `--format` | Algorithme de hachage (`md5`, `sha1`, `sha256`, `sha512`…) | `sha256` |

### Exemple SHA-256

```bash
python3 urus_cracker.py -t ef92b778ba715867219a6bc011652561c04e330e59dd0b62e40e21936954274d -w passwords.txt
```

### Exemple MD5

```bash
python3 urus_cracker.py -t 33796ec8787f71936c50756306c9a331 -w passwords.txt -f md5
```

### Exemple SHA-512

```bash
python3 urus_cracker.py -t <HASH> -w /usr/share/wordlists/rockyou.txt -f sha512
```

---

## 🛠️ Wordlists recommandées

Pour des tests efficaces, il est recommandé d'utiliser des dictionnaires réels :

- **RockYou** : `/usr/share/wordlists/rockyou.txt` (Standard Kali Linux)
- **SecLists** : Une collection complète pour tous types de services.

---

## ⚠️ Avertissement Légal

Cet outil est destiné **exclusivement** à un usage éducatif et à des tests de pénétration **autorisés**. L'utilisation de ce script pour tenter d'accéder à des comptes dont vous n'êtes pas le propriétaire ou sans autorisation explicite est **illégale**.

---

## 🔗 Liens

- **Dépôt GitHub** : [https://github.com/Maxime288/Urus-Cracker-Pro](https://github.com/Maxime288/Urus-Cracker-Pro)
