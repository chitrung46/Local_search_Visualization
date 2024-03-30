from problem import Problem
from search import LocalSearchStrategy as LCS

p = Problem("monalisa.jpg")
search = LCS()
path = search.random_restart_hill_climbing(p, 5)

p.draw_path(path)
