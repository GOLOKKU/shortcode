wget https://raw.githubusercontent.com/GOLOKKU/Graalvm-Java-Install/main/install.py
a=$(python3)
if [ -n "$a" ]; then
  python3 install.py
else
  apt install python3
  python3 install.py
fi
bash
