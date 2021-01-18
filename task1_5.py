'''Nikita - Task 5''' 

a = input('Enter side a: ')
b = input('Enter side b: ')
c = (a**2 + b**2)**(0.5)

print('The hypothenuse length is; ', c)
print('The triangle square is: ', (((a+b+c) + (-a+b+c) + (a-b+c) 
* (a+b-c))**(1/2))*0.25)


