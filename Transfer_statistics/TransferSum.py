# 调休统计小程序
# 帮助数学不行的小周同志计算每周的调休

# 各种排班时间


classSchedule_value: list = ["0日班", "1夜班", "2早班", "3小中班", "4休息", "5节休", "6调休"]
classSchedule: list = ["日班", "夜班", "早班", "小中班", "休息", "节休", "调休"]
week: list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
weekPB: dict = {"周一": "", "周二": "", "周三": "", "周四": "", "周五": "", "周六": "", "周日": "", }

# 每周正常工作时间
normalTime: int = 40
# 调休时间统计
AdjustableTime = "AdjustableTime.txt"
# 每周统计
filename_week = "WeeklyStatistics.txt"
with open(AdjustableTime, 'r') as file_object:
    times = file_object.read()
# 是否使用调休
isTX = 0
while True:
    # 每日排班变量
    print(classSchedule_value)
    z_hou = ""
    for day in week:
        z_hou = input(f"请输入{day}排班: ")
        if z_hou in ["0", "1", "2", "3", "4", "5", "6"]:
            weekPB[day] = classSchedule[int(z_hou)]
        else:
            print("录入错误请重新录入")
            break
        if classSchedule[int(z_hou)] == "日班" or classSchedule[int(z_hou)] == "夜班":
            normalTime = normalTime - 12
        elif classSchedule[int(z_hou)] == "早班" or classSchedule[int(z_hou)] == "节休":
            normalTime = normalTime - 8
        elif classSchedule[int(z_hou)] == "小中班":
            normalTime = normalTime - 4
        elif classSchedule[int(z_hou)] == "调休":
            isTX += 1
            times = int(times) - 8
    with open(AdjustableTime, 'w') as file_object:
        # 累计调休
        weekTime: int = (-1 * normalTime) if normalTime > 0 else normalTime * -1
        maxTime = int(times) + weekTime
        file_object.write(str(maxTime))
        file_object.close()
    with open(filename_week, 'a') as file_object:
        inputWeek = input("请输入当前班次的日期： ")
        if isTX != 0:
            file_object.write(inputWeek + ": " + str(weekPB) + f"本周调休{weekTime}," + f"剩余调休{maxTime}小时" +
                              f"本周使用调休总时间-8小时")
        elif isTX == 0:
            file_object.write(inputWeek + ": " + str(weekPB) + f"本周调休{weekTime}," + f"剩余调休{maxTime}小时" +
                              f"本周未使用调休")
        file_object.close()
    print(str(weekPB) + f"本周调休{weekTime}小时\n")
    break
