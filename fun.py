def sum (ls:list):
    add = 0
    for i in ls:
        add += i
    return add

def avg(ls:list):
    add = 0
    for i in ls:
        add += i
    return add//(len(ls))

def palindrome(ls):
    if type(ls)==int:
        ls = str(ls)
    if ls == ls[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
