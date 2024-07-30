import os

class Test:
    def __init__(self):
        pass

    def path_name(self):
        print(os.path.abspath(os.path.join("package")))

def main():
    test = Test()
    test.path_name()


if __name__ == "__main__":
    main()