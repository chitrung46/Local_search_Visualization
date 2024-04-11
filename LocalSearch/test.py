from problem import Problem
from search import LocalSearchStrategy as LCS

p = Problem("monalisa.jpg")
search = LCS()
# path = search.random_restart_hill_climbing(p, 5)
def schedule(t):
    return 1/(t**2)
# path = search.local_beam_search(p, 5)
path = search.simulated_annealing_search(p, schedule)


p.draw_path(path)
