

def comp(txt1, txt2):
    t1 = len(txt1)
    t2 = len(txt2)
    print(t1, t2)
    if t1 == t2:
        print('true')
        return True
    else:
        print('false')
        return False


comp("hello", "fellow")


def profitable_gamble(prob, prize, pay):
    net = prob*prize-pay
    if net > 0:
        print('from PG fn:', net, 'true')
        return True
    else:
        print('from else in PG fn:', net, 'false')
        return False


profitable_gamble(.5, 20, 3)


def difference_max_min(lst):
    diff = max(lst)-min(lst)
    return diff


def is_last_character_n(word):
    if word[-1] == "n":
        return True
    else:
        return False


print(is_last_character_n("loging"))


def convert(hours, minutes):
    hr_sec = hours*60*60
    mn_sec = minutes*60
    total = hr_sec + mn_sec
    return total


def get_container(product):
    matches = {
        "Bread": "bag",
        "Milk": "bottle",
        "Beer": "bottle",
        "Eggs": "carton",
        "Cerials": "box",
        "Candy": "plastic",
        "Cheese": None
    }
    return matches[product]


def num_to_dashes(num):
    print('-'*num)
    return "-"*num


num_to_dashes(24)


def is_empty(s):
    if len(s) > 0:
        return True
    else:
        return False


def check_equality(a, b):
    if type(a) == type(b) and a == b:
        return True
    else:
        return False


print(check_equality(1, 1))
print(check_equality("can", "can"))

print(check_equality(1, "1"))
print(check_equality(1, 3))
