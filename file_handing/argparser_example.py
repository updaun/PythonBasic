# Command line option

import argparse

parser = argparse.ArgumentParser(description="Sum two integers.")

parser.add_argument(
    '-a', "--a_value",
     dest="A_value", help="A integer", type=int,
     required=True)
parser.add_argument(
    '-b', "--b_value",
     dest="B_value", help="B integer", type=int,
     required=True)

args = parser.parse_args()
print(args)
print("A_value : ", args.A_value)
print("B_value : ", args.B_value)
print("Sum_value : ", args.A_value + args.B_value)

# command
# python argparser_example.py -a 10 -b 10

# output
# Namespace(A_value=10, B_value=10)
# A_value :  10
# B_value :  10
# Sum_value :  20