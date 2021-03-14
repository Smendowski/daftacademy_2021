import os

script_dir = os.path.dirname(__file__)
rel_path = "data/1-very_easy.txt"
abs_path = os.path.join(script_dir, rel_path)

with open(abs_path, "r") as f:
    triangle = f.read().splitlines()
    triangle = [line.replace(' ', '') for line in triangle]


