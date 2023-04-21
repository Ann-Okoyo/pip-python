#  Write a Python program to find the sum of 
# all the elements in a list.

elements = [90,70,80,60,30,60]
print(sum(elements))

# Write a Python program to find the largest 
# element in a list.
numbers=[120,90,70,60,40]
print(max(numbers))

# Write a Python program to find the second
# largest element in a list.
digits =[80,90,60,40,107]
digits.sort()
secondlargest=digits[-2]
print(secondlargest)

# Write a Python program to
# remove duplicates from a list.
numerals=[90,90,87,69,40,90,30]
newarray=[]
for numeral in numerals{
         if numeral not in newarray{
           newarray.append(numeral)
        }

       
}
print(newarray) 
       

# Write a Python program to find the 
# common elements between two lists.
numarray1=[23,24,89,70,60]
numarray2=[45,74,59,30,24]

samenumbers =list(set(numarray1)) & set(numarray2))
print(samenumbers)


    