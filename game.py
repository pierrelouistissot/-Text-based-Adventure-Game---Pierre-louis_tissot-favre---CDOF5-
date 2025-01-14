def intro():
    print("Bienvenue dans l'aventure textuelle !")
    print("Vous vous réveillez dans une forêt sombre, sans aucun souvenir de la façon dont vous êtes arrivé ici.")
    print("Devant vous se trouvent trois chemins :")
    print("1. Un sentier mystérieux enveloppé de brouillard.")
    print("2. Une clairière ensoleillée avec des fleurs.")
    print("3. Un tunnel sombre et menaçant.")
    choice = input("Quel chemin choisissez-vous ? (1/2/3): ")

    if choice == "1":
        misty_path()
    elif choice == "2":
        sunny_clearing()
    elif choice == "3":
        dark_tunnel()
    else:
        print("Choix invalide. Veuillez réessayer.")
        intro()


def misty_path():
    print("Vous marchez sur le sentier brumeux. Vous entendez des bruits étranges autour de vous.")
    print("Soudain, une créature mystérieuse apparaît devant vous !")
    print("1. Vous tentez de parler à la créature.")
    print("2. Vous fuyez immédiatement.")
    print("3. Vous attaquez la créature avec une branche trouvée au sol.")
    choice = input("Que faites-vous ? (1/2/3): ")

    if choice == "1":
        print("La créature est amicale et vous montre un chemin secret vers la sortie de la forêt. Vous êtes sauvé !")
    elif choice == "2":
        print("Vous courez, mais vous trébuchez et la créature vous attrape. Fin tragique.")
    elif choice == "3":
        print("Vous blessez la créature, mais elle devient furieuse et vous attaque. Fin tragique.")
    else:
        print("Choix invalide. Veuillez réessayer.")
        misty_path()


def sunny_clearing():
    print("Vous arrivez dans une clairière lumineuse. C'est paisible ici.")
    print("Au centre, vous voyez un coffre brillant.")
    print("1. Vous ouvrez le coffre.")
    print("2. Vous ignorez le coffre et explorez plus loin.")
    print("3. Vous vous reposez dans la clairière.")
    choice = input("Que faites-vous ? (1/2/3): ")

    if choice == "1":
        print("Le coffre contient un trésor qui vous donne la force de quitter la forêt en toute sécurité. Félicitations !")
    elif choice == "2":
        print("Vous trouvez une autre partie de la forêt, mais vous êtes rapidement perdu à nouveau. Vous trouvez une maison.")
        house_scene()
    elif choice == "3":
        print("Pendant que vous vous reposez, un serpent venimeux vous mord. Fin tragique.")
    else:
        print("Choix invalide. Veuillez réessayer.")
        sunny_clearing()


def house_scene():
    print("Vous découvrez une petite maison en bois. Elle semble abandonnée.")
    print("1. Vous entrez dans la maison.")
    print("2. Vous continuez votre chemin.")
    print("3. Vous examinez les environs de la maison.")
    choice = input("Que faites-vous ? (1/2/3): ")

    if choice == "1":
        print("À l'intérieur de la maison, vous trouvez des provisions et une carte pour sortir de la forêt. Vous êtes sauvé !")
    elif choice == "2":
        print("Vous continuez à marcher, mais vous vous perdez à nouveau. Votre aventure continue.")
        intro()
    elif choice == "3":
        print("En examinant les environs, vous trouvez un passage caché qui mène à un trésor. Félicitations !")
    else:
        print("Choix invalide. Veuillez réessayer.")
        house_scene()


def dark_tunnel():
    print("Vous entrez dans le tunnel sombre. Vous entendez des gouttes d'eau et le bruit de vos propres pas.")
    print("Soudain, une lumière apparaît au loin.")
    print("1. Vous courez vers la lumière.")
    print("2. Vous restez sur place et attendez.")
    print("3. Vous explorez le tunnel dans l'obscurité.")
    choice = input("Que faites-vous ? (1/2/3): ")

    if choice == "1":
        print("La lumière vous mène à la sortie de la forêt. Vous êtes libre !")
    elif choice == "2":
        print("Vous attendez, mais rien ne se passe. Vous entendez un bruit étrange derrière vous.")
        print("1. Vous affrontez la source du bruit.")
        print("2. Vous courez dans le tunnel.")
        sub_choice = input("Que faites-vous ? (1/2): ")
        if sub_choice == "1":
            print("Une meute de chauves-souris vole au-dessus de vous. Vous les suivez et trouvez la sortie. Vous êtes sauvé !")
        elif sub_choice == "2":
            print("Vous courez, mais vous glissez et vous vous blessez. Fin tragique.")
        else:
            print("Choix invalide. Veuillez réessayer.")
            dark_tunnel()
    elif choice == "3":
        print("Dans l'obscurité, vous tombez dans un piège caché. Fin tragique.")
    else:
        print("Choix invalide. Veuillez réessayer.")
        dark_tunnel()


if __name__ == "__main__":
    intro()
