import ternary
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import argparse
import sys

def parse_arguments():
	parser = argparse.ArgumentParser(description='Ternary phase diagram generator')
	parser.add_argument('--compo',help='number of compositions, default: 1', default=1,type=int)
	parser.add_argument('--dpi',help='sets number of dpis, default: 300', default=300,type=int)
	if len(sys.argv)==1:
		parser.print_help(sys.stderr)
		print("No arguments given, using defaults...")
	#	sys.exit(1)
	return parser.parse_args()

def create_graphs(Ncomps,dpi):
	scale = 100
	figure, tax = ternary.figure(scale=scale)
	figure, pax = ternary.figure(scale=scale)

    # Draw Boundary and Gridlines
	tax.boundary(linewidth=0.25)
	tax.gridlines(color="blue", multiple=10)

	pax.boundary(linewidth=0.55)
	pax.gridlines(color="blue", multiple=10)
 
    # Set Axis labels and Title
	fontsize = 10
	tax.set_title("BaxCuyArz Composition diagram", fontsize=20)
	tax.left_axis_label("Ba", fontsize=fontsize)
	tax.right_axis_label("Cu", fontsize=fontsize)
	tax.bottom_axis_label("Ar", fontsize=fontsize)

	fontsize = 10
	pax.set_title("BaxCuyArz Composition diagram", fontsize=20)
	pax.left_axis_label("Ba", fontsize=fontsize)
	pax.right_axis_label("Cu", fontsize=fontsize)
	pax.bottom_axis_label("Ar", fontsize=fontsize)


	p1 = []
	with open("composition.dat") as handle:
	    for line in handle:
	        p1.append(list(map(float, line.split(' '))))


	tax.scatter(p1)
	pax.scatter(p1)
	tax.legend()

	pax.ticks(axis='lbr', multiple=10, linewidth=1)

	for i in range(Ncomps):
	    tax.annotate(str(p1[i]), (p1[i]), fontsize=7,rotation=10)

	tax.savefig('Ternary_with_labels.png', dpi)
	pax.savefig('Ternary_no_labels.png', dpi)


def main():
	args = parse_arguments()
	Ncompo = args.compo
	dpis = args.dpi
	create_graphs(Ncompo,dpis)

if __name__ == "__main__":
	main()
