import random


def guess_the_number():
    # 生成一个1到100之间的随机数
    secret_number = random.randint(1, 100)

    print("欢迎参加猜数字游戏！")
    print("我已经选好了一个1到100之间的数字，请开始猜测吧！")

    attempts = 0

    while True:
        try:
            # 获取玩家的猜测
            guess = int(input("你的猜测: "))
            attempts += 1

            # 判断猜测是否正确
            if guess == secret_number:
                print(f"恭喜你猜中了！你用了 {attempts} 次尝试。")
                break
            elif guess < secret_number:
                print("太小了，请继续尝试。")
            else:
                print("太大了，请继续尝试。")

        except ValueError:
            print("请输入一个有效的数字。")


if __name__ == "__main__":
    guess_the_number()
