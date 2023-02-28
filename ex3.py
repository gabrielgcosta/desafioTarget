import json

def achaMaiorMenorMedia(dados):
    maior = 0
    menor = 0
    media = 0
    cont = 0
    for i in dados:
        if i['valor'] != 0:
            cont += 1
            media = media + i['valor']
            if i['valor'] > maior:
                maior = i['valor']
            if i['valor'] < menor or menor == 0:
                menor = i['valor']
    media = media / cont
    return maior, menor, media

def diasAcimaMedia(dados, media):
    qtdDias = 0
    for i in dados:
        if i['valor'] > media:
            qtdDias += 1

    return qtdDias


def main():
    
    with open("dados.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    
    
    maior, menor, media = achaMaiorMenorMedia(dados)
    qtdDias = diasAcimaMedia(dados, media)
    print("Maior valor de faturamento: ", maior)
    print("Menor valor de faturamento: ", menor)
    print("Quantidade de dias onde o faturamento foi superior a média mensal: ", qtdDias)

            

    

if __name__ == '__main__':

   main()