#https://datatrucmuche.com/quand-utiliser-les-assert-en-python/
# a utiliser en dév seulement pas en prod (aide au débug)

def avg(notes):
    assert notes.length > 0, ' at least one note is required'
    return sum(notes) / len (notes)