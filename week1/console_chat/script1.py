from sys import argv

prompt = "> "
try:
    name, one, two = argv
except Exception as e:
    print("Unpacking error error: %s" % e)
    name = argv[0]
    print("What is your fukin name ?:")
    one = input(prompt)
    print("What is your fukin second value ?:")
    two = input(prompt)


def get_subcommand(*args, **kwargs):
    if len(args) == 0:
        print("No subcommand provided") 
    
        args_given = True
    else:
        print("Subcommand provided")
        for arg in args:
            print(arg)
    if len(kwargs) == 0:
        print("No keyword arguments provided")
        return False
    else:
        print("No Keyword arguments provided")
        for kwarg in kwargs:
            print(kwarg)
        return True

def main():
    """
    Scripts can be used to create a function that can be used in many cases.
    Including automation of various functions
    Downloading of a youtube video
    making a testing automation script and webcrawler
    """

    print("The name of the script file is " + name)
    print("The first argument is " + one)
    print("The second argument is " + two)
    print(argv)
    get_subcommand(args=argv, kwargs=argv)
    return 0

if __name__ == "__main__":
    main()

