def konkat(*args):
    """This function concatenates

    This is a test"""
    variable = ""
    for a in args:
        variable += a
    return variable
print(konkat("dies", "ist", "ein", "test"))
print(help(konkat))
