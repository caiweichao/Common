# 1、类属性怎么定义？ 实例属性怎么定义？
# 定义在类中，方法外的属性
# 定义在初始化函数里的属性
# 2、实例方法中的self代表什么？（简答）
# 表示对象，实际调用该方法的对象
# 3、类中__init__方法在什么时候会调用的？（简答）
#
# 4、封装一个学生类Student
# -  属性：姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
# -  方法一：计算总分，
# 方法二：计算三科平均分，
# 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
# 实例化1个学生,并打印学生个人信息，计算总分，平均分。


class student:
    def __init__(self, name, age, sex, English_scores, Math_scorse, Language_scores):
        self.name = name
        self.age = age
        self.sex = sex
        self.English_scores = English_scores
        self.Math_scores = Math_scorse
        self.Language_scores = Language_scores

    def average_score_calculation(self):
        try:
            avg_scores = int(self.English_scores + self.Language_scores + self.Math_scores) / 3
        except Exception as e:
            print('计算异常请检查')
            raise e
        print(f"平均分数是{avg_scores}")
        return avg_scores

    def print_personal_information(self):
        print(f"我的名字叫{self.name}，年龄{self.age},性别{self.sex}")


if __name__ == '__main__':
    student_lich = student(name='lichkk', age=25, sex='男', English_scores=100, Math_scorse=90, Language_scores=80)
    student_lich.average_score_calculation()
    student_lich.print_personal_information()
