How to use ConfigParser in Python
What is Config Parser?
The configparser module in Python is used for working with configuration files. It is much similar to Windows INI files. You can use it to manage user-editable configuration files for an application. The configuration files are organized into sections, and each section can contain name-value pairs for configuration data. Config file sections are identified by looking for lines starting with [ and ending with ]. The value between the square brackets is the section name, and can contain any characters except square brackets. Options are listed one per line within a section. The line starts with the name of the option, which is separated from the value by a colon (:) or equal sign (=). Whitespace around the separator is ignored when the file is parsed.
A sample configuration file with section “bug_tracker” and three options would look like:
[bug_tracker]
url = http://localhost:8080/bugs/
username = dhellmann
password = SECRET

Common Usage
The most common use for a configuration file is to have a user or system administrator edit the file with a regular text editor to set application behavior defaults, and then have the application read the file, parse it, and act based on its contents. An example would be the MySQL configuration file. The script below will read the /etc/mysql/debian.cnf configuration file to get login details for MySQL, connect to MySQL and ask it for a list of all databases, go through this list calling mysqldump on each one. This script is based on a code snippet I found on http://codepoets.co.uk/2010/python-script-to-backup-mysql-databases-on-debian/ 


Backup all MySQL databases, one in each file with a timestamp on the end.




#Importing the modules
import os
import ConfigParser
import time

# On Debian, /etc/mysql/debian.cnf contains 'root' a like login and password.
config = ConfigParser.ConfigParser()
config.read("/etc/mysql/debian.cnf")
username = config.get('client', 'user')
password = config.get('client', 'password')
hostname = config.get('client', 'host')
filestamp = time.strftime('%Y-%m-%d')

# Get a list of databases with :
database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'information_schema':
        continue
    if database == 'performance_schema':
        continue
    filename = "/backups/mysql/%s-%s.sql" % (database, filestamp)
    os.popen("mysqldump --single-transaction -u %s -p%s -h %s -d %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))
