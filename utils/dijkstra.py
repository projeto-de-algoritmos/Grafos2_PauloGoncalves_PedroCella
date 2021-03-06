import tasks as TSK
import math

class optimizer:
	def __init__(self, needs: TSK.needs, taskList: list) -> None:
		
			self.needs = needs

			self.taskList = taskList

			self.graph = {}



	def resolveWeights(self, baseNode, newBaseNode=None):
		
		if newBaseNode:
			if newBaseNode.type < 3:
				self.needs.completed[newBaseNode.type] += 5



	def createNextNodeLine(self, currInstance: int):
		
			if currInstance == 0:
				self.graph.update({0: [TSK.task("Acordar", 4, 10000, True)]})

			elif currInstance == self.needs.dayTotalTime + 1:
				self.graph.update({currInstance: [TSK.task("Dormir", 4, 10000, True)]})

			else:
				self.graph.update({currInstance: []})

				for node in self.graph.get(currInstance - 1):
					if currInstance > 1:
						self.graph[currInstance].append(TSK.task(node.name, node.type, node.value, False))
					else:
						self.graph.update({currInstance: self.taskList})
			

			for index, currTask in enumerate(self.graph.get(currInstance)):
				if currTask.type is self.needs.getPriority():
					self.graph.get(currInstance)[index].value -= currTask.value * (1 / 100)
					

				if currTask.name == "Comer" and currInstance in [x for x in range(3, self.needs.dayTotalTime, 3)]:
					self.graph.get(currInstance)[index].value -= currTask.value * (1.5/100)


	def dijkstra(self):

		instance = 0
		self.createNextNodeLine(instance)
		distances = {self.graph.get(instance)[0]: [None, 0, self.graph.get(instance)[0]]}
		
		priorityQueue = {}
		self.createNextNodeLine(instance + 1)
		



		for baseNode in self.graph.get(instance):
				for adj in self.graph.get(instance + 1):
					priorityQueue.update({})

		while priorityQueue:
			self.createNextNodeLine(instance + 1)

			for baseNode in self.graph.get(instance):
				for adj in self.graph.get(instance + 1):

					# Adding in the distances array
					if adj not in distances:
						distances.update({adj: [baseNode, baseNode.value + adj.value]})

					elif baseNode.value + adj.value < distances.get(adj)[1]:
						distances.update({adj: [baseNode, baseNode.value + adj.value]})


			instance += 1
		for index, i in enumerate(distances):
			if distances.get(i)[0] != None:
				print(f"{i.name}: {distances.get(i)[0].name}, {distances.get(i)[1]}")
			else:
				print(f"{i.name}: {distances.get(i)[2].name}, {distances.get(i)[1]}")
			
			if index in [x for x in range(0, len(distances), len(self.taskList))]:
				print("\n")

		# for instance in range(1, depht + 1):
		# 	inicialDist = [math.inf] * len(self.taskList)
		# 	inicialPrev = [(None, None)] * len(self.taskList) 
		# 	self.distances.update({instance: inicialDist})
		# 	self.distancePrev.update({instance: inicialPrev})

		# 	for index, node in enumerate(self.taskList):
		# 		self.addWithPriority(node, self.distances[instance][index], instance)

		# print(self.priorityQueue)


		# if len(self.instanceList) > 3:
		
		




taskList = []


taskList.append(TSK.task("a", 1, 5, True))
taskList.append(TSK.task("b", 2, 5, True))
taskList.append(TSK.task("c", 3, 9, True))
taskList.append(TSK.task("d", 2, 90, True))
taskList.append(TSK.task("Comer", 3, 0, True))

t = optimizer(TSK.needs(5), taskList)


t.dijkstra()