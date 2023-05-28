string = input("enter a string\n")
l1 = []
l2 = []
for i in range(0,len(string)):
    l1.append(string[i])
for j in reversed(range(len(string))):
    l2.append(string[j])
if(l1 == l2):
    print("palindrome")
else:
    print("not palindrome")
