class mylist:
    def __init__(self, initial = []):
        self.list = initial

class list_of_lists:
    def __init__(self):
        # Only difference between these two lists is being explicit with the initial argument vs leaving it as default
        self.implicit_arg = [mylist()]
        self.explicit_arg = [mylist(initial=[])]
        
    def push(self, el):
        if len(self.implicit_arg[-1].list) == 5:
            self.implicit_arg.append(mylist())
        self.implicit_arg[-1].list.append(el)
        
        if len(self.explicit_arg[-1].list) == 5:
            self.explicit_arg.append(mylist(initial=[]))
        self.explicit_arg[-1].list.append(el)
        
if __name__ == "__main__":     
    nested_lists = list_of_lists()

    for i in range(100):
        nested_lists.push(i)
    # These should be the same, but they're not
    print(len(nested_lists.implicit_arg))
    print(len(nested_lists.explicit_arg))
