# 1， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
def add_fun(str_value: str, dict_value: dict):

    if str_value not in dict_value:
        dict_value.update(x=str_value)
        return dict_value

dict1 = add_fun(str_value="198", dict_value={"姓名": "lichkk"})
print(dict1)


# 2， 通过定义一个计算器函数，调用函数传递三个参数(2个数字，一个运算符)，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
def calculator(num1, num2, method):
    if method == 1:
        print(num1 + num2)
    elif method == 2:
        print(num1 - num2)
    elif method == 3:
        print(num1 * num2)
    elif method == 4:
        print(num1 / num2)
    else:
        print("输入错误")


method = input('然后提示选择【1】加 【2】减【3】乘 【4】除 操作')
calculator(1, 1, int(method))


# 3， 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，
# 询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
def football():
    x = 10
    agree_member = 0
    while x > 0:
        sex = input('请输入性别:1=男，2=女')
        age = input('请输入年龄')
        if int(sex) == 2 and 15 <= int(age) <= 22:
            agree_member += 1
        x -= 1
    print(f"合格人数为:{agree_member}")


football()
