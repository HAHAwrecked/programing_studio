#!/usr/bin/env python3
import sys
import hashlib

hash_string="02000000000"
 
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

print (encrypt_string(hash_string))

print ((encrypt_string(encrypt_string(hash_string))))


