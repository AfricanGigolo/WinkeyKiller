# -*- coding:utf-8 -*-
import tkinter as tk
import keyboard
import webbrowser

disable_button = None
enable_button = None


def disable_win_key():
    keyboard.block_key("windows")
    enable_button.config(state=tk.NORMAL)
    disable_button.config(state=tk.DISABLED)


def enable_win_key():
    keyboard.unblock_key("windows")
    disable_button.config(state=tk.NORMAL)
    enable_button.config(state=tk.DISABLED)


def open_github_page(event):
    webbrowser.open("https://github.com/AfricanGigolo/WinkeyKiller")


# 调用Tk()创建主窗口
root_window = tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root_window.title('Windows按键屏蔽工具')

root_window.geometry('300x180')

root_window.update()

disable_button = tk.Button(root_window, width=20, text="屏蔽Windows键", command=disable_win_key)
enable_button = tk.Button(root_window, width=20, text="解除屏蔽", command=enable_win_key)

enable_button.config(state=tk.DISABLED)

disable_button.pack()
enable_button.pack()


tk.Label(root_window, text="请保持软件开启，可以最小化\n退出程序将会自动解除屏蔽\n\n作者：非洲小白脸(AfricanGigolo) MIT开源许可"
                           " \n献给热爱原神的玩家").pack()
label = tk.Label(root_window, fg="blue", text="https://github.com/AfricanGigolo/WinkeyKiller", cursor='hand2')
label.bind('<Button-1>', open_github_page)
label.pack()

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
