wget https://raw.githubusercontent.com/GOLOKKU/Graalvm-Java-Install/main/install.py
if [ -d "$/data/data/com.termux" ]; then
  python3 install.py
else 
  sudo python3 install.py
fi
bash
