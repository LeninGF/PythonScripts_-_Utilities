import argparse


def print_my_name(name):
    '''
    Function to greet the user
    :param name: string
    :return:
    '''
    print('Nice 2 Meet you dear '+name)
    return 0


def main(name):
    print_my_name(name)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', '--name', required=True, type=str, help="enter your name please")
    args = vars(ap.parse_args())
    name = args["name"]

    main(name)
