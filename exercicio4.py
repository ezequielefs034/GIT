
valor = True
frutas_precos = { "Banana": 4.50,"Maçã": 7.90,"Laranja": 3.80,"Morango": 12.00,"Uva": 9.50,"Melancia": 15.00,"Abacaxi": 6.00,"Manga": 5.50,"Mamão": 6.80,
    "Limão": 4.20,"Pêra": 8.90,"Pêssego": 11.50,"Abacate": 7.00,"Cereja": 28.00,"Kiwi": 14.90,"Maracujá": 8.20,"Melão": 7.50,"Açaí": 18.00,"Goiaba": 5.00,"Amora": 22.00
}

while valor:

    entrada = input("Digite o nome da fruta: ")

    if entrada == "fim":
        print("obrigado!")
        valor =False
    elif entrada in frutas_precos.keys():
        print(frutas_precos[entrada])
    else:
        print("digite o nome corretemente da fruta!")
































