import random
veri_list = []
#通过chr()函数取随机大写字母A-Z
def A_str():
    for i in range(4):
        veri_num1 = random.randint(65,90)  #取值65-90随机一个整数
        veri_str1 = chr(veri_num1)
        veri_list.append(veri_str1)

#通过chr()函数取随机小写字母a-z
def a_str():
    for i in range(4):
        veri_num2 = random.randint(97,122)  # 取值98-122随机一个整数
        veri_str2 = chr(veri_num2)           # 转换小写字母a-z的随机
        veri_list.append(veri_str2)

#通过chr()和ord()函数取随机数字0-9
def num_1():
    for i in range(4):
        veri_num3 = random.randint(48,57)
        veri_str3 = chr(veri_num3)
        veri_list.append(veri_str3)

#执行主函数
def ver_code():
    A_str()
    a_str()
    num_1()
    veri_res = random.sample(veri_list,4)
    # print(veri_res)
    res = str(veri_res[0]) + str(veri_res[1]) + str(veri_res[2]) + str(veri_res[3])
    return res