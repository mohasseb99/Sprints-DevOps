# Sprints-DevOps
Task of devops training
<h4> Steps </h4>
- install git on your computer </br>
- create a directory called Sprints-DevOps  </br>
- cd into Sprints-Devops </br>
- inititialize git inside the directory </br>
- create a repo on your github account called: Sprints-DevOps </br>
- using the web interface of github add a new file README.md </br>
- commit the file with message "My First Git Commit from the web" </br>
- add remote repo to your local repo </br>
- create new branches (Dev, Test, Production) </br>
- change to Dev Branch </br>
- create a module (sprints.py) with function "MyFunc()" as mentioned below: </br>
	-- the function takes a list of integers and floats </br>
	-- return the mean value of even integer numbers </br>
	-- returns the max number of float point numbers </br>
	-- return 0 if the list doesn't contain neither int nor float </br>
</br>
- commit your changes with message "Task 01: sprints.MyFunc" </br>
- change to Test Branch </br>
- create a python file "test.py" </br>
- import sprints.py and call the function and test it with the lists </br>
		-- hint: https://realpython.com/python-testing/ </br>
- run the test on the code and commit with message "Task 02: Tests Passed" </br>
- change to Production Branch </br>
- write a bash script sshd.sh to do the following: </br>
	-- get an integer number input from the user Change the SSH Port </br>
	-- make sure the port is accepted in range </br>
	-- disable root login to system </br>
	-- make sure that there's at least one user with sudo privilege </br>
- add files that are passed from Test </br>
- commit your changes with message "Task 03: Securing SSH" </br>
- create a DockerFile using image python:3.8 </br>
- set work directory /var/src/app </br>
- copy all the files in local directory to the container </br>
- commit your changes to repo with message "Task 04: DockerFile added" </br>