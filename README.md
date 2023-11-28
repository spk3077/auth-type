# auth-type: Custom Ansible Module: authtype_info


counts all seen responses containing a particular Auth Type, and then prints discovered.

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


## Running

    # Activate VENV
    source myvenv/bin/activate

    # Execute playbook
    ansible-playbook play.yml

    # Deactivate VENV
    deactivate