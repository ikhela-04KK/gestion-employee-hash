import sqlite3
from Emply import Employee
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

  #mise en place de l'algorithme de hachage pour une recherche rapide
  
  def close(self):
      self._conn.close()

    


#enregistrement d'un mail dans la base de donnée
emp_db = EmploiDB('emails.db')
print(emp_db.get_email_emp())

emp1 = Employee("koffi","kan",15,"ida",50000)
emp2 = Employee("kouadio","Eunice",25,"ida2",150000)
emp1_email = emp1.create_email_emp()
emp2_email = emp2.create_email_emp()
emp_db.insert_mail(emp1_email)
emp_db.insert_mail(emp2_email)

emp_db.close()


# print()
# print(emp2.fullname())














