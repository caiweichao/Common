# 1， 定义一个类 Dog, 包含 2 个属性：名字和年龄。
# 定义一个方法 eat 吃东西。
# 定义一个类 TeddyDog, 继承 Dog 类， Teddy 在吃东西的时候还会望着你，  定义方法 watch_you.
# 定义一个类 BabyTeddyDog, 继承 TeddyDog,  BabyTeddy 吃东西不仅会望着你，还会四处转悠， 定义方法 go_around


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃东西')


class TeddyDog(Dog):
    def watch_you(self):
        self.eat()
        print('看着你')


class BabyTeddyDog(TeddyDog):
    def go_around(self):
        self.eat()
        self.watch_you()
        print('四处转悠')


# 1.编写如下程序
# 编写一个工具箱类和工具类
# 工具类：需要有工具具的名称、功能描述、价格。
# 工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
# 实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
# 工具比如锤子、斧头、螺丝刀等工具。
# 提示：不需要用到继承。
class Tool:
    def __init__(self, name, features, price):
        self.name = name
        self.features = features
        self.price = price


class Tool_Box:
    def __init__(self):
        self.tool_list = []

    def add_tool(self, tool):
        self.tool_list.append(tool)

    def remove_tool(self, tool):
        self.tool_list.remove(tool)

    def statistics_tool(self):
        num = len(self.tool_list)
        print(f'一共有{num}件工具')


if __name__ == '__main__':
    TeddyDog(name=1, age=2).watch_you()
    BabyTeddyDog(1, 2).go_around()
    hammer = Tool('锤子','砸东西',100)
    screwdriver = Tool('螺丝刀','拧螺丝',10)
    scissors = Tool('剪刀','剪东西',20)
    ToolBox = Tool_Box()
    ToolBox.add_tool(hammer)
    ToolBox.add_tool(screwdriver)
    ToolBox.add_tool(scissors)
    ToolBox.add_tool(screwdriver)
    ToolBox.statistics_tool()
    ToolBox.remove_tool(screwdriver)
    ToolBox.statistics_tool()


