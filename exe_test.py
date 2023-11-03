import tkinter

# 画面作成
tki = tkinter.Tk()
tki.geometry('800x600')
tki.title('test_GUI')

# ボタンの作成
btn = tkinter.Button(tki, text='click', font=('arial', 50))
btn.place(x=300, y=200)

# 画面表示
tki.mainloop()