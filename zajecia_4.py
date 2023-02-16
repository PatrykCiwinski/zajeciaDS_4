tools = ['lornetka', 'lupa', 'teleskop', 'sonda']

tools.insert(2,'śrubokręt')
tools.append('drewno')
tools+=['gwóźdź']
tools[2]='kierownica'
del tools[3]
tools.pop(3)
print(tools)

num = [1,2,3,4,5]
letters=['a','b','c','d']

num.extend(letters)
print(num)

nums = [1,2,3,4,5]
even = list(filter(lambda x:(x%2==0),nums))
print(even)
print()
for num in nums:
    print(num)
print()
[print(num) for num in nums]