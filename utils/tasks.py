class requirements:
	def __init__(self, DayTotalTime=960, work=60, entertainment=30, other=10) -> None:

			self.work = (100 * work) / sum([work, entertainment, other])
			self.entertainment = (100 * entertainment) / sum([work, entertainment, other])
			self.other = (100 * other) / sum([work, entertainment, other])

			self.totalWork = DayTotalTime * (self.work / 100)
			self.totalEntertainment = DayTotalTime * (self.entertainment / 100)
			self.totalOther = DayTotalTime * (self.other / 100)

			self.completedWork = 0
			self.completedEntertainment = 0
			self.completedOther = 0
			
			self.dayTotalTime = DayTotalTime

	def getWorkDelta(self):
		return self.totalWork - self.completedWork

	def getEntertainmentDelta(self):
		return self.totalEntertainment - self.completedEntertainment

	def getOtherDelta(self):
		return self.totalOther - self.completedOther

	def getPriority(self):

		if self.getWorkDelta() > self.getEntertainmentDelta() and self.getWorkDelta() > self.getOtherDelta():
			return 1
		elif self.getEntertainmentDelta() > self.getWorkDelta() and self.getEntertainmentDelta() > self.getOtherDelta():
			return 2
		elif self.getOtherDelta() > self.getWorkDelta() and self.getOtherDelta() > self.getEntertainmentDelta():
			return 3
		elif self.getWorkDelta() == self.getEntertainmentDelta():
			return 1
		elif self.getEntertainmentDelta() == self.getOtherDelta():
			return 2
		else:
			return 3

class task:
	def __init__(self, name: str,  taskType: int, taskValue:float, create: bool) -> None:
			"""
			name: str
				O nome da tarefa.

			taskType: int
				O tipo da tarefa, 1 - Trabalho, 2 - Entreterimento, 3 - Outro(s).

			taskValue: int
				A quantidade que essa tarefa vale para o seu tipo tarefa.
			"""
			self.name = name
			# self.D = duration
			self.type = taskType
			if create:
				if taskValue < 10000:
					self.value = 100 - (taskValue / 100)
				else:
					self.value = 0.001
				if self.value < 0:
					self.value = 0

			else:
				self.value = taskValue
