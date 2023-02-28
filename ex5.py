def main():
    frase = input("insira a frase a ser invertida: ")
    fraseInvertida = ''
    caracter = len(frase)-1
    for i in range (len(frase)):
        fraseInvertida += frase[caracter]
        caracter -= 1
    print(fraseInvertida)
    

if __name__ == '__main__':

   main()