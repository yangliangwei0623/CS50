# week 0

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