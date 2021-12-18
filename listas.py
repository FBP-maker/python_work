#Trabalhando com listas.
linux_distribution = ['arch','majaro','debian','ubuntu']

print(linux_distribution[0])
print(linux_distribution[1])
print(linux_distribution[2])
print(linux_distribution[3])
print(linux_distribution[-1])
print(linux_distribution[-2])
print(linux_distribution[-3])
print(linux_distribution[-4])

message0 = linux_distribution[0].title() + ": Distribuição Linux que foi criada por Judd Vinet. As grandes características desse sistema são: flexibilidade, velocidade, simplicidade e minimalismo. \n"
message1 = linux_distribution[1].title() + ": Como principais características ha a destacar o processo simples e intuitivo de instalação, a detecção automática da grande maioria do hardware, possibilidade de gerir/configurar drivers da placa gráfica recorrendo a bash scripting, e um conjunto considerável de configurações ao nível do desktop. \n"
message2 = linux_distribution[2].title() + ": Ótimo desempenho e estabilidade. \n"
message3 = linux_distribution[3].title() + ": Sendo uma das maiores distribuições Linux existentes no mundo, suas principais características são a facilidade e a acessibilidade, além na vasta quantidade de pacotes disponíveis, tornando-o um sistema completo. \n"

print(message0.title())
print(message1.title())
print(message2.title())
print(message3.title())

#Modificando elementos na lista.
linux_distribution[0]='gentoo'
print(linux_distribution)

#Acrescentando um novo elemento.
linux_distribution[0]='arch'
linux_distribution.append('gentoo')
print(linux_distribution)
print('\n') 

#Adicionando elementos a partir de uma lista vazia.
distribuicoes = []
distribuicoes.append('arch')
distribuicoes.append('manjaro')
distribuicoes.append('debian')
distribuicoes.append('ubuntu')
distribuicoes.insert(0, 'gentoo')
distribuicoes.insert(4, 'zorin')
print(distribuicoes)
print('\n')

#após a instrução del ser usanda nao podemos acessar o valor da lista.
del distribuicoes[4]      
print(distribuicoes)
print('\n')

#Removendo um item com o método pop(), "pop" remove o último item de uma lista mas permite que voce trabalhe com esse item depois da remoção.
popremove = distribuicoes.pop(0)
print(distribuicoes)
print(popremove)
print('\n')

#Removendo o item pelo valor.
distribuicoes.remove('debian')
print(distribuicoes)
print('\n')

#Usando o valor de remove depois de retirado da lista
arch_remove = 'arch'
distribuicoes.remove(arch_remove) #apaga apenas a primeira ocorrencia do valor se ouver mais de uma ocôrrencia utilizar um laço.
print(distribuicoes)
print("\nA " + arch_remove.title() + " removido para teste.")

