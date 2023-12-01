def main():
    str = input('The Answer to the Great Question of Life, the Universe and Everything is? ').strip().lower()

    if str == '42' or str.lower() == 'forty-two' or str == 'forty two':
        print('Yes')
    else:
        print('No')

main()