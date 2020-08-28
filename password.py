# x = 2
# while x >= 0:
# 	password = input('請輸入密碼: ')
# 	if password == 'a123456':
# 		print('登入成功')
# 		break
# 	if password != 'a123456':
# 		print('密碼錯誤!還有', x, '次機會!')
# 	x -= 1
# if x < 0:
# 	print('已錯誤3次', '請五分鐘後再試試!') 
# ------------------------------------------自己寫的

# password = 'a123456'
# i = 3
# while True:
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功')
# 		break
# 	else:
# 		i -= 1
# 		print('密碼錯誤! 還有', i, '次機會!')
# 		if i == 0:
# 			break
# ------------------------------------------老師寫的	
# password = 'a123456'
# i = 3
# while i > 0:
# 	pwd = input('請輸入密碼: ')
# 	i -= 1
# 	if pwd == password:
# 		print('登入成功')
# 		break
# 	elif i > 0:
# 		print('密碼錯誤! 還有', i, '次機會!')
# 	else:
# 		print('已錯誤3次', '請五分鐘後再試試!')
# ------------------------------------------自己寫的
password = 'a123456'
i = 3
while i > 0:
	pwd = input('請輸入密碼: ')
	i -= 1
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會!')
		else:
			print('已錯誤3次', '請五分鐘後再試試!')