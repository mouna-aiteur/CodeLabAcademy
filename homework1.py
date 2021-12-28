#creating list of all even numbers between 1 and 299
list = []
for i in range(1,300):
    remainder = i % 2
    if( remainder == 0):
        list.append(i)
print(list)
# printing the lenght of the list
lenght = len(list)
print(lenght)
#printing the squared value of the list
squared_list = []
for i in list :
    square = i*i
    squared_list.append(square)
print(squared_list)
# checking if 57 in the list
print("57 is in the list : ",57 in list)