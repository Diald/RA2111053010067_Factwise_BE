def to_numbers(s):
    count = 0
    n = len(s)
    for ch in s:
        if(ch!=',' and ch!=' ' and ch!='and'):
            for i in range(len(ch)):
                count+=1
    return count
s = input()
print(to_numbers(s))