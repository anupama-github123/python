amt_x=int(input("enter the mbps on wikipedia:"))
amt_y=int(input("enter the mbps on memes:"))
t_consumption=amt_x*0.01 + amt_y*0.05
if(t_consumption<100):
    print('too much consumption...')
elif(amt_y > amt_x):
    print('wow many memes')
    print('such lol')