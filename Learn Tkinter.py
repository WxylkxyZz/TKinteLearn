# # Label
# # 1. 实例化一个Obj，建立窗口window
# window = tk.Tk()
# # 2. 给窗口起名字
# window.title("label learn")
# # 3. 设定窗口大小(长x宽) 这里的乘是小x
# window.geometry('300x300')
# # 4. 给图形界面设定标签
# l1 = tk.Label(window, text="打标签", bg='blue', fg='red', font=('Arial', 12), width=10, height=2)
# # bg:背景，bg:字体颜色，font:字体，width:长，height:高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# # 5. 放置标签
# l1.pack()
# # Label内容content区域放置位置，自动调节尺寸. 放置lable的方法有：1）l.pack(); 2)l.place();
# # 6. 主窗口循环显示
# window.mainloop()
# # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。


# # Button
# window = tk.Tk()
# window.title("button learn")
# window.geometry('300x300')
# var = tk.StringVar()
# # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# l1 = tk.Label(window, textvariable=var, bg='green', fg='red', font=("Arial", 12), width=30, height=2)
# l1.pack()
# # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
# on_hit = False
#
#
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
#
#
# b = tk.Button(window, text="hit me", font=("Arial", 12), width=30, height=2, command=hit_me)
# b.pack()
#
# window.mainloop()


# # Entry
#
# window = tk.Tk()
# window.title("Entry learn")
# window.geometry('300x300')
#
# lambda_login = tk.Label(window, text='模拟登录', width=20, height=1)
# lambda_login.pack()
# # 在图形界面上设定输入框控件entry并放置控件
# account = tk.Entry(window, show=None, font=("Arial", 12))  # show设为None显示成明文形式
# account.pack()
# password = tk.Entry(window, show='*', font=("Arial", 12))
# password.pack()
#
#
# def check_button():
#     """
#     当登录按钮被点击时触发此函数
#     :return:
#     """
#     name = account.get()
#     pwd = password.get()
#     msg = f'用户名:{name}\n密码:{pwd}'
#     messagebox.showinfo(title='登录提示', message=msg)
#
#
# button = tk.Button(window, text='登录', width=15, height='2', command=check_button)
# button.pack()
#
# window.mainloop()


# # Text
#
# window = tk.Tk()
# window.title("Text learn")
# window.geometry("300x300")
# e = tk.Entry(window, show=None)
# e.pack()
#
#
# def insert_point():
#     var = e.get()
#     t.insert("insert", var)
#
#
# def insert_end():
#     var = e.get()
#     t.insert("end", var)
#
#
# b1 = tk.Button(window, text="insert point", width=10, height=2, command=insert_point)
# b1.pack()
# b2 = tk.Button(window, text="insert end", width=10, height=2, command=insert_point)
# b2.pack()
#
# t = tk.Text(window, height=3)
# t.pack()
#
# window.mainloop()


# # ListBox
# window = tk.Tk()
# window.title("ListBox learn")
# window.geometry("300x300")
#
# list_items = tk.StringVar()
# list_items.set(('python', 'Jave', 'C语言'))
#
# lb = tk.Listbox(window, listvariable=list_items)
# lb.pack()
#
# no_select = "没有选中任何选项"
#
#
# def check_button():
#     select = lb.curselection()  # 获取被选中的可选项的索引
#     print(len(select))
#     if len(select) == 0:
#         label_text.set(no_select)
#     else:
#         text = lb.get(select)
#         label_text.set(f"你已选择{text}")
#
#
# button = tk.Button(window, text="显示所选", width='15', height=1, command=check_button)
# button.pack()
#
# label_text = tk.StringVar()
# label_text.set(no_select)
# label = tk.Label(window, width=15, height=2, textvariable=label_text)
# label.pack()
#
# window.mainloop()


# # RadioButton
# window = tk.Tk()
# window.title("RadoiButton Learn")
# window.geometry("300x300")
#
# var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起
# label = tk.Label(window, width=15, height=2, bg='green', text="")
# label.pack()
#
#
# def select():
#     label.config(text=f"你选择了{var.get()}")
#
#
# r1 = tk.Radiobutton(window, text='Python', variable=var, value='python', command=select)
# r1.pack()
#
# r2 = tk.Radiobutton(window, text='Java', variable=var, value='Java', command=select)
# r2.pack()
#
# r3 = tk.Radiobutton(window, text='C语言', variable=var, value='C语言', command=select)
# r3.pack()
#
# window.mainloop()


# # CheckButton
# window = tk.Tk()
# window.title("CheckButton Learn")
# window.geometry("300x300")
#
# label = tk.Label(window, width=30, height=2, bg='green', text='')
# label.pack()
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# var3 = tk.IntVar()
#
#
# def select():
#     select_list = []
#     if var1.get() == 1:
#         select_list.append('Python')
#     if var2.get() == 1:
#         select_list.append('Java')
#     if var3.get() == 1:
#         select_list.append('C语言')
#
#     text = f"你选择了{','.join(select_list)}"
#     label.config(text=text)
#
#
# c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=select)
# c2 = tk.Checkbutton(window, text='Java', variable=var2, onvalue=1, offvalue=0, command=select)
# c3 = tk.Checkbutton(window, text='C语言', variable=var3, onvalue=1, offvalue=0, command=select)
# c1.pack()
# c2.pack()
# c3.pack()
# window.mainloop()


# # Scale
# window = tk.Tk()
# window.title("Scale Learn")
# window.geometry('300x300')
#
# label = tk.Label(window, width=20, height=2, bg='green', text="请滑动选择🙂")
# label.pack()
#
#
# def select(var):
#     label.config(text=f'你选择的是{var}')
#
#
# scale = tk.Scale(window, label="可选范围", from_=0, to=10, orient=tk.HORIZONTAL, length=400, tickinterval=2,
#                  resolution=0.1, command=select)
# # 从0到10,刻度为2，orient设置横向显示，length长度
# scale.pack()
# window.mainloop()


