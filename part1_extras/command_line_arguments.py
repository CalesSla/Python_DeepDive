import sys
import argparse
import datetime

# numbers = [int(a) for a in  sys.argv[1:]]

# print(sum(numbers))





# print(sys.argv[1:])
# my_dict = {}
# for i in range(1, len(sys.argv), 2):
#     my_dict[sys.argv[i]] = sys.argv[i+1]

# print(my_dict)





# keys = sys.argv[1::2]
# values = sys.argv[2::2]
# my_dict = dict(zip(keys, values))
# print(my_dict)



# keys = sys.argv[1::2]
# values = sys.argv[2::2]
# args = {k: v for k, v in zip(keys, values)}
# print(args)

# first_name = args.get('first-name', None)
# last_name = args.get('last-name', None)
# yob = int(args.get('yob', None))
# print(first_name, last_name, yob)




# parser = argparse.ArgumentParser(description='Calculates the fiv a//b and mod a%b of two numbers')
# parser.add_argument('a', type=int, help='First number')
# parser.add_argument('b', type=int, help='Second number')

# args = parser.parse_args(sys.argv[1:])

# a = args.a
# b = args.b

# print(f'{a}//{b} = {a//b}, {a}%{b} = {a%b}')





# parser = argparse.ArgumentParser(description='Returns a string containing the name and age of a person')
# parser.add_argument('-f', '--first', type=str, help='First name', required = False, dest = 'first_name')
# parser.add_argument('-l', '--last', type=str, help='Last name', required = True, dest = 'last_name')
# parser.add_argument('-y', '--yob', type=int, help='Year of birth', required = True  , dest = 'birth_year')

# args = parser.parse_args(sys.argv[1:])

# if args.first_name:
#     names = [args.first_name]
# else:
#     names = []

# names.append(args.last_name)
# full_name = ' '.join(names)
# current_year = datetime.datetime.utcnow().year
# age = current_year - args.birth_year

# print(f'{full_name} is {age} years old')






# parser = argparse.ArgumentParser(description = 'Prints the squares of a list of numbers, and the cubes of another list of numbers')
# parser.add_argument('-sq', help='list of numbers to square', nargs='*', type=float)
# parser.add_argument('-cu', help='list of numbers to cube', nargs='+', type=float, required=True, dest = 'cubes')

# args = parser.parse_args(sys.argv[1:])

# if args.sq:
#     squares = [a**2 for a in args.sq]
#     print(f'Squares: {squares}')

# cubes = [a**3 for a in args.cubes]
# print(f'Cubes: {cubes}')





# parser = argparse.ArgumentParser(description='Testing defaults and flags.')
# parser.add_argument('--monty', action = 'store_const', const = 'Python')
# parser.add_argument('-n', '--name', default = 'John')
# parser.add_argument('-v', '--verbose', action = 'store_const', const = True, default = False)
# parser.add_argument('-v2', action = 'store_const', const = True)
# parser.add_argument('-q', '--quiet', action = 'store_false')

# args = parser.parse_args(sys.argv[1:])

# print(args)






parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action = 'store_true')
group.add_argument('-q', '--quiet', action = 'store_true')

parser.add_argument('-n', type = complex, required = True)

args = parser.parse_args(sys.argv[1:])

print(args)