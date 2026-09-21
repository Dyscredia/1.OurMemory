print("数字炸弹游戏开始啦！请每轮输入一个数字，我将告诉你它与炸弹数的关系。看看你能多少轮猜出炸弹~\n我们的炸弹范围是(0,5]，且为整数。每轮猜测请输入不同数字~")
x = 3
M0 = input("请猜测：")
if M0 > x:
    print("太大啦！往小了猜")
    M1 = input("请猜测：")
    if M1 > x:
        print("太大啦！往小了猜")
        M11 = input("请猜测：")
        if M11 > x:
            print("太大啦！往小了猜")
            M111 = input("请猜测：")
            if M111 > x:
                print("太大啦！往小了猜")
                M1111 = input("请猜测：")
                if M1111 == x:
                    print("猜对啦！你真棒~")
                else:
                    print("你是小笨猪！")
            else:
                if M111 < x:
                    print("太小啦！往大了猜")
                    M1112 = input("请猜测：")
                    if M1112 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    print("猜对啦！你真棒~")
        else:
            if M11 < x:
                print("太小啦！往大了猜")
                M112 = input("请猜测：")
                if M112 > x:
                    print("太大啦！往小了猜")
                    M1121 = input("请猜测：")
                    if M1121 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M112 < x:
                        print("太小啦！往大了猜") 
                        M1122 = input("请猜测：") 
                        if M1122 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
               print("猜对啦！你真棒~")
    else:
        if M1 < x:
            print("太小啦！往大了猜")
            M12 = input("请猜测：")
            if M12 > x:
                print("太大啦！往小了猜")
                M121 = input("请猜测：")
                if M121 > x:
                    print("太大啦！往小了猜")
                    M1211 = input("请猜测：")
                    if M1211 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M121 < x:
                        print("太小啦！往大了猜")
                        M1212 = input("请猜测：")
                        if M1212 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
                if M12 < x:
                    print("太小啦！往大了猜")
                    M122 = input("请猜测：")
                    if M122 > x:
                        print("太大啦，往小了猜")
                        M1221 = input("请猜测：")
                        if M1221 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        if M122 < x:
                            print("太小啦！往大了猜")
                            M1222 = input("请猜测：")
                            if M1222 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    print("猜对啦！你真棒~")
        else:
            print("猜对啦！你真棒~")
else:
    if M0 < x:
        print("太小啦！往大了猜")
        M2 = input("请猜测：")
        if M2 > x:
            print("太大啦！往小了猜")
            M21 = input("请猜测：")
            if M21 > x:
                print("太大啦！往小了猜")
                M211 = input("请猜测：")
                if M211 > x:
                    print("太大啦！往小了猜")
                    M2111 = input("请猜测：")
                    if M2111 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M211 < x:
                        print("太小啦！往大了猜")
                        M2112 = input("请猜测：")
                        if M2112 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
                if M21 < x:
                    print("太小啦！往大了猜")
                    M212 = input("请猜测：")
                    if M212 > x:
                        print("太大啦！往小了猜")
                        M2121 = input("请猜测：")
                        if M2121 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        if M212 < x:
                            print("太小啦！往大了猜")
                            M2122 = input("请猜测：")
                            if M2122 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    print("猜对啦！你真棒~")
        else:
            if M2 < x:
                print("太小啦！往大了猜")
                M22 = input("请猜测：")
                if M22 > x:
                    print("太大啦！往小了猜")
                    M221 = input("请猜测：")
                    if M221 > x:
                        print("太大啦！往小了猜")
                        M2211 = input("请猜测：")
                        if M2211 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪")
                    else:
                        if M221 < x:
                            print("太小啦！往大了猜")
                            M2212 = input("请猜测：")
                            if M2212 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    if M22 < x:
                        print("太小啦！往大了猜")
                        M222 = input("请猜测：")
                        if M222 > x:
                            print("太大啦！往小了猜")
                            M2221 = input("请猜测：")
                            if M2221 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            if M222 < x:
                                print("太小啦！往大了猜")
                                M2222 = input("请猜测：")
                                if M2222 == x:
                                    print("猜对啦！你真棒~")
                                else:
                                    print("你是小笨猪！")
                            else:
                                print("猜对啦！你真棒~")
                    else:
                        print("猜对啦！你真棒~")
            else:
                print("猜对啦！你真棒~") 
    else:
        print("猜对啦！你真棒~")