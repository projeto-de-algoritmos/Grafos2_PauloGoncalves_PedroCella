from utils import tasks as TKS

taskList = []



print("Bem-vindo(a) ao Gerenciador de Tarefas!\n")

print("Para começar a utilizá-lo nos informe o numero de tarefas que deseja gerenciar,o nomde dessa tarefa, seu tipo e seu valor\n")

qtd_tarefas = int(input("Quantas tarefas deseja realiar? Observação: Recomendamos X tarefas\nQuantidade de Tarefas: "))

for i in range(qtd_tarefas):

		nome = input("Dê um nome para a tarefa: ")

		print ("Que tipo de tarefa deseja adicionar")
		tipo = int(input("1-Trabalho;\n2-Entreterimento;\n3-Outros\n"))
	
		while tipo not in range(1, len(TKS.needs().total) + 1):
			print("\n\t\tValor inserido inválido. Tente novamente\n\n")
			print ("Que tipo de tarefa deseja adicionar")
			tipo = int(input("1-Trabalho;\n2-Entreterimento;\n3-Outros\n"))
						

		print("Por fim insira um valor que represente o peso da tarefa do seu ponto de vista. Um valor entre 1 e 100, sendo 1 - baixo e 100- alto\n")
		valor = int(input("Valor da tarefa: "))
		
		repetitions = [x for x in taskList if x.name == nome and x.type == tipo]
		if repetitions:
			for i in taskList:
				if i.name == nome:
					print("Valor da tarefa atualizado.")
					i.value = valor
		else:
			taskList.append(TKS.task(nome, tipo - 1, valor, True))

# r = TKS.requirements()
# t = TKS.task("Tomar Banho", 1, )