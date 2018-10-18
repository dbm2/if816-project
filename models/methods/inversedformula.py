import sys
from sympy import sympify
from enums.methodstype import MethodsType
from models.method import Method
from models.methods.euler import Euler
from models.methods.rungekutta import RungeKutta
from models.methods.adamsbashforth import AdamsBashForth

class InversedFormula(Method):

	coefficients = [
		[1, 1],
		[2/3, 4/3, -1/3],
		[6/11, 18/11, -9/11, 2/11],
		[12/25, 48/25, -36/25, 16/25, -3/25],
		[60/137, 300/137, -300/137, 200/137, -75/137, 12/37],
		[60/147, 360/147, -450/147, 400/147, -225/147, 72/147, -10/147]
	]

	def __init__(self, type, y, t, stepsSize, steps, function, order):
		self.type = type
		self.y = y
		self.t = t
		self.stepsSize = stepsSize
		self.steps = steps
		self.function = sympify(function)
		self.order = order

		while len(self.t) < len(self.y):
			self.t.append(self.t[-1] + self.stepsSize)

	def calculate(self):		
		if self.type != MethodsType.INVERSED_FORMULA:
			predictionMethod = None
			if self.type == MethodsType.INVERSED_FORMULA_BY_EULER:
				predictionMethod = Euler(MethodsType.EULER, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.INVERSED_FORMULA_BY_EULER_INVERSE:
				predictionMethod = Euler(MethodsType.EULER_INVERSE, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.INVERSED_FORMULA_BY_EULER_IMPROVED:
				predictionMethod = Euler(MethodsType.EULER_IMPROVED, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.INVERSED_FORMULA_BY_RUNGE_KUTTA:
				predictionMethod = RungeKutta(MethodsType.RUNGE_KUTTA, self.y, self.t, self.stepsSize, self.order - 1, self.function)
				
			predictionMethod.calculate()


		for i in range(len(self.t), self.steps + 1):
			previousTs = self.t[-self.order:]
			previousYs = self.y[-self.order:]

			predictionNextYMethod = AdamsBashForth(MethodsType.ADAMS_BASHFORTH, previousYs, previousTs, self.stepsSize, self.order, self.function, self.order)
			predictionNextYMethod.calculate()

			v = self.calculateByInversedFormula(previousYs, previousTs)

			previousYs = previousYs[:-1]
			previousTs = previousTs[:-1]

			self.t.append(v[0])
			self.y.append(v[1])


	def calculateByInversedFormula(self, previousYs, previousTs):

		nextY = 0.0
		for i in range(0, self.order + 1):
			y = previousYs[self.order - i]

			if i == 0:
				t = previousTs[self.order - i]
				f = self.evaluateFunction(y, t)
				nextY += InversedFormula.coefficients[self.order - 1][i] * self.stepsSize * f
			else:
				nextY += InversedFormula.coefficients[self.order - 1][i] * y

		nextT = previousTs[-2] + self.stepsSize
	
		return (nextT, nextY)