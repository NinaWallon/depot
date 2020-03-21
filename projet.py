# Idée de projet : En combien de temps mon vaisseau spatial aura-t-il fini de miner ? (Inspiration Star Trek Fleet Command)

# 1 - Demander à l'utilisateur le type de vaisseau.
# Cuirassé, Explorateur, Intercepteur ou Prospection (conseillé).

print("Types de vaisseaux : \n 1) Cuirassé \n 2) Explorateur \n 3) Intercepteur \n 4) Prospection (conseillé) \n")

type_vaisseau = int(input("Quel type de vaisseau possédez-vous ? \n Tapez 1, 2, 3 ou 4 : "))

liste_types = [1,2,3,4]

if type_vaisseau not in liste_types :
  type_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel type de vaisseau possédez-vous ? \n Tapez 1, 2, 3 ou 4 : "))



# 2 - Demander à l'utilisateur le nom du vaisseau.
# Pourquoi ne pas demander directement ?
# Parce que sinon la liste de vaisseaux est trop longue (pas très lisible).

if type_vaisseau == 1 :
  

# 3 - Demander à l'utilisateur quelle ressource miner.
# Parsteel (pour la construction de bâtiments de station), tritanium (pour la construction de coques et cloisons de vaisseaux), dilithium (pour la contruction de bâtiments et de vaisseaux), gaz (pour améliorer les explorateurs), cristal (pour améliorer les intercepteurs), minerai (pour améliorer les cuirassés) ou latinium (pour la construction et l'assemblage de vaisseaux).

# 4 - Calcul du temps de minage en fonction de la capacité de chargement et de la vitesse de minage du vaisseau (le temps de chargement diffère en fonction de la ressource à miner).
# Convertir les secondes en minutes voire en heures (+ lisible).
