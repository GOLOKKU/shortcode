import os
import platform
import sys
import requests
from zipfile import ZipFile as zip
import tarfile as tar
import shutil
import urllib.request

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

def system():
    pl = platform.system()
    if "Linux" in pl:
        system.os="linux"
        if "com.termux" in sys.executable:
            system.path = "/data/data/com.termux/files/usr/bin/java/"
            print("Termux detected")
        else:
            system.path = "/usr/bin/java/"
            print("Linux detected")
    elif "Windows" in pl:
        system.path = "C:/java"
        system.os="windows"
        print("Windows detected")
    elif "darwin" in pl:
        system.path = "/Library/Java/JavaVirtualMachines"
        system.os="darwin"
        print("Mac Detected")
    else:
        print("Unable to Start Only support :"
        "Linux,Windows,Termux,Mac for this time "
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

def start():
    endfile=f"{system.path}/{api.file}"
    a = system.os
    output=("{}/{}".format (os.getcwd(), api.file))
    #added check if download are corrupted
    if os.path.isfile(api.name):
        site = urllib.request.urlopen(api.link)
        if site.length == os.stat(api.name).st_size:
            pass
        else:
            print("file you downloaded before are corrupted")
            download(api.link, api.name, f"Downloading {api.file}", 50)
    else:
        download(api.link, api.name, f"Downloading {api.file}", 50)
    print("download done")
    unzip(api.name, (os.getcwd()))
    if os.path.exists(system.path):
        unzip(api.name, (os.getcwd()))
    else:
        os.mkdir(system.path)
        unzip(api.name, (os.getcwd()))
    shutil.move(output, system.path)
    file = ("{}/{}".format (system.path, api.file))
    if "linux" in a:
        cmd(f"echo 'export PATH={endfile}/bin:$PATH' >> ~/.bashrc")
        cmd(f"echo 'export JAVA_HOME={endfile}' >> ~/.bashrc")
    elif "windows" in a:
        cmd(f'setx /M PATH "{endfile}\bin;%PATH%"')
        cmd(f'setx /M JAVA_HOME "{endfile}"')
    elif "darwin" in a:
        cmd(f"export PATH='{endfile}/Contents/Home/bin:$PATH'")
        cmd(f"export JAVA_HOME='{endfile}/Contents/Home'")

def main():
    print("checking graalvm github please wait")
    main.ver=input("Java version to install 8/11 : ")
    system()
    api()
    start()
    print("Thank you for using our Graalvm install script")

main()
