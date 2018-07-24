

bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].upper())


print(bicycles[3-2])

print(bicycles[-3])

motorcycles=['hero','honda','yamaha','bullet']
print(motorcycles)
motorcycles.append('duke')
print(motorcycles)

motorcycles.insert(5,'pulsar')
print(motorcycles)

motorcycles.insert(9,'harley')
print(motorcycles[5])

motorcycles.insert(0,'KTM')
print(motorcycles)

print(motorcycles[5],motorcycles[6])


del motorcycles[2]
print (motorcycles)


popped_motor=motorcycles.pop()
print(motorcycles)
print(popped_motor)

#when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
print("I love to drive a "  + motorcycles[3])
