Dr-Smoothie
===========

Backend Build instructions:
Go to backend folder.
1)run "python manage.py runserver"

TO IMPORT THE DATABASE:
1) Go to the Backend/ directory.
2) Type "manage.py syncdb"
3) Type "manage.py shell"
4) Wait for the python shell to come. Then type "import Database_import"


Frontend:

The following stept are needed for whoever is interested in running the application on a mobile platform.

1) Install NodeJS from http://nodejs.org/

2) Open a Command Prompt / Shell and type npm install -g cordova ionic

3) Chage directory to the app's root directory(frontend)

	$ cd frontend
3.5) for web users 
        ionic serve
	
4) For IOS users only:

	$ ionic platform add ios
	
	$ ionic build ios
	
	$ ionic emulate ios
	
5) For Android users only: $ ionic platform add android

	$ ionic build android
	
	$ ionic run android    # (will run in a emulator or on the phone, if it is connected to the computer)

For Testing: 
   Used Protractor that uses webdriver which uses selenium.
   Tutorial for protractor: https://github.com/angular/protractor/blob/master/docs/tutorial.md 

   npm install -g protractor
   webdriver-manager update
   webdriver-manager start

For runnint tests:
   Goto frontend\test\integration
   run "protractor conf.js"


This is it! Now please ignore the rest of this document. :)




	
I used this project https://github.com/dsimard/grunt-angular-phonegap. 
you can look at it if you want more detail.
