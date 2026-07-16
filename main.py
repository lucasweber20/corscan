import requests
import argparse
import concurrent.futures


parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Set url. Example: -u www.example.com", type=str)
parser.add_argument("-l", "--list", help="Add urls file. Example -u urls.txt", type=str)
parser.add_argument("-o", "--output", help="Save urls in file. Example: -o urls.txt", type=str)
parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

args = parser.parse_args()

def main():
    threads = 1
    threads = args.thread if args.thread and args.thread > 1 else threads
    
    urls = read_urls(args.list)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.thread) as executor:
        futures = [executor.submit(requests_urls, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def read_urls(file):
    file_read = open(file, encoding="utf-8").read().splitlines()
    result = list(dict.fromkeys(file_read))
    return result

def requests_urls(urls):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
    try:
        req = requests.get(urls, headers=headers, timeout=10)
        return req.url
    except:
        pass

if __name__ == "__main__":
    main()