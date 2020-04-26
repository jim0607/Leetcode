滑动窗口的模板：
两层for 循环
for i in range(lens):
    while j < lens:
        if 满足条件:
            更新带有 j 的信息
            j += 1
        else:
            break

    更新 res

    更新带有 i 的信息
