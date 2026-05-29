def convert(text):
    # 将 :) 替换为微小笑脸表情
    text = text.replace(":)", "🙂")
    # 将 :( 替换为微小伤心表情
    text = text.replace(":(", "🙁")
    # 返回替换后的字符串
    return text

def main():
    # 提示用户输入
    user_input = input()
    # 调用 convert 函数处理用户输入
    result = convert(user_input)
    # 打印处理后的结果
    print(result)

# 在文件最底部调用 main 函数来启动程序
main()