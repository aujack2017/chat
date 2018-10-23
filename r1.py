import os
def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8_sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ' : ' + line)
	return new


def main():
	if os.path.isfile('input.txt'):
		lines = read_file('input.txt')
		lines = convert(lines)
		for line in lines:
			print(line)
	else:
		print('檔案不存在')
	write_file('output.txt',lines)

def write_file(filename,lines):
	with open(filename,'w',encoding='utf-8_sig') as f:
		for line in lines:
			f.write(line + '\n')


main()


