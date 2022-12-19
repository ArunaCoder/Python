"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

# lista_b = lista_a
# if you do that, and change one list, the other will change too

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)