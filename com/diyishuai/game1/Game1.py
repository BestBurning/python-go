
def Game1():
    import random
    # 控制台输入
    player = int(input("请出拳:1 石头 2 剪刀 3 布"))

    # 计算机出拳
    computer = random.randint(1,3)
    print("玩家出拳:", player, ",计算机出拳:", computer)
    # 比较大小得出结果
    # 1 > 2
    # 2 > 3
    # 3 > 1

    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):
        print("玩家胜利")
    elif (player == computer):
        print("平局")
    else:
        print("计算机胜利")
