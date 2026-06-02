# Functions, Variables

**print函数**

- looking at this documentation, you’ll learn that the `print` function automatically includes the argument `end='\n'`. This `\n` indicates that the `print` function will automatically create a line break when run. The function takes an argument called `end`, and the default is to create a new line.

- However, we can technically provide an argument for `end` ourselves such that a new line is not created!

- We can modify our code as follows:

  ```python
  # Ask the user for their name
  name = input("What's your name? ")
  print("hello,", end="")
  print(name)
  ```

```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")# {}中的内容是一个变量，加上f在前面就会输出变量的值
```



**function**

```python
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
```

Notice that everything under `def hello()` is indented. Python is an indented language. It uses indentation to understand what is part of the above function. Therefore, everything in the `hello` function must be indented. When something is not indented, it treats it as if it is not inside the `hello` function.

# Conditionals

nothing new

# Loops

**for loops**

A `for` loop iterates through a `list` of items.

```python
for i in [0, 1, 2]:
    print("meow")
```

```python
for i in range(3):
    print("meow")
```


Our code can be further improved. Notice how we never use `i` explicitly in our code. That is, while Python needs the `i` as a place to store the number of the iteration of the loop, we never use it for any other purpose. **In Python, if such a variable does not have any other significance in our code, we can simply represent this variable as a single underscore `_`**. Therefore, you can modify your code as follows:

```python
for _ in range(3):
    print("meow")
```

- 
  Our code can be further improved. To stretch your mind to the possibilities within Python, consider the following code:

  ```python
  print("meow" * 3)
  ```

  Notice how it will meow three times, but the program will produce `meowmeowmeow` as the result. Consider: How could you create a line break at the end of each meow?

- 

  Indeed, you can edit your code as follows:

  ```python
  print("meow\n" * 3, end="")
  ```

  Notice how this code produces three meows, each on a separate line. By adding `end=""` and the `\n` we tell the interpreter to add a line break at the end of each meow.

**list**

`list` 实际上是一个**动态长度的泛型指针数组**

**dictionaries**

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
```

```python
#students is a list,the element is dict
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

# Exceptions

For best practice, we should only `try` the fewest lines of code possible that we are concerned could fail. 

```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")#如果有任何异常的话都不会执行这条语句
```

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass#使用pass可以不传递任何信息
main()
```

# Libraries

**使用uv代替pip**

pip install uv

```bash
uv pip install requests
Resolved 5 packages in 12ms
Prepared 5 packages in 0.45ms
Installed 5 packages in 8ms
 + certifi==2024.8.30
 + charset-normalizer==3.4.0
 + idna==3.10
 + requests==2.32.3
 + urllib3==2.2.3
```

**json**

The format in the downloaded text file is called JSON, a text-based format that is used to exchange text-based data between applications. 

json格式

 对象（Object）

- 表现形式：用一对花括号 `{}` 包裹。
- 结构：里面是一系列“键值对”（Key-Value pairs）。
- 规则：键（Key）和值（Value）之间用冒号 `:` 分隔，不同的键值对之间用逗号 `,` 分隔。
- *类比*：相当于 Python 中的字典（Dictionary）。

2. 数组（Array）

- 表现形式：用一对中括号 `[]` 包裹。
- 结构：里面是有序的值的集合。
- 规则：不同的值之间用逗号 `,` 分隔。
- *类比*：相当于 Python 中的列表（List）。

```json
{
  "name": "Alice",
  "age": 28,
  "isEmployed": true,
  "manager": null,
  "skills": [
    "Python",
    "JavaScript",
    "System Design"
  ],
  "address": {
    "city": "Shanghai",
    "street": "123 Tech Road",
    "zipCode": "200000"
  }
}
```

# Unit Tests

pytest的使用

# Object-Oriented Programming

**tuple and list**

A `tuple` is a sequence of values. Unlike a `list`, a `tuple` can’t be modified.可用[]访问

```python
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"#tuple is immutable
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house#return [name, house]，this is a list，also can be visitied by []


if __name__ == "__main__":
    main()
    
```

**dict**

```python
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}#Notice we can utilize {} braces in the return statement to create the dictionary and return it all in the same line.


if __name__ == "__main__":
    main()
```

**classes**

```python
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
```

可以在**运行时**随时为一个对象甚至一个类动态地添加、修改或删除属性和方法

```python
def __str__(self):
    #欲将对象字符串化需要写明的函数
```



**raise**

```python
class Student:
    def __init__(self, name, house):
        try:
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
        except ValueError as e:
            print(e)
            exit(1)   


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

**Decorators**

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property#getter 函数命名成什么，外部使用者就必须用什么名字来访问它。
    def name(self):
        return self._name#在setter和getter对数据进行操作都要带下划线，其他地方用不带下划线的，这样在其他地方的set和get就可以经过相关逻辑校验

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
    
