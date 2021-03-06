class needs:
	def __init__(self, DayTotalTime=960, work=60, entertainment=30, other=10) -> None:

			self.work = (100 * work) / sum([work, entertainment, other])
			self.entertainment = (100 * entertainment) / sum([work, entertainment, other])
			self.other = (100 * other) / sum([work, entertainment, other])


			self.total = [DayTotalTime * (self.work / 100), DayTotalTime * (self.entertainment / 100), DayTotalTime * (self.other / 100)]

			self.completed = [0, 0, 0]
			
			self.dayTotalTime = DayTotalTime

	def getPriority(self):
		delta = [iTotal - iCompleted for iTotal, iCompleted in zip(self.total, self.completed)]
		return self.delta.index(max(delta))

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
