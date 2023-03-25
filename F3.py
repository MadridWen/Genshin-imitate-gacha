import random
import sys
import pandas as pd

PersonFrequency = WeaponFrequency = 0  # 赋值抽卡次数为0
FourGuarantee = 0  # 赋值4星保底次数为0
FiveGuarantee = 0  # 赋值5星保底次数为01


def DecidePersonCard():  # 定义一个决定角色祈愿，抽卡到什么的函数
    star = random.randint(1, 1000)  # 决定几星
    if star in range(1, 7):
        data = [['角色（up）', 1], ['刻晴', 2], ['莫娜', 3], ['琴', 4], ['迪卢克', 5], ['七七', 6]]
        # 一个5星角色的表格数据
        Five = pd.DataFrame(data, columns=['Name', 'K'])  # 建立了一个5星角色的表格
        ChooseOne = random.randint(0, 5)  # 选择角色
        # 废弃 len() != 0    # 单个位置索引器超出界限，遇见为空的时候，却没有处理，加个条件len()!=0来避免（不知道意义）
        print("\033[31m5星\033[0m")  # 输出5星及颜色
        print(Five.iloc[ChooseOne])  # 输出角色
    elif star in range(7, 58):
        data = [['云堇', 1], ['五郎', 2], ['托马', 3], ['早柚', 4], ['九条裟罗', 5], ['凝光', 6], ['菲谢尔', 7], ['班尼特', 8],
                ['丽莎', 9], ['行秋', 10], ['迪奥娜', 11], ['安柏', 12], ['重云', 13], ['雷泽', 14], ['芭芭拉', 15], ['罗莎莉亚', 16],
                ['香菱', 17], ['凯亚', 18], ['北斗', 19], ['诺艾尔', 20], ['砂糖', 21], ['辛焱', 22], ['烟绯', 23], ['匣里龙吟', 24],
                ['匣里灭辰', 25], ['西风大剑', 26], ['绝弦', 27], ['祭礼弓', 28], ['雨裁', 29], ['弓藏', 30], ['西风秘典', 31], ['流浪乐章', 32],
                ['西风猎弓', 33], ['祭礼残章', 34], ['笛剑', 35], ['西风剑', 36], ['钟剑', 37], ['祭礼剑', 38], ['祭礼大剑', 39], ['昭心', 40],
                ['西风长枪', 41]]
        Four = pd.DataFrame(data, columns=['Name', 'K'])
        ChooseOne = random.randint(0, 40)
        # 废弃 len() != 0
        print("\033[35m4星\033[0m")
        print(Four.iloc[ChooseOne])
    else:
        data = [['飞天御剑', 1], ['铁影阔剑', 2], ['沐浴龙血的剑', 3], ['以理服人', 4], ['黑缨枪', 5], ['讨龙英杰谭', 6], ['弹弓', 7],
                ['鸦羽弓', 8], ['冷刃', 9], ['魔导绪论', 10], ['黎明神剑', 11], ['神射手之誓', 12], ['翡玉法球', 13]]
        Three = pd.DataFrame(data, columns=['Name', 'K'])
        ChooseOne = random.randint(0, 12)
        # 废弃 len() != 01
        print("\033[34m3星\033[0m")
        print(Three.iloc[ChooseOne])


def FourStarCard():  # 抽卡4星保底函数
    data = [['云堇', 1], ['五郎', 2], ['托马', 3], ['早柚', 4], ['九条裟罗', 5], ['凝光', 6], ['菲谢尔', 7], ['班尼特', 8], ['丽莎', 9],
            ['行秋', 10], ['迪奥娜', 11], ['安柏', 12], ['重云', 13], ['雷泽', 14], ['芭芭拉', 15], ['罗莎莉亚', 16], ['香菱', 17],
            ['凯亚', 18], ['北斗', 19], ['诺艾尔', 20], ['砂糖', 21], ['辛焱', 22], ['烟绯', 23], ['匣里龙吟', 24], ['匣里灭辰', 25],
            ['西风大剑', 26], ['绝弦', 27], ['祭礼弓', 28], ['雨裁', 29], ['弓藏', 30], ['西风秘典', 31], ['流浪乐章', 32], ['西风猎弓', 33],
            ['祭礼残章', 34], ['笛剑', 35], ['西风剑', 36], ['钟剑', 37], ['祭礼剑', 38], ['祭礼大剑', 39], ['昭心', 40], ['西风长枪', 41]]
    Four = pd.DataFrame(data, columns=['Name', 'K'])
    ChooseOne = random.randint(0, 40)
    # 废弃 len() != 0
    print("\033[35m4星\033[0m")
    print(Four.iloc[ChooseOne])


def FiveStarCard():
    data = [['角色（up）', 1], ['刻晴', 2], ['莫娜', 3], ['琴', 4], ['迪卢克', 5], ['七七', 6]]
    Five = pd.DataFrame(data, columns=['Name', 'K'])
    ChooseOne = random.randint(0, 5)
    print("\033[31m5星\033[0m")
    print(Five.iloc[ChooseOne])


while True:
    print('1.角色祈愿')
    print('2.武器祈愿（未做）')
    print('3.抽卡记录（未做）')
    print('4.退出')
    choice = int(input("请选择（数字）："))
    if choice in range(1, 5):  # 选择了1，2，3
        if choice == 1:  # 选择了1
            FourGuarantee = FourGuarantee + 1  # 4星保底+1次
            FiveGuarantee = FiveGuarantee + 1
            if FourGuarantee == 10 and not FiveGuarantee == 90:  # 如果4星保底了且非5星保底
                FourStarCard()  # 执行函数“FourStarCard()“
                FourGuarantee = 0  # 4星保底清零

            elif FiveGuarantee == 90:  # 如果5星保底了
                if FourGuarantee != 10:  # 同时不是4星保底
                    FiveStarCard()
                else:
                    FiveStarCard()
                    FourGuarantee = 9  # 将4星保底视为第9抽
                FiveGuarantee = 0

            else:  # 非保底
                DecidePersonCard()  # 执行函数“DecidePersonCard()”
            PersonFrequency = PersonFrequency + 1  # 抽卡次数+1次
            print('这是角色池第%d次抽卡' % PersonFrequency)

        elif choice == 2:  # 选择了2
            print('2.武器祈愿（未做）')

        elif choice == 3:  # 选择了3
            print('3.抽卡记录(目前不会做)')

        elif choice == 4:  # 选择了4
            sys.exit(0)  # 清屏

    else:
        choice = int(input("请重新输入"))  # 输入其他的数字
