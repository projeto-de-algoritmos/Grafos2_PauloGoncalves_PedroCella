import tasks as TSK
from operator import itemgetter
import math
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
			newNode.value = baseNode.value + 10000
		# (e-1)x-e+2\ 
		elif newNode.name == "Comer" :
			if newNode.value * (((math.e-1)*self.timePassed(newNode))  - math.e + 2) > 9999:
				newNode.value = 0
			else:
				newNode.subValue(((math.e-1)*self.timePassed(newNode))  - math.e + 2)

		if self.needs.completed[newNode.type] >= self.needs.total[newNode.type]:
			newNode.value = math.inf
			self.needs.resetCompleted()

		elif newNode.type is self.needs.getPriority():
			newNode.subValue(newNode.value * ((self.timePassed(newNode)**math.e) - self.timePassed(newNode) + 1))
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
			# print(newNodes)
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
taskList = []


taskList.append(TSK.task("T", 0, 90, True))
taskList.append(TSK.task("E", 1, 5, True))
taskList.append(TSK.task("O", 2,11, True))
taskList.append(TSK.task("E2", 1, 5, True))
taskList.append(TSK.task("Comer", 2, 25, True))

t = optimizer(TSK.needs(10), taskList)


t.dijkstra()
# print(t.distances)


totalOfEachTaks = {}
path, postProcessPath, completedTasks, totalTasks = t.createPath()[::]
for i in postProcessPath:
	if i[0] not in totalOfEachTaks:
		totalOfEachTaks.update({i[0]: i[1]})
	else:
		num = i[1]
		num += totalOfEachTaks.get(i[0])
		totalOfEachTaks.update({i[0]: num})

print(postProcessPath)
print(totalTasks)
print(completedTasks)
print(totalOfEachTaks)
print(len(t.distances))