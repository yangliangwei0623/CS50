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