from problem import Problem
from search import LocalSearchStrategy as LCS
import random

def schedule(t):
    return 1 / (t**2)

p = Problem("monalisa.jpg")
lcs = LCS()
# pathLCS = lcs.random_restart_hill_climbing(p, 5)
pathSA = lcs.simulated_annealing_search(p, schedule)

p.draw_path(pathSA)
# print(pathSA)
# KThen đã vào xem

