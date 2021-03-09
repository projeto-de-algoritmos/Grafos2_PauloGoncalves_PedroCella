from utils import tasks as TSK
from utils import dijkstra as DK
from prettytable import PrettyTable
import time 
taskList = []

table = PrettyTable()

table.field_names = ["Nome da Tarefa", "Tipo de Tarefa", "Valor da Tarefa"]


print("Bem-vindo(a) ao Gerenciador de Tarefas!\n")

print("Para começar a utilizá-lo nos informe o o peso das atividades, o número de tarefas que deseja gerenciar,o nome dessa tarefa, seu tipo e seu valor\n")

print("Defina num total de 100%, recomenda-se Trabalho: 60, Entreterimento: 30 e Outros: 10, o peso de cada tarefa:\n")
work = int(input("Trabalho: "))
entertainment = int(input("Entreterimento: "))
other = int(input("Outros: "))

qtd_tarefas = int(input("Quantas tarefas deseja realiar? Observação: Recomendamos 4 tarefas, algo além disso pode fazer com que o processo seja demorado\nQuantidade de Tarefas: "))

for i in range(qtd_tarefas):

		nome = input("Dê um nome para a tarefa: ")

		print ("Que tipo de tarefa deseja adicionar")
		tipo = int(input("1-Trabalho;\n2-Entreterimento;\n3-Outros\n"))
	
		while tipo not in range(1, len(TSK.needs().total) + 1):
			print("\n\t\tValor inserido inválido. Tente novamente\n\n")
			print ("Que tipo de tarefa deseja adicionar")
			tipo = int(input("1-Trabalho;\n2-Entreterimento;\n3-Outros\n"))
						

		print("Por fim insira um valor que represente o peso da tarefa do seu ponto de vista. Um valor entre 1 e 100, sendo 1 - baixo e 100- alto")
		valor = int(input("Valor da tarefa: "))
		print("\n")

		table.add_row([nome, tipo, valor])
		
		repetitions = [x for x in taskList if x.name == nome and x.type == tipo]
		if repetitions:
			for i in taskList:
				if i.name == nome:
					print("Valor da tarefa atualizado.")
					i.value = valor
		else:
			taskList.append(TSK.task(nome, tipo - 1, valor, True))

taskList.append(TSK.task("Comer", 3, 25, True))
# Tabela de Tarefas

print("")
print(table)

dayDivision = 150
result = DK.optimizer(TSK.needs(dayDivision, work, entertainment, other), taskList)

print("Calculando....\n")
result.dijkstra()

path, postProcessPath, completedTasks, totalTasks  = result.createPath()


hTable = PrettyTable()
hTable.field_names = ["Horario", "Tarefa"]

hour = 21600
hTable.add_row([time.strftime("%H:%M:%S", time.gmtime(hour)) , "Acordar"])
for i in postProcessPath[1::]:
	hour += ((i[1] * (960 / dayDivision)) * 60)
	hTable.add_row([time.strftime("%H:%M:%S", time.gmtime(hour)) , i[0]])

print("")
print(hTable)

