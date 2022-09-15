from Locohaz.Clients import *
from .data import *

class Admin:
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return self.name + "" + self.surname

    stocks_article = {
        "tonnelle": [],
        "chaises": []
    }
    def admin_identity(self):

        print("Bienvenue sur l'interface Admin")
        print(("Confirmer votre numero admin : "))

        idAdmin = int(input("votre Id: "))

        for i in adminIdentifiants:
            if i == idAdmin:
                print("vous pouvez continuer, vous etes admin Bienvenue")
                break
            else:
                print("vous netes pas admin")
                break
        return idAdmin
    def add_admin(self):
        if self.admin_identity() :
            print("vous souhaitez ajouter un admin")
            id1 = int(input("entrer Id"))
            id2 = int(input("confirmer Id"))
            if id1 == id2 and id1 not in adminIdentifiants:
                adminIdentifiants.append(id1)
                print(adminIdentifiants)
            else:
                print("veuillez corriger votre Id existe déja")
    def GestionStocks(self):
        pass




