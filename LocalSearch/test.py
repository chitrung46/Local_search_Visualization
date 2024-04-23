from problem import Problem
from search import LocalSearchStrategy as LCS
import random
import math

def schedule(t):
    # print(0.88 / (math.log(t + 1)) - 0.0000000001)
    # return 0.88 / (math.log(t + 1)) - 0.000000000001
    # print(1/ (t**2) - 0.0000000001)
    return (1/ (t**2) - 0.0000000001)

p = Problem("monalisa.jpg")
lcs = LCS()
pathHC = lcs.random_restart_hill_climbing(p, 5)
pathSA = lcs.simulated_annealing_search(p, schedule)
pathLB = lcs.local_beam_search(p, 3)

p.draw_path(pathHC)
p.draw_path(pathSA)
p.draw_path(pathLB)


