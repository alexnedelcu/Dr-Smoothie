Dr-Smoothie
===========

frontend instruction.

git is ignoring all the node modules and platform stuff and www as well.

I have not tested a fresh pull of this project. But here is what you probably need to do.

global #do npm install -g grunt-cli

After pulling the project go to frontend\com\example\drsmoothie
	
	
	# do "bower install"
	# do "npm install" (it will install all the stuff needed)
	
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
