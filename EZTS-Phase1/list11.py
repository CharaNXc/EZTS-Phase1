dp=[]
#s=0
sz=int(input("Enter the dp list size:"))
for i in range(sz):
    dp.append(int(input("Enter the new item:")))
    #s=s+dp[i]
print(dp)
print(sum(dp))