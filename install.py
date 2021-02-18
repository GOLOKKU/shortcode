import os
import sys
import requests
import tarfile as tar
from zipfile import ZipFile as zip
import platform
import json

version=int(input("Input version : "))
workdir="/".join(os.getcwd().split("\\"))
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
                perc1= int(downloaded / (1024 ** 2))
                perc2= int(total / (1024 ** 2))
                downloaded += len(data)
                f.write(data)
                done = int(long*downloaded/total)
                sys.stdout.write('\r{} [{}{}] {}'.format(msg,'█' * done, '.' * (long-done), (f"{done}% {perc1}/{perc2}")))
                sys.stdout.flush()
    sys.stdout.write('\n')

#getcpu info
pl = platform.system()
cpu=((platform.uname()[4]).lower())
if "Linux" in pl:
    ops="linux"
    if "com.termux" in sys.executable:
        path = "/data/data/com.termux/files/usr/bin/java/"
    else:
        path = "/usr/bin/java/"
elif "Windows" in pl:
    path = "C:/java/"
    ops="windows"
elif "darwin" in pl:
    path = "/Library/Java/JavaVirtualMachines"
    ops="darwin"
else:
    print("Unable to Start Only support :"
    "Linux,Windows,Termux,Mac for this time "
    "Report to github if you sure this is are bug")

if "x86_64" or "amd64" in cpu:
    cpu= "amd64"
elif "aarch64" in cpu:
    cpu= "aarch64"
else:
    print(f'{cpu} unknown CPU architecture')

#link download
apireturn = requests.get("https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest").text
build=(json.loads(apireturn)["tag_name"])[3:]
file=f"graalvm-ce-java{version}-{ops}-{cpu}-{build}"
link=(apireturn[(
    apireturn.find(f"https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-{build}/{file}")):]
    .split('"')[0]
)

print("downloading file")
output=link.split("/"[-1])
endfile=f"{path}{file}/"
print(endfile)
if os.path.isfile(path) is False: os.mkdir(path)
if os.path.isfile(output) is False : download(link, output, "mendownload gravaalm", 50)
print("Unzipping file . . .")
unzip(output, endfile)

#installation
if "linux" == ops:
    os.system(f"echo 'export PATH={endfile}/bin:$PATH' >> ~/.bashrc")
    os.system(f"echo 'export JAVA_HOME={endfile}' >> ~/.bashrc")
elif "windows" == ops:
    os.system(f'setx /M PATH "{endfile}\bin;%PATH%"')
    os.system(f'setx /M JAVA_HOME "{endfile}"')
elif "darwin" == ops:
    os.system(f"export PATH='{endfile}/Contents/Home/bin:$PATH'")
    os.system(f"export JAVA_HOME='{endfile}/Contents/Home'")
