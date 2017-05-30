# file two.py
import test1

print("top-level in two.py")
test1.func()

if __name__ == "__main__":
	print("two.py is being running  directly")
else:
	print("two.py is being imported into another module")