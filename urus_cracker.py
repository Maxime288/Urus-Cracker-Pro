#!/usr/bin/env python3
import hashlib
import argparse
import sys
import time
from datetime import datetime

# Style Urus
class C:
    G = "\033[38;5;82m"    # Vert
    R = "\033[38;5;196m"   # Rouge
    Y = "\033[38;5;226m"   # Jaune
    B = "\033[38;5;45m"    # Bleu
    CYAN = "\033[38;5;51m" # Cyan
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
    """Génère des variations courantes pour un mot donné."""
    return [
        word,                   # original (ex: urus)
        word.capitalize(),      # Majuscule (ex: Urus)
        word.upper(),           # TOUT EN MAJ (ex: URUS)
        word + "123",           # Suite classique
        word + "!",             # Symbole
        word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0') # Leet
    ]

def crack_logic(target_hash, wordlist, hash_type):
    print(f" {C.B}[*]{C.RESET} Cible   : {C.Y}{target_hash}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Format  : {C.CYAN}{hash_type.upper()}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Rules   : {C.G}Enabled (Mutations x6){C.RESET}\n")
    
    start_time = time.time()
    count = 0
    
    try:
        with open(wordlist, 'r', encoding='latin-1') as f:
            for line in f:
                base_word = line.strip()
                
                # Appliquer les règles de mutation
                for word in get_mutations(base_word):
                    # Création du hash selon le type choisi
                    h = hashlib.new(hash_type)
                    h.update(word.encode())
                    guess_hash = h.hexdigest()
                    count += 1
                    
                    if guess_hash == target_hash:
                        end_time = time.time()
                        print(f"\n\n{C.G}[+] SUCCESS! MOT DE PASSE TROUVÉ{C.RESET}")
                        print(f"{C.G}    >>> {C.BOLD}{word}{C.RESET} <<<")
                        print(f"\n {C.B}[*]{C.RESET} Tentatives : {count}")
                        print(f" {C.B}[*]{C.RESET} Temps      : {round(end_time - start_time, 2)}s")
                        return

                    if count % 1000 == 0:
                        sys.stdout.write(f" {C.CYAN}[*] Mots testés : {count}...{C.RESET}\r")
                        sys.stdout.flush()

        print(f"\n\n{C.R}[!] Échec : Hash non trouvé dans la liste (même avec mutations).{C.RESET}")

    except ValueError:
        print(f"{C.R}[!] Erreur : Le format '{hash_type}' n'est pas supporté par hashlib.{C.RESET}")
    except FileNotFoundError:
        print(f"{C.R}[!] Erreur : Wordlist introuvable.{C.RESET}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Urus-Cracker Pro")
    parser.add_argument("-t", "--target", required=True, help="Le Hash à casser")
    parser.add_argument("-w", "--wordlist", required=True, help="Dictionnaire")
    parser.add_argument("-f", "--format", default="sha256", help="Format (md5, sha1, sha256, sha512)")
    args = parser.parse_args()
    
    crack_logic(args.target, args.wordlist, args.format.lower())

if __name__ == "__main__":
    main()
