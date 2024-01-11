# wap to find the sum of first 2000 prime num
prime_sum=0
prime_count=0
i=1
while prime_count!=2001 and i>0:
            k=0
            i+=1
            for j in range(2,i):
                if i%j==0:
                    k+=1
            if k==0:
                  prime_sum+=i
                  prime_count+=1
            if prime_count==2000:
                  break
print(prime_sum)
print(prime_count)