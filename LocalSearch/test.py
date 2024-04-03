from problem import Problem
from search import LocalSearchStrategy as LCS

p = Problem("monalisa.jpg", (20, 91))
search = LCS()
# path = search.random_restart_hill_climbing(p, 5)
path = search.local_beam_search(p, 5)

p.draw_path(path)
