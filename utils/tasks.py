class task:
	def __init__(self, name: str, duration: int, taskType: int, taskValue: int, mandatory: bool) -> None:
			self.N = name
			self.D = duration
			self.T = taskType
			self.M = mandatory
			self.TV = taskValue