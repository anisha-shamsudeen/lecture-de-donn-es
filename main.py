#### Imports et définition des variables globales
"""Module contenant plusieurs fonctions sur le contenu d'un fichier"""

FILE = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    i = 0
    liste = []
    with open(filename, mode='r', encoding='utf8') as filename:
        f = filename.readlines()
    for l in f :
        l = l.split(';')
        i += 1
        for n in l :
            l[i] = int(n)
        liste.append(l)
    return liste

def get_list_k(data, k):
    """retourne la ligne k du fichier
    
    Args :
        data (list) : la liste contenant les lignes sous forme de list
        k (int) : la ligne à retourner
        
    Returns:
        list : la ligne qui correspond à la ligne k
    """
    l = data[k]
    return l

def get_first(l):
    """retourne le premier entier de la ligne l du fichier
    
    Args :
        l (list) : la liste contenant des nombres entiers.
        
    Returns:
        int : le premier élément de la list
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément de la ligne l du fichier
    
    Args :
        l (list) : la liste contenant des nombres entiers.
        
    Returns:
        int : le dernier élément de la list
    """
    return l[len(l) - 1]

def get_max(l):
    """retourne le nombre entier maximum de la list l
    
    Args :
        l (list) : la liste contenant des nombres entiers.

    Returns:
        int : l'élément maximum de la list l
    """
    maximum = l[0]
    for e in l :
        maximum = max(max, e)
    return maximum

def get_min(l):
    """retourne le nombre entier minimum de la list l
    
    Args :
        l (list) : la liste contenant des nombres entiers.

    Returns:
        int : l'élément minimum de la list l
    """
    minimum = l[0]
    for e in l :
        minimum = min(min, e)
    return minimum

def get_sum(l):
    """retourne la somme des nombres entiers de la list l
    
    Args :
        l (list) : la liste contenant des nombres entiers.

    Returns:
        int : la somme des nombres entiers de la list l
    """
    somme = 0
    for s in l :
        somme += s
    return somme


#### Fonction principale


def main():
    """ 
    Fonction qui teste les méthodes"""
    data = read_data(FILE)
    for i, l in enumerate(data):
        print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
