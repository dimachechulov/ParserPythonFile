import math
class MyClass:
    def __init__(self, var1,var2,var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var3 * var2 - var1

    def MyMethod(self):
        return self.var1+self.var2

    def get_type(self):
        return type(self.var1 / self.var2)

def MyFunction(a):
    sum = 0
    for i in range(a):
        temp = i
        while True:
            if i % 2 == 0:
                continue
            else:
                sum = (sum >> 2) / (i * 3) ^ 23
                i = i+1
                if i == a:
                    break
        i = temp
    my_list = list()
    for i in range(10):
        my_list.append(i)
    try:
        for i in range(12):
            print(my_list[i])
    except:
        print("Index out of range!!")
    finally:
        pass

def f(x):
    return math.sin(x)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n

    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def calculate_integral(a, b, tolerance):
    n = 1

    integral_old = trapezoidal_rule(a, b, n)
    integral_new = trapezoidal_rule(a, b, 2 * n)
    while math.abs(integral_new - integral_old) > tolerance:
        n = 2
        integral_old = integral_new
        integral_new = trapezoidal_rule(a, b, 2*n)
    return integral_new

def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")


def Myfunc2_test_binary_oprs(param1, param2, param3):
    if param1 == param2:
        param3 = param3 >> 2
        param1 +=4
        param2 ^= param3
        var1 = param2 + param3- (param2 / param3)
        param2 **= 2
        param3 *= 4
        param2 |= var1
        var2 = param1 %(4 + param3-param2)
    else:
        var2 = list(range(20))
        var2[10]+=var2[11] / var2[12]


def MyFunc3_test_if(param2, param1):
    var1 = 10
    if True == False:
        print(5 == type(True))

        if 5 == 10:
            var1 = 7
            if 3 == 6:
                var1 = 7
                if param1 == param2:
                    pass
                elif True:
                    pass
                else:
                    param2 = 15
            else:
                param2 %= 1000
        else:
            pass



def MyFunc4_test_loops(list1, list2, dict1):
    i = 0
    i1 = 0
    var3 = list(range(len(list1)))
    for el1 in list1:
        for el2 in list2:
            var3[el2] = el2 ** 2 >> 2
            list1[dict1[el1]] = var3[15]
            while i < len(dict.items()):
                var3[i] = 12
                i += 1
        for el in range(20):
            if el == el1:
                pass
            else:
                pass
        while i1 < el1:
            var3[i1] = i1
            i1 = i1 + 2

def is_armstrong(number):
    order = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if number == sum:
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")
def MyFunc5_test_try(list1):
    try:
        for el in range(20):
            print(el)
            el+= (1 >> 4)
    except IndexError:
        print("IndexError")
    except FileExistsError:
        pass
    except:
        print("exception")
    finally:
        print("Finally")
        try:
            for i in range(30):
                i = i + 5
                list1[i]
        except:
            print("exception 2")

def generator():
    while True:
        data = input("Inter data: ")
        yield data

def open_file(file_path):
    text = "string"
    with open(file_path, 'r') as f:
        text= f.read()
    return text

def Mysum(*args):
    return sum(args)
def test_skobki(list1):
    var = (((list1[0] << list1[2] + list1[12]) * 15 + 14 / list1[16]) << 4 >> 2 << 6 ^ 4 | 34) ^ 12
    if ((True and False) or True and False) and (True or False):
        pass
def main():
    file_path = "file.txt"
    MyFunc3_test_if(10,20)
    MyFunc4_test_loops(list(), list(), dict())
    Myfunc2_test_binary_oprs(100,50,12)
    MyFunction(10)
    q = MyClass(4,3,2)
    q.get_type()
    open_file(file_path)
    items = generator()

    for i in range(5):
        print(next(items))
    a = 7
    print(MyFunction(a))
    a = 1
    b = 5
    tolerance = 1e-6

    result = calculate_integral(a, b, tolerance)
    print("Integral of sin(x) from 1 to 5:", result)

main()









