from .data import articles
import pandas as pd
import matplotlib.pyplot as plt

prix_tonnelle = 50
prix_chaise = 2
commande = {
    "name": [],
    "tonnelle": [],
    "chaise": [],
    "total": 0
}

class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return self.name + " " + self.surname
    def informationCustomers(self):
        self.name = input("votre nom : ")
        self.surname = input("your surname :")
        return
    def CommandeTonnelle(self):
        print("vous vouhaitez des tonnelles ")
        quantityTonnelles = int(input("what quantity ? "))

        if quantityTonnelles > articles["tonnelles"]:
            print("nous ne disposons du nombre demandé")
        else:
            #commande["tonnelle"] = commande["tonnelle"] + quantityTonnelles
            commande["tonnelle"].append(quantityTonnelles)
            print(" votre commande a été enregistré")
            print(commande)

    def CommandeChaise(self):
        print("vous vouhaitez des chaises")
        quantityChaise = int(input("what quantity ? "))
        if quantityChaise > articles["Chaises"]:
            print("nous ne disposons du nombre demandé")
        else:
            #commande["chaise"] =commande["chaise"] + quantityChaise
            commande["chaise"].append(quantityChaise)
            print(" votre commande a été enregistré")
            print(commande)

    def Commande(self):

        name = input("entrer un nom: ")
        commande['name'].append(name)
        print("**********************************************************")
        print("Tap 1 pour tonnelle and 2 for chair")
        print("***********************************************************")

        choix = int(input("entrer votre choix : "))

        if choix == 1:
            print(self.CommandeTonnelle())
            print("souhaitez vous aussi des chaises : 3 pour oui 4 pour non")
            reponse = int(input("Votre lettre"))
            if reponse == 3:
                self.CommandeChaise()
            elif reponse == 4:
                print("Merci")
            else:
                print("choississez une lettre ")
        if choix == 2:
            print(self.CommandeChaise())
            print("souhaitez vous aussi des tonnelles : 3 pour oui 4 pour non")
            reponse = int(input("Votre lettre"))
        else:
            print("that product doesn't exist")
    def Total(self):
       cout = (commande["tonnelle"][0] * prix_tonnelle )+ (commande["chaise"][0] * prix_chaise)
       commande["total"] += cout
       return
    def CreateDataframe(self):
        df = pd.DataFrame(commande)
        df.describe()
        return df
    def CreateCsv(self):
        self.CreateDataframe().to_csv("commande.csv", index=False)
        return "fichier créé"

    def CreateGraph(self):
        self.CreateDataframe().plot(x="tonnelle", y="chaise", color="green")
        plt.show()
















