from .tasks import task as TKS
from .tasks import needs as ND
from operator import itemgetter
from prettytable import PrettyTable
import math

class optimizer:
	def __init__(self, needs: ND, taskList: list) -> None:

			self.startNode = TKS("Acordar", 3, 10000, True)
			self.endNode = TKS("Dormir", 3, 10000, True)

			self.needs = needs
			self.taskList = taskList

			self.distances = {}


	def timePassed(self, node):
		"""
		Calcula quanto tempo se passou desde o node que foi passado para a função.
		"""
		tmpNode = node
		totalInstances = 1

		while self.distances.get(tmpNode)[0].name != "Acordar":
			tmpNode = self.distances.get(tmpNode)[0]
			if not tmpNode:
				break
			totalInstances += 1
		return totalInstances


	def resolveWeights(self, baseNode, newNode):
		"""
		Função que muda os valores de cada node para cada novo conjunto de nodes.
		"""

		if baseNode.name == "Comer" and newNode.name == "Comer": # Caso de comer grafico 2
			newNode.value = baseNode.value + 10000

		elif newNode.name == "Comer" :

			if self.needs.completed[newNode.type] >= self.needs.total[newNode.type]:

				newNode.value = math.inf
				self.needs.resetCompleted()
			# ((e-1) * x ) - (e + 2)
			elif newNode.value * (((math.e-1)*self.sameTaksB4(newNode))  - math.e + 2) > 9999: #Caso o crescimento seja muito para calcular e não ficar um numero muito pequeno.
				newNode.value = 0
			else:
				newNode.subValue(((math.e-1)*self.sameTaksB4(newNode))  - math.e + 2)


		else: # Caso de trabalhos, entreterimento e outros grafico 1
			if self.needs.completed[newNode.type] >= self.needs.total[newNode.type]:
				newNode.value = math.inf
				self.needs.resetCompleted()

			elif newNode.type is self.needs.getPriority():
				# x^(e) - x + 1
				newNode.subValue(newNode.value * ((self.sameTaksB4(newNode)**math.e) - self.sameTaksB4(newNode) + 1))
				self.needs.resetCompleted()


	def sameTaksB4(self, node):
		"""
		Conta quantas tarefas iguais ao node que foi passado foram feitas anteriomente.
		"""
		sameTasks = 0
		tmpNode = node
		while self.distances[tmpNode][0].name != "Acordar":
			if self.distances[tmpNode][0].name == node.name:
				sameTasks+=1
			else:
				break
			tmpNode = self.distances.get(tmpNode)[0]
		return sameTasks


	def countTasksDone(self, node):
		"""
		Função para calcular quanto de cada tipo de tarefa foi feito.
		"""
		tmpNode = node
		valueToSum = 1
		while self.distances[tmpNode][0].name != "Acordar":
			self.needs.addToCompleted(self.distances[tmpNode][0].type, valueToSum)
			tmpNode = self.distances.get(tmpNode)[0]
			# print(tmpNode)


	def createNextNodeLine(self, baseNode):
			"""
			Função para criar o proximo conjunto de tarefas.
			"""
			newDistances = []

			if self.timePassed(baseNode) >= self.needs.dayTotalTime + 2 or not baseNode: # Caso se tenha passado o total de tempo total, retornar para criar o node de dormir.
				return False			
			
			for tmpNode in self.taskList:

				newNode = TKS(tmpNode.name, tmpNode.type, tmpNode.value, False)

				self.distances.update({newNode: [baseNode, None]}) # Adicionando o novo node nas distancias, pois ele é um novo node é não pode ser visitado 2x.

				self.countTasksDone(newNode) # Contando quantas tarefas foram feitas para o resolveWeights.
				self.resolveWeights(baseNode, newNode) # Calcula o peso do novo node.

				self.distances.update({newNode: [baseNode, newNode.value + baseNode.value]}) # atualiza a distancia do novo node.

				newDistances.append((newNode, baseNode, newNode.value))

			return newDistances


	def dijkstra(self):

		totalChoices = 500 # Total de caminhos aceitos.
		priorityQueue = []
		self.distances.update({self.startNode: [self.startNode, 0]})
		
		priorityQueue += self.createNextNodeLine(self.startNode) # Instance 0, "Acordar"
		priorityQueue.sort(key=itemgetter(2))
		
		priorityQueue = priorityQueue[0:totalChoices]

		while priorityQueue:
			
			current = priorityQueue.pop(0) if len(priorityQueue) > 0 else False
			# 
			# print(self.timePassed(current[0]))
			newNodes = self.createNextNodeLine(current[0])
			
			if not newNodes: # Quando se chega no ultimo node.

				if self.endNode not in self.distances: # Caso ele não esteja nas distancias.
					self.distances.update({self.endNode: [current[0], current[0].value]})
				elif self.distances.get(self.endNode)[1] > current[0].value: # Caso o novo valor seja menor que o ja cadastrado.
					self.distances.update({self.endNode: [current[0], current[0].value]})
			
			else:
				priorityQueue += newNodes
				priorityQueue.sort(key=itemgetter(2)) # Ordenação para os melhores caminhos.
				priorityQueue = priorityQueue[0:totalChoices] # Descarte dos piores caminhos.

	def createPath(self):
		"""
		Constroi o caminho para o resultado do dijkstra.
		"""
		tmpNode = self.endNode
		instance = self.needs.dayTotalTime + 1
		path=[(tmpNode.name, instance)]
		while self.distances[tmpNode][0].name != "Acordar":
			tmpNode = self.distances.get(tmpNode)[0]
			instance-=1
			path.append((tmpNode.name, instance))

		instance-=1

		path.append((self.distances.get(tmpNode)[0].name, instance))
		self.needs.resetCompleted()
		self.countTasksDone(self.endNode)

		postProcess = [[path[len(path) - 1][0], 0]]
		j = 0
		for i in path[len(path)::-1]:
			if i[0] == postProcess[j][0]:
				postProcess[j][1] += 1
			else:
				postProcess.append([i[0], 1])
				j+=1

		# Path - Caminho com as instancias.
		# Postprocess - Caminho com a quantidade feita de cada um.
		return path[::-1], postProcess, self.needs.completed, self.needs.total
