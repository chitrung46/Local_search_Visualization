import heapq
import math
import random
import math

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial=1):
        path = []

        for i in range(num_trial):
            x, y = problem.random_coor()
            curr_state = (x, y, problem.get_value(x, y))
            curr_path = [curr_state]

            while True:
                curr_x, curr_y, curr_v = curr_state
                successors = problem.get_successors(curr_x, curr_y)
                next_state = successors[0]

                # find best successor
                for succ in successors:
                    if succ[2] > next_state[2]:
                        next_state = succ

                if next_state[2] > curr_v:
                    curr_state = next_state
                    curr_path.append(next_state)
                else:
                    if len(path) == 0 or curr_path[-1][2] > path[-1][2]:
                        path = curr_path
                    break
        return path

    # Local Beam Search
    def local_beam_search(self, problem, k=1):
        x, y = problem.get_initial_coor()
        initial = (x, y, problem.get_value(x, y)) 
        states = [(initial, [initial])]
        path = states[-1][1]

        while True:
            new_states = []
            for (x, y, _), path in states:
                successors = problem.get_successors(x, y)

                for successor in successors:
                    new_path = path + [successor]
                    new_states.append((successor, new_path))

            new_states = sorted(new_states, key=lambda x: x[0][2], reverse=True)[:k]
            if path[-1][2] < new_states[0][0][2]:
                path = new_states[0][1]
                states = new_states
            else:
                return path

    def simulated_annealing_search(self, problem, schedule):
        x, y = problem.get_initial_coor()
        curr_state = (x, y, problem.get_value(x, y))
        curr_energy = int(curr_state[2])
        path = [curr_state]
        t = 1

        while True:
            T = schedule(t)
            if T == 0:
                return path
            
            next_state = random.choice(problem.get_successors(curr_state[0], curr_state[1]))

            next_energy = int(next_state[2])
            delta_E = next_energy - curr_energy

            if delta_E > 0 or math.exp(delta_E / T) > random.random():
                curr_state = next_state
                curr_energy = next_energy
                path.append(next_state)
            t += 1
