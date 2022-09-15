# This is a sample Python script.
from Locohaz.Clients import *
from Locohaz.Admin import *
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
   print("Bienvenue dans notre application")
   print(" LOCOHAZ")
"""
   client = Client('olivier', "zoungrana")

   client1 = client
   client1.Commande()
   client1.Total()
   client1.CreateDataframe()
   client1.CreateCsv()
   client1.CreateGraph()
"""

admin = Admin('olivier', 'zoungrana')
admin1 = admin
admin1.add_admin()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
