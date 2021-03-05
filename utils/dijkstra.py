import tasks as TSK
import math




class optimizer:
	def __init__(self, requirements: TSK.requirements, taskList: list) -> None:
		
			self.requirements = requirements


			self.buildGraph(taskList)

	
			# self.path = [("Acordar", 0), (ondeVeio, currentNode, Distance)]
			self.path = [("Acordar", 0)]
			self.priorityQueue = []

			self.distances = {0: 0}
			self.distancePrev = {}
	# def getMinWeight(self):
	# 	minValue = self.taskList[0].value
	# 	minIndex = 0


	# 	for index, currTask in enumerate(self.taskList):
	# 		if currTask.value < minValue:
	# 			minValue = currTask.value
	# 			minIndex = index

	# 	return [minValue, minIndex]

	def addWithPriority(self, node, distance, instance):
		self.priorityQueue.append((node, distance, instance))

	def decreasePriority(self, node, distance, instance):
		pass

	def extractMin(self):
		pass

	def resolveWeights(self):
		
		deltaWork = self.requirements.getWorkDelta()
		deltaEntertainment = self.requirements.getEntertainmentDelta()
		deltaOther = self.requirements.getOtherDelta()

		if deltaWork > deltaEntertainment and deltaWork > deltaOther:
			priority = 1
		elif deltaEntertainment > deltaWork and deltaEntertainment > deltaOther:
			priority = 2
		elif deltaOther > deltaWork and deltaOther > deltaEntertainment:
			priority = 3
		elif deltaWork == deltaEntertainment:
			priority = 1
		elif deltaEntertainment == deltaOther:
			priority = 2
		else:
			priority = 3

		for index, currTask in enumerate(self.taskList):
			if currTask.type is priority:
				self.taskList[index].value -= currTask.value * (1 / 100)
	
	def buildGraph(self, taskList):

		self.graph = {}

		start = TSK.task("Acordar", 4, 10000)
		end = TSK.task("Dormir", 4, 10000)

		self.graph.update({0: [start]})

		for i in range(1, self.requirements.dayTotalTime + 1):

			self.graph.update({i: []})

			for index, node in enumerate(taskList):

				self.graph[i].append(TSK.task(taskList[index].name, taskList[index].type, taskList[index].value))
				
		self.graph.update({self.requirements.dayTotalTime + 1: [end]})

		print(self.graph)
	def dijkstra(self, depht: int):
		instances = 0
		
		for instance in range(1, depht + 1):
			inicialDist = [math.inf] * len(self.taskList)
			inicialPrev = [(None, None)] * len(self.taskList) 
			self.distances.update({instance: inicialDist})
			self.distancePrev.update({instance: inicialPrev})

			for index, node in enumerate(self.taskList):
				self.addWithPriority(node, self.distances[instance][index], instance)

		print(self.priorityQueue)
		for instance in range(1, depht + 1):
			pass

		# if len(self.instanceList) > 3:
		
		




taskList = []


taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 2, 5))
taskList.append(TSK.task("Tomar Banho", 3, 9999))
taskList.append(TSK.task("Tomar Banho", 2, 90))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 2, 5))
taskList.append(TSK.task("Tomar Banho", 3, 9999))
taskList.append(TSK.task("Tomar Banho", 2, 90))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 2, 5))
taskList.append(TSK.task("Tomar Banho", 3, 9999))
taskList.append(TSK.task("Tomar Banho", 2, 90))
taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 1, 5))

t = optimizer(TSK.requirements(), taskList)