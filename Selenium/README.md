For the first time, just install selenium in your system
Use command "pip install selenium" to install selenium module
Now download geckodriver from https://github.com/mozilla/geckodriver/releases 
And untar it using command "tar -xvzf gecko*" 
And make it executive using command "chmod +x geckodriver"
Now place it in /usr/local/bin using command "sudo mv geckodriver /usr/local/bin/"
And now finally you are ready to go.



For the first time
Open terminal and type python and Enter:
Now enter the following code:-

from selenium import webdriver
driver = webriver.Firefox()
driver.get("http://www.discord.com/login")



And now enter your email and password andd login
It may ask to solve captcha.
Solve it and make sure App is working fine.
Now just close the firefox.

In Terminal too, just press Ctrl + D and now you are good to go:-


Finally run the provided script "Discord.py"
