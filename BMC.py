import numpy as np
import random

"""
3 generadores de números aleatorios, basados en distribuciones de probabilidad: Poisson, Normal y lineal.
"""
def randomLineal():
    return random.randrange(0,4)

def randomPoisson():
    poisson = np.random.poisson(0.5, 1000)
    return poisson[250]

def randomNormal():
    return np.random.standard_normal() 

listDNA = ["A","T","C","G"]    
listRNA = ["A","U","C","G"]    

"""
verificador ADN : solo letras A, C, T, G, no espacios ni caracteres extraños. Recibe un texto de entrada, hilera o archivo, y verifica que el contenido sean solo A, C, T o G
"""
def evaluate_DNA_string(stringDNA):
    stringDNA = stringDNA.upper()
    for charDNA in stringDNA:
        if charDNA not in listDNA:
            print ("Error, esta tira no es valida")
            return
    print ("Exito, esta tira es valida")
"""
verificador ARN : solo letras A, C, U, G, no espacios ni caracteres extraños. Idem, para A, C, U, G.
"""
def evaluate_RNA_string(stringRNA):
    stringRNA = stringRNA.upper()
    for charRNA in stringRNA:
        if charRNA not in listRNA:
            print ("Error, esta tira no es valida")
            return
    print ("Exito, esta tira es valida")
"""
obtener el elemento i-ésimo de una hilera dada
"""
def nthTerm(n, hilera):
    listaHilera = list(hilera)
    return listaHilera[n]
"""
brindar el largo de hilera de un archivo de entrada o texto dado
"""
def getLength(hilera):
    return len(hilera)

"""
verificar si la hilera s es palíndromo
"""
def esPalindromo (hilera):
    listaNum = list(hilera)
    listaInv = list(hilera)
    listaInv.reverse()
    if listaInv == listaNum:
        return True
    else:
        return False
"""
verificar si s es un substring de t, además el proceso inverso, si t es un superstring de s
"""
def substring(hilera1,hilera2):
    hileraPartida1 = hilera2.split(hilera1)
    if(len(hileraPartida1)>1):
        print("El primer string es un substring del segundo.")
    else:
        print("La primera hilera no es un substring de la segunda.")

def superstring(hilera1,hilera2):
    hileraPartida1 = hilera1.split(hilera2)
    if(len(hileraPartida1)>1):
        print("El primer string es un superstring del segundo.")
    else:
        print("La primera hilera no es un superstring de la segunda.")
"""
verificar si s es una subsecuencia de t, además el proceso inverso, si t es una supersecuencia de s
"""
def subsecuencia(hilera1,hilera2):
    listaHilera = list(hilera1)
    for caracter in hilera2:
        if len(listaHilera)==0:
            print("El primer string es una subsecuencia del segundo.")
            return
        elif caracter == listaHilera[0]:
            listaHilera.pop(0)
    print("La primera hilera no es una subsecuencia de la segunda.")

def supersecuencia(hilera1,hilera2):
    listaHilera = list(hilera2)
    for caracter in hilera1:
        if len(listaHilera)==0:
            print("El primer string es una supersecuencia del segundo.")
            return
        elif caracter == listaHilera[0]:
            listaHilera.pop(0)
    print("La primera hilera no es una supersecuencia de la segunda.")

"""
operación concatenación de dos hileras s y t dadas
"""
def concatenar(s, t):
    return s+t
"""
calcular el complemento de una hilera de ADN
"""
def complementoADN(hilera):
    print(hilera)
    stringADN = list(hilera)
    for i in range (0,len(stringADN)):
        if stringADN[i] == 'A':
            stringADN[i] = 'T'
        elif stringADN[i] == 'T':
            stringADN[i] = 'A'
        elif stringADN[i] == 'C':
            stringADN[i] = 'G'
        elif stringADN[i] == 'G':
            stringADN[i] = 'C'
    stringADN = ''.join(stringADN)
    print (stringADN)
    return stringADN
"""
calcular el complemento inverso de una hilera de ADN
"""
def complementoInversoADN(hilera):
    listaComplemento = list(complementoADN(hilera))
    listaComplemento.reverse()
    return ''.join(listaComplemento)

"""
- operación intervalo de una hilera dada, recibe índices i y j de entrada, puede devolver la hilera vacía
"""
def intervalo(i,j,hilera):
    if len(hilera)==0:
        return ""
    elif i<0 or j<0:
        return ""
    if len(hilera)>=j:
        j = len(hilera)-1
    if i>j:
        temp = i
        i=j
        j=temp
    listahilera = list(hilera)
    listaFinal=[]
    for indice in range (i,j+1):
        listaFinal.append(listahilera[indice])
    return ''.join(listaFinal)

