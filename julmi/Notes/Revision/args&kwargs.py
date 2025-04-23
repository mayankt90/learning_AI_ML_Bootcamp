def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args_kwargs(1, 2, 3, name="Alice", age=25)




# In the above code, we define a function `print_args_kwargs`
# that takes any number of positional arguments (`*args`)
# keyword arguments (`**kwargs`) --> Keyword wale aese hote hh name="Alice", age=25.