from solution import answer

input = ["vmxibkgrlm", "wrw blf hvv ozhg mrtsg'h vkrhlwv?", "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!", "vmxibkgrlm~\n\s\\"]
output = ["encryption", "did you see last night's episode?", "Yeah! I can't believe Lance lost his job at the colony!!", "vmxibkgrlm~\n\s\\"]

for index, item in enumerate(input):
    result = answer(item)
    if(result == output[index]):
        print("correct!")
    else:
        print("incorrect!")
        print("your answer:   " + result)
        print("correct answer:" + output[index])


'''
Use verify [file] to test your solution and see how it does. 
When you are finished editing your code, use submit [file] 
to submit your answer. If your solution passes the test cases, 
it will be removed from your home folder.
'''