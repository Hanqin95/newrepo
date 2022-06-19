name_list = ["zhang","Li","Wang","zhangsan"]


"""
print(name_list.index("Wang"))


name_list[1] = "Lisi"
name_list.append("second dog")
name_list.insert(1,"CAT")
temp_list = ["Monkey","Pig"]
name_list.extend(temp_list)
name_list.remove("Monkey")
name_list.pop() #默认删除列表中最后一个数据
name_list.pop(3)#指定要删除元素的位置
name_list.clear()#清空列表所有内容
print(name_list)
"""
#del name_list[1]#将一个变量从内存中删除
#print(len(name_list))
#count = name_list.count("zhang")
#print("there are %d zhang"%count)
#name_list.remove("zhang")#删除第一个出现的zhang
#print(name_list)

#num_list = [2, 4, 5 ,2, 3,98]
#num_list.sort()
#num_list.sort(reverse = True) #降序排列
#print(num_list)
#for my_name in name_list:
#	print("my name ist %s" % my_name)

info_tuple = ("zhangsan", 18,1.75)
tuple_B = ()
print(type(tuple_B))

single_tuple = (5,) #单个元组变量必须后面跟一个点，否则会将其认证为整数
print(type(single_tuple))
print(info_tuple[0])
print(info_tuple.index("zhangsan"))#显示第一个出现的位置
print(info_tuple.count("zhangsan"))

for my_info in info_tuple:
	print(my_info)

print("%s is %d years old and %.2f high" % info_tuple)

NEW = list(info_tuple)  #用list可以将元组转化成列表
print (type(NEW))