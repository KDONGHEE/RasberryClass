n = int(input())

num = n  
count = 0

while True:
    result = (num // 10) + (num % 10)  
    new = ((num % 10) * 10) + (result % 10) 
    count += 1
    if n == new :
        break
    num = new
print(count)