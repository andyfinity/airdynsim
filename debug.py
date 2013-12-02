is_array = lambda var: isinstance(var, (list, tuple, dict))

def printr(a,indent=0):
    for key,value in a.iteritems():
        if is_array(value):
            print(" " * indent + key)
            printr(value,indent+1)
        else:
            print(" " * indent + value)