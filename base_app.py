import sqlite3
from employé import Employee

conn = sqlite3.connect('ikhela.db')

c=conn.cursor()

# c.execute("""CREATE TABLE employees ( 
#         premier text,
#         dernier text,
#         pay integer
#         )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:premier, :dernier, :pay)", {'premier': emp.first,'dernier': emp.last, 'pay': emp.pay})
        
def get_emps_by_name():
    c.execute("SELECT * FROM employees")# pour afficher toutes tables confondu, et aussi dernier=:dernier",{'dernier':lastname}
    return c.fetchall()

def update_pay(emp,pay): 
    with conn:  # esssayons de de remplacer les valeurs de SET par d'autre pouvoir si ça vas être modifié
        c.execute("""UPDATE employees SET pay=:pay
                    WHERE premier= :premier AND dernier=:dernier
                """,
                    {'premier':emp.first, 'dernier':emp.last, 'pay':emp.pay}
                )

def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE premier = :premier AND dernier = :dernier""",
                {'premier':emp.first, 'dernier':emp.last, 'pay':emp.pay}
                )
        
emp_1=Employee('John','Doe',80000)# nous avons créer une classe qui permet d'ajouter des elements à notre base de données
emp_2=Employee('Jane','Doe',90000)
emp_3=Employee('marc','chiu',45000)
emp_4=Employee('marc','Doe',80000)
# insert_emp(emp_1)
# print()
# insert_emp(emp_2)
# print()
# insert_emp(emp_3)
# print()
# insert_emp(emp_4)
emps=get_emps_by_name() 
# print(emps)
# 

# update_pay(emp_1, 18500)
# remove_emp(emp_2)
update_pay(emp_1, 195000)# permet de modifier son solde uniquement 
print(emps)
# emps=get_emps_by_name("Doe") 
# print(emps)



conn.commit()
conn.close()
