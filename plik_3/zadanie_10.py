def print_args_kwargs(*args, **kwargs):
    print("Argumenty args:")
    for i, arg in enumerate(args, start=1):
        print(f"  {i}: {arg}")

    print("Keywords kwargs:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_args_kwargs(1, 'python', True, name='Marlena', age=26)

