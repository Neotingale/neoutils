from sympy import Symbol, diff
from prettytable import PrettyTable
from .utils import parseLatex


def bisectionMethod (f_x_str : str, lower : float, upper : float, tolerance : float = 1e-6, iterations : int = 50, table : PrettyTable = None) :
	"""
	Metodo numerico de biseccion.

	:param f_x_str: La funcion a resolver en formato LaTeX
	:param lower: Limite inferior del intervalo
	:param upper: Limite superior del intervalo
	:param tolerance: Tolerancia minima a error (Default: 1e-6)
	:param iterations: Numero maximo de iteraciones (Default: 50)
	:param table: Tabla donde se guardaran los datos (Default: None)
	:return: Aproximacion de la raiz
	"""
	try :
		x = Symbol('x')
		f_x = parseLatex(f_x_str)
		
		if table : table.field_names = [ "Iteracion", "Lower", "Upper", "Mid", "f(Mid)", "Error" ]
		
		for i in range(iterations) :
			mid = (lower + upper) / 2
			f_mid = f_x.subs(x, mid)
			error = abs(f_mid)
			
			if table : table.add_row([ i + 1, lower, upper, mid, f_mid, error ])
			
			if error < tolerance : return mid
			
			if f_x.subs(x, lower) * f_mid < 0 : upper = mid
			else : lower = mid
		
		raise ValueError(f"Se llego al limite de iteraciones ({iterations})")
	except Exception as e :
		print(f"Error: {e}")


def falseRuleMethod (f_x_str : str, lower : float, upper : float, tolerance : float = 1e-6, iterations : int = 50, table : PrettyTable = None) :
	"""
	Metodo de la regla falsa.

	:param f_x_str: La funcion a resolver en formato LaTeX
	:param lower: Limite inferior del intervalo
	:param upper: Limite superior del intervalo
	:param tolerance: Tolerancia minima a error (Default: 1e-6)
	:param iterations: Numero maximo de iteraciones (Default: 50)
	:param table: Tabla donde se guardaran los datos (Default: None)
	:return: Aproximacion de la raiz
	"""
	try :
		x = Symbol('x')
		f_x = parseLatex(f_x_str)
		
		if table : table.field_names = [ "Iteracion", "Lower", "Upper", "Root", "f(Root)", "Error" ]
		
		for i in range(iterations) :
			f_lower = f_x.subs(x, lower)
			f_upper = f_x.subs(x, upper)
			root = (lower * f_upper - upper * f_lower) / (f_upper - f_lower)
			f_root = f_x.subs(x, root)
			error = abs(f_root)
			
			if table : table.add_row([ i + 1, lower, upper, root, f_root, error ])
			
			if error < tolerance : return root
			
			if f_lower * f_root < 0 : upper = root
			else : lower = root
		
		raise ValueError(f"Se llego al limite de iteraciones ({iterations})")
	except Exception as e :
		print(f"Error: {e}")


def staticPointMethod (g_x_str : str, x_0 : float, tolerance : float = 1e-6, iterations : int = 50, table : PrettyTable = None) :
	"""
	Metodo numerico del punto fijo.

	:param g_x_str: La funcion g(x) en formato string
	:param x_0: El valor inicial de x
	:param tolerance: La tolerancia minima a error (Default: 1e-6)
	:param iterations: Numero maximo de iteraciones (Default: 50)
	:param table: La tabla donde se guardaran los datos (Default: None)
	:return: Aproximacion de la raiz
	"""
	try :
		x = Symbol('x')
		g_x = parseLatex(g_x_str)
		
		if table : table.field_names = [ "Iteracion", "x_0", "g(x)", "Error" ]
		
		for i in range(iterations) :
			x_1 = g_x.subs(x, x_0)
			error = abs(x_1 - x_0)
			
			if table : table.add_row([ i + 1, x_0, x_1, error ])
			
			if error < tolerance : return x_1
			x_0 = x_1
		
		raise ValueError(f"Se llego al limite de iteraciones ({iterations})")
	except Exception as e :
		print(f"Error: {e}")


def newtonRaphsonMethod (f_x_str : str, x_0 : float, tolerance : float = 1e-6, iterations : int = 50, table : PrettyTable = None) :
	"""
	Metodo de Newton-Raphson.

	:param f_x_str: La función a resolver en formato LaTeX
	:param x_0: Valor inicial de x
	:param tolerance: Tolerancia mínima a error (Default: 1e-6)
	:param iterations: Número máximo de iteraciones (Default: 50)
	:param table: Tabla donde se guardarán los datos (Default: None)
	:return: Aproximación de la raíz
	"""
	try :
		x = Symbol('x')
		f_x = parseLatex(f_x_str)
		f_prime = diff(f_x, x)
		
		if table : table.field_names = [ "Iteración", "x", "f(x)", "Error" ]
		
		for i in range(iterations) :
			f_val = f_x.subs(x, x_0)
			f_prime_val = f_prime.subs(x, x_0)
			
			if f_prime_val == 0 : raise ValueError("La derivada es cero, método no aplicable.")
			
			x_1 = x_0 - f_val / f_prime_val
			error = abs(x_1 - x_0)
			
			if table : table.add_row([ i + 1, x_0, f_val, error ])
			
			if error < tolerance : return x_1
			x_0 = x_1
		
		raise ValueError(f"Se llegó al límite de iteraciones ({iterations})")
	except Exception as e :
		print(f"Error: {e}")


def secMethod (f_x_str : str, x_irem1 : float, x_i : float, tolerance : float = 1e-6, iterations : int = 20, table : PrettyTable = None) :
	"""
	Metodo de la secante.

	:param f_x_str: La función a resolver en formato LaTeX
	:param x_irem1: Valor de x_{-1}
	:param x_i: Valor inicial de x_0
	:param tolerance: Tolerancia mínima a error (Default: 1e-6)
	:param iterations: Número máximo de iteraciones (Default: 20)
	:param table: Tabla donde se guardarán los datos (Default: None)
	:return: Aproximación de la raíz
	"""
	try :
		x = Symbol('x')
		f_x = parseLatex(f_x_str)
		
		if table : table.field_names = [ "Iteración", "x_{-1}", "x_0", "f(x_0)", "Error" ]
		
		for i in range(iterations) :
			f_x_irem1 = f_x.subs(x, x_irem1)
			f_x_i = f_x.subs(x, x_i)
			
			if f_x_irem1 == f_x_i : raise ValueError("División por cero detectada en el método de la secante.")
			
			x_iadd1 = x_i - ((x_irem1 - x_i) * f_x_i) / (f_x_irem1 - f_x_i)
			error = abs(x_iadd1 - x_i)
			
			if table : table.add_row([ i + 1, x_irem1, x_i, f_x_i, error ])
			
			if error < tolerance : return x_iadd1
			
			x_irem1 = x_i
			x_i = x_iadd1
		
		raise ValueError(f"Se llegó al límite de iteraciones ({iterations})")
	except Exception as e :
		print(f"Error: {e}")
