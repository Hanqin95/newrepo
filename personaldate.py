"""
name = "Ming"
print(name)

age = 18 #integer整数数字变量#
gender = True #bool 非零的数是真 0是假
#True = 1
#False = 0



height = 1.75 #float浮点数，小数
weight = 75.0 #float
weight = 75 #int

print(type(age))#type函数查看变量类型

i = 10
f = 10.5
b= True

result = i + f -b
print(result)

first_name = "san"
last_name = "zhang"
full_name = last_name + " " + first_name 
print(full_name)

print("zhang"*10)
"""
"""
int("x") #将字符串转换成整数
float("x")#将字符串转换成小数
"""
"""
price_str = input("苹果的单价: ")
weight_str = input("苹果的重量: ")
money = float(price_str) * float(weight_str)
print("总共:" + str(money)+"元")
"""

"""
price = float(input("苹果的单价: "))
weight = float(input("苹果的重量: "))
money = price * weight
print("总共："+str(money) + "元")
"""
# %s:输出字符串  %d:输出整数 %06d:输出六位数  前面补零    %f输出浮点数    %.02f输出浮点数并保留两位小数   %%输出%
"""
name = "Ming"
print("My name is %s" % name)
"""

#student_no  = 1
#print ("my number is %06d" % student_no)

"""
price = 8.5
weight = 7.5
money = price * weight
print("Applle is %.02f €, you got %.02f kilo and must pay %.02f €" %(price, weight, money))

scale = 0.25
print("数据比例是%.02f%%"%(scale*100))
"""

