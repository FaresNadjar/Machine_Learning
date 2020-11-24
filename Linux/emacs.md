# Emacs CHEATSHEET
## Commandes de base : 

- CTRL-v : next screen
- ALT-v : previous screen
- CTRL-l : center the screen around the mouse
- CTRL-f : next character
- CTRL-b : Previous character
- ALT-f : next word
- ALT-b : previous word
- CTRL-n : next line 
- CTRL-p : previous line
- CTRL-a : beginning of line
- CTRL-e : end of line
- ALT-a : beginning of sentence
- ALT-e : end of sentence
- ALT-< : beginning of document 
- ALT-> : end of document 
- CTRL-u 8 CTRL-f : avance de 8 caractères
- CTRL-u 8 ALT-b : recule de 8 mots
- CTRL-g : stoppe une execution en cas de bug

## Fenetres : 
- CTRL-x 1 : laisse une seule fenetre ouverte
- CTRL-u 0 CTRL-l : la fenetre commence là ou il y a le curseur
- CTRL-h k CTRL-f : une nouvelle fenetre apparait avec un help sur CTRL f


## Insertion et suppression : 
Il suffit d'écrire et d'effacer au clavier.

- CTRL-u (n) (char) : insère char n fois
- CTRL-d :Efface le caractère situé après le curseur
- ALT-d : Supprime le mot situé après le curseur
- CTRL-k : Supprime du curseur à la fin de la ligne
- ALT-k : Supprime jusqu'à la fin de la phrase courante

## supprimer une selection de texte : 
- Placez le curseur sur la lettre du début de séléction
- Faites CTRL-SPC. Emacs devrait afficher un message "Mark set"
   en bas de l'écran.
- Déplacez le curseur sur la lettre de fin de séléction
- Faites CTRL-w.

## Supprimer une ligne
- Placez le curseur au début d'une ligne non vide puis 
- Faites CTRL-k pour supprimer le texte de celle-ci.
- Refaites CTRL-k : vous verrez que cela supprime le Newline qui suit cette ligne.

## Récupérer le dernier texte supprimé : 
- CTRL-y : place la dernière suppression
- ALT-y : recupère la suppression antérieure pour pouvoir etre collée avec CTRL-y
- CTRL-/ : annule la dernière modif


## Fichiers : 
- CTRL-x CTRL-f : ouvre un fichier 
- CTRL-x CTRL-s : Sauvegarde le fichier
- CTRL-x CTRL-b	: Liste des tampons.
- CTRL-x CTRL-c	: Quitte Emacs.
- CTRL-x 1 : Détruit toutes les fenêtres, sauf une.
- CTRL-x u : Annulation

## Recherche : 
- CTRL-s

## Fenetres multiples : 
- Placez le curseur sur une ligne et faites CTRL-l CTRL-l.
- Faites maintenant CTRL-x 2 pour diviser l'écran en deux fenêtres. Toutes les deux affichent la meme fenetre et le curseur    reste dans celle du haut.
- Faites CTRL-ALT-v pour faire défiler le texte de la fenêtre du bas
- Tapez CTRL-x o afin de placer le curseur dans la fenêtre du bas.
- Utilisez CTRL-v et ALT-v pour la faire défiler. Conservez ces instructions dans la fenêtre du haut.
- Faites à nouveau CTRL-x o pour replacer le curseur dans la fenêtre du haut. Le curseur est exactement où il était avant.

## Cadres multiples :
- Tapez ALT-x make-frame <Entree> Voyez un nouveau cadre apparaître dans votre écran.
- Tapez ALT-x delete-frame <Entree> Ceci détruit le cadre sélectionné.

