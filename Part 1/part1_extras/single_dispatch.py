def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(val):
        def inner(fn):
            registry[val] = fn
            return fn
        return inner
    
    def decorator(val):
        fn = registry.get(val, registry['default'])
        return fn()
    
    decorator.register = register
    return decorator


@switcher
def dow():
    return 'Invalid day'

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def create_function(val):
    func_name = 'dow_' + str(val)
    code = f'''def {func_name}():\n\treturn "{days[val-1]}"'''
    exec(code, globals())
    return func_name

for i in range(1, len(days)+1):
    dow.register(i)(globals()[create_function(i)])

print(dow(8))