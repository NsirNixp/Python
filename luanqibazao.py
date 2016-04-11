import os
if os.path.isfile('a.txt'):
  os.remove('a.txt')
else:
  print 'fuck you'
