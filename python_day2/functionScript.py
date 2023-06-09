def operation(x,y,_operation):
    if(_operation=="sum"):
        return x+y
    elif(_operation=="sub"):
        return x-y
    elif(_operation=="multi"):
        return x*y
    elif(_operation=="divide"):
        if(y!=0):
            return x/y

print(operation(10,2,"divide"))