# Canvas
# window = tk.Tk()
# window.title("Canvas Learn 1")
# window.geometry("500x400")
#
# canvas = tk.Canvas(window, bg='pink', height=300, width=150)
# canvas.pack()
# line = canvas.create_line(0, 0, 150, 300)
# window.mainloop()

# window = tk.Tk()
# window.title("Canvas Learn 2")
# window.geometry("500x400")
# canvas = tk.Canvas(window, bg='pink', height=300, width=200)
# canvas.pack()
# oval = canvas.create_oval(75, 75, 150, 150, fill='red')
# rect = canvas.create_rectangle(75, 175, 125, 250, fill='Purple')
# window.mainloop()

# window = tk.Tk()
# window.title("Canvas Learn 3")
# window.geometry("500x400")
# canvas = tk.Canvas(window, width=300, height=300, bg='pink')
# canvas.pack()
# oval = canvas.create_oval(100, 100, 150, 150, fill='Purple')
#
#
# def movie():
#     canvas.move(oval, 50, 25)
#
#
# button = tk.Button(window, text="点此移动⚪", command=movie)
# button.pack()
# window.mainloop()
#
# window = tk.Tk()
# window.title("Canvas Learn 4")
# window.geometry("600x400")
#
# canvas = tk.Canvas(window, height=330, width=510, bg="pink")
# canvas.pack()
# image_file = ImageTk.PhotoImage(file='./8a81ecd8fdd266b3221da325875c0ea8.gif')
# image = canvas.create_image(10, 10, anchor='nw', image=image_file)
# window.mainloop()


# # Menu
#
# window = tk.Tk()
# window.title("Menu Learn")
# window.geometry("600x400")
# label = tk.Label(window, text='$', height='300', width='400', bg='pink')
# label.pack()
#
# counter = 0
#
#
# def do_job():
#     global counter
#     label.config(text=f"do -> {str(counter)}")
#     counter += 1
#
#
# menubar = tk.Menu(window)  # 先创建菜单栏！
#
# # 已经创建好了菜单栏！ 开始填充
#
# # 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项） 此时menubar是画板
# file_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New', command=do_job)
# file_menu.add_command(label='Open', command=do_job)
# file_menu.add_command(label='Save', command=do_job)
# # 添加一条分割线
# file_menu.add_separator()
# file_menu.add_command(label='Exit', command=window.quit())  # 用tkinter里面自带的quit()函数
#
# # 创建Edit菜单项
# edit_menu = tk.Menu(menubar, tearoff=0)  # 此时menubar是画板
# menubar.add_cascade(label='Edit', menu=edit_menu)
# edit_menu.add_command(label='Cut', command=do_job)
# edit_menu.add_command(label='Copy', command=do_job)
# edit_menu.add_command(label='Paste', command=do_job)
#
# # 创建二级菜单 此处想象画板 此时画板成了一级菜单
# submenu = tk.Menu(file_menu, tearoff=0)
# file_menu.add_cascade(label='Import', menu=submenu, underline=0)
# submenu.add_command(label='Submenu_1', command=do_job)
#
# # 创建菜单栏完成后，配置让菜单栏menubar显示出来
# window.config(menu=menubar)
# # 主窗口循环显示
# window.mainloop()

# # Frame
# window = tk.Tk()
# window.title('Frame Learn')
# window.geometry('300x300')
# # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成!!!
# tk.Label(window, bg='pink', text='On the window', font=('Arial', 16)).pack()
#
# frame = tk.Frame(window)
# frame.pack()
# # 此刻以frame为画板
# frame_l = tk.Frame(frame)
# frame_r = tk.Frame(frame)
# frame_l.pack(side='left')
# frame_r.pack(side='right')
#
# # 创建三组标签
# tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
# tk.Label(frame_r, text='on the frame_r1', bg='red').pack()
# tk.Label(frame_r, text='on the frame_r2', bg='red').pack()
# tk.Label(frame_r, text='on the frame_r3', bg='red').pack()
#
# window.mainloop()


# Messagebox

# window = tk.Tk()
# window.title("Messagebox Learn")
# window.geometry("600x400")
#
#
# def hit():
#     # tk.messagebox.showinfo(title='Info', message='show Info : \nxxx')
#     # tk.messagebox.showinfo(title='Warn', message='show Warn : \nxxx')
#     # tk.messagebox.showinfo(title='Error', message='show Error: \nxxx')
#     tk.messagebox.askyesno(title='Ask question', message='傻子!')
#     tk.messagebox.askyesno(title='Yes or No', message='you are bendan')
#     tk.messagebox.askokcancel(title='True or False', message='you are bendan')
#
#
# button = tk.Button(window, text='try hit me', bg='pink', command=hit)
# button.pack()
# window.mainloop()


# pack/grid/place
# window = tk.Tk()
# window.title("pgp Learn")
# window.geometry("600x400")
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
# window.mainloop()

# tk.Label(window, text='N', fg='pink', font=('Arial', 20)).pack(side='top')
# tk.Label(window, text='S', fg='pink', font=('Arial', 20)).pack(side='bottom')
# tk.Label(window, text='W', fg='pink', font=('Arial', 20)).pack(side='left')
# tk.Label(window, text='E', fg='pink', font=('Arial', 20)).pack(side='right')
# window.mainloop()
#
# tk.Label(window, text='Place', fg='pink', font=('Arial', 20)).place(x=50, y=50, anchor='nw')
# window.mainloop()
