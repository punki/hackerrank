import queue as queue

# T = int(input())
T = 1


def smaller_tuple(x, y):
    for i in range(len(x)):
        if x[i] < y[i]:
            return True
    return False


def all_elements_are_equal(t):
    first = t[0]
    for x in t:
        if x != first:
            return False
    return True


def generate_new_elements(element):
    new_es = []
    # add one
    new_es.extend(add_chocolate(element, -1))
    # add two
    new_es.extend(add_chocolate(element, -2))
    # add five
    new_es.extend(add_chocolate(element, -5))
    return new_es


def add_chocolate(element, number):
    new_es = []
    for i in range(len(element)):
        left = [x + number for x in element[:i]]
        center = element[i]
        right = [x + number for x in element[i + 1:]]
        t_array = []
        t_array.extend(left)
        t_array.append(center)
        t_array.extend(right)
        new_es.append(tuple(t_array))
    return new_es


for problem in range(T):
    # N = int(input().strip())
    # start = tuple([(int(x)) for x in input().strip().split(' ')])

    N = 4
    start = [2, 2, 3, 7]

    # N = 4
    # start = tuple([53,361,188,665,786,898,447,562,272,123,229,629,670,848,994,54,822,46,208,17,449,302,466,832,931,778,156,39,31,777,749,436,138,289,453,276,539,901,839,811,24,420,440,46,269,786,101,443,832,661,460,281,964,278,465,247,408,622,638,440,751,739,876,889,380,330,517,919,583,356,83,959,129,875,5,750,662,106,193,494,120,653,128,84,283,593,683,44,567,321,484,318,412,712,559,792,394,77,711,977,785,146,936,914,22,942,664,36,400,857])

    if all_elements_are_equal(start):
        print(0)

    max_1 = max(start)
    start.remove(max_1)
    max_2 = max(start)
    start.remove(max_2)
