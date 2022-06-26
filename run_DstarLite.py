import matplotlib.pyplot as plt
from plot_model import plot_model
from dstar_lite import dstar_lite
from plot_solution import plot_solution
from create_dstarlite_model import CreateDstarLiteModel

# dist_type: manhattan or euclidean
# expand_method: random or heading
setting = {'adj_type': '4adj', 'dist_type': 'manhattan', 'expand_method':'random'}
model = CreateDstarLiteModel(setting)


[model, path] = dstar_lite(model)

print(path.nodes)
print(path.dirs)
print(path.x)
print(path.y)

ax = plot_model(model)
plot_solution(path, ax)
plt.show()
