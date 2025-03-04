from setuptools import setup, find_packages

setup(
	name='neoutils',
	version='1.0.0',
	description='Librería personal para la materia de Métodos Numéricos',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='Manuel Rodriguez',
	author_email='alu.23130570@correo.itlalaguna.edu.mx',
	url='https://github.com/Neotingale/neoutils',
	packages=find_packages(),
	install_requires=[
		'sympy>=1.12',
		'prettytable>=3.14.0',
		'antlr4-python3-runtime==4.11.0'
	],
	python_requires='>=3.8',
	license='CC BY 4.0',
	classifiers=[
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
	],
	include_package_data=True
)
