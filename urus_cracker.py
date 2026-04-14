#!/usr/bin/env python3
import hashlib
import argparse
import sys
import time

# Couleurs Urus
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
{C.CYAN}           Multi-Format Hash Cracker v1.6 (Final Fix){C.RESET}
"""

def get_mutations(word):
    """Génère des variations pour maximiser les chances."""
    return [
        word,                   # original
        word.capitalize(),      # Majuscule
        word + "123",           # Chiffres
        word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0') # Leet
    ]

def crack_hash(target_hash, wordlist, hash_type):
    # Nettoyage du hash cible (enlève espaces et force minuscules)
    target_hash = target_hash.strip().lower()
    
    print(f" {C.B}[*]{C.RESET} Cible   : {C.Y}{target_hash}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Format  : {C.CYAN}{hash_type.upper()}{C.RESET}")
    
    start_time = time.time()
    count = 0
    
    try:
        with open(wordlist, 'r', encoding='latin-1') as f:
            for line in f:
                # NETTOYAGE CRITIQUE : retire \n, \r et les espaces invisibles
                base_word = line.strip()
                if not base_word:
                    continue
                
                for word in get_mutations(base_word):
                    # On nettoie encore le mot muté pour être sûr
                    clean_word = word.strip()
                    
                    try:
                        h = hashlib.new(hash_type)
                        h.update(clean_word.encode('utf-8'))
                        guess_hash = h.hexdigest()
                        count += 1
                        
                        if guess_hash == target_hash:
                            duration = round(time.time() - start_time, 2)
                            print(f"\n\n{C.G}{C.BOLD}[+] SUCCÈS : MOT DE PASSE TROUVÉ !{C.RESET}")
                            print(f"{C.G}    >>> {C.BOLD}{clean_word}{C.RESET} <<<")
                            print(f"\n {C.B}[*]{C.RESET} Tentatives : {count}")
                            print(f" {C.B}[*]{C.RESET} Temps      : {duration}s")
                            return True

                        if count % 1000 == 0:
                            sys.stdout.write(f" {C.CYAN}[*] Testés : {count}...{C.RESET}\r")
                            sys.stdout.flush()
                    except:
                        continue

        print(f"\n\n{C.R}[!] Échec : Le hash n'a pas été trouvé.{C.RESET}")
        print(f" {C.Y}[i] Conseil : Vérifiez que le hash est bien du {hash_type.upper()}{C.RESET}")
        return False

    except Exception as e:
        print(f"\n{C.R}[!] Erreur : {e}{C.RESET}")

if __name__ == "__main__":
    print(BANNER)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-w", "--wordlist", required=True)
    parser.add_argument("-f", "--format", default="sha256")
    args = parser.parse_args()
    
    try:
        crack_hash(args.target, args.wordlist, args.format.lower())
    except KeyboardInterrupt:
        print("\nArrêt...")
