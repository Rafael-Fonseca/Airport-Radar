'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''
#Classe que estancia uma pilha
class Stack:
    def __init__(self):
        self.items = []

    #return: Um boleano que indica se a pilha está vazia ou não
    def isEmpty(self):
        return self.items == []

    #param item: Algo para adicionar
    #return: None, Adiciona o item no ultimo index da pilha
    def push(self, item):
        self.items.append(item)

    #return: Retira o último item adicionado nesta lista
    def pop(self):
        return self.items.pop()

    #return: O valor do último index
    def peek(self):
        return self.items[len(self.items) - 1]

    #return: Quantidade de itens na pilha
    def size(self):
        return len(self.items)

