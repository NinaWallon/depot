# Idée de projet : En combien de temps mon vaisseau spatial aura-t-il fini de miner ? (Inspiration Star Trek Fleet Command)

# 1 - Demander à l'utilisateur le type de vaisseau.
# Cuirassé, Explorateur, Intercepteur ou Prospection (conseillé).

print("\nTypes de vaisseaux : \n 1) Cuirassé \n 2) Explorateur \n 3) Intercepteur \n 4) Prospection (conseillé) \n")

type_vaisseau = int(input("Quel type de vaisseau possédez-vous ? \n Tapez 1, 2, 3 ou 4 : "))

liste_types = [1,2,3,4]

if type_vaisseau not in liste_types :
  type_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel type de vaisseau possédez-vous ? \n Tapez 1, 2, 3 ou 4 : "))



# 2 - Demander à l'utilisateur le nom du vaisseau.
# Pourquoi ne pas demander directement ?
# Parce que sinon la liste de vaisseaux est trop longue (pas très lisible).

if type_vaisseau == 1 :

  print("\nVaisseaux cuirassés : \n 1) Corvette d'Orion \n 2) Talla \n 3) Kumari \n 4) Bortas \n 5) USS Intrepid \n 6) Legionary \n 7) Augur \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

  liste_cuirasse = [1,2,3,4,5,6,7]

  if modele_vaisseau not in liste_cuirasse :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))
  
  indice = modele_vaisseau

# Vaisseaux sous forme de dictionnaires avec capacité de chargement (en unités) + vitesse de minage (en sec/unité).

vaisseau_1_1 = {"nom" : "Corvette d'Orion" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_1_2 = {"nom" : "Talla" , "capacite" : 80 , "vitesse" : 1 }
vaisseau_1_3 = {"nom" : "Kumari" , "capacite" : 200 , "vitesse" : 1 }
vaisseau_1_4 = {"nom" : "Bortas" , "capacite" : 230 , "vitesse" : 1 }
vaisseau_1_5 = {"nom" : "USS Intrepid" , "capacite" : 250 , "vitesse" : 1 }
vaisseau_1_6 = {"nom" : "Legionary" , "capacite" : 230 , "vitesse" : 1 }
vaisseau_1_7 = {"nom" : "Augur" , "capacite" : 300 , "vitesse" : 1 }


if type_vaisseau == 2 :

  print("\nVaisseaux explorateurs : \n 1) Realta \n 2) Turas \n 3) Jellyfish \n 4) USS Franklin \n 5) Vahklas \n 6) Brel \n 7) USS Mayflower \n 8) USS Enterprise \n 9) Centurion \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 9 (voir liste des modèles ci-dessus) : "))

  liste_explorateur = [1,2,3,4,5,6,7,8,9]

  if modele_vaisseau not in liste_explorateur :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 9 (voir liste des modèles ci-dessus) : "))
  
  indice = 7 + modele_vaisseau

# Vaisseaux sous forme de dictionnaires avec capacité de chargement (en unités) + vitesse de minage (en sec/unité).

