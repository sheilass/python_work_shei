#Aplicação de atividades do livro, pg 59

#Use uma variável para representar o nome de uma pessoa e exiba uma mensagem para essa pessoa. Sua mensagem deve ser simples como: "Olá Sheila, gostaria de aprender Python hoje?"
nome = "sheila"
message = f"Olá {nome.title()}, gostaria de aprender Python hoje?"
print(message)

#Use uma variável para representar o nome de uma pessoa e, em seguida, exiba o nome dessa pessoa em letras minúsculas, maiúsculas e as primeiras letras maiúsculas
nome_dois = "sheilA"
print(nome_dois.lower())
print(nome_dois.upper())
print(nome_dois.title())

#Encontre uma citação de uma pessoa famosa que voce admira. Exiba a citação e o nome do autor. Sua saída deve ter uma tabulação e o texto em itálico
message = f"\t\n\x1b[3mAlbert Einstein\x1b[0m disse uma vez:\x1b[3m\"Uma pessoa que nunca cometeu um erro nunca tentou nada novo\"\x1b[0m."
print(message)

#Repita o exercício anterior mas desta vez represente o nome da pessoa famosa usando uma variável chamada famous_person.Depois, escreva sua mensagem e a represente  com uma nova variável chamada message.
famous_person =  "Albert Einstein"
# para colocar as aspas duplas coloque o \" e para colocar o texto em itálico colocar no inicio da palavra ou frase o \x1b\3m e finalizar com \x1b\0m"
citacao = "\"Uma pessoa que nunca cometeu um erro nunca tentou nada novo\""
message =  f"\t\x1b[3m{famous_person}\x1b[0m disse uma vez:\x1b[3m{citacao}\x1b[0m."
print(message)

#Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no inicio e no final do nome. Lembre-se de usar cada combinação de caracteres, \t e \n, pelo menos uma vez
#Exiba o nome uma vez  para que o espaço em branco ao redor  do nome seja mostrado.Em seguida, printe o nome usando cada uma das três funções de remoção, lstrip(), rstrip() e strip()
nome_aleatorio =" Nomes:\n\tMunhoz\n\tMariano "
print("opa"+nome_aleatorio.lstrip()+"sem espaço na esquerda")
print("opa"+nome_aleatorio.rstrip()+"sem espaço na direita")
print("opa"+nome_aleatorio.strip()+"sem espaço na direita e esquerda")




