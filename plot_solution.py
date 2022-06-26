import matplotlib.pyplot as plt


def plot_solution(path, ax):
    ax.plot(path.x, path.y, 'b', linewidth=1)
    ax.plot(path.x, path.y, 'o', markersize=4,
            markeredgecolor='b', markerfacecolor='b')
