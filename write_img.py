import sys


def w_img(org_file, dst_file):
	org = open(org_file, 'rb')
	dst = open(dst_file, 'rb+')

	data = org.read(512)
	dst.write(data)
	org.close()
	dst.close()

if __name__ == '__main__':
	print sys.argv[1]
	print sys.argv[2]
	w_img(sys.argv[1], sys.argv[2])
