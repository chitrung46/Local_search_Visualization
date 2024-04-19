import random

import cv2
import matplotlib.pyplot as plt
import numpy as np


class Problem:
    def __init__(self, filename, initial_coor=None):
        self.X, self.Y, self.Z = self.load_state_space(filename)
        self.initial_coor = self.set_initial_coor(initial_coor)

    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z = img
        return X, Y, Z

    def random_coor(self):
        return (random.choice(self.X), random.choice(self.Y))

    def set_initial_coor(self, coor):
        if coor == None:
            return self.random_coor()
        else:
            return coor

    def get_initial_coor(self):
        return self.initial_coor

    def get_value(self, x, y):
        return self.Z[y, x]

    def get_successors(self, x, y):
        successors = []

        if x < self.X[-1]:
            successors.append((x + 1, y, self.Z[y, x + 1]))
        if x > 0:
            successors.append((x - 1, y, self.Z[y, x - 1]))
        if y < self.Y[-1]:
            successors.append((x, y + 1, self.Z[y + 1, x]))
        if y > 0:
            successors.append((x, y - 1, self.Z[y - 1, x]))

        return successors

    def show(self):
        X, Y = np.meshgrid(self.X, self.Y)
        plt.figure(figsize=(8, 6))
        ax = plt.axes(projection="3d")
        ax.plot_surface(
            X, Y, self.Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none"
        )
        plt.show()

    def draw_path(self, path):
        Xpath = [t[0] for t in path]
        Ypath = [t[1] for t in path]
        Zpath = [t[2] for t in path]

        X, Y = np.meshgrid(self.X, self.Y)
        plt.figure(figsize=(8, 6))
        ax = plt.axes(projection="3d")
        ax.plot_surface(
            X, Y, self.Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none"
        )
        ax.plot(Xpath, Ypath, Zpath, "r-", zorder=3, linewidth=0.5)
        plt.show()
