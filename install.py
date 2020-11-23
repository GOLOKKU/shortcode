import os
import platform
import sys
import subprocess as sub
import requests
from zipfile import ZipFile as zip
import tarfile as tar

#PR For zip and tar alternative are welcome
#or maybe i will implement it soon
def unzip(loc, output):
    if loc.endswith("zip"):
        zap=zip(loc, 'r')
        zap.extractall(output)
        zap.close()
    elif loc.endswith("tar.gz"):
        tir = tar.open(loc, "r:gz")
        tir.extractall(output)
        tir.close()
    elif loc.endswith("tar"):
        tir = tar.open(loc, "r:")
        tir.extractall(output)
        tir.close()

def download(url, save, msg, long):
    with open(save, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(long*downloaded/total)
                sys.stdout.write('\r{} [{}{}]'.format(msg,'█' * done, '.' * (long-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

def search(file, string):
    for i in open(file, "r"):
        if string in i:
            search.r=i

def cmd(line):
    os.system(line)

def mkdir(loc):
    os.mkdir(loc)

def mv(loc0, loc1):
    os.rename(loc0, loc1)

def system():
    pl = platform.system()
    if "Linux" in pl:
        system.os="linux"
        if "com.termux" in sys.executable:
            system.path = "/data/data/com.termux/files/usr/bin/java/"
            print("termux detected")
        else:
            system.path = "/usr/bin/java/"
    elif "Windows" in pl:
        system.path = "C:\java"
        system.os="windows"
        print("Windows Detected")
    else:
        print("Unable to Start Only support :"
        "Linux,Windows,Termux for this time "
        "Report to github if you sure this is are bug")

def api():
    #PR without downloading github api data are welcome
    #or maybe i will implement it soon
    download("https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest", "Api.json", "Getting Github Data info ", 3)

    search("get.json", f'"name": "graalvm-ce-java{main.ver}-{system.os}-amd64-')
    api.name=search.r[15:-10]
    api.ver=search.r[47:-14]
    api.file=(f"graalvm-ce-java11-{api.ver}")
    api.link=(f"https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-{api.ver}/{api.name}")

    print(api.ver)
    print(api.name)
    print(api.file)
    print(api.link)

def start():
    a = system.os
    download(api.link, api.name, f"Downloading {api.name}", 50)
    print("download done")
    unzip(api.name, (os.getcwd()))
    mkdir(system.path)
    mv((os.getcwd()), system.path)
    if "linux" in a:
        cmd(f"echo 'export PATH={system.path}{api.l}/bin:$PATH' >> ~/.bashrc")
        cmd(f"echo 'export JAVA_HOME={system.path}{api.l}' >> ~/.bashrc")
    elif "windows" in a:
        cmd(f'setx /M PATH "{system.path}\bin;%PATH%"')
        cmd(f'setx /M JAVA_HOME "{system.path}"')

def main():
    print("checking graalvm github please wait")
    main.ver=input("Java version to install 8/11 : ")
    system()
    api()
    start()
    print("Thank you for using our Graalvm install script")

main()
