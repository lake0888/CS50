import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^(<iframe).*(src=\"https?://(www\.)?youtube.com/embed/\w+\").*(></iframe>)$", s)
    if matches:
        array = matches.groups()
        index_src = find_src(array)
        if index_src != -1:
            url = array[index_src]
            url = url.split("src=")[1].replace("\"", "")
            url = re.sub(r"https?://(www\.)?youtube.com/embed/", "https://youtu.be/", url)
            return url

def find_src(array):
    i = 0
    while i < len(array):
        if array[i].startswith("src="):
            return i
        i += 1
    return -1


if __name__ == "__main__":
    main()