"""
Csinalj egy fuggvenyt ami kap egy matrixot es egy erteket parameterul es kicsereli a foatloban levo ertekeket a kapottra (az eredeti matrixot ne modositsa)
"""

import random
import pprint


matrix = [[random.randint(0,9) for i in range(10)] for i in range(10)]



def change_diagonal(matrix, value):
    new_matrix = []
    
    for i,row in enumerate(matrix):
        new_row = row[:]
        new_row[i] = value
        new_matrix.append(new_row)
    return new_matrix
        




changed = change_diagonal(matrix, "YO")

pprint.pprint(matrix)
pprint.pprint(changed)