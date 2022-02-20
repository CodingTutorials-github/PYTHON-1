# break and continue Statements, and else Clauses on Loops
# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of
# the list (with for) or when the condition becomes false (with while), but not when the loop is terminated
# by a break statement. This is exemplified by the following loop, which searches for prime numbers:


# CODE EXAMPLE: (done in python IDLE)
>>> for n in range(2, 10):
... for x in range(2, n):
... if n % x == 0:
... print(n, 'equals', x, '*', n//x)
... break
... else:
...# loop fell through without finding a factor
... print(n, 'is a prime number')
...




# OUTPUT
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
