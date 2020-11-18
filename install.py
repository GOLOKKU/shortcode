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
    x = input("Input java version you want to install (8/11): ")
    sysos()
    findString("get.json", f'"name": "graalvm-ce-java{x}-{sysos.systemos}-amd64-')
    v=findString.r[45:-10]
    l=f"graalvm-ce-java{x}-{v}/"
    findString("get.json", f"graalvm-ce-java{x}-{sysos.systemos}-amd64-")
    a=findString.r[31:-2]
    z =(f"Graalvm{x}.tar.gz")

def sysos():
    k = platform.system()
    print("checking OS please wait")

    if "com.termux" in sys.executable:
        print("Termux detected")
        Termux()
    elif "Linux" in k:
        systemos="linux"
        a = su.getoutput("cat /etc/*-release")
        #still looking for alternative
        a=(str(a).split("\n")[0]).split("DISTRIB_ID=")[1]
        if "Ubuntu" or "Debian" in a:
            print("Debian-Ubuntu Detected")
            Debian()
        else:
            print("Unable to Start Only support Debian-Ubuntu Linux for this time")
    elif "Windows" in k:
        systemos="windows"
        print("Windows Detected")
        Windows()
    else:
        print("Unable to Start Only support \nDebian-Ubuntu,Windows,Termux for this time")

#Installing on System
def Debian():
    exe("sudo apt update ; sudo apt install unzip tar")
    exe(f"sudo wget {main.a} -o {main.z}")
    exe(f"tar -xzf {main.z}")
    exe(f"sudo mkdir /usr/lib/jvm ; sudo mv {main.l} /usr/lib/jvm")
    exe(f"echo 'export PATH=/usr/lib/jvm/{main.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME=/usr/lib/jvm/{main.l}' >> ~/.bashrc")

def Termux():
    path = "/data/data/com.termux/files/usr/bin/java/"
    exe("pkg update ; pkg install unzip tar")
    exe(f"wget {main.a} -o {main.z}")
    exe(f"tar -xzf {main.z}")
    exe(f"mkdir {path} ; mv {main.l} {path}")
    exe(f"echo 'export PATH={path}{main.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME={path}{main.l}' >> ~/.bashrc")

def Windows():
    ps = "powershell"
    exe(f"{ps} wget {main.a} -o {main.z}")
    exe(f"{ps} tar -xzf {main.z}")
    exe("mkdir C:\Java")
    exe(f"{ps} mv {main.l}")
    exe(f"{main.l}")
    exe('setx /M PATH "C:\java\bin;%PATH%"')
    exe('setx /M JAVA_HOME "C:\java"')

main()
