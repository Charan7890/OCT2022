
array = list(map(int,input().split(' ')))

n = len(array)
ws = int(input())

i,j,ans,res=0,0,0,0

while j<n:
    
    ans+=array[j]
    
    if j-i+1 < ws:
        j+=1
        
        
    elif j-i+1 == ws:
        if res<ans:
            res = ans
        ans -= array[i] 
        i+=1
        j+=1
        
        
print(res)
        
        
    
