# variable function in Python and functions in dictionary

def foo():
    return {
        "un":input("entrez un nombre")
    }

val = foo()

print(val)


def bar():
    print('I am in bar')

dico = {
    'bar':bar
}

dico['bar']()