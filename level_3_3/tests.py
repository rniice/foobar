from solution_3 import answer
import time

def microseconds():
    return int(round(time.time() * 1000000))

#input of 3 is a special case, or need more general outcome path.
input = ["4", "15", "1", "2", "3", "5", "6", "7", "8", "9", "31", "30", "1"]
output = [2, 5, 0, 1, 2, 3, 3, 4, 3, 4, 6, 6, 0]

#input = ["3", "5", "6", "7", "8", "9", "31", "30"]
#output = [2, 3, 3, 4, 3, 4, 6, 6]

for index, item in enumerate(input):

    start = microseconds()
    result = answer(item)
    end = microseconds()
    delta = end - start

    if(result == output[index]):
        print("index: " + str(index) + "; value: " + str(item) + "; correct: " + str(result) + "; elapsed[us]: " + str(delta))
    else:
        print("index: " + str(index) + "; value: " + str(item) + "; incorrect: " + str(result) + "; elapsed[us]: " + str(delta))
