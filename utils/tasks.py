
class needs:
	def __init__(self, DayTotalTime=150, work=60, entertainment=30, other=10) -> None:

			# Transforma os pesos de cada coisa em uma porcentagem do dia.
			self.work = (100 * work) / sum([work, entertainment, other])
			self.entertainment = (100 * entertainment) / sum([work, entertainment, other])
			self.other = (100 * other) / sum([work, entertainment, other])

			# O total que se precisa ser feito durante o dia.
			self.total = [DayTotalTime * (self.work / 100), DayTotalTime * (self.entertainment / 100), DayTotalTime * (self.other / 100), 2]

			# Quanto se foi feito durante o dia.
			self.completed = [0] * len(self.total)
			
			self.dayTotalTime = DayTotalTime

	def getPriority(self):
		"""
		Retorna o indice da tarefa que foi menos feita.
		"""
		delta = [iTotal - iCompleted for iTotal, iCompleted in zip(self.total, self.completed)]
		return delta.index(max(delta))

	def resetCompleted(self):
		self.completed = [0] * len(self.total)
		
	def addToCompleted(self, index, value):
		if self.completed[index] + value > self.total[index]:
			self.completed[index] = self.total[index]
		else:
			self.completed[index] += value


class task:
	def __init__(self, name: str,  taskType: int, taskValue:float, create: bool) -> None:
			"""
			name: str
				O nome da tarefa.

			taskType: int
				O tipo da tarefa, 0 - Trabalho, 1 - Entreterimento, 2 - Outro(s), 3 - Nodes especiais.

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


	def subValue(self, value):
		if self.value - value < 0:
			self.value = 0
		if self.value - value >= 10000:
			self.value = 10000
