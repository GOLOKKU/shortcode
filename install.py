import os

def findString(filename, string):
    for i in open(filename, "r"):
        if string in i:findString.r=i

def exec(command):
    os.system(command)

e="sudo"

exec(f"{e} apt-get update ; sudo apt-get install gcc zlib1g-dev build-essential unzip")

print("Checking graalvm github please wait : ")

exec("curl https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest -o get.json")

x = (str(input("Input java version you want to install (8/11): ")))

findString("get.json", f'"name": "graalvm-ce-java{x}-linux-amd64-')

v=findString.r[45:-10]

l=f"graalvm-ce-java{x}-{v}/"

findString("get.json", f"graalvm-ce-java{x}-linux-amd64-")

a=findString.r[31:-2];z =(f"Graalvm{x}.tar.gz")

exec(f"{e} wget {a} -o {z}")

exec(f"tar -xzf {z}")

exec(f"sudo mkdir /usr/lib/jvm")

exec(f"sudo mv {l} /usr/lib/jvm")

exec(f"echo 'export PATH=/usr/lib/jvm/{l}/bin:$PATH' >> ~/.bashrc")

exec(f"echo 'export JAVA_HOME=/usr/lib/jvm/{l}' >> ~/.bashrc")

print('Installation are done please execute "source ~/.bashrc"')
