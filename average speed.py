q=int(input("Enter a num"))
w=int(input("Enter a num"))
e=int(input("Enter a num"))
sum=q+w+e
avg=sum/3
print ("avg is",avg)
if avg >q and avg>w and avg>e:
    print ("%d is higher than %d,%d,%d"%(avg,q,w,e))
elif  avg>q  and avg>w:
    print ("%d is higher than %d, %d " %(avg,q,w))       
elif  avg>q  and avg>e:
    print ("%d is higher than %d, %d " %(avg,q,e))  

else:
    print("invalid text")    