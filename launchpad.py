import sys
from launchpadlib.launchpad import Launchpad

f = open('LaunchpadBugs.csv', 'w')
launchpad = Launchpad.login_with('My App', 'production', version='devel')
print('Hello, %s!' % launchpad.me.display_name)

project = launchpad.projects[sys.argv[1]]
bug_tasks = project.searchTasks(status=[
    'New', "Won't Fix", 'Incomplete', 'Opinion', 'Expired',
    'Confirmed', 'Triaged', 'Fix Committed', 'Fix Released',
    'Incomplete (with response)', 'Incomplete (without response)'])
rows = []
rows.append('Bug_ID, Title, Date_Created, Status, Importance,Date_Fix_Committed, Date_Fix_Released')
for task in bug_tasks:
    rows.append(
        '%s, %s, %s, %s, %s, %s, %s,' % (
            task.bug.id,
            (task.title).replace(',',' '),
            task.date_created,
            task.status,
            task.importance,
            task.date_fix_committed,
            task.date_fix_released,
            )
        )
for row in rows:
    f.write(row)
    f.write('\n')

f.close()