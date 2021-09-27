'''
Problem-06:Given a list, iterate it, and display numbers divisible by five, 
and if you find a number greater than 150, stop the loop iteration.
'''

for i in list_num:
    if i < 150:
        if (i % 5 == 0):
            print('Number is divided by 5 = ', i)
    else:
        print('Oh no this is gatter then 150')
        break

#problem num_06: Reverse the following list using for loop
for i in reversed(list_num):
    print(i)