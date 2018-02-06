from solution import answer

input = [10, 143]
output = [1, 3]

for index, item in enumerate(input):
    result = answer(item)
    if(result == output[index]):
        print("correct!")
    else:
        print("incorrect!")
        print("your answer:   " + result)
        print("correct answer:" + output[index])
