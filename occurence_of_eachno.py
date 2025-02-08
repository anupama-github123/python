input_array=[1,2,3,2]
dis_array=list(set(input_array)) #[1,2,3]
result_array=[0] *len(dis_array)#[1,0,0]
for i in range(len(dis_array)):
    for j in range(len(input_array)):
            if(dis_array[i] ==input_array[j]):
                result_array[i]=result_array[i]+1
print(result_array)