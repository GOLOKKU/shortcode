import argparse
import tarfile as tar
import requests
import platform
import json
import os
import hashlib
from zipfile import ZipFile as zip

#arg parser

parser = argparse.ArgumentParser(description = 'Graalvm install script usage')
parser.add_argument('-java', default=11, type=int,
                    help='example : java version 11 `-java 11`')
parser.add_argument('-version', default="latest" ,type=str,
                    help='example : graalvm version 21.1.0 `-version 21.1.0`')
parser.add_argument('-path', default="default" ,type=str,
                    help=f'example : path installation `-path /usr/lib/jvm/java11-graalvm-21.1.0`')

args = parser.parse_args()

#function
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
                print('{} [{}{}] {}% {}M/{}M'.format(msg,'█' * done, '.' * (long-done), done, perc1, perc2))
    print('Done')

#checking system
operating_system = platform.system().lower()
cpu=((platform.uname()[4]).lower())

if (args.version=="latest"): 
    apireturn = requests.get("https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest").text
    version=(json.loads(apireturn)["tag_name"])[3:]

else:
    version=args.version

if cpu=="x86_64": cpu= "amd64"

if "linux" in operating_system:
    default_path = f"/usr/lib/jvm"
    setpath1=f'echo \'export PATH="/usr/lib/jvm/graalvm-ce-java{args.java}-{version}/bin:$PATH"\' >> /etc/profile'
    setpath2=f'echo \'export JAVA_HOME="/usr/lib/jvm/graalvm-ce-java{args.java}-{version}"\' >> /etc/profile'

elif "windows" in operating_system:
    default_path = f"C:/java"
    setpath1=f'setx /M PATH "C:/java/graalvm-ce-java{args.java}-{version}/bin;%PATH%"'
    setpath2=f'setx /M JAVA_HOME "C:/java/graalvm-ce-java{args.java}-{version}"'

elif "darwin" in operating_system:
    default_path = f"/Library/Java"
    setpath1=f'export PATH=/Library/Java/java{args.java}-graalvm-{version}/Contents/Home/bin:$PATH'
    setpath2=f'export JAVA_HOME=/Library/Java/java{args.java}-graalvm-{version}/Contents/Home'

else:
    print("Unkown os")
    exit()

print(f"Detected os : {operating_system}")

if (args.path=="default"): path=default_path
else: path=args.path

search=f"https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-{version}/" \
       f"graalvm-ce-java{args.java}-{operating_system}-{cpu}-{version}"

release_list=requests.get(f"https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/tags/vm-{version}").text
if "message" in release_list: 
    print("Version not found")
    exit()

link=((release_list[release_list.find(search):]).split('"')[0])
output=("{}/{}".format (path, link.split('/')[-1]))

os.makedirs(path, exist_ok=True)
if (os.path.isfile(output) == False): download(link, output, "Downloading graalvm", 100)
print("Downloading done")

if (os.path.isfile(output+".sha256") == False): download(link+".sha256", output+".sha256", "Downloading graalvm checksum", 100)

#installation
sha256_hash = hashlib.sha256()
with open(output,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)

if (open(output+".sha256", "r").read() == sha256_hash.hexdigest()) == False:
    print("checksum does not match. please try redownload graalvm")
    exit()

print("Checksum done")
unzip(output, path)
print("Unzip done")

os.system(setpath1)
os.system(setpath2)

print("Done added to PATH environment variable")