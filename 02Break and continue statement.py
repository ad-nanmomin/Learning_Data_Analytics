"""
Break statement
Used when we want to abruptly exit a particular block of code

Continue statement
used when we want to skip a certain block of code

both of these statements are used in loops

"""
# lets  see an example
#printing numbers upt0 100 but no multiples of 5
a=1
while True:
    if a%5!=0:
        print(a)
        a+=1
    elif a==100:
        break
    else:
        a+=1
        continue

