def quick_sort(lista):
    
    if len(lista) <= 1:
        return lista
    else:

        pivo = lista[-1]
       
        menores = [x for x in lista[:-1] if x <= pivo]
        maiores = [x for x in lista[:-1] if x > pivo]
        
       
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


minha_lista = [35, 12, 89, 7, 44, 2, 90, 15]

print("1. Lista original (bagunçada):")
print(minha_lista)

print("\nOrdenando com Quick Sort...")
lista_ordenada = quick_sort(minha_lista)

print("\n2. Lista final (ordenada):")
print(lista_ordenada)