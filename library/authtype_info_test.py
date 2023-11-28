"""
File: authtype_info_test.py
Assignment: Mini-Project 3
Lanuguage: python3
Author: Sean Kells <spk3077@rit.edu>
Purpose: Test authtype_info ansible module
Running: python3 authtype_info_test.py <site> <authtype>
Example Run: python3 authtype_info_test.py http://httpbin.org/basic-auth/foo/bar Basic
"""
from authtype_info import *

VALID_AUTH_SCHEMES: set = {
    'Basic', 
    'Digest',
    'Bearer',
    'HOBA',
    'Mutual',
    'Negotiate',
    'VAPID',
    'SCRAM',
    'AWS4-HMAC-SHA256'
}

def _check_input():
    """
    _check_input checks for input errors

    :return: Nothing
    """
    # Check invalid argument number (too few arguments)
    if len(sys.argv) < 3:
        print("Too few input arguments are present; two is necessary")
        print("EX: python3 authtype_info_test.py <site> <authtype>")
        print("EX: python3 authtype_info_test.py http://httpbin.org/basic-auth/foo/bar Basic")
        exit(1)
    
    # Check invalid argument number (too many arguments)
    elif len(sys.argv) > 3:
        print("Too many input arguments; two is necessary")
        print("EX: python3 authtype_info_test.py <site> <authtype>")
        print("EX: python3 authtype_info_test.py http://httpbin.org/basic-auth/foo/bar Basic")
        exit(1)

    # Check <authtype> Argument Validity
    elif sys.argv[2] not in VALID_AUTH_SCHEMES:
        print("The specified authentication scheme is not supported")
        print("EX: python3 authtype_info_test.py <site> <authtype>")
        print("EX: python3 authtype_info_test.py http://httpbin.org/basic-auth/foo/bar Basic")
        exit(1)


def main():
    """
    main is the entry to the test code

    :return: Nothing
    """
    _check_input()
    if check_request(sys.argv[1], sys.argv[2]):
        print("Success! Authentication Scheme was present.")
    else:
        print("Failed! Authentication scheme not present.")


if __name__ == '__main__':
    main()