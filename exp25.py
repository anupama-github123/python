head_count=0
tail_count=0 

print ("enter the count of head/tail or stop:")

while True:
    flip=input()

    if flip =="stop":
        break
    elif flip =="head":
        head_count=head_count+1
    elif flip =="tail":
        tail_count=tail_count+1

    
print('head won',head_count,'times and tail won',tail_count,'times')
t_count=head_count+tail_count
print("total count:",t_count)
head_pnge=100*(head_count/t_count)
tail_pnge=(tail_count/t_count)*100
print('head percentage is',head_pnge,'and tail percentage is',tail_pnge)




