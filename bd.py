import sqlite3
from empl import Employee
import hashlib
import threading
 #creation d'ue base de donnée pour les tresoin
 # 2- Resumé sur les base de donnée , l'algèbre relationnelle 


class EmploiDB:
  def __init__(self,db_name):
    self._conn = sqlite3.connect(db_name)
    self._cursor = self._conn.cursor()
    self._cursor.execute("""CREATE TABLE IF NOT EXISTS emails (
    email VARCHAR(255)
    )"""
              )
  #une insertion 
  def insert_mail(self,email):
    with self._conn:
      self._cursor.execute("INSERT INTO emails VALUES (:email)",{'email':email})

  #permettra de modifier les informations d'un employé
  def update_mail(self,email):
    self._cursor.execute("UPDATE emails SET email=:email WHERE email=:email",{'email':email})
  
  #permet de supprimer un employé avec un email 
  def delete_mail(self,email):
      self._cursor.execute("DELETE FROM emails WHERE email=:email",{'email':email})

  #afficher les emails disponible dans la base de donnée
  def get_email_emp(self):
    self._cursor.execute("SELECT * FROM emails")
    return self._cursor.fetchall()

  #Mise en place d'une fonctoin de hachage qui va se comporter comme un decorateur lorsque les données seront saisies
  def hash_email(self,email):
    for mail in email:
      hash_mail = hashlib.sha256(b"salt" + mail.encode())
      return hash_mail.hexdigest()
  
  #fonction qui permert de verifier si un email existe dans la base de donnée avec le hash
  def check_email(self,email):
    hashed_email = self.hash_email(email)
    for mail in self.get_email_emp():
        return self.hash_email(mail[0]) == hashed_email #cette fonction retourne True si le hash est correcte, False sinon 

      
    
  def close(self):
      self._conn.close()

emp_db = EmploiDB('/workspaces/gestionEmp/emails.db')
print(type((emp_db.get_email_emp())[1][0]))



def get_identity():
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    age = int(input("Entrez votre âge : "))
    filiere = input("Entrez votre filière : ")
    deptr = input("Entrez votre département : ")
    sal = int(input("Entrez votre salaire : "))
    return nom,prenom,age, filiere,deptr,sal

def main_thread():
  
    while True:
      
      # Demande les informations d'identité à l'utilisateur
      nom,prenom,filiere,age,deptr,sal =get_identity()
      emp= Employee(nom,prenom,filiere,age,deptr,sal)

      #creation de l'email de l'utilisateur 
      emp_email = emp.create_email_emp()

      #1ere verificaition du thread de l'email 
      verify_thread = threading.Thread(target=emp_db.check_email,args=(emp_email,))

      #2eme creer un thread pour hasher 
      hash_mail_thread = threading.Thread(target=emp_db.hash_email,args=(emp_email,))

      #lancer les deux threads en même temps 
      verify_thread.start()
      hash_mail_thread.start()

      #lance le thread de l'email 
      verify_thread.join()
      hash_mail_thread.join()

      hashed_mail = hash_mail_thread.result
      if email_exist := verify_thread.result:
        print(f"L'email {email_exist} existe dans la base de données.")
      else:
        print(f"L'email {email_exist} n'existe pas dans la base de données.")

      # afficher le hash de l'adresse e-mail
      print(f"Le hash de l'email est: {hashed_mail}")
    
main_thread() 

 













