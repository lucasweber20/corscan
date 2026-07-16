import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Set url. Example: -u www.example.com", type=str)
parser.add_argument("-l", "--list", help="Add urls file. Example -u urls.txt", type=str)
parser.add_argument("-o", "--output", help="Save urls in file. Example: -o urls.txt", type=str)

args = parser.parse_args()

def main():
    urls = read_urls(args.list)

def read_urls(file):
    file_read = open(file, encoding="utf-8").read().splitlines()
    result = list(dict.fromkeys(file_read))
    return result

if __name__ == "__main__":
    main()