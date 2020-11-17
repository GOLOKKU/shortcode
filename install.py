import os
import platform
import sys

#ReadFile And Find String
def findString(filename, string):
    for i in open(filename, "r"):
        if string in i:findString.r=i

#Make execution command shell faster
def exe(command):
    os.system(command)

#main
def main():
    #geting Graalvm latest version using github API
    print("Checking graalvm github please wait : ")
    exe("curl https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest -o get.json")
    x = (str(input("Input java version you want to install (8/11): ")))
    
    findString("get.json", f'"name": "graalvm-ce-java{x}-linux-amd64-')
    v=findString.r[45:-10]
    l=f"graalvm-ce-java{x}-{v}/"
    findString("get.json", f"graalvm-ce-java{x}-linux-amd64-")
    a=findString.r[31:-2]
    z =(f"Graalvm{x}.tar.gz")

    k = platform.system()
    print("checking OS please wait")
    if "Linux" in k:
        if "com.termux" in sys.executable:
            print("Termux detected")
        else:
            print("Linux Detected")
            linux()
        Termux()
    elif "Windows" in k:
        print("Windows")
        Windows()

#Installing on System
def linux():
    exe("sudo apt-get update ; sudo apt-get install gcc zlib1g-dev build-essential unzip")
    exe(f"sudo wget {main.a} -o {main.z}")
    exe(f"tar -xzf {main.z}")
    exe(f"sudo mkdir /usr/lib/jvm ; sudo mv {main.l} /usr/lib/jvm")
    exe(f"echo 'export PATH=/usr/lib/jvm/{main.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME=/usr/lib/jvm/{main.l}' >> ~/.bashrc")

def Termux():
    path = "/data/data/com.termux/files/usr/bin/java/"
    exe("pkg update ; pkg install build-essential unzip")
    exe(f"wget {main.a} -o {main.z}")
    exe(f"tar -xzf {main.z}")
    exe(f"mkdir {path} ; mv {main.l} {path}")
    exe(f"echo 'export PATH={path}{main.l}/bin:$PATH' >> ~/.bashrc")
    exe(f"echo 'export JAVA_HOME={path}{main.l}' >> ~/.bashrc")

def Windows():
    ps = "powershell"
    exe(f"{ps} wget ")
    exe(f"{ps} tar -xzf {main.z}")
    exe("mkdir C:\Java")
    exe(f"{ps} mv {main.l}")
    exe(f"{main.l}")
    exe('setx /M PATH "C:\java\bin;%PATH%"')
    exe('setx /M JAVA_HOME "C:\java"')

main()
