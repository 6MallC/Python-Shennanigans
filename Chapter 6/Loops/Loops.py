# for loops go for a set number of times
# while loops go until a condition is met
# you can nest loops
# just blowing through the exercises, I know these already

# exercise 1
evensum = 0
for i in range(2,101,2):
    evensum += i
print(evensum)
# exercise 2
pwroftwo = 1
while pwroftwo <= 1000:
 pwroftwo *= 2
print("power of 2 below 1000 = ", pwroftwo)
# exercise 3
for i in range (1,11):
    for j in range (1,11):
        print(i * j, end="\t")
    print()

# there are also keywords for controlling loops
# break will exit the loop
# continue skips the iteration
# pass doesnt do anything and serves as a placeholder
# now for exercises
brsum = 0
for i in range (1,101):
    brsum += i
    if brsum > 500:
        print(f"sum has reached {brsum} at {i}")
        break 

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

for i in range(1,11):
    if 4<= i <= 7:
        pass
    else:
        print(i)