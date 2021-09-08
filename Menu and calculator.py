x = 10000
y = 5000
j = 13000
k = 15000

print("This is our food menu:\n1. Nasi Padang Rp 10.000\n2. Nasi Goreng Rp 13.0000\n3. Nasi Campur Rp 15.000\n")
a = input("Where menu do you want? ")
print('\nAnd this is our drink menu:\n1. Coca Cola Rp 5.000\n2. Cold Tea Rp 5.000\n3. Hot Tea Rp 5.000')
b = input("Where menu do you want? ")

if a == "1" and b == '1':
    print('\nNasi Padang and Coca Cola\nTotal: Rp ' + str(x+y))

if a == "1" and b == '2':
    print('\nNasi Padang and Cold Tea\nTotal: Rp ' + str(x+y))

if a == '1' and b == '3':
    print('\nNasi Padang and Hot Tea\nTotal: Rp ' + str(x+y))

if a == '2' and b == '1':
    print('\nNasi Goreng and Coca Cola\nTotal: Rp ' + str(j+y))

if a == '2' and b == '2':
    print('\nNasi Goreng and Cold Tea\nTotal: Rp ' + str(j+y))

if a == '2' and b == '3':
    print('\nNasi Goreng and Hot Tea\nTotal: Rp ' + str(j+y))

if a == '3' and b == '1':
    print('\nNasi Campur and Coca Cola\nTotal: Rp ' + str(j+y))

if a == '3' and b == '2':
    print('\nNasi Campur and Cold Tea\nTotal: Rp ' + str(j+y))

if a == '3' and b == '3':
    print('\nNasi Campur and Hot Tea\nTotal: Rp ' + str(j+y))

if a == '1' and b == '-':
    print('\nNasi Padang only\nTotal: Rp ' + str(x))

if a == '2' and b == '-':
    print('\nNasi Goreng only\nTotal: Rp ' + str(j))

if a == '3' and b == '-':
    print('\nNasi Campur only\nTotal: Rp ' + str(k))

if a == '-' and b == '1':
    print('\nCoca Cola only\nTotal: Rp ' + str(y))

if a == '-' and b == '2':
    print('\nCoca Cola only\nTotal: Rp ' + str(y))

if a == '-' and b == '3':
    print('\n1Coca Cola only\nTotal: Rp ' + str(y))

print(input())
