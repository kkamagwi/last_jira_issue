# Last of JIRA

Program "last of JIRA" created to find last issue of each user

Application:

  - get nick from JIRA.
  - display statics in command line.

## First
To work with our program you need:
- Python 2.7 or 3.5
- Virtual enviremet
- Sys, requests, optparse libs
- JIRA account.

## How to install requirments
You should copy this command in to command line:
```sh
$ pip install -r requirements.txt
```
# To run program
You may insert
```sh
python3 last_of_jira.py -u username -p password -a assignee_username
```