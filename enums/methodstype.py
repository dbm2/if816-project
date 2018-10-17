import sys
from enum import Enum
from pprint import pprint

class MethodsType(Enum):
	EULER = "euler"
	EULER_INVERSE = "euler_inverso"
	EULER_IMPROVED = "euler_aprimorado"
	RUNGE_KUTTA = "runge_kutta"
	ADAMS_BASHFORTH = "adam_bashforth"
	ADAMS_BASHFORTH_BY_EULER = "adam_bashforth_by_euler"
	ADAMS_BASHFORTH_BY_EULER_INVERSE = "adam_bashforth_by_euler_inverso"
	ADAMS_BASHFORTH_BY_EULER_IMPROVED = "adam_bashforth_by_euler_aprimorado"
	ADAMS_BASHFORTH_BY_RUNGE_KUTTA = "adam_bashforth_by_runge_kutta"
	ADAMS_MOULTON = "adam_multon"
	ADAMS_MOULTON_BY_EULER = "adam_multon_by_euler"
	ADAMS_MOULTON_BY_EULER_INVERSE = "adam_multon_by_euler_inverso"
	ADAMS_MOULTON_BY_EULER_IMPROVED = "adam_multon_by_euler_aprimorado"
	ADAMS_MOULTON_BY_RUNGE_KUTTA = "adam_multon_by_runge_kutta"
	INVERSED_FORMULA = "formula_inversa"
	INVERSED_FORMULA_BY_EULER = "formula_inversa_by_euler"
	INVERSED_FORMULA_BY_EULER_INVERSE = "formula_inversa_by_euler_inverso"
	INVERSED_FORMULA_BY_EULER_IMPROVED = "formula_inversa_by_euler_aprimorado"
	INVERSED_FORMULA_BY_RUNGE_KUTTA = "formula_inversa_by_runge_kutta"

	@staticmethod
	def fromString(string):
		for method in reversed(MethodsType):
			if method.value in string:
				return method

		return None

	def isDefinedByOrder(self):
		if (self == MethodsType.EULER) or (self == MethodsType.EULER_INVERSE) or (self == MethodsType.EULER_IMPROVED):
			return False
		elif (self == MethodsType.RUNGE_KUTTA):
			return False

		return True

	def isEuler(self):
		return (self == MethodsType.EULER) or (self == MethodsType.EULER_INVERSE) or (self == MethodsType.EULER_IMPROVED)

	def isRungeKutta(self):
		return (self == MethodsType.RUNGE_KUTTA)

	def isAdamsBashForth(self):
		return (self == MethodsType.ADAMS_BASHFORTH) or (self == MethodsType.ADAMS_BASHFORTH_BY_EULER) or (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_INVERSE) or (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_IMPROVED) or (self == MethodsType.ADAMS_BASHFORTH_BY_RUNGE_KUTTA)

	def isAdamsMoulton(self):
		return (self == MethodsType.ADAMS_MOULTON) or (self == MethodsType.ADAMS_MOULTON_BY_EULER) or (self == MethodsType.ADAMS_MOULTON_BY_EULER_INVERSE) or (self == MethodsType.ADAMS_MOULTON_BY_EULER_IMPROVED) or (self == MethodsType.ADAMS_MOULTON_BY_RUNGE_KUTTA)

	def isInversedFormula(self):
		return (self == MethodsType.INVERSED_FORMULA) or (self == MethodsType.INVERSED_FORMULA_BY_EULER) or (self == MethodsType.INVERSED_FORMULA_BY_EULER_INVERSE) or (self == MethodsType.INVERSED_FORMULA_BY_EULER_IMPROVED) or (self == MethodsType.INVERSED_FORMULA_BY_RUNGE_KUTTA)

	def getName(self):
		if (self == MethodsType.EULER):
			return "Metodo de Euler"
		elif (self == MethodsType.EULER_INVERSE):
			return "Metodo de Euler Inverso"
		elif (self == MethodsType.EULER_IMPROVED):
			return "Metodo de Euler Aprimorado"
		elif (self == MethodsType.RUNGE_KUTTA):
			return "Metodo de Runge-Kutta"
		elif (self == MethodsType.ADAMS_BASHFORTH):
			return "Metodo de Adams-Bashforth"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER):
			return "Metodo de Adams-Bashforth por Euler"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_INVERSE):
			return "Metodo de Adams-Bashforth por Euler Inverso"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_IMPROVED):
			return "Metodo de Adams-Bashforth por Euler Aprimorado"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_RUNGE_KUTTA):
			return "Metodo de Adams-Bashforth por Runge-Kutta"
		elif (self == MethodsType.ADAMS_MOULTON):
			return "Metodo de Adams-Moulton"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER):
			return "Metodo de Adams-Moulton por Euler"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER_INVERSE):
			return "Metodo de Adams-Moulton por Euler Inverso"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER_IMPROVED):
			return "Metodo de Adams-Moulton por Euler Aprimorado"
		elif (self == MethodsType.ADAMS_MOULTON_BY_RUNGE_KUTTA):
			return "Metodo de Adams-Moulton por Runge-Kutta"
		elif (self == MethodsType.INVERSED_FORMULA):
			return "Metodo Formula Inversa de Diferenciacao"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER):
			return "Metodo Formula Inversa de Diferenciacao por Euler"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER_INVERSE):
			return "Metodo Formula Inversa de Diferenciacao por Euler Inverso"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER_IMPROVED):
			return "Metodo Formula Inversa de Diferenciacao por Euler Aprimorado"
		elif (self == MethodsType.INVERSED_FORMULA_BY_RUNGE_KUTTA):
			return "Metodo Formula Inversa de Diferenciacao por Runge-Kutta"

	def getColor(self):
		if (self == MethodsType.EULER):
			return "#cce6ff"
		elif (self == MethodsType.EULER_INVERSE):
			return "#66b3ff"
		elif (self == MethodsType.EULER_IMPROVED):
			return "#0080ff"
		elif (self == MethodsType.RUNGE_KUTTA):
			return "#66cc66"
		elif (self == MethodsType.ADAMS_BASHFORTH):
			return "#ffccee"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER):
			return "#ff66cc"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_INVERSE):
			return "#ff00aa"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_EULER_IMPROVED):
			return "#b30077"
		elif (self == MethodsType.ADAMS_BASHFORTH_BY_RUNGE_KUTTA):
			return "#800055"
		elif (self == MethodsType.ADAMS_MOULTON):
			return "#ffe6cc"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER):
			return "#ffbf80"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER_INVERSE):
			return "#ff9933"
		elif (self == MethodsType.ADAMS_MOULTON_BY_EULER_IMPROVED):
			return "#e67300"
		elif (self == MethodsType.ADAMS_MOULTON_BY_RUNGE_KUTTA):
			return "#994d00"
		elif (self == MethodsType.INVERSED_FORMULA):
			return "#ffffcc"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER):
			return "#ffff80"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER_INVERSE):
			return "#ffff00"
		elif (self == MethodsType.INVERSED_FORMULA_BY_EULER_IMPROVED):
			return "#cccc00"
		elif (self == MethodsType.INVERSED_FORMULA_BY_RUNGE_KUTTA):
			return "#808000"