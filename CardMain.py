def show_content():
    print("*"*50)
    print("指令 1新建名片  2查看名片  3查找名片  0退出")
    print("*"*50)

def new_card():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    email = input("请输入email：")
    dic = {'name':name,
           'phone':phone,
           'email':email}
    card_list.append(dic)

def show_all_card():
    print("姓名\t\t电话\t\temail");
    print("=" * 50)
    for card in card_list:
        print("%s\t\t%s\t\t%s"%(card["name"],card["phone"],card["email"]))

def find_card():
    find_name = input("请输入查找的姓名：")
    for card in card_list:
        if(find_name == card["name"]):
            print("姓名\t\t电话\t\temail");
            print("%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["email"]))
            print("指令 1修改名片  2删除名片  0退出")
            findCMD = input("请输入指令：");
            if findCMD == "1":
                xname = input("姓名：")
                xphone = input("电话：")
                xemail = input("email：")
                card["name"] = xname;
                card["phone"] = xphone;
                card["xemail"] = xemail;
            elif findCMD == "2":
                print("已删除名片：%s"%card)
                card_list.remove(card);
            return ;
    else:
        print("没找到对应的名片")

def handle_input_cmd():
    cmd = input("请输入对应指令: ");
    if cmd == "1":
        # print("新建名片cmd")
        new_card()
    elif cmd == "2":
        # print("查看名片cmd")
        show_all_card()
    elif cmd == "3":
       find_card()
    elif cmd == "0":
        exit();
        return ;


# 名片列表
card_list = [];
show_content()
while True:
    handle_input_cmd();


