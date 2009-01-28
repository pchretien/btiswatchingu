-------------------------------------------------------------------------------
-- BTisWatchingU --
-------------------------------------------------------------------------------

Python files:
	- python/bt_db.py
	- python/bt_db_mysql.py
	- python/bt_device.py
	- python/bt_main.py
	- python/bt_ping.py
	
Database files:
	- mysql/v1.0.0/table/bt_device.sql		Creates the table bt_device for the first time
	- mysql/v1.0.0/table/bt_device_name.sql		Creates the table bt_device_name for the first time
	- mysql/v1.0.0/table/location.sql		Creates the table bt_location for the first time
	- mysql/v1.0.0/table/ping.sql			Creates the table bt_ping for the first time
	- mysql/v1.0.0/table/bt_user.sql		Creates the table bt_user for the first time
	
Other files:
	- README.txt 			this file
	- LICENSE.txt 			GPL license
	- .project			Eclipse project file
	- .pydevproject			Eclipse PyDev project file
	- python/bt_db_mysql.config	MySql connection parameters
	
Dependencies:
	- MySql database server
	  http://www.mysql.com/
	  
	- MySqldb library for python
	  http://sourceforge.net/projects/mysql-python
	
	- PyBluez bluetooth library for python
	  http://code.google.com/p/pybluez/
	  
This program scans for bluetooth devices and add their address and name to a 
centralized database. This database have some simple facilities to determine
where and when the device have been spotted.

You will find the latest version of this code at the following address:
http://github.com/pchretien

You can contact me at the following email address:
philippe.chretien@gmail.com

Thank you,

Philippe Chrétien