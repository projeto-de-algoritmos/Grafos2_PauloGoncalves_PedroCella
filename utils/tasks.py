class requirements:
	def __init__(self, DayTotalTime=960, work=5, entertainment=960, other=960) -> None:

			self.work = (100 * work) / sum([work, entertainment, other])
			self.entertainment = (100 * entertainment) / sum([work, entertainment, other])
			self.other = (100 * other) / sum([work, entertainment, other])

			self.totalWork = DayTotalTime * (self.work / 100)
			self.totalEntertainment = DayTotalTime * (self.entertainment / 100)
			self.totalOther = DayTotalTime * (self.other / 100)

			self.completedWork = 0
			self.completedEntertainment = 0
			self.completedOther = 0
	
	def getWorkDelta(self):
		return self.totalWork - self.completedWork

	def getEntertainmentDelta(self):
		return self.totalEntertainment - self.completedEntertainment

	def getOtherDelta(self):
		return self.totalOther - self.completedOther

class task:
	def __init__(self, name: str,  taskType: int, taskValue:float) -> None:
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
			if taskValue < 10000:
				self.value = 100 - (taskValue / 100)
			else:
				self.value = 0.001
