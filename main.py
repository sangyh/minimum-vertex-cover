"""
Wrapper function to call the algorithm executables
Possible algorithm options:
	[BnB|Approx|LS1|LS2]

Sample Execution:
	python CS6140_project/main.py -inst Data/karate.graph -alg Approx -time 600 -seed 1045

"""
import BnB
import ls1
#import ls2
import Approx
import sys
from sys import argv
import argparse

	
if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='Wrapper Function for Vertex Cover Graphs')
	parser.add_argument('-inst',action='store',type=str,required=True,help='Input graph datafile')
	parser.add_argument('-alg',action='store',type=str,required=True,help='Input Alg  [BnB|Approx|LS1|LS2]')
	parser.add_argument('-time',action='store',default=600,type=float,required=False,help='Cutoff running time (s)')
	parser.add_argument('-seed',action='store',default=1000,type=int,required=False,help='Random Seed for algorithm')		
	args=parser.parse_args()

	algorithm = args.alg
	graph_file = args.inst
	output_dir = 'Output/'
	cutoff = args.time
	randSeed = args.seed

	if algorithm == 'Approx':
		Approx.main(graph_file, output_dir, cutoff, randSeed)

	elif algorithm == 'LS1':
		ls1.main(graph_file, output_dir, cutoff, randSeed)

	elif algorithm == 'LS2':
		ls2.main(graph_file, output_dir, cutoff, randSeed)

	elif algorithm == 'BnB':
		BnB.main(graph_file, output_dir, cutoff, randSeed)
		
	else:
		print('Inputted incorrect algorithm option, please try any of: [BnB|Approx|LS1|LS2]')
