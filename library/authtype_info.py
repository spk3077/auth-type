#!/usr/bin/python
"""
File: authtype_info.py
Assignment: Mini-Project 3
Lanuguage: python3
Author: Sean Kells <spk3077@rit.edu>
Purpose: Determine if authorization type exists in input list of websites
Running: Refer to play.yml
Example Test: ./library ansible -m authtype_info -a 'type=Basic webfile=./webfiles/formatted/top500_formatted.txt' localhost
"""
DOCUMENTATION = r'''
---
module: authtype_info

short_description: This is my test module

version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    type:
        description:
            - Authentication type to check for
            - Possible values: Basic, Digest, Bearer, HOBA, Mutual, Negotiate, VAPID', SCRAM, AWS4-HMAC-SHA256
        required: true
        type: str
    webfile:
        description: Path to file containing list of websites to assess
        required: true
        type: str

author:
    - Sean Kells (@spk3077)
'''

EXAMPLES = r'''
# Auth Type Basic
- name: Test Auth Basic
  authtype_info:
    type: Basic
    webfile: ./webfiles/formatted/top500_formatted.txt

# Auth Type Digest
- name: Test Auth Digest
  authtype_info:
    type: Digest
    webfile: ./webfiles/formatted/top500_formatted.txt

# fail the module
- name: Test Failure of Module
  authtype_info:
    type: NTLM # Not a valid choice
    webfile: ./webfiles/formatted/top500_formatted.txt
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
sites:
    description: The sites that had the authorization type specified.
    type: list
    returned: always
    sample: '['https://www.google.com', 'https://jersy.com']
'''
import requests
from ansible.module_utils.basic import *


def check_request(site: str, auth_type: str) -> bool:
    """
    check_request send HTTP GET request to inputted site to assess if authorization type is present

    :param site: the website to assess
    :param auth_type: Authorization type to check for
    :return: if authorization type is present in response headers
    """
    resp = requests.get(site)
    print(resp)
    print("---------------------------------------")
    print(resp.headers)

    return True
    

def get_websites(file_path: str) -> tuple[bool, set]:
    """
    get_websites opens the file specified by file_path and returns list containing file content

    :param file_path: the path to the file
    :return: tuple[if error present, set of sites in file]
    """
    param_sites: set = set()
    has_error: bool = False
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                param_sites.add(line)
            
    except (FileNotFoundError, IOError, Exception):
        has_error = True

    return has_error, param_sites


def main():
    """
    main is the entry to the ansible module

    :return: Nothing
    """
    fields: dict = {
        "type": 
        {
            "required": True,
            "choices": ['Basic', 'Digest', 'Bearer', 'HOBA', 'Mutual', 'Negotiate', 'VAPID', 'SCRAM', 'AWS4-HMAC-SHA256'],
            "type": "str"
        },
        "webfile": 
        {
            "required": True, 
            "type": "str" 
        }
	}
      
    results: dict = {
        'changed' : False,
        'sites' : []
    }
    
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    has_errors, param_sites = get_websites(module.params['webfile'])

    for site in param_sites:
        site(check_request)

    if not has_errors():
        module.exit_json(**results)
    else:
        module.fail_json(**results)


if __name__ == '__main__':
    main()