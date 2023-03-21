
class Employee: 
  
    def __init__(self,nom="",prenom="",age=0,salaire=0,deprt="",sal=0):
      self._nom =nom
      self._prenom =prenom
      self._deprt =deprt
      self._age = age
      self._sal =salaire



    # Mettre une property qui empêche l'utilisateur inscrit un nom avec des caractères nom reconnu comme des chiffres 
    
    #ici on crée un email pour l'organisation
    #ici comme ça on peut mettre une verification si le l'email qui sera envoyé est déja inscrit dans la base de donnée , il va le modifier de selle sorte à avoir une email eligible ou nom

    
    def create_email_emp(self):
      return f'{self._nom}{self._prenom}@ikhela.io'
      
    def fullname(self):
      return f'{self._nom},{self._prenom}'

#Avant d'aller plus loin , il faut que tu commmences les testes , de telle sorte à voir ce qui ce marche , ce qui ne marche pas
