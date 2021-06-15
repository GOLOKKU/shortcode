# Graalvm Install script

GOLOK KU [Python](https://www.python.org/)3 script to install [Graalvm java](https://www.graalvm.org/) 8/11

### Feature
 - Install Graalvm java latest version using [Github API](https://docs.github.com/en/free-pro-team@latest/rest)
 - Easy to install only one line command line
 - Linux,Windows, MacOS(Not tested yet)
 - Checksum download check
 
#### [Todo](https://github.com/GOLOKKU/Graalvm-Java-Install/blob/main/other/todo.md)

### Installation
Requirement : Python3, Wget

Installation command
#### Linux
```sh
wget https://raw.githubusercontent.com/GOLOKKU/Graalvm-Java-Install/main/install.py -o install.py && python install.py
```
#### Windows (cmd run as admin)
```sh
wget https://raw.githubusercontent.com/GOLOKKU/Graalvm-Java-Install/main/install.py -o install.py ; python install.py
```
#### Info 

Linux
Default graavlm install path `/usr/lib/jvm/` Tested

Windows
Default graavlm install path `C:\Java` Tested

MacOS
Default graavlm install path `/Library/Java` Not tested

if you found any problem you can [Report here](https://github.com/GOLOKKU/shortcode/issues)

License [MIT](https://github.com/GOLOKKU/Graalvm-Java-Install/blob/main/LICENSE)