vaisseau_2_1 = {"nom" : "Realta" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_2_2 = {"nom" : "Turas" , "capacite" : 80 , "vitesse" : 1 }
vaisseau_2_3 = {"nom" : "Jellyfish" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_2_4 = {"nom" : "USS Franklin" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_2_5 = {"nom" : "Vahklas" , "capacite" : 200 , "vitesse" : 1 }
vaisseau_2_6 = {"nom" : "Brel" , "capacite" : 250 , "vitesse" : 1 }
vaisseau_2_7 = {"nom" : "USS Mayflower" , "capacite" : 230 , "vitesse" : 1 }
vaisseau_2_8 = {"nom" : "USS Enterprise" , "capacite" : 300 , "vitesse" : 1 }
vaisseau_2_9 = {"nom" : "Centurion" , "capacite" : 230 , "vitesse" : 1 }


if type_vaisseau == 3 :

  print("\nVaisseaux intercepteurs : \n 1) Phindra \n 2) Kehra \n 3) Vi'Dar \n 4) Classe D3 \n 5) Classe D4 \n 6) USS Saladin \n 7) Gladius \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

  liste_intercepteur = [1,2,3,4,5,6,7]

  if modele_vaisseau not in liste_intercepteur :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 7 (voir liste des modèles ci-dessus) : "))

  indice = 16 + modele_vaisseau

# Vaisseaux sous forme de dictionnaires avec capacité de chargement (en unités) + vitesse de minage (en sec/unité).

vaisseau_3_1 = {"nom" : "Phindra" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_3_2 = {"nom" : "Kehra" , "capacite" : 80 , "vitesse" : 1 }
vaisseau_3_3 = {"nom" : "Vi'Dar" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_3_4 = {"nom" : "Classe D3" , "capacite" : 100 , "vitesse" : 1 }
vaisseau_3_5 = {"nom" : "Classe D4" , "capacite" : 200 , "vitesse" : 1 }
vaisseau_3_6 = {"nom" : "USS Saladin" , "capacite" : 250 , "vitesse" : 1 }
vaisseau_3_7 = {"nom" : "Gladius" , "capacite" : 230 , "vitesse" : 1 }


if type_vaisseau == 4 :

  print("\nVaisseaux de prospection : \n 1) ECS Fortunate \n 2) Envoy \n 3) Botany Bay \n 4) North Star \n 5) D'Vor Ferengi \n 6) ECS Horizon \n 7) USS Antares \n 8) Valkis \n")

  modele_vaisseau = int(input("Quel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 8 (voir liste des modèles ci-dessus) : "))

  liste_prospection = [1,2,3,4,5,6,7,8]

  if modele_vaisseau not in liste_prospection :
    modele_vaisseau = int(input("Erreur de saisi, veuillez recommencer. \nQuel modèle de vaisseau possédez-vous ? \n Tapez un chiffre entre 1 et 8 (voir liste des modèles ci-dessus) : "))

  indice = 23 + modele_vaisseau

# Vaisseaux sous forme de dictionnaires avec capacité de chargement (en unités) + vitesse de minage (en unité/sec).

vaisseau_4_1 = {"nom" : "ECS Fortunate" , "capacite" : 200 , "vitesse" : 2 }
vaisseau_4_2 = {"nom" : "Envoy" , "capacite" : 900 , "vitesse" : 3 }
vaisseau_4_3 = {"nom" : "Botany Bay" , "capacite" : 1000 , "vitesse" : 3 }
vaisseau_4_4 = {"nom" : "North Star" , "capacite" : 300 , "vitesse" : 6 }
vaisseau_4_5 = {"nom" : "D'Vor Ferengi" , "capacite" : 3955 , "vitesse" : 2 }
vaisseau_4_6 = {"nom" : "ECS Horizon" , "capacite" : 1750 , "vitesse" : 8 }
vaisseau_4_7 = {"nom" : "USS Antares" , "capacite" : 3000 , "vitesse" : 9 }
vaisseau_4_8 = {"nom" : "Valkis" , "capacite" : 3000 , "vitesse" : 9 }

vaisseau = (vaisseau_1_1, vaisseau_1_2, vaisseau_1_3, vaisseau_1_4, vaisseau_1_5, vaisseau_1_6, vaisseau_1_7, vaisseau_2_1, vaisseau_2_2, vaisseau_2_3, vaisseau_2_4, vaisseau_2_5, vaisseau_2_6, vaisseau_2_7, vaisseau_2_8, vaisseau_2_9, vaisseau_3_1, vaisseau_3_2, vaisseau_3_3, vaisseau_3_4, vaisseau_3_5, vaisseau_3_6, vaisseau_3_7, vaisseau_4_1, vaisseau_4_2, vaisseau_4_3, vaisseau_4_4, vaisseau_4_5, vaisseau_4_6, vaisseau_4_7, vaisseau_4_8)


# 3 - Demander à l'utilisateur quelle ressource miner.
# Parsteel (pour la construction de bâtiments de station), tritanium (pour la construction de coques et cloisons de vaisseaux),
# dilithium (pour la contruction de bâtiments et de vaisseaux), gaz (pour améliorer les explorateurs),
# cristal (pour améliorer les intercepteurs), minerai (pour améliorer les cuirassés)
# ou latinium (pour la construction et l'assemblage de vaisseaux).

print("\nListe de ressources à miner : \n 1) Parsteel \n 2) Tritanium \n 3) Dilithium \n 4) Minerai \n 5) Gaz \n 6) Cristal \n 7) Latinium \n")

ressource = int(input("Quelle ressource voulez-vous miner ? \n Tapez un chiffre entre 1 et 7 (voir liste des ressources ci-dessus) : "))

liste_ressources = [1,2,3,4,5,6,7]

if ressource not in liste_ressources :
  ressource = int(input("Erreur de saisi, veuillez recommencer. \nQuelle ressource voulez-vous miner ? \n Tapez un chiffre en 1 et 7 (voir liste des ressources ci-dessus) : "))


# Coefficient des ressources

res_1 = {"nom" : "Parsteel" , "coef" : 1}
res_2 = {"nom" : "Tritanium" , "coef" : 4}
res_3 = {"nom" : "Dilithium" , "coef" : 15}
res_4 = {"nom" : "Minerai" , "coef" : 5}
res_5 = {"nom" : "Gaz" , "coef" : 5}
res_6 = {"nom" : "Cristal" , "coef" : 5}
res_7 = {"nom" : "Latinium" , "coef" : 50}

res = (res_1, res_2, res_3, res_4, res_5, res_6, res_7)

# 4 - Calcul du temps de minage en fonction de la capacité de chargement et de la vitesse de minage du vaisseau
# (le temps de chargement diffère en fonction de la ressource à miner).
# Convertir les secondes en heure.s, minute.s, seconde.s (+ lisible).

temps_sec = vaisseau[indice-1]["capacite"]/vaisseau[indice-1]["vitesse"]*res[ressource-1]["coef"]

temps_h = temps_sec // 3600
minutes_restantes = temps_sec % 3600

temps_min = minutes_restantes // 60
secondes_restantes = minutes_restantes % 60

print("\n\nVotre vaisseau aura fini de miner dans ", temps_h, " heure.s, ", temps_min, " minute.s et ", round(secondes_restantes,0), " seconde.s.")
