#Convidados3.4:
convidados = ['bill','munger','júlio']
assunto0 = convidados[0] + ". Quais são so atuais projetos em desenvolvimento e planos da fundação."
assunto1 = '\n' + convidados[1] + ". Quais os principais investimentos e planos para futuro."
assunto2 = '\n' + convidados[2] + ". De onde saiu a inspiração para sua obra pontos fortes de fracos além de suas pretençoes."
print(assunto0.title() + '\n' + assunto1.title()+ '\n' + assunto2.title())
#exercício 3.5
print('\n' + convidados[1].title() + " :Não podera comparecer por questões de saúde.")
convidados[1] = 'albert'

convite0 = "Convidamos so sernhor: " + convidados[0] + " para o jantar...."
convite1 = "Convidamos so sernhor: " + convidados[1] + " para o jantar...."
convite2 = "Convidamos so sernhor: " + convidados[2] + " para o jantar...."

print('\n' + convite0.title() + '\n' + convite1.title()+ '\n' + convite2.title())

#exercício 3.6
print('\n' + "Acrescentado mais convidados: Jobs, Linch e Linux")

convidados.insert(0, 'Linux')
convidados.insert(2, 'Jobs')
convidados.append('Linch')


convite3 = "Convidamos so sernhor: " + convidados[3] + " para o jantar...."
convite4 = "Convidamos so sernhor: " + convidados[4] + " para o jantar...."
convite5 = "Convidamos so sernhor: " + convidados[5] + " para o jantar...."


print('\n' + convite0.title() + '\n' + convite1.title() + '\n' + convite2.title() + '\n' + convite3.title() + '\n' + convite4.title() + '\n' + convite5.title())
#exercício3.7
print("Poderam ser convidados apenas duas pessoas da lista:")
print(convidados)

popremove0 = convidados.pop(5)
print('\n' + "Sentimos muito mas o jantar foi cancelado " + "Sr  " +popremove0 + ".")
popremove1 = convidados.pop(4)
print('\n' + "Sentimos muito mas o jantar foi cancelado " + "Sr  " +popremove1 + ".")
popremove2 = convidados.pop(3)
print('\n' + "Sentimos muito mas o jantar foi cancelado " + "Sr  " +popremove2 + ".")
popremove3 = convidados.pop(2)
print('\n' + "Sentimos muito mas o jantar foi cancelado " + "Sr  " +popremove3 + ".")
print('\n' + "Confirmando seu preseça lugar jantar" + " " + convidados[0] + "." + '\n' + "Confirmando seu preseça lugar jantar" + " " + convidados[1].title())
del convidados [0]
del convidados [0]
print(convidados)
