# authtype_info: Custom Ansible Module
Determine if input HTTP authentication type exists in input list of websites. Output discovered sites from the input list to the registered result, 'site'.


## Prerequisites
The script assumes you are running the web server on the latest Ubuntu version.
Run the necessary commands below:

    # Update APT Packages
    sudo apt update

    # Upgrade current packages (ought to get latest Python)
    sudo apt upgrade

    # Install ansible-playbook
    sudo apt install ansible-playbook

    # Install python (should be present)
    sudo apt install python3

    # Install venv
    apt install python3.10-venv

    # Install Python Dependencies
    pip install -r library/requirements.txt


## Options
The following options are used to operate the custom ansible module in ansible:

    **type**
    required: True
    choices: 'Basic', 'Digest', 'Bearer', 'HOBA', 'Mutual', 'Negotiate', 'VAPID', 'SCRAM', 'AWS4-HMAC-SHA256'
    type: str

    The HTTP authentication type to search for within the list of provided websites

    **webfile**
    required: True
    type: str

    The path to a formatted, each line contains a single URL, text file containing a list of websites to assess


## Running

    # Activate VENV
    source myvenv/bin/activate

    # Execute playbook
    ansible-playbook play.yml

    # Deactivate VENV
    deactivate