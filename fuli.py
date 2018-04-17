# 设计一个复利计算函数 invest()，它包含三个参数：amount（资金），rate（利率），time（投资时间）。
# 输入每个参数后调用函数，应该返回每一年的资金总额。它看起来就应该像这样（假设利率为5%）
def invest(amount,time,rate = 0.05):
    print("Please Enter Money:"+str(amount))
    for year in range(1,time):
        amount = amount * (1+rate)
        print(str(year) +" year: $"+str(amount))
invest(100,100)