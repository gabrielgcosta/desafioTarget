def main():
    faturamento = [["SP",67836.43],[ "RJ",36678.66],["MG",29229.88],["ES",27165.48],["Outros",19849.53]]
    fatTotal = 0
    for i in range (len(faturamento)):
        fatTotal += faturamento[i][1]
    print(fatTotal)

    for i in range (len(faturamento)):
        porcentagem = 0
        porcentagem = (faturamento[i][1] * 100)/fatTotal
        print('Estado: %s, Porcentagem: %.2f' %(faturamento[i][0], porcentagem) + '%')

if __name__ == '__main__':

   main()