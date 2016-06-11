class FooParent:
    def __init__(self):
        print("initial FooParent")

class FooChildren(FooParent):
    def __init__(self):
        print("initial FooChildren")
        FooParent.__init__(self)
        print('initial FooParent in class FooChildren')


class BooParent:
    def __init__(self):
        print('initial BooParent')

class CooChildren(BooParent, object):
    def __init__(self):
        print("initial CooChildren")
        super(CooChildren, self).__init__()
        print("initial BooParent in class CooChildren")

print("########1")
FooChildren()
print("########2")
CooChildren()
