import os

script_dir = os.path.dirname(__file__)
rel_path = "data/1-very_easy.txt"
abs_path = os.path.join(script_dir, rel_path)

triangle = {}
with open(abs_path, "r") as f:
    file = f.read().splitlines()
    file = [line.replace(' ', '') for line in file]
    for idx, line in enumerate(file):
        triangle[idx + 1] = [int(x) for x in line]

print(triangle)
#triangle = sorted(triangle)
#print(triangle)
SIZE = len(triangle)

lista = [1, 1, 2]
min = min(lista)
min_idx = lista.index(min)
print(min_idx)

def search_min_path(triangle: dict) -> str:
    working_layer = 0



# def traverse(curr_idx, curr_layer):
#     next_idx = 0
#     next_layer = 0
#
#     if not curr_layer == SIZE:
#         return triangle[curr_idx] + traverse(next_idx, next_layer)
#
#
# chain = traverse(0, 0)



