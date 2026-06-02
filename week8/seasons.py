from datetime import date
import sys
import inflect

def main():
    dob = input("Date of Birth: ")
    try:
        # 尝试将输入的字符串解析为 ISO 标准的日期格式
        birth_date = date.fromisoformat(dob)
    except ValueError:
        # 如果格式错误或日期无效，干净地退出
        sys.exit("Invalid date")

    # 获取今天的日期
    today_date = date.today()
    
    # 打印最终结果
    print(get_minutes(birth_date, today_date))

def get_minutes(birth_date, today_date):
    """
    计算两个日期之间相差的分钟数，并返回格式化后的英文字符串。
    """
    # 实例化 inflect 引擎
    p = inflect.engine()
    
    # 日期对象相减会返回一个 timedelta 对象
    delta = today_date - birth_date
    
    # 计算总分钟数 (总天数 * 24小时 * 60分钟)
    total_minutes = delta.days * 24 * 60
    
    # 使用 inflect 将数字转为单词，设置 andword="" 移除单词间的 "and"
    words = p.number_to_words(total_minutes, andword="")
    
    # 将首字母大写并加上 " minutes" 后缀
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()