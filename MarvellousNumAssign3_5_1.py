
def ChkPrime(Received_list):
    prime_list = []
    
    for num in Received_list:
        if(num == 0 or num == 1):
            continue
        
        else:
            flag = 1
            for i in range(2, num):
                
                if(num%i == 0):
                    flag = 0
                

            
        if flag == 1:
            prime_list.append(num)
    
    #print(prime_list)
    return prime_list