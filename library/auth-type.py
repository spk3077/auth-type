#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
      fields = {
		"type": {
            "required": True,
            "choices": ['Basic', 'Digest', 'Bearer', 'HOBA', 'Mutual', 'Negotiate', 'VAPID', 'SCRAM', 'AWS4-HMAC-SHA256'],
            "type": "str"
        },
		"webfile": {"required": True, "type": "str" },
        "state": {
        	"default": "present", 
        	"choices": ['present', 'absent'],  
        	"type": 'str' 
        }
	}


	module = AnsibleModule(argument_spec=fields)
	response = {"hello": "world"}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()