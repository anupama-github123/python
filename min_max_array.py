'''
my_list = []
while True:
    value = input("Enter a value (or type 'stop' to finish): ")
    if value == 'stop':
        break
    my_list.append(value) # You can convert to int/float if needed

print("Final list:", my_list)
'''
my_list=[1,2,3,4,9,7,0,-2]
print('max:',max(my_list))
print('min:',min(my_list))