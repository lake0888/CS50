def convert(str):
    index_happy = str.find(':)')
    index_sad = str.find(':(')

    if index_happy != -1:
        str = str.replace(':)', '🙂')

    if index_sad != -1:
        str = str.replace(':(', '🙁')

    return str

def main():
    print(convert(input()))

main()