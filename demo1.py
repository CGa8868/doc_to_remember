import pyautogui
import time

# 打开 Markdown 软件
# 这里假设你的 Markdown 软件是在桌面上的一个图标，使用 pyautogui 来模拟双击图标的操作
pyautogui.doubleClick(x=100, y=100)  # 替换 (x, y) 为你软件图标的位置

# 等待软件打开
time.sleep(5)

# 模拟点击文件按钮
pyautogui.click(x=200, y=200)  # 替换 (x, y) 为文件按钮的位置

# 等待文件菜单出现
time.sleep(2)

# 模拟点击打开按钮
pyautogui.click(x=300, y=300)  # 替换 (x, y) 为打开按钮的位置

# 等待打开文件对话框出现
time.sleep(2)

# 输入文件路径并按下回车键
pyautogui.write('G:\\file\\DESKTOP\\demo的演讲2.md')
pyautogui.press('enter')

# 等待文件加载
time.sleep(5)

# 在文档中添加内容
pyautogui.write('123')

# 等待一段时间
time.sleep(5)

# 模拟点击保存按钮
pyautogui.click(x=400, y=400)  # 替换 (x, y) 为保存按钮的位置