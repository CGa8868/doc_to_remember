import pyautogui
import time


def click_until_found(image, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            pyautogui.click(x, y)
            return True
        except Exception as e:
            print("未找到图像:", e)
            time.sleep(1)
    return False


try:
    # 打开 Markdown 软件
    pyautogui.press('win')
    pyautogui.write('Markdown软件的名称')
    pyautogui.press('enter')
    time.sleep(5)  # 等待软件打开

    # 模拟点击文件按钮
    if click_until_found('file_button.png'):
        # 等待文件菜单出现
        time.sleep(2)

        # 模拟点击打开按钮
        if click_until_found('open_button.png'):
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
            if click_until_found('save_button.png'):
                print("保存成功")
            else:
                print("保存按钮未找到")
        else:
            print("打开按钮未找到")
    else:
        print("文件按钮未找到")
except Exception as e:
    print("发生错误:", e)