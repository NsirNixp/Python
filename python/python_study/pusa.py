
import os
def num2chn(num):
	chr = ('零','贰','叁','肆','伍','陆','柒','捌','玖')
	bit = ('分', '角', '元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟', '万')

	try:
		num = float(num)
		num_str = ('%0.2f' % num).replace('.','')[::-1]
	except ValueError:
		return None

	n = len(num_str)
	if n >= 15:
		return None

	result = []
	for i in range(0, n):
		if num_str[i] == '0' and i!=2 and i!=6 and i!=10:
			s = chr[0]
		elif num_str[i] == '0' and (i==2 or i==6 or i==10):
			s = bit[i]
		else:
			s = bit[i] + chr[int(num_str[i])]
		result.append(s)

	rst = ''.join(result)[::-1]
	r = "[" + chr[0] + "]"
	rst = result.compile(r).sub(chr[0],rst).rstrip(chr[0])

	for i in [2, 6, 10]:
		rst = rst.replace(chr[0] + bit[i], bit[i])
	if rst[-1] == bit[2]:
		rst += "整"

	print('%0.2f' % num)
	print(rst)
	return rst


if __name__ == '__main__':
	num2chn(152)