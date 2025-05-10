def make_shirt (size= 'large', quote= 'I love Python'):
    """Shirts again"""
    print(f"\nThe shirt size is: {size.title()}")
    print(f"The shirt says '{quote}'")

make_shirt(size='Medium')
make_shirt()
make_shirt(quote='Python is pretty cool')