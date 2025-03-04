import sympy as sp
from utils import parseLatex


def maclaurinSeries(expr_str : str, n : int):
	"""
	Genera una serie de maclaurin a partir de una expresión
	:param expr_str: El valor principal de la serie 
	:param n: El tamaño de la serie
	:return: El valor final de la serie
	"""
	try:
		expr = parseLatex(expr_str)
		x = sp.symbols('x')
		expr = sp.sympify(expr)
		return sp.series(expr, x, n)
	except Exception as e:
		print(f"Error: {e}")
	
