import colorama, os, platform


def encode(text):
    if isinstance(text, str):
        encoded_text = text.encode('utf-8').hex()
    elif isinstance(text, list):
        encoded_text = ''
        for i in text:
            encoded_text += f'{i}\n'.encode('utf-8').hex()
    return encoded_text


def decode(encoded_text):
    if isinstance(encoded_text, str):
        decoded_text = bytes.fromhex(encoded_text).decode('utf-8')
    elif isinstance(encoded_text, list):
        decoded_text = ''
        for i in encoded_text:
            decoded_text += f'{bytes.fromhex(i).decode('utf-8')}\n'
    return decoded_text


def greeting():
    print(f'''{colorama.Fore.MAGENTA}
    ███████╗███╗░░██╗░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░░░░░██╗██████╗░███████╗░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
    ██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░░░░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
    █████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║██║██╔██╗██║██║░░██╗░░░██╔╝░██║░░██║█████╗░░██║░░╚═╝██║░░██║██║░░██║██║██╔██╗██║██║░░██╗░
    ██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██║██║╚████║██║░░╚██╗░██╔╝░░██║░░██║██╔══╝░░██║░░██╗██║░░██║██║░░██║██║██║╚████║██║░░╚██╗
    ███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝██║██║░╚███║╚██████╔╝██╔╝░░░██████╔╝███████╗╚█████╔╝╚█████╔╝██████╔╝██║██║░╚███║╚██████╔╝
    ╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
    \t\t\t\t{colorama.Fore.RED}Created by RKorum in Russia{colorama.Fore.RESET}
    ''')


os.system('')
greeting()

while True:
    try:
        coding = input('1. Encoding   2. Decoding\n3. Encode from file   4. Decode from File\n5. clear the terminal\n>> ')
        if coding == '1':
            text = str(input('Enter text to encode...\n>> '))
            new_text = encode(text)
            print(f'{colorama.Fore.CYAN}Encoded text:{colorama.Fore.LIGHTWHITE_EX}\n {new_text}\n{colorama.Fore.RESET}')
        elif coding == '2':
            encoded_text = str(input('Enter text to decode...\n>> '))
            original_text = decode(encoded_text)
            print(f'{colorama.Fore.CYAN}Decoded text:{colorama.Fore.LIGHTWHITE_EX}\n {original_text}\n{colorama.Fore.RESET}')
        elif coding == '3':
            file_path = str(input('Enter path to file...\n>> '))
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                lines = encode(lines)
                with open(file_path, 'w') as f:
                    f.write(lines)
                print(f'\n{colorama.Fore.GREEN}Файл успешно зашифрован{colorama.Fore.RESET}\n')
            except Exception as e:
                print(f'{colorama.Fore.RED}Error, enter current path to file (error from console: {e}){colorama.Fore.RESET}')

        elif coding == '4':
            file_path = str(input('Enter path to file...\n>> '))
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                lines = decode(lines)
                with open(file_path, 'w') as f:
                    f.write(lines.replace('\n\n', '\n'))
                print(f'\n{colorama.Fore.GREEN}Файл успешно расшифрован{colorama.Fore.RESET}\n')

            except Exception as e:
                print(f'{colorama.Fore.RED}Error, enter current path to file (error from console: {e}){colorama.Fore.RESET}')

        elif coding == '5':
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            greeting()

        else:
            print(f'{colorama.Fore.RED}Invalid choice. Enter 1 for encoding or 2 for decoding or 3 and 4 for encode/decode from file or 5 for clear the terminal.{colorama.Fore.RESET}')
    except ValueError:
        print(f'{colorama.Fore.RED}Please enter a valid number (1 for encoding, 2 for decoding, 3 and 4 encode/decode from file or 5 for clear the terminal).{colorama.Fore.RESET}')
