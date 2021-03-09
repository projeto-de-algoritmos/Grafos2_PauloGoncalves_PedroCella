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
		Função que 
		"""

		if baseNode.name == "Comer" and newNode.name == "Comer":
			newNode.value = baseNode.value + 10000
		# (e-1)x-e+2\ 
		elif newNode.name == "Comer" :
			if self.needs.completed[newNode.type] >= self.needs.total[newNode.type]:
				newNode.value = math.inf
				self.needs.resetCompleted()
			elif newNode.value * (((math.e-1)*self.sameTaksB4(newNode))  - math.e + 2) > 9999:
				newNode.value = 0
			else:
				newNode.subValue(((math.e-1)*self.sameTaksB4(newNode))  - math.e + 2)
		else:
			if self.needs.completed[newNode.type] >= self.needs.total[newNode.type]:
				newNode.value = math.inf
				self.needs.resetCompleted()

			elif newNode.type is self.needs.getPriority():
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
		
		tmpNode = node
		valueToSum = 1
		while self.distances[tmpNode][0].name != "Acordar":
			self.needs.addToCompleted(self.distances[tmpNode][0].type, valueToSum)
			tmpNode = self.distances.get(tmpNode)[0]
			# print(tmpNode)


	def createNextNodeLine(self, baseNode):
			newDistances = []

			if self.timePassed(baseNode) >= self.needs.dayTotalTime +2 or not baseNode:
				return False			
			
			for tmpNode in self.taskList:

				newNode = TKS(tmpNode.name, tmpNode.type, tmpNode.value, False)

				self.distances.update({newNode: [baseNode, None]})

				self.countTasksDone(newNode)
				self.resolveWeights(baseNode, newNode)

				self.distances.update({newNode: [baseNode, newNode.value + baseNode.value]})

				newDistances.append((newNode, baseNode, newNode.value))

			return newDistances


	def dijkstra(self):

		totalChoices = 500
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
			
			if not newNodes:

				if self.endNode not in self.distances:
					self.distances.update({self.endNode: [current[0], current[0].value]})
				elif self.distances.get(self.endNode)[1] > current[0].value:
					self.distances.update({self.endNode: [current[0], current[0].value]})
			
			else:
				priorityQueue += newNodes
				priorityQueue.sort(key=itemgetter(2))
				priorityQueue = priorityQueue[0:totalChoices]

	def createPath(self):
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
	
		return path[::-1], postProcess, self.needs.completed, self.needs.total
