# Distributed Data Sharing Protocol (DDSP)
Distributed Data Sharing Protocol (DDSP) is a light weight protocol for decentralizedly sharing data among nodes in local area networks.

## Running Environment
Ubuntu 14.04 Server

Python 3.4.3

netifaces

## Environment Setup
### Change Default Python Version

* Edit ~./bashrc
```
$vim ~./bashrc
```

* Add two lines at the end of the file:
```
alias python=python3  #Change default Python version to Python 3
alias pip=pip3  #Change default Pip version to Pip 3
```

* Apply Modification
```
$source ~./bashrc
```

### Install Netifaces
```
$sudo pip install netifaces
```

## Usage
```
#!python
from DDSP import DDSP
ddsp = DDSP(interface_name, datapath, port)
```
