data = input()

data = data.replace('XXXX', 'AAAA') #replace함수 숙지할것
data = data.replace('XX', 'BB')

for i in data:
    if i == 'X':
        print(-1)
        exit()

print(data)
