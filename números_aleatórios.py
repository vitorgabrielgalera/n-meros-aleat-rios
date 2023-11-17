#numpy é uma biblioteca para coisas relacionadas a matemática
import numpy as np
#o np faz que acessemos a biblioteca
#random faz que possamos acessar os comandos relacionados a aleatoriedade
#o segundo random faz que ele retorne um float aleatorio entre 0 e 1
x = np.random.random()
print(f"meu número aleatório é : {x}")

#numpy é uma biblioteca para coisas relacionadas a matemática
import numpy as np
lista = ["a","b","c","d","e","f","g","h"]
#o np faz que acessemos a biblioteca
#random faz que possamos acessar os comandos relacionados a aleatoriedade
#choice pega um item aleatório de uma lista
x = np.random.choice(lista,99)
print(f"meu número aleatório é : {x}")