# Created by -  Zahed Khan
import os

from PyInquirer import style_from_dict, Token, prompt
from CryptoLibrary.utils import CryptoUtility

__version__ = '0.0.1'


class guild_encrypter(object):

    def __init__(self):
        self.key_path = None
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
                'choices': ['Guild Encrypt', 'Guild Decrypt', 'Open config', 'Quit'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['questions'] == 'Guild Encrypt'.lower():
            self.encrypt()
        elif answer['questions'] == 'Guild Decrypt'.lower():
            self.decrypt()
        elif answer['questions'] == 'Open config'.lower():
            self.open_config()
        else:
            print('Bye Bye Guild QA...')
            pass

    def encrypt(self):  # 1
        questions = [
            {
                'type': 'password',
                'message': 'Enter the string to be encrypted:',
                'name': 'password'
            }
        ]
        crypto = CryptoUtility(self.key_path)
        if not crypto.import_public_key_from_file():
            print('No public Key found!')
        else:
            answer = prompt(questions, style=self.style)
            print('Encrypted password: (use inlc. "crypt:")\n')
            cipher_text = crypto.encrypt_text(answer['password'])
            print(cipher_text)
            print()
        self.main_menu()

    def decrypt(self):  # 2
        questions = [
            {
                'type': 'input',
                'name': 'cipher_text',
                'message': 'Input encrypted cipher text:',
            }
        ]
        input_password = [
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter the password of private key to decrypt:'
            }
        ]
        answer = prompt(questions, style=self.style)
        crypto = CryptoUtility(self.key_path)
        if not crypto.password:
            input_pwd = prompt(input_password, style=self.style)
            crypto.password = input_pwd['password']
        crypto.import_private_key_from_file()
        password = crypto.decrypt_text(answer['cipher_text'])
        print(f'Your password is: {password}')
        print()
        self.main_menu()

    def open_config(self):  # 3
        questions = [
            {
                'type': 'list',
                'name': 'questions',
                'message': 'Guild QA Team! What do you want to do?',
                'choices': ['Configure key pair',
                            'Configure public key',
                            'Back'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['questions'] == 'Configure key pair'.lower():
            self.configure_key_pair()
        elif answer['questions'] == 'Configure public key'.lower():
            self.configure_public_key()
        else:
            self.main_menu()

    def configure_key_pair(self):  # 3.1
        questions = [
            {
                'type': 'list',
                'name': 'questions',
                'message': 'Guild QA Team! What do you want to do?',
                'choices': ['Generate key pair',
                            'Set key path',
                            'Set key pair from string',
                            'Delete key pair',
                            'Save private key password',
                            'Delete saved password',
                            'Back'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['questions'] == 'Generate key pair'.lower():
            self.generate_key_pair()
        elif answer['questions'] == 'Set key path'.lower():
            self.set_key_path()
        elif answer['questions'] == 'Set key pair from string'.lower():
            self.set_key_pair_from_string()
        elif answer['questions'] == 'Delete key pair'.lower():
            self.delete_key_pair()
        elif answer['questions'] == 'Save private key password'.lower():
            self.save_private_key_password()
        elif answer['questions'] == 'Delete saved password'.lower():
            self.delete_saved_password()
        else:
            self.open_config()

    def generate_key_pair(self):  # 3.1.1
        questions = [
            {
                'type': 'list',
                'name': 'regenerate',
                'message': 'Do you want to regenerate the key pair?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            },
            {
                'type': 'list',
                'name': 'save_pwd',
                'message': 'Do you want save password?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower(),
                'when': lambda answer: answer['regenerate'] == 'yes'
            }
        ]
        crypto = CryptoUtility(self.key_path)

        answer = prompt(questions, style=self.style)

        if answer['regenerate'] == 'yes':
            crypto.generate_key_pair()
            print('Generating key pair...')
            crypto.password = self._set_password()
            if answer['save_pwd'] == 'yes':
                print(crypto.export_password_hash_to_file())
            else:
                crypto.delete_password_hash_file()
            print(crypto.export_private_key_to_file())
            print(crypto.export_public_key_to_file())
            print('Key pair successfully generated!\n')
            self._show_public_key()
            self.configure_key_pair()
        else:
            self.configure_key_pair()

    def set_key_path(self):  # 3.1.2
        questions = [
            {
                'type': 'input',
                'name': 'key_path',
                'message': 'Input path of key store folder:',
            },
            {
                'type': 'list',
                'name': 'create_dir',
                'message': 'Directory does not exist, do you want to create it?',
                'choices': ['Yes', 'No'],
                'when': lambda answer: not os.path.isdir(answer['key_path']),
                'filter': lambda val: val.lower()
            }
        ]

        answer = prompt(questions, style=self.style)
        key_path = answer['key_path']
        if key_path != '':
            if 'create_dir' in answer and answer['create_dir'] == 'yes':
                if not os.path.isdir(key_path):
                    try:
                        os.mkdir(key_path)
                    except OSError as e:
                        print(e)
            if not os.path.isdir(key_path):
                print(f'key_path: "{key_path}" is not a valid directory!')
            elif not os.access(key_path, os.W_OK | os.X_OK):
                print(f'Permission Denied.'
                      f'key_path: "{key_path}" is not writeable or not executable.')
            self.key_path = key_path
        self.configure_key_pair()

    def set_key_pair_from_string(self):  # 3.1.3
        questions = [
            {
                'type': 'input',
                'name': 'private_key_store',
                'message': 'Input private key store json:',
            },
            {
                'type': 'password',
                'message': 'Enter the password to decrypt private key:',
                'name': 'password',
                'when': lambda answer: answer['private_key_store'] != ''
            }
        ]

        new_password = [
            {
                'type': 'list',
                'name': 'new_pwd',
                'message': 'Do you want set a new password?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]

        save_password = [
            {
                'type': 'list',
                'name': 'save_pwd',
                'message': 'Do you want to save password?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]

        crypto = CryptoUtility(self.key_path)
        answer = prompt(questions, style=self.style)
        if answer['private_key_store'] != '':
            print('Setting key pair...')
            try:
                crypto.password = answer['password']
                if not crypto.set_private_key(answer['private_key_store']):
                    self.configure_key_pair()

                answer = prompt(new_password, style=self.style)
                if answer['new_pwd'] == 'yes':
                    crypto.password = self._set_password()

                answer = prompt(save_password, style=self.style)
                if answer['save_pwd'] == 'yes':
                    crypto.export_password_hash_to_file()
                else:
                    crypto.delete_password_hash_file()
                print(crypto.export_private_key_to_file())
                print(crypto.export_public_key_to_file())
                print('Key pair successfully generated!')
            except Exception as e:
                print(e)
        self.configure_key_pair()

    def delete_key_pair(self):  # 3.1.4
        delete_password = [
            {
                'type': 'list',
                'name': 'delete_keys',
                'message': 'Do you really want to delete key pair?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(delete_password, style=self.style)
        if answer['delete_keys'] == 'yes':
            crypto = CryptoUtility(self.key_path)
            if crypto.delete_key_store():
                print('Successfully deleted!')
        self.configure_key_pair()

    def save_private_key_password(self):  # 3.1.5
        input_password = [
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter the password to decrypt private key:'
            }
        ]
        crypto = CryptoUtility(self.key_path)

        if not crypto.password:
            input_pwd = prompt(input_password, style=self.style)
            crypto.password = input_pwd['password']
            if crypto.import_private_key_from_file():
                crypto.export_password_hash_to_file()
                print('Saved password successfully!')
            else:
                print('Wrong Password!')
        else:
            print('Password already saved.')
        self.configure_key_pair()

    def delete_saved_password(self):  # 3.1.6
        delete_password = [
            {
                'type': 'list',
                'name': 'delete_pwd',
                'message': 'Guild QA! Do you really want to delete saved password?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(delete_password, style=self.style)
        if answer['delete_pwd'] == 'yes':
            crypto = CryptoUtility(self.key_path)
            if crypto.delete_password_hash_file():
                print('Successfully deleted!')
        self.configure_key_pair()

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
            self.open_config()

    def get_public_key(self):  # 3.2.1
        self._show_public_key()
        self.configure_public_key()

    def set_public_key_from_string(self):  # 3.2.2
        questions = [
            {
                'type': 'input',
                'name': 'public_key',
                'message': 'Input public_key as Base64:',
            }
        ]
        crypto = CryptoUtility(self.key_path)
        answer = prompt(questions, style=self.style)
        if answer['public_key'] != '':
            try:
                crypto.set_public_key(answer['public_key'])
                print(crypto.export_public_key_to_file())
                print('Key successfully stored!\n')
            except Exception as e:
                print(e)
        self.configure_public_key()

    def delete_public_key(self):
        delete_password = [
            {
                'type': 'list',
                'name': 'delete_public',
                'message': 'Guild QA Team! Do you really want to delete public key?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        answer = prompt(delete_password, style=self.style)
        if answer['delete_public'] == 'yes':
            crypto = CryptoUtility(self.key_path)
            if crypto.delete_public_key_file():
                print('Successfully deleted!')
        self.configure_public_key()

    def _set_password(self):
        questions = [
            {
                'type': 'password',
                'message': 'Guild QA Team! Enter the password to secure the private key:',
                'name': 'password1'
            },
            {
                'type': 'password',
                'message': 'Guild QA Team! Reenter the password to secure the private key:',
                'name': 'password2'
            }
        ]
        answer = prompt(questions, style=self.style)
        if answer['password1'] != answer['password2']:
            print('The entered passwords are not equal. Please retry:')
            password = self._set_password()
        elif answer['password1'] == '' or not answer['password1']:
            print('Passwords shall not be empty!')
            password = self._set_password()
        else:
            password = answer['password1']
        return password

    def _show_public_key(self):
        crypto = CryptoUtility(self.key_path)
        key = crypto.import_public_key_from_file()
        if key:
            print(f'Public Key: {key}')
            print()


if __name__ == "__main__":
    guild_encrypter().main()
