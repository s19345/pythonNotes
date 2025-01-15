def build_sentence(*args, **kwargs):
    sentence = ' '.join(args)
    ending = kwargs.get('end', '')
    return sentence + ending

print(build_sentence("Marlena", "ma", "26", "lat", end="."))