"""
- operación prefijo de una hilera, recibe índices s y k de entrada, para obtener los primeros k símbolos de s, puede devolver la hilera vacía
"""
def prefijo(i,hilera):
    if len(hilera)==0:
        return ""
    if i<0:
        return ""
    if len(hilera)>=i:
        return hilera
    listahilera = list(hilera)
    listaFinal=[]
    for indice in range (0,i+1):
        listaFinal.append(listahilera[indice])
    return ''.join(listaFinal)
"""
- operación sufijo de una hilera, recibe índices s y k de entrada, para obtener los últimos k símbolos de s, puede devolver la hilera vacía
"""
def sufijo(i,hilera):
    if len(hilera)==0:
        return ""
    if i<0:
        return ""
    if len(hilera)>=i:
        return hilera
    listahilera = list(hilera)
    listaFinal=listahilera[-i:]
    return ''.join(listaFinal)
"""
verificar si la hilera p es un prefijo de la hilera s
"""
def esPrefijo(p,s):
    if (p==prefijo(len(p)-1,s)):
        return True
    return False
"""
verificar si la hilera s es un sufijo de la hilera t
"""
def esSufijo(s,t):
    if (s==sufijo(len(s)-1,t)):
        return True
    return False

def generarADN(length):
    secuenciaADN = ""
    for i in range(0,length):
        secuenciaADN = secuenciaADN + listDNA[randomLineal()]
    return secuenciaADN

def adn2arn(adn):
    listaADN = list(adn)
    for i in range(0,len(adn)):
        if listaADN[i]=="T":
            listaADN[i]="U"
    return ''.join(listaADN)

def split(hilera, num):
    return [ hilera[start:start+num] for start in range(0, len(hilera), num) ]

listaAminoacidos = [ ["Isoleucine","Ile","I",["ATT", "ATC", "ATA"]],
                     ["Leucine","Leu","L",["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"]],
                     ["Valine","Val","V",["GTT", "GTC", "GTA", "GTG"]],
                     ["Phenylalanine","Phe","F",["TTT", "TTC"]],
                     ["Methionine","Met","M",["ATG"]],
                     ["Cysteine","Cys","C",["TGT", "TGC"]],
                     ["Alanine","Ala","A",["GCT", "GCC", "GCA", "GCG"]],
                     ["Glycine","Gly","G",["GGT", "GGC", "GGA", "GGG"]],
                     ["Proline","Pro","P",["CCT", "CCC", "CCA", "CCG"]],
                     ["Threonine","Thr","T",["ACT", "ACC", "ACA", "ACG"]],
                     ["Serine","Ser","S",["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"]],
                     ["Tyrosine","Tyr","Y",["TAT", "TAC"]],
                     ["Tryptophan","Trp","W",["TGG"]],
                     ["Glutamine","Gln","Q",["CAA", "CAG"]],
                     ["Asparagine","Asn","N",["AAT", "AAC"]],
                     ["Histidine","His","H",["CAT", "CAC"]],
                     ["Glutamic acid","Glu","E",["GAA", "GAG"]],
                     ["Aspartic acid","Asp","D",["GAT", "GAC"]],
                     ["Lysine","Lys","K",["AAA", "AAG"]],
                     ["Arginine","Arg","R",["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"]],
                     ["STOP","STOP","STOP",["TAA", "TAG", "TGA"]]]
def adnName(hilera):
    listaHilera = split(hilera,3)
    if len(listaHilera)<3:
        print("Error: Hilera muy corta.")
        return
    if len(listaHilera[-1])<3:
        del listaHilera[-1]
    print("Elegir tipo de nombres que desea utilizar:")
    print("1. Nombre Largo.")
    print("2. Nombre de 3 letras.")
    print("3. Nombre de 1 letra")
    opcion = input("Elegir tipo de nombres que desea utilizar: ")
    if opcion in ["1","2","3"]:
        opcion = int(opcion)-1
        final = ""
        for codon in listaHilera:
            for elemento in listaAminoacidos:
                if codon in elemento[3]:
                    final = final + " " + elemento[opcion]
        print(final)
    else:
        print("Error: Opcion no valida")
    
def openFile(fileName):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return myfile

def writeFile(fileName,hilera):
    text_file = open(fileName, "w")
    text_file.write(hilera)
    text_file.close()
