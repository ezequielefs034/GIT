def bubble_sort_otimizado(lista):
    n = len(lista)
    
    for i in range(n):
        trocou = False  
        
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True  
                
        
        if not trocou:
            print(f"-> O algoritmo parou mais cedo na rodada {i+1} porque já estava ordenado.")
            break
            
    return lista

minha_lista = [40, 20, 10, 30, 50, 60, 70]

print("1. Lista original (bagunçada):")
print(minha_lista)

print("\nOrdenando...")
lista_ordenada = bubble_sort_otimizado(minha_lista)

print("\n2. Lista final (ordenada):")
print(lista_ordenada)