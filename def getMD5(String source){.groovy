
def a_str = 'a=1&b=2&c=3&d=4'
println getMD5(a_str)
def getMD5(String source){
//	选择以什么格式加密，这里选择的是md5
	MessageDigest md5 = MessageDigest.getInstance("MD5")
//	将需要加密的字符串进行分解
	md5.update(source.getBytes())
	byte[] digest = md5.digest()
	StringBuffer sb = new StringBuffer()
	digest.eachByte {
		 sb.append(String.format("%02x", it &amp; 0xff)) 
	}
	return sb.toString()
}