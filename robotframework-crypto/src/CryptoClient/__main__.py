
from PyInquirer import style_from_dict, Token, prompt
from CryptoLibrary.utils import CryptoUtility

__version__ = '0.0.1'


class Encrypter(object):

    def __init__(self):
        self.style = style_from_dict({
            Token.QuestionMark: '#fac731 bold',
            Token.Answer: '#06c8ff bold',
            Token.Instruction: '',  # default
            Token.Separator: '#cc5454',
            Token.Selected: '#0abf5b',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Question: '',
        })

    def main(self):
        self.main_menu()

    def main_menu(self):
        questions = [
            {
                'type': 'list',
                'name': 'questions',
                'message': 'Guild QA Team! What do you want to do?',
                'choices': ['Guild Encrypt', 'Open config', 'Quit'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['questions'] == 'Guild Encrypt'.lower():
            self.encrypt()
        elif answer['questions'] == 'Open config'.lower():
            self.configure_public_key()
        else:
            print('Bye Bye Guild QA Team...')
            pass

    def encrypt(self):  # 1
        questions = [
            {
                'type': 'password',
                'message': 'Enter the password to encrypt',
                'name': 'password'
            }
        ]
        crypto = CryptoUtility()
        if not crypto.import_public_key_from_file():
            print('No public Key found!')
        else:
            answer = prompt(questions, style=self.style)
            print('Encrypted password: (use inlc. "guild:")\n')
            cipher_text = crypto.encrypt_text(answer['password'])
            print(cipher_text)

    def configure_public_key(self):  # 3.2
        questions = [
            {
                'type': 'list',
                'name': 'questions',
                'message': 'Guild QA Team! What do you want to do?',
                'choices': ['Set public key from string',
                            'Get public key from string',
                            'Delete public key',
                            'Back'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['questions'] == 'Get public key from string'.lower():
            self.get_public_key()
        elif answer['questions'] == 'Set public key from string'.lower():
            self.set_public_key_from_string()
        elif answer['questions'] == 'Delete public key'.lower():
            self.delete_public_key()
        else:
            self.main_menu()

    def get_public_key(self):  # 3.2.1
        self._show_public_key()

    def set_public_key_from_string(self):  # 3.2.2
        questions = [
            {
                'type': 'input',
                'name': 'public_key',
                'message': 'Input public_key as Base64:',
            }
        ]
        crypto = CryptoUtility()
        answer = prompt(questions, style=self.style)
        if answer['public_key'] != '':
            try:
                crypto.set_public_key(answer['public_key'])
                print(crypto.export_public_key_to_file())
                print('Key successfully stored!\n')
            except Exception as e:
                print(e)
        self.main_menu()

    def delete_public_key(self):
        delete_password = [
            {
                'type': 'list',
                'name': 'delete_public',
                'message': 'Do you really want to delete public key?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(delete_password, style=self.style)
        if answer['delete_public'] == 'yes':
            crypto = CryptoUtility()
            if crypto.delete_public_key_file():
                print('Successfully deleted!')

    def _show_public_key(self):
        crypto = CryptoUtility()
        key = crypto.import_public_key_from_file()
        if key:
            print(f'Public Key: {key}')
            print()


if __name__ == "__main__":
    Encrypter().main()
