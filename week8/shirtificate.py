from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # 设置标题的字体：Helvetica, 粗体(B), 字号 45
        self.set_font("helvetica", "B", 45)
        # 打印一个单元格包含标题，宽度 0 (代表横跨整页)，高度 50，居中(C)对齐
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        # 换行，防止后面的内容覆盖到标题上
        self.ln(20)

def main():
    # 1. 获取用户输入的名字
    name = input("Name: ")
    
    # 2. 实例化我们自定义的 PDF 类
    pdf = PDF(orientation="portrait", format="a4")
    pdf.add_page()
    
    # 3. 关闭自动换页，防止因为排版靠下导致生成了多余的第二页空页
    pdf.set_auto_page_break(auto=False, margin=0)
    
    # 4. 插入 T 恤图片
    # A4 纸的总宽度是 210mm。
    # 如果我们将图片宽度设为 190mm，那么为了水平居中，左右边距应该是 (210 - 190) / 2 = 10mm
    pdf.image("week8\\image.png", x=10, y=70, w=190)
    
    # 5. 设置印在衣服上的文字样式
    # 字体大小设置得适中一点，以防名字太长
    pdf.set_font("helvetica", "B", 28)
    # 将文本颜色设置为白色 (RGB: 255, 255, 255)
    pdf.set_text_color(255, 255, 255)
    
    # 6. 将光标 Y 轴向下移动到衣服胸前的位置
    pdf.set_y(140)
    # 打印文字并居中
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    
    # 7. 输出并保存文件
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()