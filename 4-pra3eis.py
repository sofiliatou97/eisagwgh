'''
Example:
python 4-pra3eis.py
	Enter text: seven(times(five()))
	Result: 7 * 5 = 35
'''


try:
    text = raw_input("Enter text: ")
except:
    quit()

info = text.split("(")[:-1]

number = {'zero': 0,'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight':8,"nine": 9}

a = number[info[0]]
b = number[info[2]]

operation = {'plus': a + b, 'minus': a-b, 'times': a*b}
operationShow = {'plus': '+', 'minus': '-', 'times': '*'}

print "Result: " + str(a) + " " + operationShow[info[1]] + " " + str(b) + " = " + str(operation[info[1]])
