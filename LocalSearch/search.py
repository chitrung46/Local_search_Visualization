import heapq
import math
import random
import math

class LocalSearchStrategy:
    def get_best_successors(self, x, y, space):
        X, Y, val = space
        successors = []

        if x < X[-1]:
            successors.append([x+1, y, val[y,x+1]])
        if x > 0:
            successors.append([x-1, y, val[y,x-1]])
        if y < Y[-1]:
            successors.append([x, y+1, val[y+1,x]])
        if y > 0:
            successors.append([x, y-1, val[y-1,x]])

        best_succ = successors[0]

        for succ in successors:
            if succ[2] > best_succ[2]:
                best_succ = succ

        return best_succ

    def random_restart_hill_climbing(self, problem, num_trial=1):
        X = problem.X
        Y = problem.Y
        V = problem.Z  # evaluation value
        path = []

        for i in range(num_trial):
            x = random.choice(X)
            y = random.choice(Y)
            curr = (x, y, V[y, x])
            curr_path = [curr]

            while True:
                curr_x, curr_y, curr_v = curr
                next = self.get_best_successors(curr_x, curr_y, (X, Y, V))

                if next[2] > curr_v:
                    curr = next
                    curr_path.append(next)
                else:
                    print(curr_path)
                    if len(path) == 0 or curr_path[-1][2] > path[-1][2]:
                        path = curr_path
                    break
        print(path)
        return path

    # Local Beam Search
    def get_successors(self, x, y, space):
        X, Y, val = space
        successors = []

        if x < X[-1]:
            successors.append([x+1, y, val[y,x+1]])
        if x > 0:
            successors.append([x-1, y, val[y,x-1]])
        if y < Y[-1]:
            successors.append([x, y+1, val[y+1,x]])
        if y > 0:
            successors.append([x, y-1, val[y-1,x]])

        return successors


    def local_beam_search(self, problem, k=1):
        X, Y, V = problem.X, problem.Y, problem.Z

        if problem.initial_coor is None:
            x, y = random.choice(X), random.choice(Y)
        else:
            x, y = problem.initial_coor[0], problem.initial_coor[1]
        states = [((x, y, V[y, x]), [(x, y, V[y, x])])]  # (x, y), path
        path = states[-1][1]

        while True:
            new_state = []
            for (x, y, _), path in states:
                successors = self.get_successors(x, y, (X, Y, V))

                for successor in successors:
                    new_path = path + [successor]
                    new_state.append((successor, new_path))

            new_state = sorted(new_state, key=lambda x: x[0][2], reverse=True)[:k]
            if path[-1][2] < new_state[0][0][2]:
                path = new_state[0][1]
                states = new_state
            else:
                print(best_path)
                return best_path

    def simulated_annealing_search(self, problem, schedule):
        X = problem.X
        Y = problem.Y
        Z = problem.Z
        
        if problem.initial_coor is None:
            x, y = random.choice(X), random.choice(Y)
        else: 
            x, y = problem.initial_coor[0], problem.initial_coor[1]
        current_state = (x, y, Z[y, x])
        current_energy = int(Z[y, x])

        path = [current_state]
        t = 1
        while True:
            T = schedule(t)
            if T <= 0.0000000001:
                return path
            
            next_state = random.choice(self.get_successors(current_state[0], current_state[1], (X,Y,Z)))

            if next_state in path:
                continue
            next_energy = int(next_state[2])
            delta_E = next_energy - current_energy

            if delta_E > 0 or math.exp(delta_E / T) > random.random():
                current_state = next_state
                current_energy = next_energy
                path.append(next_state)
            t += 1
