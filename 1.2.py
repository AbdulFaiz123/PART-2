def per(n):
    if len(str(n))==1:
        print(f'single{n}')
        return "done"
    digits =[int(i) for i in str(n)]

    res =0
    for j in digits:
        res+=j
    print(f"res={res}")
    per(res)
r = int(input("enter the number"))
per(r)