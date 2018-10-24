

nameMap = {}
option = 1
while option!=0 :
    option = int(input("**********************************\n"
          "***********  输入选项    **********\n"
          "1 新建名片\n"
          "2 查询全部\n"
          "3 查询名片\n\n\n"
          "0 退出\n"
          "**********************************\n"
          ))
    if option==0 :
        exit(0)
    elif option==1 :
        name = input("请输入姓名:")
        phoneNum = input("请输入手机:")
        weChat = input("请输入微信号:")
        nameMap[name]=phoneNum+"||"+weChat
    elif option == 2 :
        print("\t姓名         \t手机        \t微信号")
        for k in nameMap :
            values = nameMap[k].split("||")
            print("\t"+k+"      \t"+values[0]+"         \t"+values[1])
    elif option == 3 :
        queryName = input("请输入姓名:")
        print("\t姓名     \t手机        \t微信号")
        print("\t" + queryName + "      \t" + nameMap[queryName].split("||")[0] + "     \t" + nameMap[queryName].split("||")[1])
    else:
        print("输入有误请重新输入")
print(option)



