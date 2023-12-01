def common_types(str):
    if str.endswith('.gif'):
        return 'image/gif'
    elif str.endswith('.jpeg') or str.endswith('.jpg'):
        return 'image/jpeg'
    elif str.endswith('.png'):
        return 'image/png'
    elif str.endswith('.pdf'):
        return 'application/pdf'
    elif str.endswith('.txt'):
        return 'text/plain'
    elif str.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

def main():
    str = input('Enter the file ').strip().lower()
    print(common_types(str))

main()