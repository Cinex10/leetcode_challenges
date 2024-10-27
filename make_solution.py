import sys
import os


def to_snake_case(text):
    result = text.lower().replace(' ', '_')
    result = ''.join(c for c in result if c.isalnum() or c == '_')
    return result

tmp = sys.argv[1]
problem_name = to_snake_case(tmp)

folder_path = f'solutions/{problem_name}'
os.makedirs(folder_path, exist_ok=True)

filenames = [
    os.path.join(folder_path, f'solution.py'),
    os.path.join(folder_path, f'test_solution.py'),
]

for filename in filenames:
    with open(filename, 'w') as f:
        pass

print(f'{tmp} solution folde structure created ✅')


