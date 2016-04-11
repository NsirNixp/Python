import os
import sys
import re
import urllib

vancal_item = re.compile(r'http://vt.vancl.com/item/(\d+).*', re.I)
item_pic = re.compile(r'(http://images.vancl.com/product/.*?/small.*?\.jpg)', re.I)

def download(dir, url):
	global vancal_item, item_pic
	if not os.path.isdir(dir):
		os.mkdir(dir)

	html = urllib.urlopen(url).read()
	items = [item for item in vancal_item.findall(html)]
	for idx, item in enumerate(items):
		item_url = 'http://vt.vancl.com/item/' + item +'.html'
		print idx, ':', item_url
		try:
			os.makedirs(dl_dir)
		except:
			pass

		item_html = urllib.urlopen(item_url).read()
		item_pics = [item for item in item_pic.findall(item_html)]
		for sidx, sitem in enumerate(item_pics):
			tmp = sitem.replace('small', 'mid')
			name = tmp.split('/')[-1]
			dl_name = os.path.join(dl_dir, name)
			urllib.urlretrieve(tmp, dl_name)
	return

def main():
	dir = 'img'
	ss = 'http://www.vt.vancl.com/list/women/'
	ed = '/view=1'
	for idx in range(10):
		download(dir, ss + str(idx+1) +ed)

if __name__ == '__main__':
	main()




