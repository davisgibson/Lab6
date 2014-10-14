#total = 0
#print 'How many numbers would you like to enter?'
#input1 = int(raw_input())
#
#for x in range(input1):
#    print 'Enter any number.'
#    input2 = int(raw_input())
#    total = total + input2
#print total



#total = []
#print 'how many numbers would you like to enter?'
#input3 = int(raw_input())
#
#for y in range(input3):
#    print 'Enter any number.'
#    input4 = int(raw_input())
#    total.append(input4)
#print sum(total)


#print 'What number would you like to take the factorial of?'
#number = int(raw_input())
#factorial = 1
#for z in range(1, number + 1,1):
#    factorial = factorial * z
#print factorial



factors = []
print 'What number would you like to find the factors of?'
number = int(raw_input())
count = 1

while (count < number):
    if number%count == 0:
        factors.append(count)
    count = count + 1
print factors

















