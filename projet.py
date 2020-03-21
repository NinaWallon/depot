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

  print("Vaisseaux cuirassés : \n 1) Corvette d'Orion \n 2) Talla \n 3) Kumari \n 4) Bortas \n 5) USS Intrepid \n 6) Legionary \n 7) Augur \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

  liste_cuirasse = [1,2,3,4,5,6,7]

  if modele_vaisseau not in liste_cuirasse :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))


if type_vaisseau == 2 :

  print("Vaisseaux explorateurs : \n 1) Realta \n 2) Turas \n 3) Jellyfish \n 4) USS Franklin \n 5) Vahklas \n 6) Brel \n 7) USS Mayflower \n 8) USS Enterprise \n 9) Centurion \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 9 (voir liste des modèles ci-dessus) : "))

  liste_explorateur = [1,2,3,4,5,6,7,8,9]

  if modele_vaisseau not in liste_explorateur :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 9 (voir liste des modèles ci-dessus) : "))

if type_vaisseau == 3 :

  print("Vaisseaux intercepteurs : \n 1) Phindra \n 2) Kehra \n 3) Vi'Dar \n 4) Classe D3 \n 5) Classe D4 \n 6) USS Saladin \n 7) Gladius \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

  liste_intercepteur = [1,2,3,4,5,6,7]

  if modele_vaisseau not in liste_intercepteur :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

if type_vaisseau == 4 :

  print("Vaisseaux de prospection : \n 1) ECS Fortunate \n 2) Envoy \n 3) Botany Bay \n 4) NOrth Star \n 5) D'Vor Frengi \n 6) ECS Horizon \n 7) USS Antares \n 8) Valkis \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 8 (voir liste des modèles ci-dessus) : "))

  liste_prospection = [1,2,3,4,5,6,7,8]

  if modele_vaisseau not in liste_prospection :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 8 (voir liste des modèles ci-dessus) : "))


# 3 - Demander à l'utilisateur quelle ressource miner.
# Parsteel (pour la construction de bâtiments de station), tritanium (pour la construction de coques et cloisons de vaisseaux),
# dilithium (pour la contruction de bâtiments et de vaisseaux), gaz (pour améliorer les explorateurs),
# cristal (pour améliorer les intercepteurs), minerai (pour améliorer les cuirassés)
# ou latinium (pour la construction et l'assemblage de vaisseaux).

# 4 - Calcul du temps de minage en fonction de la capacité de chargement et de la vitesse de minage du vaisseau
# (le temps de chargement diffère en fonction de la ressource à miner).
# Convertir les secondes en minutes voire en heures (+ lisible).
