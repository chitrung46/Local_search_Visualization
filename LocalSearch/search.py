import heapq
import math
import random


class LocalSearchStrategy:
    def get_best_successors(self, x, y, space):
        X, Y, val = space
        neighbors = []

        if x < X[-1]:
            neighbors.append([x + 1, y, val[y, x + 1]])
        if x > 0:
            neighbors.append([x - 1, y, val[y, x - 1]])
        if y < Y[-1]:
            neighbors.append([x, y + 1, val[y + 1, x]])
        if y > 0:
            neighbors.append([x, y - 1, val[y - 1, x]])

        best_neighbor = neighbors[0]

        for neigh in neighbors:
            if neigh[2] > best_neighbor[2]:
                best_neighbor = neigh

        return best_neighbor

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

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if dx != 0 and dy != 0:
                    continue
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < len(X) and 0 <= new_y < len(Y):
                    successors.append((new_x, new_y, val[new_y, new_x]))

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
                print(path)
                return path
    
    #Simulated-annealing   
    def simulated_annealing_search(self, problem, schedule):
        X, Y, V = problem.X, problem.Y, problem.Z

        if problem.initial_coor is None:
            x, y = random.choice(X), random.choice(Y)
        else:
            x, y = problem.initial_coor[0], problem.initial_coor[1]

        state = [(x, y), [(x, y, V[y, x])]]
        T = 1

        while True:
            T = schedule(T)

            if T <= 0:
                return state[1]

            (x, y), path = state
            next_state = random.choice(self.get_successors(x, y, (X, Y, V)))

            delta = int(next_state[2]) - int(V[y, x])

            if delta > 0 or random.random() < math.exp(delta/T):
                path = state[1] + [next_state]
                state = [(next_state[0], next_state[1]), path]

            else:
                print(state[1])
                return state[1]
