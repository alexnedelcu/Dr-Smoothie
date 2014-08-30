Dr-Smoothie
===========

The following stept are needed for whoever is interested in running the application on a mobile platform.

1) Install NodeJS from http://nodejs.org/

2) Open a Command Prompt / Shell and type npm install -g cordova ionic

3) Chage directory to the app's root directory

	$ cd myApp
	
4) For IOS users only:

	$ ionic platform add ios
	
	$ ionic build ios
	
	$ ionic emulate ios
	
5) For Android users only: $ ionic platform add android

	$ ionic build android
	
	$ ionic run android    # (will run in a emulator or on the phone, if it is connected to the computer)

This is it! Now please ignore the rest of this document. :)


TO IMPORT THE DATABASE:
1) Go to the Backend/ directory.
2) Type "manage.py syncdb"
3) Type "manage.py shell"
4) Wait for the python shell to come. Then type "import Database_import"

	
I used this project https://github.com/dsimard/grunt-angular-phonegap. 
you can look at it if you want more detail.
