from enum import Enum
from prettytable import PrettyTable
from sympy.parsing.latex import parse_latex


def parseString(expr : str):
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
	STATIC_POINT = 2
	

def printTable(table_obj : PrettyTable, table_type : TableType):
	"""
	
	:param table_obj: 
	:param table_type: 
	:return: 
	"""
	pass