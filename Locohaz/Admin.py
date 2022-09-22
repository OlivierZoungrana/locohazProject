from Locohaz.Clients import *
from .data import *

class Admin:
    def __init__(self,*args):
        self.name = args[0]
        self.surname = args[1]
    def __repr__(self):
        return self.name + "" + self.surname

    stocks_article = {
        "tonnelle": [],
        "chaises": []
    }
    def is_admin(self):

        print("Bienvenue sur l'interface Admin")
        print(("Confirmer votre numero admin : "))

        idAdmin = int(input("votre Id: "))

        for i in adminIdentifiants:
            if i == idAdmin:
                print("vous pouvez continuer, vous etes admin Bienvenue")
                return idAdmin
                break
            else:
                print("vous netes pas admin Aurevoir")
                break
        return
    def add_admin(self):
        if self.is_admin() :
            print("vous souhaitez ajouter un admin")
            id1 = int(input("entrer Id"))
            id2 = int(input("confirmer Id"))
            if id1 == id2 and id1 not in adminIdentifiants:
                if 0<len(str(id1))<=3 & str(id1).startswith("1"):
                    adminIdentifiants.append(id1)
                    print(adminIdentifiants)
                else:
                    print("votre id ne contient pas les caractères requis")
            else:
                print("veuillez corriger votre Id existe déja")
    def Add_article_inStock(self):
        print("ajouter un article dans la stock")
        article = input("intitulé article : ")
        quantity= int(input("entrer la quantite: "))

        if article in articles:
            articles[article] += quantity
            print(articles)
        else:
            articles[article] +=quantity
            print(articles)





