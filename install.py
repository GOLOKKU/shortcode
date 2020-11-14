import os as s
def p(a): print(a)
def find(f, a):
    file = open(f, "r")
    for i in file:
        if a in i:find.r=i
def cmd(a): s.system(a)
e="sudo"
cmd(e," apt-get update ; sudo apt-get install gcc zlib1g-dev build-essential unzip")
p("Checking graalvm github please wait : ")
cmd("curl https://api.github.com/repos/graalvm/graalvm-ce-builds/releases/latest -o get.json")
x=(str(int(input("Input java version you want to install (8/11): "))))
find("get.json", '"name": "graalvm-ce-java'+x+'-linux-amd64-');v=find.r[45:-10];l="graalvm-ce-java",x,"-",v,"/"
find("get.json", "graalvm-ce-java"+x+"-linux-amd64-");a=find.r[31:-2];z =("Graalvm"+x+".tar.gz")
cmd(e,"wget ",a," -o ",z)
cmd("tar -xzf ",z," ; sudo mkdir /usr/lib/jvm ; sudo mv ",l," /usr/lib/jvm")
cmd("echo 'export PATH=/usr/lib/jvm/",l,"/bin:$PATH' >> ~/.bashrc ; echo 'export JAVA_HOME=/usr/lib/jvm/",l,"' >> ~/.bashrc")
input('Installation are done please execute "source ~/.bashrc" \n')