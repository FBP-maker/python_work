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

