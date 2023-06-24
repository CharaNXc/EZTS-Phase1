s1={10,20,30}
s2={40,50,60,10}
e1={70,80,90,100,10}
s3=s1.union(s2)
s4=s1|s2
print(s3)
print(s4)

s5=s1.intersection(s2)
s6=s1&s2
print(s5)
print(s6)

print(s1.intersection_update(s2,e1))




print(s1.difference(s2))
      #print(s8)

s9=s1-s2
print(s9)