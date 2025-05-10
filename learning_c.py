from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

line_list = []

for line in lines:
    line = line.replace('python', 'c')
    print(line)
    line_list.append(line)

print(line_list)