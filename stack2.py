class Stack:
    '''
    Classe que estancia uma pilha
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        '''

        :return: Um boleano que indica se a pilha está vazia ou não
        '''
        return self.items == []

    def push(self, item):
        '''

        :param item: Algo para adicionar
        :return: None, Adiciona o item no ultimo index da pilha
        '''
        self.items.append(item)

    def pop(self):
        '''

        :return: Retira o último item adicionado nesta lista
        '''
        return self.items.pop()

    def peek(self):
        '''

        :return: O valor do último index
        '''
        return self.items[len(self.items) - 1]

    def size(self):
        '''

        :return: Quantidade de itens na pilha
        '''
        return len(self.items)

'''
teste = Stack()
teste.push(1)
teste.push(5)
teste.push(3)
a = teste.pop()
print(a)
#print(teste.size())
#print(teste.items[1])
'''
