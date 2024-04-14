import cv2
import matplotlib.pyplot as plt
import numpy as np


class Problem:
    def __init__(self, filename, initial_coor=None):
        self.X, self.Y, self.Z = self.load_state_space(filename)
        self.initial_coor = initial_coor

    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z = img
        return X, Y, Z

    def show(self):
        X, Y = np.meshgrid(self.X, self.Y)
        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection="3d")
        ax.plot_surface(
            X, Y, self.Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none"
        )
        plt.show()

    def draw_path(self, path):
        print(path)
        Xpath = [t[0] for t in path]
        Ypath = [t[1] for t in path]
        Zpath = [t[2] for t in path]

        X, Y = np.meshgrid(self.X, self.Y)
        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection="3d")
        ax.plot_surface(
            X, Y, self.Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none"
        )
        ax.plot(Xpath, Ypath, Zpath, "r-", zorder=3, linewidth=0.5)
        plt.show()