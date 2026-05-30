months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

while True:
    s = input("Date: ").strip()
    
   
    try:
        if "/" in s: # 使用 in 替代 count() > 0 更加直观
            m, d, y = s.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if m < 1 or m > 12 or d < 1 or d > 31:
                raise ValueError
            print(f"{y:04d}-{m:02d}-{d:02d}")
            break # 成功输出后，必须跳出循环
    except ValueError:
        pass
        
    try:
        if "," in s:
            m, d, y = s.split()
            m = m.strip(",")
            d = d.strip(",")
            y = y.strip(",")
            m = months.index(m) + 1
            d = int(d)
            y = int(y)
            if d < 1 or d > 31:
                raise ValueError
            print(f"{y:04d}-{m:02d}-{d:02d}")
            break # 成功输出后，必须跳出循环
    except ValueError:
        pass