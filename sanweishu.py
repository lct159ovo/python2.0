count =0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != k and j != i and k != j:
                print(i,j,k)
                count += 1  # 每次满足条件时增加计数器的值

print("总共有", count, "组ijk不相等的三位数")
