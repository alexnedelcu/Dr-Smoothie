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





frontend instruction.

git is ignoring all the node modules and platform stuff and www as well.

Here is what you need to do to get working...


After pulling the project go to frontend\com\example\drsmoothie
	
	#do "npm install -g grunt-cli"
	#do "npm install -g bower"
	# do "npm install" (it will install all the stuff needed)
	# do "bower install"
	# do "grunt serve" loads the localhost
	
	# work in the app folder. thats where html files and js files are at.
	# for cordova build 
		-> do "cordova platform add android"
		-> "grunt phonegap:check" 
		-> "grunt phonegap:build"
		-> "grunt phonegap:emulate"
		
	#to debug on android
		-> "grunt phonegap:build"
		-> "phonegap remote login --username you@gmail.com --password YourPassword" (you need to create account first)
		-> "grunt phonegap:send" (will send it to the website and download apk from there)
	After doing a build, you will see www folder. You can open it to test in browser.
	But since we are using angular and grunt, you can just do "grunt serve" to load in localhost.
	


	
	
	
	
I used this project https://github.com/dsimard/grunt-angular-phonegap. 
you can look at it if you want more detail.
