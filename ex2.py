def verificaFibonacci(numero):
    ultimo = 1
    penultimo = 1
    termo = 0

    if numero == 0 or numero == 1:
        print('O número selecionado está na sequência de Fibonacci')
        return

    while termo < numero:
        termo = ultimo + penultimo
        if termo == numero:
            print('O número selecionado está na sequência de Fibonacci')
            return

        penultimo = ultimo
        ultimo = termo
    print('O número selecionado não está na sequência de Fibonacci')
    return


def main():
    numero = input("Insira o número que deseja encontrar: ")
    verificaFibonacci(int(numero))

if __name__ == '__main__':

   main()