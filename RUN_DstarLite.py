import time
from cal_cost import cal_cost
import matplotlib.pyplot as plt
from plot_model import plot_model
from dstar_lite import dstar_lite
from plot_solution import plot_solution
from plot_animation import PlotAnimation1
from cal_smoothness import cal_smoothness
from create_dstarlite_model import CreateDstarLiteModel

# dist_type: manhattan or euclidean
# expand_method: random or heading
setting = {'adj_type': '4adj', 'dist_type': 'manhattan',
           'expand_method': 'heading'}

# model
model = CreateDstarLiteModel(setting)

# process time
t_start = time.process_time()

# dstar lite
[model, path] = dstar_lite(model)
path_time = time.process_time()-t_start

# cost and smoothness
path_length = cal_cost(path)
path_smoothness = cal_smoothness(path)
path_turns = path_smoothness/90

# results
print(path.nodes)
print(path.dirs)
print(path_length, path_smoothness, path_turns, path_time)

# plot
fig, ax = plot_model(model)
plot_solution(path, ax)
plt.show()

# # animation
# fig, ax = plot_model(model)
# animation = PlotAnimation1(fig, ax, path)
# animation.anim.save('results/animation1.gif', fps=4)
# plt.show()
