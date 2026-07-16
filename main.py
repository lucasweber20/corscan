import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Set url. Example: -u www.example.com", type=str)
parser.add_argument("-l", "--list", help="Add urls file. Example -u urls.txt", type=str)
parser.add_argument("-o", "--output", help="Save urls in file. Example: -o urls.txt", type=str)

args = parser.parse_args()

def main():
    pass

if __name__ == "__main__":
    main()