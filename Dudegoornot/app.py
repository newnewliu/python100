print(r'''

                                 __)),
                                //_ _)
                                ( "\"
                                 \_-/
                             ,---/  '---.
                            /     - -    \
                           /  \_. _|__,/  \
                          /  )\        )\_ \
                         / _/  (   '  ) /  /
                        / |     (_____) | /
                       /,'      /     \/ /,
                     _/(_      (   ._, )-'
                    `--,/      |____|__|
                               |    )  |
                               |   /   |
                               |  / \  |
                              / `|  | _)
                              |  |  |  |
                              |  /  \  |
                              | |    \ |
                              | \    | \_
                       gnv   /__(    '-._`,
''')
print("欢迎来到渣男go or not!")
print("我将帮助你决定一个dude的去留")
print("现在你碰到了一个南仁，你感觉这玩意真好啊。")
quality_1 = input("他好在哪呢？输入“气质”，“经济实力”，“学历”或者“不知道” ")
criminal = input("别急，问一下他是瓢虫、毒虫还是蠹虫？输入对应的称号或者na")

if criminal != "na":
    if quality_1 == "气质":
        print("气质球用不顶")
    elif quality_1 == "经济实力":
        print("钱球用不顶")
    elif quality_1 == "学历":
        print("学历球用不顶")
    elif quality_1 == "不知道":
        print("？？？神金病")

elif criminal == "na":
    if quality_1 == "气质" :
        education = input("是好学校吗？Y or N")
        if education != "N":
            print("上，但仍要观察人品各方面")
        else:
            print("转人工吧")
    elif quality_1 == "经济实力" :
        marriage = input("结婚了吗？")
        if marriage == "Y" or "y":
            print("也行，多搞点钱")
        else:
            print("可以，吃饭带上我谢谢")
    elif quality_1 == "学历":
        family = input("家里情况还好吗？")
        if family == "Y" or "y":
            appear = input("长得下得去嘴吗？")
            if appear == "Y" or "y":
                quality_2 = input("真诚敞亮吗？")
                if quality_2 == "Y" or "y":
                    mbti= input("是白羊射手或者n人吗？")
                    if mbti =="Y" or "y":
                        print("我是大学生介绍给我吧求你了求你了求你了求你了求你了求你了")
                    else:
                        print("冲！有合适的兄弟介绍给我谢谢")
                else:
                    print("有戏，转人工")
            elif input("有钱吗？") == "Y" or "y":
                print("行，吃好的带上我")
            elif input("有钱吗？") != "Y" or "y":
                print("丑到何种程度具体考察一下吧，转人工")
        elif input("长得惊为天人吗？")== "Y" or "y":
            print("也行，玩玩吧")
        elif input("长得惊为天人吗？") != "Y" or "y":
            print("哈？？转人工吧开始好奇了")

    elif quality_1 == "不知道":
        greencard = input("是不是有绿卡？")
        if greencard != "n":
            print("上上上")
        elif input("是不是在排卵期前后或者任何可能导致荷尔蒙波动的时期？") !="n":
            print("这段时间过了再思考")
        elif input("是不是在排卵期前后或者任何可能导致荷尔蒙波动的时期？") == "n":
            print("玩呢??")

elif criminal == "不知道":
    print("搞搞清楚不然球用不顶")

print("欢迎再次光临，转人工+v:zhaowoganma818")
