# devops-task-server
A lightweight task server similar to Jenkins, but intended for Devops.

# Setup Instructions:
Download Git and install Git Bash
https://git-scm.com/downloads

Once Installed, generate an SSH Key
$  ssh-keygen -t rsa -b 4096 -C <youremail>

Add id_rsa.pub to:
https://github.com/settings/keys

Clone the repository
$ git clone https://github.com/rpiskule-lewis/devops-task-server

If you are running windows home, you may need to update windows:
https://www.microsoft.com/en-us/software-download/windows10

You will then need to install this (Steps 1-6):
https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

### Running Without Docker:

Install Python 3.8.5:
https://www.python.org/downloads/release/python-385/
