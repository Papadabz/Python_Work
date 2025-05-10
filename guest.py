from pathlib import Path

guest_name = input('What is your name?\n')

path = Path('guest.txt')
path.write_text(f"Guest: {guest_name}")