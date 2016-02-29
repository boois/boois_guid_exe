# -*- coding: utf-8 -*-
import uuid
import win32clipboard as w
import win32con

while True:
    print u"boois-guid by 萧鸣 boois@qq.com v1.0"
    print u"请敲回车默认为32位无横线guid,'c u 32 -' c=拷贝到剪切板;u=大写;32=长度;-=带横线;可随意排列"
    inp_str = raw_input(">")
    is_hen = False
    length = 32
    is_upper = False
    is_clipb = False
    if inp_str.find("c")!=-1:
        is_clipb = True
        inp_str = inp_str.replace("c","")

    if inp_str.find("u")!=-1:
        is_upper = True
        inp_str = inp_str.replace("u","")

    if inp_str.find("-")!=-1:
        is_hen = True
        inp_str = inp_str.replace("-","")

    inp_str = inp_str.strip()
    #print inp_str
    if inp_str.isdigit():
        length = int(inp_str)
        if length<0:
            length = 0
        if length > 36:
            length = 36
    else:
        length = 32

    if not is_hen and length>32:
        length = 32

    uid = uuid.uuid4().__str__()
    if not is_hen:
        uid = uid.replace("-","")
    uid = uid[:length]
    uid = uid.upper() if is_upper else uid
    if is_clipb:
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, uid)
        w.CloseClipboard()
        print u"您开启了黏贴板,下面的guid已复制到您的黏贴板"
    print uid

