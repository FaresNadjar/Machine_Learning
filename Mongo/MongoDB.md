# Intro

MongoDb est un système de base de données dans la mouvance NoSQL. Il est orienté documents. 
Rappel : Dans un système de base de données relationnelles, les informations sont stockées par ligne dans des tables. Ces tables sont mises en relation en utilisants des clés primaires et étrangères. Dans MongoDb, l'information est modélisée sur un document au format JSON (Javascript Object Notation).

Le format JSON (JavaScript Object Notation) se base sur 2 types d'éléments:
- la paire clé/valeur, par exemple \nom\: \Phoenix\
- le tableau, par exemple \couleurs-primaires\ : [\cyan\, \jaune\, \magenta\]

Sachant que la valeur d'une paire clé/valeur peut être un objet et que le tableau peut contenir des objets, on peut ordonner les informations sur plusieurs niveaux:

{\acteur\: { \nom\: \Phoenix\, \prenom\ : \Joaquim\ },

\roles\ : [ 

         {\personnage\ : \Theodore\, \film\ : \her\}, 
         
         {\personnage\ : \Leonard Kraditor\,\film\ : \Two Lovers \} 
         
        ] 
                

# Commandes principales : 
- use name_DB : Création de la base de données name_DB si elle n'existe pas. Cette base contient des collections dans lesquelles on ajoute nos documents. Une collection est donc un ensemble de documents de même nature. 
- db.Collection_Name.insert( <document> ) : création implicite de la collection lors de l'insertion du premier document
- db.Collection_Name.count() :renvoie le nombre de documents présents dans Collection_Name
- db.Collection_Name.find() : Donne l'ensemble des documents inclus dans la collection (Nul pour les gros documents). La méthode find prend pour premier paramètre un objet JSON qu'elle va prendre comme critère de recherche.
- db.produits.find({dixmill:9999}) : renvoie les documents pour lesquels dixmill=9999. Différentes opérandes pour les critères de recherche.
    - $gt : plus grand que
    
    - $lt : plus petit que

    - $gte : plus grand ou égal à
    
    - $lte: plus petit ou égal à
    
    - $or : pour récupérer les documents qui correspondent à 2 critères différents
    
    - $and : pour cumuler des critères

- db.C_Name.find({Critere_Recherche} , {_id:0, var1:1, var3:1...}) : Retourne les valeurs suivant le critère de recherche, mais pas toute la base, seulement les colonnes dont les titres sont à 1 (ici var1 et var3)
- db.C_Name.sort() : Permet de trier la Collection 
(Ex: db.produits.find({mill : {$in: [500, 600, 700]}}).sort({mill:-1})) avec -1 pour décroissant et 1 pour croissant pour la variable mill 

- update() : permet de mettre à jour les données qu'on a 
 - db.produits.update({dixmill: 666} , {$set : {suspicieux:true}}) : ajoute suspicieux = True pour la première occurence de dixmill:666
 
 - db.produits.update({dixmill: 666} , {$set : {suspicieux:true}}, {multi:true}) : ajoute suspicieux = True pour toutes les occurences de dixmill:666
 
 - db.produits.update({dixmill: 666} , {$unset : {suspicieux:1}}, {multi:true}) : Suppression de la propriété suspicieux ajoutée au préalable
 
- db.produits.remove({mill: 600}) : Supprime tous les elements pour lesquels on a mill:600

# Mise à jour d'un tableau (Explication à travers un exemple) : 
- db.produits.insert({compteur:100001, tab:['a','b','c']}) : insère la ligne compteur 100001 contenant tab

- db.produits.update({compteur:100001}, {$push : {tab : 'd'}}) : $push permet d'ajouter 'd' à tab (il existe $pushAll pour ajouter un tableau de valeur)

- db.produits.update({compteur:100001}, {$pop : {tab:1}}) : Suppression du dernier élément si 1 et du premier élement si -1

- db.produits.update({compteur:100001}, {$addToSet : {tab : 'b'}}) : Permet d'ajouter 'b' à tab sans doublons
