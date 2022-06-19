"""
i = 0
while i < 5:
	print("hallo Python")
	i +=1
print("end i= %d"%i)
"""
"""
i = 0
a = 0 
while i <= 100:
	a += i
	i += 1

print(a)
"""
"""
i = 0 
while i < 10:
	if i == 3:
		break

	print (i)

	i += 1

print("over")
"""
"""
i = 0
a = 0
while i < 5 : 
	if i == 3:
		i += 1
		continue #跳过当前步骤返回判断
	print (i)
	i += 1
"""

"""
row = 1 
while row <= 5:
	print("*" * row)
	row += 1
"""
"""
print("*",end="---")   #,end="---"取消换行
print("*")

row = 1
while row <= 5:
	col = 1
	while col <= row:
		print("%d"%col)
		col += 1
	row += 1
	print("第%d行"%row)
"""

row = 1
while row <= 9:
	col = 1
	while col <= row:
		#print("*",end=" ")
		print("%d * %d = %d"%(col,row,col*row), end="\t")
		col += 1 	

	print("%d"%row)
	row += 1


#\t文本垂直方向对齐   \n文本换行   \转义字符
print("1\t2\t3")
print("11\t22\t33")

print("hello\npython")
print("hello\"python")