print()


def encode_rus(step, x):
    y = ''
    for i in range(len(x)):
        if x[i].isalpha():
            if x[i].isupper():
                if (ord(x[i]) + step) < 1072:
                    y += chr(ord(x[i]) + step)
                else:
                    y += chr(ord(x[i]) + step - 32)
            else:
                if (ord(x[i]) + step) < 1104:
                    y += chr(ord(x[i]) + step)
                else:
                    y += chr(ord(x[i]) + step - 32)
        else:
            y += x[i]
    print(y)


def decode_rus(step, x):
    y = ''
    for i in range(len(x)):
        if x[i].isalpha():
            if x[i].isupper():
                if (ord(x[i]) - step) > 1039:
                    y += chr(ord(x[i]) - step)
                else:
                    y += chr(ord(x[i]) - step + 32)
            else:
                if (ord(x[i]) - step) > 1071:
                    y += chr(ord(x[i]) - step)
                else:
                    y += chr(ord(x[i]) - step + 32)
        else:
            y += x[i]
    print(y)


def encode_en(step, x):
    y = ''
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
    print(y)


def decode_en(step, x):
    y = ''
    for i in range(len(x)):
        if x[i].isalpha():
            if x[i].isupper():
                if (ord(x[i]) - step) > 64:
                    y += chr(ord(x[i]) - step)
                else:
                    y += chr(ord(x[i]) - step + 26)
            else:
                if (ord(x[i]) - step) > 96:
                    y += chr(ord(x[i]) - step)
                else:
                    y += chr(ord(x[i]) - step + 26)
        else:
            y += x[i]
    print(y)


nap = input('Введите направление (шифрование или дешифрование):')
lan = input('Введите язык ввода (en, rus):')
x = input('Введите ваше сообщение:')

while True:
    step = int(input('Введите шаг сдвига:'))

    if nap.lower() == 'шифрование' or 'encode':
        if lan.lower() == 'rus':
            encode_rus(step, x)
        elif lan.lower() == 'en':
            encode_en(step, x)
        else:
            print('При выборе языка была допущена ошибка')
    elif nap.lower() == 'дешифрование' or 'decodeR':
        if lan.lower() == 'rus':
            decode_rus(step, x)
        elif lan.lower() == 'en':
            decode_en(step, x)
        else:
            print('При выборе языка была допущена ошибка')
    else:
        print('При выборе направления была допущена ошибка')

    m = input('Хотите изменить шаг сдвига?')
    if m.lower() == 'нет' or m.lower() == 'no':
        print("Спасибо, что воспользовались шифратором Цезаря!")
        break

