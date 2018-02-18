from solution import answer

input = [

        [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]],
        [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0]]

        ]
output = [7, 11]


for index, item in enumerate(input):
    print("index: " + str(index))

    result = answer(item)
    if(result == output[index]):
        print("correct!")
        print("your answer:   " + str(result))
        print("correct answer:" + str(output[index]))
    else:
        print("incorrect!")
        print("your answer:   " + str(result))
        print("correct answer:" + str(output[index]))
