# Selenium Python Project Using OrangeHRM Demo Login Page

This project consists of a simple script to login to the [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) web page. This is my initial portfolio project that I will improve upon as I gain more knowledge on Selenium Test Automation.

As I gain more skills in Test Automation, I have also successfully integrated this script using Jenkins.

Started by user admin

Running as SYSTEM
Building in workspace C:\Users\XAVIER\.jenkins\workspace\page-object-model
The recommended git tool is: NONE
using credential e4df4403-a580-47f1-a431-b088dc961457
 > git.exe rev-parse --resolve-git-dir C:\Users\XAVIER\.jenkins\workspace\page-object-model\.git # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/rxavierremo/page-object-model.git # timeout=10
Fetching upstream changes from https://github.com/rxavierremo/page-object-model.git
 > git.exe --version # timeout=10
 > git --version # 'git version 2.44.0.windows.1'
using GIT_ASKPASS to set credentials 
 > git.exe fetch --tags --force --progress -- https://github.com/rxavierremo/page-object-model.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/main^{commit}" # timeout=10
Checking out Revision a6b8f8c6f8d110308f20d8fce2666407bf290f2d (refs/remotes/origin/main)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f a6b8f8c6f8d110308f20d8fce2666407bf290f2d # timeout=10
Commit message: "Updated test script"
 > git.exe rev-list --no-walk a6b8f8c6f8d110308f20d8fce2666407bf290f2d # timeout=10
[page-object-model] $ cmd /c call C:\Users\XAVIER\AppData\Local\Temp\jenkins2103946835878229993.bat

C:\Users\XAVIER\.jenkins\workspace\page-object-model>cd tests 

C:\Users\XAVIER\.jenkins\workspace\page-object-model\tests>pytest .\test_orangehrm_login_page.py 
============================= test session starts =============================
platform win32 -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\XAVIER\.jenkins\workspace\page-object-model\tests
collected 1 item

test_orangehrm_login_page.py .                                           [100%]

============================= 1 passed in 17.04s ==============================

C:\Users\XAVIER\.jenkins\workspace\page-object-model\tests>exit 0 
Finished: SUCCESS

