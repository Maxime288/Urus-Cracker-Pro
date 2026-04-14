#!/usr/bin/env python3
"""
🔨 Urus-Cracker Pro v1.5
Outil de brute-force de hash (Multi-format) avec système de mutations.
Inspiré par John The Ripper.
"""

import hashlib
import argparse
import sys
import time
from datetime import datetime

# ──────────────────────────────────────────────────────────────
# Couleurs & Style Urus
# ──────────────────────────────────────────────────────────────
class C:
    G = "\033[38;5;82m"    # Vert
    R = "\033[38;5;196m"   # Rouge
    Y = "\033[38;5;226m"   # Jaune
    B = "\033[38;5;45m"    # Bleu
    CYAN = "\033[38;5;51m" # Cyan
    BOLD = "\033[1m"
    RESET = "\033[0m"

BANNER = fr"""
{C.B}  _    _                      _____                _             {C.RESET}
{C.B} | |  | |                    / ____|              | |            {C.RESET}
{C.B} | |  | |_ __ _   _ ___     | |     _ __ __ _  ___| | _____ _ __ {C.RESET}
{C.B} | |  | | '__| | | / __|    | |    | '__/ _` |/ __| |/ / _ \ '__|{C.RESET}
{C.B} | |__| | |  | |_| \__ \    | |____| | | (_| | (__|   <  __/ |   {C.RESET}
{C.B}  \____/|_|   \__,_|___/     \_____|_|  \__,_|\___|_|\_\___|_|   {C.RESET}
{C.CYAN}           Multi-Format Hash Cracker v1.5 (Stealth & Rules){C.RESET}
"""

def get_mutations(word):
    """Génère des variations intelligentes pour maximiser les chances de succès."""
    return [
        word,                   # Original (ex: urus)
        word.capitalize(),      # Première majuscule (ex: Urus)
        word.upper(),           # Tout en majuscule (ex: URUS)
        word + "123",           # Suffixe numérique commun
        word + "!",             # Suffixe spécial
        word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0') # Leet Speak
    ]

def crack_hash(target_hash, wordlist, hash_type):
    """Logique principale de cracking avec comparaison de hashs."""
    print(f" {C.B}[*]{C.RESET} Cible   : {C.Y}{target_hash}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Format  : {C.CYAN}{hash_type.upper()}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Rules   : {C.G}Activées (6 mutations/mot){C.RESET}\n")
    
    start_time = time.time()
    count = 0
    
    try:
        with open(wordlist, 'r', encoding='latin-1') as f:
            for line in f:
                # Nettoyage strict pour éviter les erreurs de caractères invisibles
                base_word = line.strip()
                if not base_word:
                    continue
                
                # Test de chaque mutation
                for word in get_mutations(base_word):
                    try:
                        # Création du hash dynamique
                        h = hashlib.new(hash_type)
                        h.update(word.encode('utf-8'))
                        guess_hash = h.hexdigest()
                        count += 1
                        
                        # Comparaison
                        if guess_hash.lower() == target_hash.lower():
                            duration = round(time.time() - start_time, 2)
                            print(f"\n\n{C.G}{C.BOLD}[+] SUCCÈS : MOT DE PASSE TROUVÉ !{C.RESET}")
                            print(f"{C.G}    >>> {C.BOLD}{word}{C.RESET} <<<")
                            print(f"\n {C.B}[*]{C.RESET} Tentatives : {count}")
                            print(f" {C.B}[*]{C.RESET} Temps      : {duration}s")
                            return True

                        # Feedback visuel
                        if count % 1000 == 0:
                            sys.stdout.write(f" {C.CYAN}[*] Testés : {count}...{C.RESET}\r")
                            sys.stdout.flush()
                            
                    except UnicodeEncodeError:
                        continue # Saute les mots avec caractères illisibles

        print(f"\n\n{C.R}[!] Échec : Le hash n'a pas pu être cassé avec cette wordlist.{C.RESET}")
        return False

    except ValueError:
        print(f"{C.R}[!] Erreur : Format '{hash_type}' non supporté par votre système.{C.RESET}")
    except FileNotFoundError:
        print(f"{C.R}[!] Erreur : Le fichier '{wordlist}' est introuvable.{C.RESET}")
    except Exception as e:
        print(f"{C.R}[!] Erreur imprévue : {e}{C.RESET}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Urus-Cracker Pro")
    parser.add_argument("-t", "--target", required=True, help="Le Hash cible à casser")
    parser.add_argument("-w", "--wordlist", required=True, help="Chemin vers le dictionnaire (ex: passwords.txt)")
    parser.add_argument("-f", "--format", default="sha256", help="Format du hash (md5, sha1, sha256, sha512)")
    
    args = parser.parse_args()
    
    crack_hash(args.target, args.wordlist, args.format.lower())

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}[!] Interruption par l'utilisateur. Sortie...{C.RESET}")
        sys.exit()
