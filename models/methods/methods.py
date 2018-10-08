import sys
from enum import Enum
from pprint import pprint

class Methods(Enum):
	EULER = "euler"
	EULER_INVERSE = "euler_inverso"
	EULER_IMPROVED = "euler_aprimorado"
	RUNGE_KUTTA = "runge_kutta"
	ADAM_BASHFORTH = "adam_bashforth"
	ADAM_BASHFORTH_BY_EULER = "adam_bashforth_by_euler"
	ADAM_BASHFORTH_BY_EULER_INVERSE = "adam_bashforth_by_euler_inverso"
	ADAM_BASHFORTH_BY_EULER_IMPROVED = "adam_bashforth_by_euler_aprimorado"
	ADAM_BASHFORTH_BY_RUNGE_KUTTA = "adam_bashforth_by_runge_kutta"
	ADAM_MULTON = "adam_multon"
	ADAM_MULTON_BY_EULER = "adam_multon_by_euler"
	ADAM_MULTON_BY_EULER_INVERSE = "adam_multon_by_euler_inverso"
	ADAM_MULTON_BY_EULER_IMPROVED = "adam_multon_by_euler_aprimorado"
	ADAM_MULTON_BY_RUNGE_KUTTA = "adam_multon_by_runge_kutta"
	INVERSED_FORMULA = "formula_inversa"
	INVERSED_FORMULA_BY_EULER = "formula_inversa_by_euler"
	INVERSED_FORMULA_BY_EULER_INVERSE = "formula_inversa_by_euler_inverso"
	INVERSED_FORMULA_BY_EULER_IMPROVED = "formula_inversa_by_euler_aprimorado"
	INVERSED_FORMULA_BY_RUNGE_KUTTA = "formula_inversa_by_runge_kutta"

	@staticmethod
	def fromString(string):
		for method in reversed(Methods):
			if method.value in string:
				return method

		return None

	def isDefinedByOrder(self):
		if (self == Methods.EULER) or (self == Methods.EULER_INVERSE) or (self == Methods.EULER_IMPROVED):
			return False
		elif (self == Methods.RUNGE_KUTTA):
			return False

		return True