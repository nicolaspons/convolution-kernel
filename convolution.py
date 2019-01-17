"""
x: vecteur de l'image
k: vecteur du kernel
"""
def convolution(x, k):
    # on inverse les lignes et les colonnes, ça revient à inverser le vecteur
    k = k[::-1]
    # on calcule la taille du kernel et de l'image 
    n = int(len(x)**0.5)
    m = int(len(k)**0.5)
    l = []
    # mid est le centre du kernel
    mid = (m // 2, m // 2)
    for pixel in range(len(x)):
        # on calcule la postition courrante de l'index sur le vecteur x avec la notation matricielle
        currPos = (pixel % n, pixel // n)
        res = 0
        for element in range(len(k)):
            # initPosker correspond à la position initiale de l'element sur le kernel sous forme de notation matricielle
            initPosKer = (element % m, element // m)
            """
            On va calculer la nouvelle position de l'element en fonction cette fois-ci du pixel actuel
            Cela va nous permettre par la suite de vérifier si cette position est dans les bornes du vecteur x
            """
            posKer = tuple(map(lambda x, y, z: x - y + z, initPosKer, mid, currPos))
            """
            On vérifie si la position de l'element (en notation matricielle est bonne c'est-à-dire dans les bornes du vecteur x
            Si c'est le cas, on applique la convolution
            """
            if posKer[0] >= 0 and posKer[0] < n and posKer[1] >= 0 and posKer[1] < n:
                idX = posKer[0] + n * posKer[1]
                idK = initPosKer[0] + m * initPosKer[1]
                res += x[idX] * k[idK]
        l.append(res)
    return l

if __name__ == "__main__":
    pass