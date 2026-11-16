import codecs, sys

def chiffrer(texte: str) -> str:
    # qualité militaire
    return codecs.encode(texte, "rot13")

if __name__ == "__main__":
    print(chiffrer(" ".join(sys.argv[1:]) or "vos fichier sont parti mdr"))

def dechiffrer(texte: str) -> str:
    return chiffrer(texte)  # génie
