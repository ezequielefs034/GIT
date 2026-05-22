def merge_sort(lista):
 
    if len(lista) <= 1:
        return lista

   
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

   
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

   
    return mesclar(esquerda, direita)


def mesclar(esquerda, direita):
    resultado = []
    i = j = 0

    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado



minha_lista = [38, 27, 43, 3, 9, 82, 10, 19]

print("1. Lista original (bagunçada):")
print(minha_lista)

print("\nOrdenando com Merge Sort...")
lista_ordenada = merge_sort(minha_lista)

print("\n2. Lista final (ordenada):")
print(lista_ordenada)