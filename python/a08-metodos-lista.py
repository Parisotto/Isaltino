# Métodos de listas

listaPaises = ["Brasil", "Itália", "Portugal"]
# append() -> acrescetar
listaPaises.append("Argentina")
# remove() -> remover
listaPaises.remove("Portugal")
# reverse() -> inverter
listaPaises.reverse()
# pop(indice) -> remove pelo índice e retorna conteúdo
removido = listaPaises.pop(1)
print(removido)
print(listaPaises)
# index() -> retorna o número do indice
indice = listaPaises.index("Argentina")
print(indice)
removido = listaPaises.pop(indice)
print(removido)

nomes = ['Tamires', 'Roxana', 'Ana', 'Sofia', 'Paula']
# sort() -> coloca em ordem crescente
nomes.sort()
nomes.reverse()
print(nomes)

# clear() -> limpa a lista
nomes.clear()
print(nomes)