"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module joueur.py
        Ce module contient l'implémentation de la structure de données
        qui gère un joueur et ses caractéristiques
"""
from os import linesep
from unittest import defaultTestLoader
import const


def Joueur(couleur, nom, nb_points, nb_faux_mvt, pos_pacman, pos_fantome,
           objets):
  """Créer un nouveau joueur à partir de ses caractéristiques

    Args:
        couleur (str): une lettre majuscule indiquant la couleur du joueur
        nom (str): un nom de joueur
        nb_points (int): un entier qui indique le nombre de points du joueur
        nb_faux_mouvements (int): un entier qui indique le nombre de faux mouvements autorisés pour le joueur
        pos_pacman (tuple): une paire d'entiers indiquant sur quelle case se trouve le pacman du joueur
        pos_fantome (tuple): une paire d'entiers indiquant sur quelle case se trouve le fantome du joueur
        objets (dict): un dictionnaire indiquant la durée restante pour chaque objet du joueur

    Returns:
        dict: un dictionnaire représentant le joueur
    """
  return {
      "couleur": couleur,
      "nom": nom,
      "nb_points": nb_points,
      "nb_faux_mouvements": nb_faux_mvt,
      "pos_pacman": pos_pacman,
      "pos_fantome": pos_fantome,
      "objets": objets
  }


def joueur_from_str(description):
  """créer un joueur à partir d'un chaine de caractères qui contient
      ses caractéristiques séparées par des ; dans l'ordre suivant:
      "couleur;nb_points;nb_faux_mvt;lin_p;col_p;lin_f;col_f;duree_glout;
      duree_immo;duree_mur;nom_joueur"

  Args:
      description (str): la chaine de caractères contenant les caractéristiques
                          du joueur

  Returns:
      dict: le joueur ayant les caractéristiques décrite dans la chaine.
  """
  val = description.split(";")

  #création du joueur
  return Joueur(val[0], val[10], int(val[1]), int(val[2]), (int(val[3]), int(val[4])), \
                (int(val[5]), int(val[6])), {const.GLOUTON: int(val[7]), const.IMMOBILITE: int(val[8]), \
                                             const.PASSEMURAILLE: int(val[9])})


def get_couleur(joueur):
  """retourne la couleur du joueur

    Args:
        joueur (dict): le joueur considéré

    Returns:
        str: une lettre indiquant la couleur du joueur
    """
  return joueur['couleur']


def get_nom(joueur):
  """retourne le nom du joueur

    Args:
        joueur (dict): le joueur considéré

    Returns:
        str: le nom du joueur
    """
  return joueur['nom']


def get_nb_points(joueur):
  """retourne le nombre de points du joueur
    joueur (dict): le joueur considéré

    Returns:
        int: la réserve du joueur
    """
  return joueur["nb_points"]


def get_nb_faux_mvt(joueur):
  """retourne le nombre de faux mouvements autorisés pour le joueur
    joueur (dict): le joueur considéré

    Returns:
        int: le nombre de faux mouvements autorisés du joueur
    """
  return joueur["nb_faux_mouvements"]


def get_objets(joueur):
  """retourne la liste des objets possédés par le joueur
    joueur (dict): le joueur considéré

    Returns:
        list(int): la liste des objets possédés par le joueur
    """
  if "objets" in joueur:
    return [objet for objet, duree in joueur["objets"].items() if duree > 0]
  return None


def get_duree(joueur, objet):
  """retourne la duree de vie de l'objet possédé par le joueur
    joueur (dict): le joueur considéré
    objet (str): un identifiant d'objet

    Returns:
        int: un entier indiquant la durée de vie l'objet possédé par le joueur
            0 indique que le joueur n'a pas l'objet ou que celui-ci a une durée de vie de 0
    """
  if "objets" in joueur:
    objets = joueur["objets"]
  if objet in objets:
    return objets[objet]
  return 0


def get_pos_pacman(joueur):
  """retourne la position du pacman du joueur. ATTENTION c'est la position stockée dans le
        pacman. On ne la calcule pas
    joueur (dict): le joueur considéré

    Returns:
        tuple: une paire d'entiers indiquant la position du pacman du joueur.
    """
  if "pos_pacman" in joueur:
    return joueur["pos_pacman"]
  return None


def get_pos_fantome(joueur):
  """retourne la position du fantome du joueur. ATTENTION c'est la position stockée dans le
        fantome. On ne la calcule pas
    joueur (dict): le joueur considéré

    Returns:
        tuple: une paire d'entiers indiquant la position du fantome du joueur.
    """
  if "pos_fantome" in joueur:
    return joueur["pos_fantome"]
  return None


def set_pos_pacman(joueur, pos):
  """met à jour la position du pacman du joueur

    Args:
        joueur (dict): le joueur considéré
        pos (tuple): une paire d'entiers (lin,col) indiquant la position du joueur
    """
  joueur["pos_pacman"] = pos


def set_pos_fantome(joueur, pos):
  """met à jour la position du fantome du joueur

    Args:
        joueur (dict): le joueur considéré
        pos (tuple): une paire d'entiers (lin,col) indiquant la position du joueur
    """
  joueur["pos_fantome"] = pos


def add_points(joueur, quantite):
  """ modifie le nombre de points du joueur.
        ATTENTION! La quantité ajoutée peut être négative et le total du joueur peut devenir négatif aussi

    Args:
        joueur (dict): le joueur considéré
        quantite (int)): un entier positif ou négatif inquant la variation du nombre de points
    Returns:
        int: le nouveau nombre de points du joueur
    """
  if "nb_points" in joueur:
    joueur["nb_points"] += quantite
    return joueur["nb_points"]
  return None


def faux_mouvement(joueur):
  """Enlève 1 au nombre de faux mouvements autorisés pour le joueur

    Args:
        joueur (dict): le joueur considéré
    Returns:
        int: le nombre de faux mouvements autorisés restants
    """
  joueur["nb_faux_mouvements"] -= 1
  return joueur["nb_faux_mouvements"]


def reinit_faux_mouvements(joueur):
  """Réinitialise le nombre de faux mouvements autorisés pour le joueur

    Args:
        joueur (dict): le joueur considéré
    """
  joueur["nb_faux_mouvements"] = 4


def ajouter_objet(joueur, objet):
  """ajoute un objet au joueur.
        La durée de vie de l'objet (si elle est supérieure à 0) est ajoutée
        Le nombre de points du joueur est mis à jour
        Les informations sur les objets sont stockées dans const.PROP_OBJET
    Args:
        joueur (dict): le joueur considéré
        objet (int): l'objet considéré
    """
  if objet in const.PROP_OBJET:
    point, durabilite = const.PROP_OBJET[objet]
    add_points(joueur, point)
    objets = joueur["objets"]
    if objet in objets:
      objets[objet] += durabilite


def maj_duree(joueur):
  """décrémente la durée de vie des objets possédés par le joueur.
        Si la durée d'un objet est à 0 celle-ci reste à 0

    Args:
        joueur (dict): le joueur considéré
    """
  for objet in joueur["objets"]:
    if joueur["objets"][objet] > 0:
      joueur["objets"][objet] -= 1
  return joueur


# A NE PAS DEMANDER
def joueur_2_str(joueur, separateur=";"):
  return str(joueur["couleur"])+separateur+str(joueur["nb_points"])+\
      separateur+str(joueur["nb_faux_mvt"])+separateur+\
      str(joueur["pos_pacman"][0])+separateur+str(joueur["pos_pacman"][1])+\
      separateur+str(joueur["pos_fantome"][0])+separateur+str(joueur["pos_fantome"][1])+\
      separateur+str(joueur["objets"][const.GLOUTON])+separateur+\
      str(joueur["objets"][const.IMMOBILITE])+separateur+\
      str(joueur["objets"][const.PASSEMURAILLE])+separateur+joueur["nom"]+'\n'
