if os.path.exists(filename):
    with open(filename) as f:
        print(f.read())
try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("No file found")
