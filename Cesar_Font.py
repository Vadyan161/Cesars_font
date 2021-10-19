# put your python code here
def encode_en2(x):
    y = ''
    step = 0

    for k in range(len(x)):
        if x[k].isalpha():
            step += 1

    for i in range(len(x)):
        if x[i].isalpha():
            if x[i].isupper():
                if (ord(x[i]) + step) < 91:
                    y += chr(ord(x[i]) + step)
                else:
                    y += chr(ord(x[i]) + step - 26)
            else:
                if (ord(x[i]) + step) < 123:
                    y += chr(ord(x[i]) + step)
                else:
                    y += chr(ord(x[i]) + step - 26)
        else:
            y += x[i]
    return y


x = input().split()
k = []

for i in range(len(x)):
    k.append(str(encode_en2(x[i])))

print(*k)



