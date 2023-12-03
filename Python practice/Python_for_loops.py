#for loops are best used to execute code a fixed number of times. 
        # you can ittarate over range, string, sequance ect. 

#count to 10

for counter in range(1,11):
    print(counter)

#count backwords

for x in reversed(range(1,10)):
    print(x)
print("happy new year")

#count by 5's

for i in range(0,100,5):
    print(i)

#itarate over a string

credit_numb = "1234-5678-9012-3456"

for str in credit_numb:
    print(credit_numb)

#or 
credit_numb = "1234-5678-9012-3456"

for str in credit_numb:
    print(str)

#conditions continue and break
#continue skips over an iteration
#break breaks out of the loop entirely

#skips over 15
for x in range(1,21):
    if x == 15:
        continue
    print(x)

#breaks the loop at 15
for x in range(1,21):
    if x == 15:
        break
    print(x)