"""This module shows various examples of computing hashes."""

import hashlib
import requests

# Computing hash of a string
STRING_TO_HASH = 'This is a string'
HASH_OF_STRING = hashlib.sha256(STRING_TO_HASH).hexdigest()
print "Hash of string: " + STRING_TO_HASH + " is " + str(HASH_OF_STRING)

# Computing hash of a file
FILE_NAME = 'test_file.txt'
with open(FILE_NAME) as file_handle:
    FILE_CONTENT = file_handle.read()
    HASH_OF_FILE = hashlib.sha256(FILE_CONTENT).hexdigest()
print "Hash of file: " + str(FILE_NAME) + " is " + str(HASH_OF_FILE)

# Computing hash of a web document
WEB_URL = 'https://en.wikipedia.org/wiki/Mahatma_Gandhi'
RESPONSE = requests.get(WEB_URL)
WEB_DOCUMENT = RESPONSE.text.encode('utf-8')
HASH_OF_WEB_DOCUMENT = hashlib.sha256(WEB_DOCUMENT).hexdigest()
print "Hash of content of web page: " + str(WEB_URL) + " is " + str(HASH_OF_WEB_DOCUMENT)
