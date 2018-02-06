from solution import answer

input = [{"n": "1211", "b": 10},{"n": "210022", "b": 3}]
output = [1, 3]

for index, item in enumerate(input):
    result = answer(item['n'], item['b'])
    if(result == output[index]):
        print("correct!")
    else:
        print("incorrect!")
        print("your answer:   " + result)
        print("correct answer:" + output[index])
