class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' %s)
    return 10/n

def main():
    foo(0)

main()
print 'End'
