import os
import grammar


def main():
    prog = '''
    str = "Hello"
    name = input("Input name: ")
    print(str, name)
    a = 2
    b = 3 + a
    r = a < b
    '''
    prog = grammar.parse(prog)
    print(*prog.tree, sep=os.linesep)


if __name__ == "__main__":
    main()