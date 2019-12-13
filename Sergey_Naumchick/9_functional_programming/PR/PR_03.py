# 3. Write decorator that print function name before and after function execution.
# `func.__name__`

def func_name_show(function_to_decorate):
    # Decorator will show name before and after execution
    def wraper():
        print(function_to_decorate.__name__)

        function_to_decorate()

        print(function_to_decorate.__name__)
    return wraper

@func_name_show
def func_count():
    s = 'zckzlkvjsdlkjvlsdkv'
    print(s)

func_count()

