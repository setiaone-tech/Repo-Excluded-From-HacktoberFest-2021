# Python program to reverse a entered number

n = int(input('please give a number : '))
print 'Number before being reversed : %d' % n
reverse = 0
while n != 0:
    reverse = reverse * 10 + n % 10
    n = n // 10
print 'Number after being reversed : %d' % reverse
