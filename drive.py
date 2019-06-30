title = ('這是一個可以知道各國幾歲可以開車的程式')
print(title)
country = input('請問你是哪國人: ')
age = input('請輸入你的年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('恭喜你可以去考駕照了')
	else:
		print('你還沒到可以考駕照的年齡')
elif country == '美國':
	if age >= 16:
		print('恭喜你可以去考駕照了')
	else:
		print('你還沒到可以考駕照的年齡')
else:
	print('只能輸入 台灣/美國')