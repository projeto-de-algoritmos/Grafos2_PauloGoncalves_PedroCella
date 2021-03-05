import tasks as TSK


class optimizer:
	def __init__(self, requirements: TSK.requirements, taskList: list) -> None:
		
			self.requirements = requirements

			self.taskList = taskList

			self.instanceList = []
			self.instanceList.append(taskList)
		
			self.path = [("Acordar", 0)]

	# def getMinWeight(self):
	# 	minValue = self.taskList[0].value
	# 	minIndex = 0


	# 	for index, currTask in enumerate(self.taskList):
	# 		if currTask.value < minValue:
	# 			minValue = currTask.value
	# 			minIndex = index

	# 	return [minValue, minIndex]



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
				self.taskList[index].value -= currTask.value * (0.05 / 100)
			

	def dijkstra(self, depht: int):
		instances = 0
		
		for instance in range(0, depht):
			pass

		# if len(self.instanceList) > 3:
		
		




taskList = []


taskList.append(TSK.task("Tomar Banho", 1, 5))
taskList.append(TSK.task("Tomar Banho", 2, 5))
taskList.append(TSK.task("Tomar Banho", 3, 9999))
taskList.append(TSK.task("Tomar Banho", 2, 90))
taskList.append(TSK.task("Tomar Banho", 1, 5))


t = optimizer(TSK.requirements, taskList)

t.dijkstra(950)