#Notice how we’ve written @property above a function called house. Doing so defines house as a property of our class. With house as a property, we gain the ability to define how some attribute of our class, _house, should be set and retrieved. Indeed, we can now define a function called a “setter”, via @house.setter, which will be called whenever the house property is set—for example, with student.house = "Gryffindor". Here, we’ve made our setter validate values of house for us. Notice how we raise a ValueError if the value of house is not any of the Harry Potter houses, otherwise, we’ll use house to update the value of _house. Why _house and not house? house is a property of our class, with functions via which a user attempts to set our class attribute. _house is that class attribute itself. The leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. _house should only be set through the house setter. Notice how the house property simply returns that value of _house, our class attribute that has presumably been validated using our house setter. When a user calls student.house, they’re getting the value of _house through our house “getter”.
```

**Class Methods**

```python
#ometimes, we want to add functionality to a class itself, not to instances of that class.
#@classmethod is a function that we can use to add functionality to a class as a whole.
import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
#otice how the __init__ method is removed because we don’t need to instantiate a hat anywhere in our code. self, therefore, is no longer relevant and is removed. We specify this sort as a @classmethod, replacing self with cls. Finally, notice how Hat is capitalized by convention near the end of this code, because this is the name of our class.
```

**Inheritance**

```python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...
```

**Operator Overloading**

e.g. 在类中重写`__add__`函数就可以重载+，其他类似，需要使用时可查阅

# Et cetera

**if name == "main":**

```python
def my_main_logic():
    print("Hello Python")

# 这才是一个“开关”
if __name__ == "__main__":
    my_main_logic()
    
#直接运行文件时，Python 解释器会在后台悄悄把一个内置变量 __name__ 赋值为字符串 "__main__"。此时 if 条件成立
#你的主逻辑被执行从另一个文件中 import 这个文件时，Python 依然会从上到下读取该文件，但此时 __name__ 的值会被设为该文件的文件名（例如 "calculator"）。此时 if 条件不成立，主逻辑不会被意外触发，仅仅是加载了里面的函数和类供你使用。
```

**with**

```python
#核心作用是自动管理资源（也被称为“上下文管理器”），确保在你用完某个资源后，系统能自动帮你做好“善后清理”工作，即使中间程序报错崩溃了也不例外。
file = open("data.txt", "w")
file.write("hello world")
file.close() # 必须手动关闭文件！
with open("data.txt", "w") as file:
    file.write("hello world")
# 只要缩进结束（离开 with 块），文件就会自动被安全关闭！

任何可以使用 with 关键字调用的对象，都必须实现上下文管理协议。该协议要求对象在内部定义两个魔术方法（Magic Methods）：

__enter__(self)：在进入 with 代码块之前被调用。它的主要任务是分配或获取资源，并将其返回。返回的值会被绑定到 as 后面的变量上（如果有的话）。

__exit__(self, exc_type, exc_val, exc_tb)：在离开 with 代码块时（无论是因为代码正常执行完毕，还是因为抛出了异常）被严格调用。它的主要任务是执行清理工作（如关闭文件、释放锁、断开连接等）。如果代码块内发生异常，这三个参数将分别接收异常的类型、值和追踪栈（Traceback）；如果 __exit__ 返回 True，则异常会被吞噬（抑制），否则异常将继续向上抛出。

```

**包**

文件夹下面有一个名为

```python
__init__.py(__是 _ _)
```

该文件夹便被声明为包

模块与包

1. **模块 (Module)：最小的独立单位** 本质上就是一个单独的 `.py` 文件。里面包含了 Python 的函数、类和变量定义。它是代码重用的最基础单元。
2. **包 (Package)：文件系统的目录结构** 本质上是一个包含了多个模块（`.py` 文件）的**文件夹**。为了让 Python 将这个普通的文件夹识别为一个“包”，文件夹内部通常需要包含一个特殊的 `__init__.py` 文件。

**包 (Package) 的核心作用**

随着代码量的增加，把所有功能都塞进一个 `.py` 文件（模块）是不现实的。我们必须将代码拆分到不同的文件夹中，这就催生了“包”的作用：

- **隔离命名空间（避免命名冲突）** 这是包最关键的作用。在大型项目中，不同的开发者可能会创建同名的文件（比如大家都喜欢用 `utils.py` 或 `config.py`）。如果没有包，这些同名模块就会互相覆盖。有了包结构之后，`network_pkg.utils` 和 `database_pkg.utils` 就是两个完全独立的东西，井水不犯河水。
- **组织与层级化代码** 就像你在电脑上用文件夹整理照片和文档一样，包允许你按照业务逻辑或功能模块将代码分门别类。通过点号 (`.`) 来访问，例如 `from app.models.user import User`，这种层级结构让项目的架构一目了然，极大地提升了可维护性。
- **集中处理初始化逻辑** 当一个包被导入时，它目录下的 `__init__.py` 文件会自动执行。你可以利用这个特性在 `__init__.py` 中编写初始化代码（例如建立数据库连接、加载配置文件）。
- **控制暴露的接口** 在 `__init__.py` 中，你可以通过定义特殊的 `__all__` 变量，来精确控制当外部使用者执行 `from your_package import *` 时，到底哪些子模块会被公开出去，从而将内部的实现细节隐藏起来。

**set**

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])#Notice how no checking needs to be included to ensure there are no duplicates. The set object takes care of this for us automatically.

for house in sorted(houses):
    print(house)
```

