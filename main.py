
# ==========================================
# APPLICATION PYTHON DE GESTION DES TACHES
# Projet : Outils collaboratifs avec Git/GitHub
# ==========================================

# Liste qui contient toutes les tâches
taches = []


# 1. Fonction pour ajouter une tâche
def ajouter_tache():
    print("\n--- AJOUTER UNE TACHE ---")

    titre = input("Titre de la tâche : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return

    # Ajouter la tâche dans la liste
    taches.append(titre)

    print("Tâche ajoutée avec succès.")


# 2. Fonction pour afficher toutes les tâches
def afficher_taches():
    print("\n--- LISTE DES TACHES ---")

    if len(taches) == 0:
        print("Aucune tâche enregistrée.")
        return

    for i, titre in enumerate(taches, start=1):
        print(f"{i}. {titre}")


# 3. Fonction pour rechercher une tâche
def rechercher_tache():
    print("\n--- RECHERCHER UNE TACHE ---")

    mot_cle = input("Donner un mot-clé : ").strip()

    if mot_cle == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
        return

    resultat = False

    for i, titre in enumerate(taches, start=1):
        if mot_cle.lower() in titre.lower():
            print(f"{i}. {titre}")
            resultat = True

    if resultat == False:
        print("Aucune tâche correspondante trouvée.")


# 4. Fonction pour afficher le menu principal
def menu():

    while True:

        print("\n================================")
        print("       GESTION DES TACHES")
        print("================================")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Rechercher une tâche")
        print("0. Quitter")
        print("================================")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_tache()

        elif choix == "2":
            afficher_taches()

        elif choix == "3":
            rechercher_tache()

        elif choix == "0":
            print("Merci d'avoir utilisé notre application !")
            print("Au revoir.")
            break

        else:
            print("Erreur : option invalide. Choisissez 1, 2, 3 ou 0.")


# 5. Lancement du programme
# L'application démarre avec le menu principal.
if __name__ == "__main__":
    menu()
