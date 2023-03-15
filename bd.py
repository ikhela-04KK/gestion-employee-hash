import sqlite3
from empl import Employee
import hashlib
 #creation d'ue base de donnée pour les tresoin
 # 2- Resumé sur les base de donnée , l'algèbre relationnelle 
 # """

class EmploiDB:
  def __init__(self,db_name):
    self._conn = sqlite3.connect(db_name)
    self._cursor = self._conn.cursor()
    
    self._cursor.execute("""CREATE TABLE IF NOT EXISTS emails (
    email VARCHAR(255)
    )"""
              )

  def insert_mail(self,email):
    with self._conn:
      self._cursor.execute("INSERT INTO emails VALUES (:email)",{'email':email})

  #afficher les emails disponible dans la base de donnée
  def get_email_emp(self):
    self._cursor.execute("SELECT * FROM emails")
    return self._cursor.fetchall()

  #Mise en place d'une fonctoin de hachage qui va se comporter comme un decorateur lorsque les données seront saisies
  def hash_email(self,email):
    hash_mail = hashlib.sha256(b"salt" + email.encode())
    return hash_mail.hexdigest()
  
  #fonction qui permert de verifier si un email existe dans la base de donnée avec le hash
  def check_email(self,email):
    hashed_email = self.hash_email(email)
    for mail in self.get_email_emp():
      return hashed_email == self.hash_email(mail)#cette fonction retourne True si le hash est correcte, False sinon
    
    
    
    
    # je pourrais utililser pour mettre directement les mails hashés, les mots de passes hachés dans la base de donnéreturn self._cursor.execute("SELECT * FROM emails WHERE email = :email",{'email':hash_mail.hexdigest()}).fetchone()
  

    
    # return hashlib.sha256(self._cursor.execute("SELECT email FROM emails").fetchone()[0].encode('utf-8')).hexdigest()
   
  
  
  
  
  def close(self):
      self._conn.close()
      
      

    


#enregistrement d'un mail dans la base de donnée
emp_db = EmploiDB('emails.db')
print(emp_db.get_email_emp())



# emp1 = Employee("koffi","kan",15,"ida",50000)
emp3 = Employee("koffi","kan",15,"ida",50000)
# emp2 = Employee("kouadio","Eunice",25,"ida2",150000)


# emp1_email = emp1.create_email_emp()
# emp2_email = emp2.create_email_emp()
emp3_email = emp3.create_email_emp()
#test de verification des mails existant dans la base de données avec hash
print(emp_db.check_email(emp3_email))


# emp_db.insert_mail(emp1_email)
# emp_db.insert_mail(emp2_email)



emp_db.close()


# print()
# print(emp2.fullname())