**Global Variables**

尽量少使用global variables，用类来代替（封装与其相关的操作）,用的话注意在函数内部对全局变量再赋值时，需要加上global xxx.

```python
balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance#不加会报错
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
```

**Constants**

Constants are typically denoted by capital variable names and are placed at the top of our code. Though this *looks* like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code! Instead, you’re on the honor system: if a variable name is written in all caps, just don’t change it!

**type hints**

python不进行隐式转换，遇到类型不匹配会直接报告Type Error（但是是动态类型，即允许变量的类型在执行过程中发生改变，给变量赋什么类型的值它就是什么类型）

可以用下面这样的方式表明类型，然后通过`mypy`来检查（对执行没有任何影响）

```python
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
```

**Docstrings**（文档字符串）

```python
def meow(n):
    """Meow n times."""
    return "meow\n" * n

"""
它和普通的 # 注释有什么区别？ 普通的 # 注释主要是给写代码的人看的，Python 运行代码时会直接忽略它。而 Docstring 是附着在函数上的官方说明，Python 会把它当作函数的一个特殊属性（__doc__）保留下来。当你在集成开发环境（IDE，比如 VS Code 或 PyCharm）中将鼠标悬停在 meow 函数上时，IDE 就会弹出 "Meow n times." 这个提示。
"""

(reStructuredText (reST) / Sphinx 风格,可通过Sphinx工具一键生成文档)
"""
Meow n times.  <-- 第一行：用一句话简述函数的作用。

:param n: Number of times to meow  <-- 【参数描述】告诉读者参数 n 代表什么（喵的次数）。
:type n: int                       <-- 【参数类型】规定参数 n 必须是一个整数（integer）。
:raise TypeError: If n is not an int <-- 【异常说明】警告使用者：如果传进来的 n 不是整数，函数会抛出 TypeError 错误。
:return: A string of n meows, one per line <-- 【返回值描述】说明函数最终会输出什么（返回包含 n 个 meow 的字符串，每行一个）。
:rtype: str                        <-- 【返回值类型】规定返回的结果是一个字符串（string）。
"""
```

**unpacking**

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")



def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")#字典中的key值要和参数名相对应，顺序无所谓
```

**args and kwargs**

- `args` are positional arguments, such as those we provide to print like `print("Hello", "World")`.
- `kwargs` are named arguments, or “keyword arguments”, such as those we provide to print like `print(end="")`.

```python
def f(*args, **kwargs):# *在这里相当于打包符,args存储为列表，kwargs存储为字典
    print("Positional:", args)

f(100, 50, 25)#输出100,50,25
```

```python
def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)#输出  Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}
```

**map**

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    """
    Notice how map takes two arguments. First, it takes a function we want applied to every element of a list. Second, it takes that list itself, to which we’ll apply the aforementioned function. Hence, all words in words will be handed to the str.upper function and returned to uppercased.
    """
    print(*uppercased)


if __name__ == "__main__":
    main()
```

**List Comprehensions**

list comprehensions allow you to create a list on the fly in one elegant one-liner.

```python
squares = [i * i for i in range(10)]
print(squares)  # [ 表达式（函数） for 变量 in 可迭代对象 ]
```

```python
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]，[ 表达式 for 变量 in 可迭代对象 if 筛选条件 ]
```

**filter**

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
```



lambda 参数: 返回值表达式（lambda表达式格式）

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)#filter can also use lambda functions

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
```

**Generators and Iterators**

```python
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i #先算出一个结果交给你，然后在这里按暂停，等下次来要的时候，我再接着往下算。”（避免一次要算太多导致内内存爆满，无论你要 10 只羊还是 10 亿只羊，使用 yield 的生成器在任何时刻，内存中永远只有当前这一只羊的数据。这种机制在计算机科学中被称为 “惰性求值 / 延迟计算” (Lazy Evaluation)。）

if __name__ == "__main__":
    main()
"""
for 循环向 sheep 索要第 1 只羊。

sheep 运行到 yield，交出第 1 只羊，并原地暂停。

main 函数收到并 print 打印在屏幕上。此时，第 1 只羊的数据就被内存丢弃了。

for 循环向 sheep 索要第 2 只羊。

sheep 解除暂停，继续循环，交出第 2 只羊，再次暂停。
"""
```

