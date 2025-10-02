#Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.
# Filtrar pares (filter + lambda)


lista = [1,2,3,4,5]
print(list(filter(lambda num:num % 2 == 0, lista)))