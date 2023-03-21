import sqlite3
import hashlib
import threading
from empl import Employee

# from contextlib import closing
 #creation d'ue base de donnée pour les tresoin
 # 2- Resumé sur les base de donnée , l'algèbre relationnelle 



class EmploiDB:
  def __init__(self,db_name):
    self._conn = sqlite3.connect(db_name,check_same_thread=False)
    self._cursor = self._conn.cursor()
    self._cursor.execute("""CREATE TABLE IF NOT EXISTS emails (
    email VARCHAR(255)
    )"""
              )
    self._lock = threading.Lock()
  #une insertion
  
  '''
  utilisation des verroues avec Lock pour permet à la base de donnée d'utiliser des threads 
  
  il y'a avait le problème de concurrent d'accès c'est ça qui nous a permis de regler le problème on pouvait aussi utilisé async/await pour regler le probmème 
  '''  
  def __enter__(self):
      self._lock.acquire() # permet au système d'acquérire le verroue
      return self

  def __exit__(self, exc_type, exc_val, exc_tb):
      self._lock.release() # permet de relâcher le verroue 
      self.close()
      
  
       
  def insert_mail(self,email):
    # with self._conn:
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
      

#creation d'un verrou de thread pour eviter les accès concurrents à la base de donnée avec Lock



with EmploiDB('/workspaces/gestionEmp/emails.db') as emp_db:
  # print(type(([emp_db.get_email_emp()))

  def get_identity():
      nom = input("Entrez votre nom : ")
      prenom = input("Entrez votre prénom : ") 
      age = int(input("Entrez votre âge : "))
      filiere = input("Entrez votre filière : ")
      deptr = input("Entrez votre département : ")
      sal = int(input("Entrez votre salaire : "))
      return nom,prenom,age, filiere,deptr,sal

  def main_thread():
  
      # Demande les informations d'identité à l'utilisateur
      nom,prenom,filiere,age,deptr,sal =get_identity()
      emp= Employee(nom,prenom,filiere,age,deptr,sal)

      #creation de l'email de l'utilisateur 
      emp_email = emp.create_email_emp()

      #1ere verificaition du thread de l'email 
      verify_thread = threading.Thread(target=emp_db.check_email,args=(emp_email,))

      #2eme creer un thread pour hasher 
      hash_mail_thread = threading.Thread(target=emp_db.hash_email,args=(emp_email,))

      #lancer les deux threads en même temps*
      hash_mail_thread.start()
      verify_thread.start()


      #lance le thread de l'email 
      verify_thread.join()
      hash_mail_thread.join()
      
      if emp_db.check_email(emp_email):
          print("Cet email existe déjà dans la base de données.")
      else:
          emp_db.insert_mail(emp_email)
          print("Email ajouté avec succès.")
          
  main_thread() 

  













