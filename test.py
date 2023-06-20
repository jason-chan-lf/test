import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--swagger')

    args = parser.parse_args()
    print ("This is the swagger argument: " + args.swagger + ".")
