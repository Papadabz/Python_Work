def make_sandwich(*ingredients):
    """Show ingredients going into a sandwich"""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")