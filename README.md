# teletel
A Python program to programatically run commands on servers via telnet  

## What does this do?
teletel lets you send any number of command to any number of servers via telnet.  

## Why telnet? It's insecure, why not use ssh?
Hey, I never said it was. I plan on adding ssh support eventually. If you need something sent securely just write a shell script or use Ansible. This is meant to be quick and simple for now.  

## Who would use this?
Ideally, you would use this on a server where you can't run ssh for whatever reason. It was originally written to run quick status checks on mission critical servers that ran a stripped down version of QNX.

## What's upcoming?

* Finish support for reading commands and servers from files
* Tidy up he verbose display code
* Change up the options to better match usage
* Maybe add ssh support as an option?
* Bug check some more
* Figure out a way to multiple multiple args with the same command
