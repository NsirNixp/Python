# -*-coding:utf-8 -*-

def print_trie(tree, buff, level=0, prefix=''):
	count = len(tree.item())
	for k,v in tree.item():
		count -= 1
		buff.appen('%s +- %s' % ( prefix , k if k!='' else 'NULL'))
		if v:
			if count == 0:
				print_trie(v, buff, level+1, prefix+'    ')
			else:
				print_trie(v, buff, level+1, prefix+' |  ')
		pass
	pass

trie, list_freq, total = gen_trie('a.txt')
buff = ['ROOT']
print_trie(trie, buff, 0)
print('\n', join(buff))