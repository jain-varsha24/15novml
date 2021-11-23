#Question2
print(5**9)
print(3//2)
print(7//30)
print(7/30)
print(6 == 6)
a = 20
a+= 30
a%=3
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print(False in ‘False’)
print(((True == False) or (False > True)) and (False <= True))

#Question3
s1= "nice to have it"
s2 = "here"
print(s1+' '+s2)

#Question4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Question5
s1= "nice to have it"
s2 = "here"
a.insert(0,s1)
a.append(s2)
print(a)

#Question6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
a = []
for i in numbers :
    if (i==237):
        a.append(i)
        break
    elif (i% 2 == 0):
        
        a.append(i)
print(a)

#Question7
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

col = color_list_1-color_list_2
print(col)

#Question8
str = "My name is varsha jain"
if (str.isalpha()):
    print("string is pangram")
else :
    print("string is not pangram")

#Question9
n= eval(input("enter a number"))
sum = n + (n*10 +n)+(n*100+n*10+n)
print(sum)

#Question 10
n = input('enter a string')
n1= n.split('#')
print(n1)
l1 = n1[0].split()
l2 = n1[1].split()
print(l1)
print(l2)

#question 11
l = input("enter a string")
s =l.split(',')
s.sort()
print(s)

#Question12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
d1 = d['Marks']
d2 = d['Student']
print(d1)
high = max(d1)
j=0
for i in range(len(d1)):
    if d1[i]==high:
        j =i
print(d2[j])

#Question 13
str = eval(input("enter a string "))
c1 = 0
c2 = 0
for i in str:
    if (i.isalpha()):
        c1+=1
    elif (i.isdigit()):
        c2+=1
print("no. of alphabets are",c1)
print("no. of digits are ",c2)

#Question 14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
inp = input("enter subject name")
new1 = []
new2 =[]
new3=[]
sub = d['Subject']
l1 = d['Name']
l2=d['Ratings']
for i in range(len(sub)):
    if sub[i] == inp:
        new1+=sub[i]
        new2+=l1[i]
        new3+=l2[i]
d1={}
d1['Name']=new2
d1['Subject']=new1
d1['Ratings']=new3
print(d1)
    


     
