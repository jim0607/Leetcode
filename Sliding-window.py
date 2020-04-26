滑动窗口的模板：
两层for 循环:
for i in range(lens):
    while j < lens and 满足条件:
        更新带有 j 的信息
        j += 1
    更新 res if 满足条件
    更新带有 i 的信息
