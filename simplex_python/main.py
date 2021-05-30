import numpy as np

def read_input():
    n = input("Votre fonction objective Z est composée de combien de variable? \n")
    msg = ''
    for i in range(int(n)):
        msg = msg + "a" + str(i+1) + "x" + str(i+1) + " + "
    z = "Z = " + msg[:-3]
    coef_str = input("entrer les (ai) 1<=i<=" + str(n) + " de la fonction " + z + ". Fait entrer les variable dans une seule ligne séparées par un espace. \n")
    coef_li_str = list(coef_str.split(" "))
    coef = [float(i) for i in coef_li_str]
    inequalities = []
    v = input("Quel est le nombre de contraintes? À part que toutes les variables de Z sont positives. \n")
    coef.extend(np.zeros(int(v)).tolist())
    b_list = []

    for i in range(int(v)):
        type = input("Quelle est le type de l'inégalité? \n 1 - (<=) \n 2 - (>=)\n ")
        if (type == '1'):
            coef_in_str = input("entrer les (ai) 1<=i<=" + str(v) + " et b, de l'inégalité " + msg[:-3] + " <= b. Fait entrer les variable dans une seule ligne séparées par un espace. \n")
            coef_li_str_in = list(coef_in_str.split(" "))
            b = coef_li_str_in.pop(len(coef_li_str_in)-1)
            in_coef = [float(i) for i in coef_li_str_in] + [1 if i==j else 0 for j in range(int(v))]
            b_list = b_list + [float(b)]

        if (type == '2'):
            coef_in_str = input("entrer les (ai) 1<=i<=" + str(n) + " et b, de l'inégalité " + msg[:-3] + " >= b. Fait entrer les variable dans une seule ligne séparées par un espace. \n" )
            coef_li_str_in = list(coef_in_str.split(" "))
            b = coef_li_str_in.pop(len(coef_li_str_in)-1)
            in_coef = [float(i) for i in coef_li_str_in] + [-1 if i==j else 0 for j in range(int(v))]
            b_list = b_list + [float(b)]
        inequalities.append(in_coef)
    
    res = []
    res.append(coef)
    res.append(inequalities)
    res.append(b_list)
    res.append(int(n))
    res.append(int(v))
    return res


def prod_scal(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum = sum + v1[i]*v2[i]
    return sum


def min_max(array, i):
    max = 0
    min = 0
    for j in range(len(array)-1):
        if (array[j+1] > array[max]):
            max = j+1
        if (array[j+1] < array[min]):
            min = j+1
    if (i==1):
        return max
    else:
        return min


def devide(a1, a2):
    l = []
    for i in range(len(a1)):
        if(a2[i] != 0):
            d = a1[i] / a2[i]
        else:
            d = float('nan');
        l.append(d)
    return np.array(l)


li = read_input()
# li=[[100.0, 200.0, 0.0, 0.0, 0.0, 0.0], [[1.0, 4.0, 1, 0, 0, 0], [4.0, 2.0, 0, 1, 0, 0], [1.0, 0.0, 0, 0, 1, 0], [1.0, 1.0, 0, 0, 0, 1]], [480.0, 440.0, 90.0, 150.0], 2, 4]

nb_inequality = np.array(li.pop())
nb_var = np.array(li.pop())
bj = li.pop()
matrice = np.array(li.pop())
cj = np.array(li.pop())
zj_li = []
zj_li.extend(np.zeros(nb_var+nb_inequality).tolist())
zj = np.array(zj_li)
vb_li = []
vb_li.extend(np.zeros(nb_inequality).tolist())
vb = np.array(vb_li)
cj_zj = cj - zj

while (cj_zj[min_max(cj_zj,1)]>0):
    vs = devide(bj, matrice.T[min_max(cj_zj,1)])
    pivot = matrice[min_max(vs,2)][min_max(cj_zj,1)]
    vb[min_max(vs,2)] = cj[min_max(cj_zj,1)]
    elt = bj.pop(min_max(vs, 2))
    bj.insert(min_max(vs, 2), elt / pivot)
    matrice[min_max(vs, 2)] = matrice[min_max(vs,2)] / pivot

    for i in range(nb_inequality):
        if (i!=min_max(vs, 2)):
            a = bj[min_max(vs, 2)]
            elt = bj.pop(i)
            bj.insert(i, (elt - matrice[i][min_max(cj_zj, 1)] * a))
            print(a)
            matrice[i] = matrice[i] - matrice[i][min_max(cj_zj, 1)]*matrice[min_max(vs, 2)]
            print(bj)

    for i in range(nb_var+nb_inequality):
        sum = np.sum(matrice.T[i]*vb)
        zj[i] = sum

    print(matrice)

    cj_zj= cj - zj
    print(cj_zj)

print("Z= ", prod_scal(bj,vb))
