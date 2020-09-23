
# devops-task-server

A lightweight task server similar to Jenkins, but intended for Devops.

# Setup Instructions:

Download Git and install Git Bash
  [https://git-scm.com/downloads](https://git-scm.com/downloads)

Once Installed, generate an SSH Key 
```
$ ssh-keygen -t rsa -b 4096 -C
```

Add id_rsa.pub to your github account:
[https://github.com/settings/keys](https://github.com/settings/keys)

Clone this git repository 
```
$ git clone  git@github.com:rpiskule-lewis/devops-task-server
```

### Windows Home

If you are running windows home, you may need to update windows. This can take serveral hours:  
[https://www.microsoft.com/en-us/software-download/windows10](https://www.microsoft.com/en-us/software-download/windows10)

You will then need to install this (Steps 1-6). This will take about 30 minutes:  
[https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package)

# Running the Container
Included in this repository is startup.bat. Once Docker Desktop is installed, simply run `startup.bat` and the container will compile and run. 