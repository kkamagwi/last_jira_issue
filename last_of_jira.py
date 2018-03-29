import sys
import os
from optparse import OptionParser

from jira import JIRA

SERVER = os.environ.get('SERVER')

def last_issue_by_user(username, password, assignee):
    jira = JIRA(basic_auth=(username, password), options={'server': SERVER})
    var = "assignee = '{}' order by created desc".format(assignee)
    last_issue = jira.search_issues(var)[0]
    issues = jira.issue(last_issue)
    issue = issues.fields.issuetype.name
    print(issue, 'by ', assignee)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username", help="Username from JIRA")
    parser.add_option("-p", "--password", dest="password", help="Password from JIRA")
    parser.add_option("-a", "--assignee", dest="assignee", help="Assignee in JIRA")

    (options, args) = parser.parse_args()
    if not options.username or not options.assignee:
        parser.print_help()
        sys.exit(0)

    print(last_issue_by_user(options.username, options.password, options.assignee))
