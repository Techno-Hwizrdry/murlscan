# MurlScan
A Python 3 script that detects malicious URLs.

## Prerequisites
This module requires python3 (version 3.6 or later) and python3-pip.

These prerequisites can be installed on a Debian based linux machine, like so:

`sudo apt-get install python3 python3-pip`

You will also need an API key from IP Quality Score to use this module.  You can sign up for one [here.](https://www.ipqualityscore.com/create-account)

## Setup
Once those prerequisites have been installed, git clone this repo, cd into it, and set up the virtual environment:

`cd /path/to/murlscan && ./setup_virtualenv.sh`

setup_virtualenv.sh will set murlscan as the virtual environment, activate it, and call pip3 to download and install all the python3 dependencies for this script.  These dependencies are listed in requirements.txt.

### MurlScan Config File
Set APIKEY in murlscan.conf to your IP Quality Score API key.

STRICTNESS can be either 0, 1, or 2.  Stricter checks may provide a higher false-positive rate. It is recommend to defaulting to level "0", the lowest strictness setting, and increasing to "1" or "2" depending on your levels of abuse.

## Usage
To scan a single URL:

`python3 murlscan.py -u https://example.com`

To scan multiple URLs:

`python3 murlscan.py -i urls.txt`

Your input text file should list 1 URL per line.

To output the results with all their fields to a csv file:

`python3 murlscan.py -i urls.txt -o output.csv`

murlscan.py will use ./murlscan.conf by default, but you can specify a different filepath if it's located elsewhere:

`python3 murlscan.py -i urls.txt -c path/to/murlscan.conf`

Help:

`python murlscan.py -h`
