call_d=int(input("enter the call duration:"))
if(call_d>500):
    t_amt=call_d*0.01
elif(call_d>800):
    t_amt=500*0.01+call_d-500 *0.008
else:
    t_amt=500*0.01+299*0.008+call_d-800*0.005


print('total amount:',t_amt)
print('monthly bill:',t_amt*30)