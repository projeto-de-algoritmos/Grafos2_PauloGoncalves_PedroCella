class requirements:
	def __init__(self, work, entertainment) -> None:
			pass


class task:
	def __init__(self, name: str,  taskType: int, taskValue: int) -> None:
			"""
			name: str
				O nome da tarefa.

			taskType: int
				O tipo da tarefa, 1 - produtividade, 2 - relaxamento.

			taskValue: int
				A quantidade que essa tarefa vale para o seu tipo tarefa.
			"""
			self.name = name
			# self.D = duration
			self.taskType = taskType
			self.taskValue = taskValue