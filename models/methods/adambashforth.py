import sys
from models.enums.methodstype import MethodsType
from models.methods.method import Method

class AdamBashForth(Method):

	def __init__(self, type, y, t, stepsSize, steps, function, order):
		self.type = type
		self.y = y
		self.t = t
		self.stepsSize = stepsSize
		self.steps = steps
		self.function = function
		self.order = order