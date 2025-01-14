import cours
import datetime

import os
import win32com.client

Dossier_cour = "" # Dossier dans lequel on trouve les dossier de matière

def pin_unpin(folder_path):

    folder_path = f"{Dossier_cour}{folder_path}"
    if not os.path.exists(folder_path):
        return

    shell = win32com.client.Dispatch("Shell.Application")
    
    # Obtient l'objet Folder correspondant au chemin du dossier
    folder = shell.NameSpace(os.path.dirname(folder_path))
    
    # Obtient l'objet ShellFolderItem
    item = folder.ParseName(os.path.basename(folder_path))

    # Accède au menu contextuel de l'élément
    verb_to_pin = None
    for verb in item.Verbs():
        # Rechercher l'action "Épingler à l'écran de démarrage"
        if "Épingler &à l’accès rapide" in verb.Name:
            verb_to_pin = verb
            break

    if verb_to_pin is not None:
        verb_to_pin.DoIt()


def pin_list_folder():
    shell = win32com.client.Dispatch("Shell.Application")
    quick_access = shell.Namespace("shell:::{679f85cb-0220-4080-b29b-5540cc05aab6}")
    return [element for element in [item.Name for item in quick_access.Items()] if element not in ['Bureau', 'Téléchargements', 'Documents', 'Images', 'Musique', 'Cours', 'Corbeille', 'Vidéos']] # Sert un peu a rien puisque le programme n'arriveras pas a désépingler un dossier qui n'est pas dans dossier_cour
    

def get_week_info():

    emploi_du_temps = {
        "Lundi": cours.monday,
        "Mardi": cours.tuesday,
        "Mercredi": cours.wensday,
        "Jeudi": cours.thursday,
        "Vendredi": cours.friday,
    }
    # Obtenir la date actuelle
    today = datetime.date.today()

    # Trouver le jour de la semaine
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    jour_semaine = jours_semaine[today.weekday()]

    # Trouver le numéro de la semaine
    week_number = today.isocalendar()[1]

    # Vérifier si la semaine est paire ou impaire
    semaine_type = "a" if week_number % 2 == 0 else "b"

    cours_aujourdhui = emploi_du_temps.get(jour_semaine, [])

    return semaine_type, cours_aujourdhui

# Appel de la fonction
semaine, cours_aujourdhui = get_week_info()

# Affichage du résultat
##print(pin_list_folder())
for folder in pin_list_folder() :
    ##print(folder)
    pin_unpin(folder)

# Afficher les cours du jour
for cour in cours_aujourdhui:
    # Obtenir l'heure actuelle
    time_now_obj = datetime.datetime.now().time()
    
    
    # Convertir time2 en un objet time
    time_start_obj = datetime.datetime.strptime(cour.start_hour, "%H:%M:%S").time()
    time_end_obj = datetime.datetime.strptime(cour.end_hour, "%H:%M:%S").time()
    
    # Comparer l'heure actuelle avec time2
    if time_start_obj < time_now_obj and time_now_obj < time_end_obj:
        if semaine in cour.week :
            pin_unpin(cour.name)
            ##print(cour.name)
            break