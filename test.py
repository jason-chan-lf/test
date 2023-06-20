import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--swagger')

    args = parser.parse_args()
    print (args.swagger)
