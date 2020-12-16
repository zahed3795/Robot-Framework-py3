from CryptoLibrary.utils import CryptoUtility
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import re

__version__ = '0.2.4'


class CryptoLibrary(object):
    ROBOT_LIBRARY_DOC_FORMAT = 'reST'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, password=None, variable_decryption=False, key_path=None):
        """
        +--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | **password:**            | Password for private key can be given as argument. This should be stored as secret! Use environment variables instead of hard coding it here.            |
        +--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | **variable_decryption:** | If set to ``True`` all variables that are available on Test Suite or on Test Case start,                                                                 |
        |                          | that contain a encrypted text, will be decrypted automatically.                                                                                          |
        +--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | **key_path:**            | A path that defines where the key pair is stored physically.                                                                                             |
        |                          | Path needs to be an absolute path or relative to ``cryptoutility.py``.                                                                                   |
        +--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        """
        self.ROBOT_LIBRARY_LISTENER = self
        self.value_list = list()
        self.crypto = CryptoUtility(key_path)
        self.original_log_level = 'INFO'
        self.disable_logging = False
        if password:
            self.crypto.password = password
        self.variable_decryption = variable_decryption
        self.builtin = BuiltIn()

    def conceal_text_in_logs(self, text):
        """This keyword conceals the password, passed as input, in the logs.
        Only ``***`` will be shown in the logs.

        Because CrytoLibrary is a global Library, this text will be hidden from the point
        where it is concealed until robot execution ends.
        Earlier appearances will be visible in the logs!"""
        logger.info(f'Conceal the text in the logs.')
        self.value_list.append(text)

    def get_decrypted_text(self, cipher_text):
        """Decrypts cipher text and returns the plain text.

        Example:

        .. code :: robotframework

            ${plain_text}=    Get Decrypted Text    crypt:sZ2i7bIQDlsWKJVhBb+Dz4w=

        """
        logger.info(f'Decrypting text and return value.')
        plaintext = self.crypto.decrypt_text(cipher_text)
        self.value_list.append(plaintext)
        return plaintext

    def suppress_logging(self, disable: bool = True):
        """Disables the logging of robot framework until ``Unsuppress Logging`` has been called."""
        if disable:
            logger.info('disable logging...')
            self.original_log_level = self.builtin.set_log_level('NONE')
        else:
            self.builtin.set_log_level(self.original_log_level)
            logger.info('enable logging...')
            logger.debug(f'Switching Loglevel from NONE to {self.original_log_level}.')

    def unsuppress_logging(self):
        """Enables the logging of robot framework and set it back to the original log level."""
        self.suppress_logging(False)

    def _start_test(self, test, result):
        self._decrypt_variable_in_scope(self.builtin.set_test_variable)

    def _start_suite(self, suite, result):
        self._decrypt_variable_in_scope(self.builtin.set_suite_variable)

    def _decrypt_variable_in_scope(self, set_scope_variable):
        if self.variable_decryption:
            variables = self.builtin.get_variables()
            for var in variables:
                value = self.builtin.get_variable_value(var)
                if isinstance(value, str) and re.fullmatch(self.crypto.CIPHER_PATTERN, value):
                    plain = self.get_decrypted_text(value)
                    set_scope_variable(var, plain)

    def _log_message(self, message):
        if self.value_list:
            pattern = re.compile("|".join([re.escape(x) for x in self.value_list]))
            message.message = pattern.sub('***', message.message)
