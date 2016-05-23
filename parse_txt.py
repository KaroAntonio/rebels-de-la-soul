import json

headers = ['me']

text = {}
for title in headers:
    f = open('assets/'+title+'.txt')
    lines = []
    for line in f:
		line = line.strip()
		line = line.strip('[')
		if ']' in line: line = line[:-1]
		print(line, ']' in line)
		lines.append(line)
    text[title] = lines
    f.close()
    
with open('assets/words.json', 'w') as outfile:
    json.dump(text, outfile)
    
