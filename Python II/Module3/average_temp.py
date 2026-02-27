temperatures = {
'Monday': [67, 71, 74, 77],
'Tuesday': [52, 56, 66 , 50],
'Wednesday': [77, 80, 87 , 95],
'Thursday': [67, 77, 81 , 77],
'Friday': [54 , 60 , 67, 60],
}
for k, v in temperatures.items():
     :
     print(f'{k}: {sum(v)/len(v):.0f}')
     
#Answer: The for loop navigates through multi dimensional list. consider k as a counter.
#when k = 0 it reads first list of list ie Monday[], sum all the values insides Monday[] divide by lenghth of the Monday list.
#289/4 = 72.25 but in code it is explicitly mentioned that consider 0 digits after decimal point. So, answer is 72
#The for loop will run till there are items present in the temperature list.
