# ternaryplot
Ternary phase diagram generator using ternary library
	Jorge Luis Galvez Vallejo

Requirements: 
	Python3
	Ternary library found at:
	https://github.com/marcharper/python-ternary
	Matplotlib
	Argparse

Usage: python3 function.py 

For help: python3 function.py -h

To insert more points:
	Open composition.dat in a text editor (NOT WORD)
	Add a new line with the desired compositions
	Either:
		Edit the maketernary.py script to set default to new number
		of lines
	Or: 
		Use: python3 function.py --compo x
Where x is the new number of compositions
