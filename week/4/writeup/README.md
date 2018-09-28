Writeup 3 - Pentesting I
======

Name: Hamid Aina
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Hamid Aina

## Assignment 4 Writeup

### Part 1 (45 pts)

As we know, Command Injection attacks is a way of system exploitation where hackers take advantage of unchecked inputs to input their own commands. In many cases, they are able to gain root privileges and access system files that aren’t meant to be seen. I began by using the command nc cornerstoneairlines.co 45 to access Fred’s network admin panel. From there I became curious as to how I could make use of command injection. To do so, I entered the IP address for the main page when prompted and put a semi-colon and the command I wanted to execute.

I entered: 142.93.118.186; ls. This enabled me to see all files from the root of Fred’s server. After manipulating the command, I found that I didn’t need an IP address to precede my command. I also found that I had to chain my commands with a semi-colon because Fred’s system only allows one input at a time. So, I did the following: test; cd home; ls. This sequence of commands allowed me to see the contents of the home directory. It was there that I saw a file names flag.txt I wasn’t sure how to read the contents of the file from the command line at first, but this was resolved after a little Google search. 

I entered the following: test; cd home; cat flag.txt and was greeted with the following message: Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}. I first tried going through the bin, boot, and dev directories and didn’t find anything useful. Then I though of the most reasonable place the flag could be and decided to cd into the home directory and I found it.

In the future, I recommend that Fred ensures that he sanitizes user inputs before executing what was entered. By not checking the input, he allowed me to enter his directories and access potentially confidential information.


### Part 2 (55 pts)

My approach consisted of using a general shell and an inner shell. The purpose of the general shell was to respond to the following commands: shell, pull, help, or quit and interface the user upon starting my script. After that I began to implement what would happen for each command case. In the case of a user inputting shell, I entered a while loop for the inner shell that would essentially handle cases of either: an exit command, cd command, and anything else. For the last case, my run function would be called to examine and execute the contents of the command. 
In the case of pull, I executed my run function with a special parameter to indicate that the instructions for a pull should be performed. This included splitting the command string and writing data the second parameter of the pull.
Looking at quit, this was simply an if statement to see whether the input command matched “quit”, and if so I exited the program and closed the socket. 
Lastly, help was implemented in main by using a simple else statement, which meant that if user input didn’t match anything up until this point, just print the usage function. This would apply to help being input, as well as any malformed input.

