import os
def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8_sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	allen_word_count = 0
	viki_work_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0
	person = None
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				if s[2] == '貼圖':
					allen_sticker_count += 1
				elif s[2] == '圖片':
					allen_pic_count += 1
				else:
					allen_word_count += len(m)

		if name == 'Viki':
			for m in s[2:]:
				if s[2] == '貼圖':
					viki_sticker_count += 1
				elif s[2] == '圖片':
					viki_pic_count += 1
				else:
					viki_work_count += len(m)

	print('Allen 說了：', allen_word_count, '個字, ', '用了', allen_sticker_count, '貼圖, 用了', allen_pic_count, '張圖片')
	print('Viki 說了：', viki_work_count, '個字, ', '用了', viki_sticker_count, '貼圖, 用了', viki_pic_count, '張圖片')

	return new


def main():
	if os.path.isfile('LINE-Viki.txt'):
		lines = read_file('LINE-Viki.txt')
		lines = convert(lines)
		for line in lines:
			print(line)
	else:
		print('檔案不存在')
	#write_file('output02.txt',lines)

def write_file(filename,lines):
	with open(filename,'w',encoding='utf-8_sig') as f:
		for line in lines:
			f.write(line + '\n')


main()


