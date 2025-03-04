from setuptools import setup, find_packages

setup(
	name = 'neoutils',
	version = '1.0.0',
	description = 'Librería personal para la materia de Métodos Numéricos',
	author = 'Manuel Rodriguez',
	url = 'https://github.com/Neotingale/neoutils',
	packages = find_packages(),
	install_requires = [
		'setuptools>=75.8.0',
		'sympy>=1.12',
		'prettytable>=3.14.0',
		'antlr4-python3-runtime>=4.11.0'
	],
	python_requires = '>=3.8'
)
