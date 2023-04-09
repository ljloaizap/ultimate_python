from pathlib import Path


file = Path('files_7/test_file.txt')
text = file.read_text('utf-8').split('\n')
# print(text)

text.insert(0, 'Hello World!\n')
file.write_text('\n'.join(text), 'utf-8')
