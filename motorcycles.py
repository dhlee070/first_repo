motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0]='ducati'
# print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(-1, 'mazda')
print(motorcycles )
del motorcycles[-2]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
motorcycles.remove('honda')
print(motorcycles)