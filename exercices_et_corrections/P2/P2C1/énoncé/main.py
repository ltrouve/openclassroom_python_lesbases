def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    # Créez deux variables  nombre_a_gauche  et  nombre_a_droite  , et affectez-leur chacune un nombre entier.
    nombre_a_gauche=4
    nombre_a_droite=5
    # Créez une variable  symbole  pour stocker le symbole d'opération (+, -, * ou /).
    operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")
    # Créez une dernière variable  resultat  initialisée à 0, qui contiendra ensuite le résultat du calcul.
    resultat=0
    # Vérifiez que les deux variables  nombre_a_gauche  et  nombre_a_droite  sont bien des nombres entiers.
    # Si l'une ou les deux ne sont pas des entiers, affichez un message d'erreur correspondant et quittez le programme. (Aide : Utiliser la fonction  isinstance()  )
    if not isinstance(nombre_a_gauche,int) or not isinstance(nombre_a_droite,int):
        print("pas des entiers")
        exit()
    else:
        print(f"{nombre_a_gauche}   {nombre_a_droite}  sont bien des entiers")
    # Vérifiez que le symbole stocké dans la variable  symbole  correspond bien à une des 4 opérations autorisées (+, -, * ou /) à l’aide du  match.
    # Si le symbole n'est pas correct, affichez un message d'erreur correspondant, et quittez le programme.
    match operation:
        case "+":
            resultat = nombre_a_gauche + nombre_a_droite
        case "-":
            resultat = nombre_a_gauche - nombre_a_droite
        case "*":
            resultat = nombre_a_gauche * nombre_a_droite
        case "/":
            # Vérifie si la variable `nombre_a_droite` n'est pas nulle pour la division
            if nombre_a_droite == 0:
                print("Erreur: impossible de diviser par zéro.")
            else:
                resultat = nombre_a_gauche / nombre_a_droite
        # Si on est dans le cas par défaut, c'est que le symbole est incorrect.
        case _:
            print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

    # Affiche le résultat
    print(f"Le résultat de l'opération est: {resultat}")



# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()