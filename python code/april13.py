# 1. swap two number without third variable:
a,b=5,10
print(f' Numbers before swap a :{a} and b :{b}')
def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    return (x,y)

g,h=(swap(a,b))
print(f'After Swap the value is a:{g} and b :{h}')





# 2. reverse a number
# num = int(input('Enter a number : '))

num=123
def reverse(n):
    rev=0
    while n > 0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev

print(f"Origial Number:{num}")
print(f"Reverse Number : {reverse(num)}")






# 3. prime Number between 1 to 10
def primee():
    for num in range(1,11):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)
    
primee()







# 4. Missing Number between from a asequence
def missing():
    lst = [1,2,4,5,6]
    for i in range(1,len(lst)):
        if i not in lst:
            return i
        
print(missing())












# 5. compress string
s='aabbbcdddk'
freq={}
for c in s:
    freq[c]=freq.get(c,0)+1
result = "".join(f"{char}{count}" for char , count in freq.items())
print (result)











# 6. list of squares
num = int(input("End number for square :"))
square = [i*i for i in range(1,num)]
print(square)











# 7. check string contains only numbers
str = (input("Enter String :"))
def string(x):
    str = x
    if str.isdigit():
        return True
    else:
        return False

print(f"Is string contain only numbers: {string(str)}")











# 8. Remove Duplicates from list we use set because it don;'t allow duplicates
lst = [1,2,2,2,3,3,4,4,56,77,4,2,2,2,4,4]
lst = list[set(lst)]
print(lst)












# 9. find first unique element in list

lst = ['a', 'b', 'a', 'c', 'b']

def unique(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    for item in lst:
        if counts[item] == 1:
            return item
    return None

print(f"Firs tunique element is {unique(lst)}")










# 10. find even elements in nusted list
lst=[[1,2,3],[4,5,6],[7,8,9,]]
print(lst)
for x in lst:
    for y in x:
        if y % 2 == 0:
            print(y)












# 11. built distionary of indices
lst = ['a', 'b', 'a']
def counts(lst):
    dict={}
    for i,x in enumerate(lst):
        if x not in dict:
            dict[x] = [i]
        else:
            dict[x].append(i)
    return dict

print(counts(lst))











# 12. convert list of dicts into dict 
def converts():
    lst=[{'name':"A",'marks':30},{'name':"B",'marks':50}]
    dict = {}

    for p in lst:
        name = p['name']
        age = p['marks']
        dict[name]=age

    return dict

print(converts())