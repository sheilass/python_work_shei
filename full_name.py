#Manipulação de Strings
first_name = "ada"
last_name = "lovelace"
#para inserir o valor de uma variável em uma string, deve colocar o f antes da aspa inicial (f-strings)
full_name = f"{first_name} {last_name}"
print(full_name)
#usando a f-strings para compor uma frase completa
print(f"Hello, {full_name.title()}!")
#usando a f-strings para atribuir mensagem a uma variável
message = f"Hellooo, {full_name.title()}!"
print(message)
#adicionando uma tabulação ao texto
print("\tPython")
#adicionando uma quebra de linha
print("Languages:\nPython")
#adicionando uma quebra de linha com tabulação
print("Languages:\n\tPython\n\tC#\n\tJavaScript")
