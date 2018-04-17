#游戏开始，首先玩家选择 Big or Small（押大小），
#选择完成后开始摇三个骰子计算总值，11 <= 总值 <=18 为 “大”，3 <= 总值 <= 10 为 “小”。
# 然后告诉玩家猜对或是猜错的结果
import random
def shake(numbers):
    print("开始摇骰子。。。。。。。")
    points = None
    if points == None:
        points = []
    while numbers>0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return  sum(points)

def panduan(correct_result):
    print("结果为："+ str(correct_result))
    isBig = 11 <= correct_result <= 18
    isSmall = 3 <= correct_result <= 10
    if isBig:
        return "大"
    elif isSmall:
        return "小"




def guess():
    print("游戏开始##########")
    choices = ["大","小"]
    gus_result = input("请选择大或小:")
    if gus_result in choices:

        total_points = shake(3)
        result = panduan(total_points)
        if result == gus_result:
            print("您猜对了！")
        else:
            print("您猜错了！")
    else:
        print("Invalid Choice!")
        guess()
guess()

