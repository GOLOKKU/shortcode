import os
import platform
import sys
import subprocess as su

def findString(filename, string):
    for i in open(filename, "r"):
        if string in i:findString.r=i

#Make execution command shell faster
def exe(command):
    os.system(command)

#main
def main():
    print("Checking graalvm github please wait : ")
    exe("curl https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest -o get.json")
    main.x = input("Input java version you want to install (8/11): ")
    main.systemos=""
    k = platform.system()
    print("checking OS please wait")
    if "com.termux" in sys.executable:
        print("Termux detected")
        api()
        Termux()
    elif "Linux" in k:
        main.systemos="linux"
        a = su.getoutput("cat /etc/*-release")
        #still looking for alternative
        a=(str(a).split("\n")[0]).split("DISTRIB_ID=")[1]
        if "Ubuntu" or "Debian" in a:
            print("Debian-Ubuntu Detected")
            api()
            Debian()
        else:
            print("Unable to Start Only support Debian-Ubuntu Linux for this time")
    elif "Windows" in k:
        main.systemos="linux"
        print("Windows Detected")
        api()
        Windows()
    else:
        print("Unable to Start Only support \nDebian-Ubuntu,Windows,Termux for this time")

def api():
    findString("get.json", f'"name": "graalvm-ce-java{main.x}-{main.systemos}-amd64-')
    api.v=findString.r[45:-10]
    api.l=f"graalvm-ce-java{main.x}-{api.v}/"
    findString("get.json", f"graalvm-ce-java{main.x}-{main.systemos}-amd64-")
    api.a=findString.r[31:-2]
    api.z =(f"Graalvm{main.x}.tar.gz")

#Installing on System
def Debian():
    exe("sudo apt update ; sudo apt install unzip tar")
    exe(f"sudo wget {api.a} -o {api.z}")
    exe(f"tar -xzf {api.z}")
    exe(f"sudo mkdir /usr/lib/jvm ; sudo mv {api.l} /usr/lib/jvm")
    exe(f"echo 'export PATH=/usr/lib/jvm/{api.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME=/usr/lib/jvm/{api.l}' >> ~/.bashrc")

def Termux():
    path = "/data/data/com.termux/files/usr/bin/java/"
    exe("pkg update ; pkg install unzip tar")
    exe(f"wget {api.a} -o {api.z}")
    exe(f"tar -xzf {api.z}")
    exe(f"mkdir {path} ; mv {api.l} {path}")
    exe(f"echo 'export PATH={path}{api.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME={path}{api.l}' >> ~/.bashrc")

def Windows():
    ps = "powershell"
    exe(f"{ps} wget {api.a} -o {api.z}")
    exe(f"{ps} tar -xzf {api.z}")
    exe("mkdir C:\Java")
    exe(f"{ps} mv {api.l}")
    exe('setx /M PATH "C:\java\bin;%PATH%"')
    exe('setx /M JAVA_HOME "C:\java"')

main()
