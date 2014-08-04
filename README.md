Dr-Smoothie
===========

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
	After doing a build, you will see www folder. You can open it to test in browser.
	But since we are using angular and grunt, you can just do "grunt serve" to load in localhost.
	


	
	
	
	
I used this project https://github.com/dsimard/grunt-angular-phonegap. 
you can look at it if you want more detail.
