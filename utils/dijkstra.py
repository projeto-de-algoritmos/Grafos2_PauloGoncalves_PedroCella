import tasks as TSK
import math

class optimizer:
	def __init__(self, requirements: TSK.requirements, taskList: list) -> None:
		
			self.requirements = requirements

			self.taskList = taskList

			self.graph = {}

			self.path = [("Acordar", 0)]
			self.priorityQueue = []

			self.distances = {0: 0}
			self.distancePrev = {}

	def addWithPriority(self, node, distance, instance):
		self.priorityQueue.append((node, distance, instance))

	def decreasePriority(self, node, distance, instance):
		pass

	def extractMin(self):
		pass


	def createNextNodeLine(self, currInstance: int):
		
			if currInstance == 0:
				self.graph.update({0: [TSK.task("Acordar", 4, 10000, True)]})

			else:
				self.graph.update({currInstance: []})

				for node in self.graph.get(currInstance - 1):
					if currInstance > 1:
						self.graph[currInstance].append(TSK.task(node.name, node.type, node.value, False))
					else:
						self.graph.update({currInstance: self.taskList})
			

	def resolveWeights(self, currInstance: int):
		

		for index, currTask in enumerate(self.graph.get(currInstance)):
			if currTask.type is self.requirements.getPriority():
				self.graph.get(currInstance)[index].value -= currTask.value * (1 / 100)
	

	def dijkstra(self, depht: int):
		
		
		for instance in range(0, depht + 1):
			self.createNextNodeLine(instance)

		for instance in range(0, depht + 1):
			for node in self.graph.get(instance):
				print(f"{node.name}, {node.type}, {node.value}: {instance}")
			print("\n")
		# print("")
		# print(self.graph)

		for instance in range(1, depht + 1):
			inicialDist = [math.inf] * len(self.taskList)
			inicialPrev = [(None, None)] * len(self.taskList) 
			self.distances.update({instance: inicialDist})
			self.distancePrev.update({instance: inicialPrev})

			for index, node in enumerate(self.taskList):
				self.addWithPriority(node, self.distances[instance][index], instance)

		# print(self.priorityQueue)
		for instance in range(1, depht + 1):
			pass

		# if len(self.instanceList) > 3:
		
		




taskList = []


taskList.append(TSK.task("a", 1, 5, True))
taskList.append(TSK.task("b", 2, 5, True))
taskList.append(TSK.task("c", 3, 5, True))
taskList.append(TSK.task("d", 2, 90, True))


t = optimizer(TSK.requirements(), taskList)


t.dijkstra(150)