_sentinel = object()

def validate(a = _sentinel):
    if a is not _sentinel:
        print('argument was provided')
    else:
        print('argument was not provided')

        