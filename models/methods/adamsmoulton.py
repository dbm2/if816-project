import sys
from sympy import sympify
from enums.methodstype import MethodsType
from models.method import Method
from models.methods.euler import Euler
from models.methods.rungekutta import RungeKutta
from models.methods.adamsbashforth import AdamsBashForth

class AdamsMoulton(Method):

	coefficients = [
		[1],
		[1/2, 1/2], 
		[5/12, 2/3, -1/12], 
		[3/8, 19/24, -5/24, 1/24], 
		[251/720, 323/360, -11/30, 53/360, -19/720],
		[98/288, 1427/1440, -133/240, 241/720, -173/1440, 3/160],
		[19087/60480, 2713/2520, -15487/20160, 586/945, -6737/20160, 263/2520, -863/60480],
		[5257/17280, 1389849/120960, -4511/4480, 123133/120960, -88547/120960, 1537/4480, -11351/120960, 257/24192]
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

		if self.type != MethodsType.ADAMS_MOULTON:
			predictionMethod = None
			if self.type == MethodsType.ADAMS_MOULTON_BY_EULER:
				predictionMethod = Euler(MethodsType.EULER, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_MOULTON_BY_EULER_INVERSE:
				predictionMethod = Euler(MethodsType.EULER_INVERSE, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_MOULTON_BY_EULER_IMPROVED:
				predictionMethod = Euler(MethodsType.EULER_IMPROVED, self.y, self.t, self.stepsSize, self.order - 1, self.function)
			elif self.type == MethodsType.ADAMS_MOULTON_BY_RUNGE_KUTTA:
				predictionMethod = RungeKutta(MethodsType.RUNGE_KUTTA, self.y, self.t, self.stepsSize, self.order - 1, self.function)
				
			predictionMethod.calculate()


		for i in range(len(self.t), self.steps + 1):
			previousTs = self.t[-self.order:]
			previousYs = self.y[-self.order:]

			predictionNextYMethod = AdamsBashForth(MethodsType.ADAMS_BASHFORTH, previousYs, previousTs, self.stepsSize, self.order, self.function, self.order)
			predictionNextYMethod.calculate()

			v = self.calculateByAdamsMoulton(previousYs, previousTs)

			previousYs = previousYs[:-1]
			previousTs = previousTs[:-1]

			self.t.append(v[0])
			self.y.append(v[1])


	def calculateByAdamsMoulton(self, previousYs, previousTs):

		previousFunctionsEvaluations = 0.0
		for i in range(0, self.order):
			y = previousYs[self.order - i]
			t = previousTs[self.order - i]
			f = self.evaluateFunction(y, t)
			previousFunctionsEvaluations += (AdamsMoulton.coefficients[self.order - 1][i] * f)

		nextT = previousTs[-2] + self.stepsSize
		nextY = previousYs[-2] + self.stepsSize * previousFunctionsEvaluations

		return (nextT, nextY)