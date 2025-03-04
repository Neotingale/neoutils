from enum import Enum
from prettytable import PrettyTable
from sympy import simplify, init_printing
from sympy.parsing.latex import parse_latex


def parseLatex(expr : str):
	"""
	Convierte una cadena de texto con alguna ecuación en formato LaTeX a una expresión de Sympy para su uso posterior.
	:param expr: Expresión en formato LaTeX
	:return: Expresión en formato Sympy
	"""
	try: return parse_latex(expr)
	except Exception as e:
		print(f"Error: {e}")


class TableType(Enum):
	BISECTION = 0,
	FALSE_ERROR = 1,
	STATIC_POINT = 2,
	SEC = 3
	

def printTable(table_obj : PrettyTable, table_type : TableType):
	"""
	Imprime la tabla para los métodos numéricos
	:param table_obj: 
	:param table_type: 
	:return: 
	"""
	pass

def printLatex(expr : str, use_latex : bool = True):
	"""
	
	:param expr: 
	:param use_latex: 
	:return: 
	"""
	try:
		init_printing(use_latex=use_latex)
		expr = parse_latex(expr)
		result = simplify(expr)
		print(result)
	except Exception as e:
		print(f"Error: {e}")