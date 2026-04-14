#!/usr/bin/env python3
import sys

# Style Urus
class C:
    G = "\033[38;5;82m"    # Vert
    Y = "\033[38;5;226m"   # Jaune
    B = "\033[38;5;45m"    # Bleu
    RESET = "\033[0m"

BANNER = fr"""
{C.B}  _    _                      _    _           _ _____  {C.RESET}
{C.B} | |  | |                    | |  | |         (_)  __ \ {C.RESET}
{C.B} | |  | |_ __ _   _ ___      | |__| | __ _ ___ _| |  | |{C.RESET}
{C.B} | |  | | '__| | | / __|     |  __  |/ _` / __| | |  | |{C.RESET}
{C.B} | |__| | |  | |_| \__ \     | |  | | (_| \__ \ | |__| |{C.RESET}
{C.B}  \____/|_|   \__,_|___/     |_|  |_|\__,_|___/_|_____/ {C.RESET}
{C.G}             Identify your hash format instantly{C.RESET}
"""

def identify_hash(h):
    h = h.strip()
    length = len(h)
    
    print(f" {C.B}[*]{C.RESET} Hash    : {C.Y}{h}{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Longueur: {C.G}{length} caractères{C.RESET}")
    print(f" {C.B}[*]{C.RESET} Résultat: ", end="")

    if length == 32:
        print(f"{C.G}MD5{C.RESET}")
    elif length == 40:
        print(f"{C.G}SHA-1{C.RESET}")
    elif length == 56:
        print(f"{C.G}SHA-224{C.RESET}")
    elif length == 64:
        print(f"{C.G}SHA-256{C.RESET}")
    elif length == 96:
        print(f"{C.G}SHA-384{C.RESET}")
    elif length == 128:
        print(f"{C.G}SHA-512{C.RESET}")
    else:
        print(f"{C.Y}Format inconnu ou non standard{C.RESET}")

if __name__ == "__main__":
    print(BANNER)
    if len(sys.argv) < 2:
        print(f" Usage: python3 hash_id.py <votre_hash>")
    else:
        identify_hash(sys.argv[1])
