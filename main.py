from caesar import Caesar
from message import Message


def main():
    src = input('Enter your name: ')
    dest = input('Enter reciever: ')
    data = input('Enter message: ').lower()
    shift = int(input('Enter key: '))

    caesar = Caesar(shift)
    message1 = Message(src, dest, data)

    print(message1)

    encrypted = caesar.encrypt(message1.data)
    decrypted = caesar.decrypt(encrypted)

    print(encrypted)
    print(decrypted)


if __name__ == '__main__':
    main()
