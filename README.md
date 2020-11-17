# Graalvm Install script

GOLOK KU [Python](https://www.python.org/) 3 script to install [Graalvm]() 8/11

### Feature
 - Install Graalvm java latest version using [Github API](https://www.graalvm.org/)
 - Easy to install
 
### Todo :
 - ~~Add termux install support~~
 - ~~Add windows install support~~
 - ~~Make Code more readable~~ Thanks [@f77-droid](https://github.com/f77-droid)
 - Add option install location
 - ???
### Installation
Requirement : All already packaged

Installation GUIDE
#### Debian-Ubuntu
```sh
wget https://github.com/GOLOKKU/Graalvm-Java-Install/blob/main/install.py ; sudo python3 install.py ; source ~/.bashrc
```
#### Termux
```sh
wget https://github.com/GOLOKKU/Graalvm-Java-Install/blob/main/install.py ; python3 install.py ; source ~/.bashrc
```
#### Windows (Without Command Line)
```sh
Download Graalvm Install script
Run script
```
#### Info 

Ubuntu-Debian
Graavlm located at `/usr/lib/jvm/`

Termux
Graavlm located at `/data/data/com.termux/files/usr/bin/java/`

Windows
Graavlm located at `C:\Java`

Note this is only tested on ubuntu WSL 1 20.04 
if you found any problem you can [Report here](https://github.com/GOLOKKU/shortcode/issues)

License [MIT](https://github.com/GOLOKKU/Graalvm-Java-Install/blob/main/LICENSE)
