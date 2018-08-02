from pip._vendor.chardet.enums import MachineState


class ManagedFile:
    ''' A demo of a context manager

    '''
    def __init__(self, name):
        # called when ManagedFile(name) called
        self.name = name

    def __enter__(self):
        ''' Acquires resources
          useless method as open already does this.
          called when with.... as....: is used
          '''
        self.file = open(self.name, 'w')
        # assigned to the as ... variable
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' takes exceptions as resources
        '''
        if self.file:
            self.file.close()

# with ManagedFile('hello.txt') as f:
#     f.write('hello, people!')


from contextlib import contextmanager
'''
# turns below statement into context usable with "with" statement
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')

'''

# class Indenter:
#     def __init__(self):
#         self.level = 0
#
#     def __enter__(self):
#         self.level += 1
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.level -= 1
#
#     def print(self, text):
#         print('    ' * self.level + text)

# with Indenter() as indent:
#     indent.print('hi!')
#     with indent:
#         indent.print('hello')
#         with indent:
#             indent.print('bonjour')
#     indent.print('hey')

'''
# does not work
@contextmanager
def indenter(text=''):
    level = 0
    try:
        level += 1
        yield '    ' * level + text
    finally:
        level -= 1

with indenter() as indent:
    indent('hi!')
    with indent('hello'):
        with indent('bonjour'):
            pass
    indent('hey')

'''