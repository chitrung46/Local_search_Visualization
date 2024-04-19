import random

from problem import Problem
from search import LocalSearchStrategy as LCS


def schedule(t):
    return 1 / (t**2) - 0.0000000001


p = Problem("monalisa.jpg")
lcs = LCS()

pathHC = lcs.random_restart_hill_climbing(p, 5)
pathLB = lcs.local_beam_search(p, 3)
pathSA = lcs.simulated_annealing_search(p, schedule)

p.draw_path(pathHC)
p.draw_path(pathLB)
p.draw_path(pathSA)
# print(pathSA)
# KThen đã vào xem
