import tasks as TSK
from operator import itemgetter

class optimizer:
	def __init__(self, needs: TSK.needs, taskList: list) -> None:

			self.startNode = TSK.task("Acordar", 4, 10000, True)
			self.endNode = TSK.task("Dormir", 4, 10000, True)

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
		

		if baseNode.name == "Comer" and newNode.name == "Comer":
			newNode.value = baseNode.value + 100
			print("Rolo")

		elif newNode.name == "Comer" and self.timePassed(baseNode) in [x for x in range(3, self.needs.dayTotalTime, 3)]:
			print("Olas")
			newNode.value -= newNode.value * (1.5 / 100)
		print(self.needs.getPriority())
		if newNode.type is self.needs.getPriority():
			
			newNode.value -= newNode.value * (0.5 / 100)
			self.needs.resetCompleted()
				

	def countTasksDone(self, node):
		
		tmpNode = node
		valueToSum = 1
		while self.distances[tmpNode][0].name != "Acordar":
			self.needs.addToCompleted(self.distances[tmpNode][0].type, valueToSum)
			tmpNode = self.distances.get(tmpNode)[0]
			# print(tmpNode)


	def createNextNodeLine(self, baseNode):
			newDistances = []

			if self.timePassed(baseNode) >= self.needs.dayTotalTime or not baseNode:
				return False			
			
			for tmpNode in self.taskList:

				newNode = TSK.task(tmpNode.name, tmpNode.type, tmpNode.value, False)

				self.distances.update({newNode: [baseNode, None]})

				self.countTasksDone(newNode)
				self.resolveWeights(baseNode, newNode)

				self.distances.update({newNode: [baseNode, newNode.value + baseNode.value]})

				newDistances.append((newNode, baseNode, newNode.value))
				return newDistances


	def dijkstra(self):

		totalChoices = 100
		priorityQueue = []

		
		self.distances.update({self.startNode: [self.startNode, 0]})
		
		priorityQueue += self.createNextNodeLine(self.startNode) # Instance 0, "Acordar"
		priorityQueue.sort(key=itemgetter(2))
		
		priorityQueue = priorityQueue[0:totalChoices]
		
		while priorityQueue:
			
			current = priorityQueue.pop(0) if len(priorityQueue) > 0 else False
			# print(self.timePassed(current[0]))
			newNodes = self.createNextNodeLine(current[0])
			# print(priorityQueue)
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
		return path
taskList = []


taskList.append(TSK.task("a", 1, 5, True))
taskList.append(TSK.task("b", 1, 5, True))
taskList.append(TSK.task("c", 2, 9, True))
taskList.append(TSK.task("d", 1, 90, True))
taskList.append(TSK.task("Comer", 2, 0, True))

t = optimizer(TSK.needs(960), taskList)


t.dijkstra()
# print(t.createPath()[::-1])