import hashlib
import threading

# Cette fonction crée un hash SHA256 d'une chaîne de caractères
def hash_string(string):
    sha256 = hashlib.sha256()
    sha256.update(string.encode())
    return sha256.hexdigest()

# Cette fonction vérifie si un email se trouve dans la liste de hashes en utilisant des threads
def check_email(email, hash_list):
    email_hash = hash_string(email)
    for h in hash_list:
        if email_hash == h:
            print(f"{email} est présent dans la liste des emails")
            return True
    print(f"{email} n'est pas présent dans la liste des emails")
    return False

# Exemple d'utilisation de la fonction check_email avec des threads
email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@hotmail.com"]
hash_list = [hash_string(e) for e in email_list] # Convertit la liste d'emails en une liste de hashes
threads = []

while True:
    # Demande les informations d'identité à l'utilisateur
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    age = input("Entrez votre âge : ")
    filiere = input("Entrez votre filière : ")
    email = input("Entrez votre email : ")

    # Crée un nouveau thread pour vérifier si l'email est présent dans la liste de hashes
    t = threading.Thread(target=check_email, args=(email, hash_list))
    threads.append(t)
    t.start()

    # Attend que tous les threads soient terminés avant de demander une nouvelle entrée utilisateur
    for t in threads:
        t.join()
    threads.clear()
