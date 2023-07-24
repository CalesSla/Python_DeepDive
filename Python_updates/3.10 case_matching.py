
# Case statements
def respond(language):
    match language:
        case 'Java':
            return 'Hmm, coffee!'
        case 'Python':
            return 'I love Python too!'
        case 'Rust':
            return 'I heard Rust is nice.'
        case 'Go':
            return 'Great, but a bit verbose.'
        case _:
            return 'I like many languages.'

print(respond('Java'))
print(respond('Slava'))


# Case statements multiple patterns
def respond(language):
    match language:
        case 'Java' | 'Python' | 'Rust':
            return 'I heard that language is nice.'
        case 'Go':
            return 'Great, but a bit verbose.'
        case _:
            return 'I like many languages.'

print(respond('Java'))
print(respond('Python'))
print('\n')

symbols = {'F': '\u2192',
           'B': '\u2190',
           'L': '\u2191',
           'R': '\u2193',
           'pick': '\u2923',
           'drop': '\u2925'}

print(symbols)
print('\n')


# Robot commands simmulation
def op(command):
    match command:
        case 'F':
            return symbols['F']
        case 'B':
            return symbols['B']
        case 'L':
            return symbols['L']
        case 'R':
            return symbols['R']
        case 'pick':
            return symbols['pick']
        case 'drop':
            return symbols['drop']
        case _:
            raise ValueError(f'Unknown command {command!r}')
        
print(op('F'))

print([op('F'), op('B'), op('L'), op('R'), op('pick'), op('drop')])
print('\n')


# Multiple patterns robot commands simmulation
def op(command):
    match command:
        case ['move', ('F' | 'B' | 'L' | 'R') as direction]:
            return symbols[direction]
        case 'pick':
            return symbols['pick']
        case 'drop':
            return symbols['drop']
        case _:
            raise ValueError(f'Unknown command {command!r}')
    
print(op('pick'))
print('\n')


# Multiple patterns robot commands simmulation with tuple unpacking
def op(command):
    match command:
        case [*directions]:
            return tuple(symbols[direction] for direction in directions)
        case 'pick':
            return symbols['pick']
        case 'drop':
            return symbols['drop']
        case _:
            raise ValueError(f'Unknown command {command!r}')
        
print([op(['F', 'F', 'L']),
 op('pick'),
 op(['R', 'L', 'F']),
 op('drop')
])
print('\n')


# Multiple patterns robot commands simmulation with tuple unpacking and set comparison
def op(command):
    match command:
        case [*directions] if set(directions) < symbols.keys():
            return tuple(symbols[direction] for direction in directions)
        case 'pick':
            return symbols['pick']
        case 'drop':
            return symbols['drop']
        case _:
            raise ValueError(f'Unknown command {command!r}')

print([op(['F', 'F', 'L']),
 op('pick'),
 op(['R', 'L', 'F']),
 op('drop')
])
print('\n')

