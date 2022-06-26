from cal_cost import cal_cost
import matplotlib.pyplot as plt
from plot_model import plot_model
from dstar_lite import dstar_lite
from plot_solution import plot_solution
from cal_smoothness import cal_smoothness
from create_dstarlite_model import CreateDstarLiteModel

# dist_type: manhattan or euclidean
# expand_method: random or heading
setting = {'adj_type': '4adj', 'dist_type': 'manhattan', 'expand_method':'heading'}
model = CreateDstarLiteModel(setting)

# dstar lite
[model, path] = dstar_lite(model)

# cost and smoothness
path_length = cal_cost(path)
path_smoothness = cal_smoothness(path)
path_turns = path_smoothness/90

# results
print(path.nodes)
print(path.dirs)
print(path_length, path_smoothness, path_turns)

# plot
ax = plot_model(model)
plot_solution(path, ax)
plt.show()
