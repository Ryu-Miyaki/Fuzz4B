# Fuzz4B
We developed a tool named Fuzz4B, which is a front-end to [AFL](https://github.com/google/AFL) for developers who are inexperienced in fuzz testing. Fuzz4B is not only a front-end, but it also allows developers to reproduce a crash and minimize a fuzz that causes the crash.  

# Demonstration Video
[![Introduction](http://img.youtube.com/vi/wo6VcdlPoM0/0.jpg)](http://www.youtube.com/watch?v=wo6VcdlPoM0 "https://img.youtube.com/vi/wo6VcdlPoM0/0.jpg")

# Installation
We tested Fuzz4B on Ubuntu 18.04 LTS.  
Run the following commands to install AFL (We use AFL 2.52b. See [here](https://github.com/google/AFL/blob/master/docs/INSTALL) for more information).
```
wget https://lcamtuf.coredump.cx/afl.tgz
tar -vxzf afl.tgz
cd afl-2.52b
make
make install
```
Run the following commands to intall the required packages and clone the repository.  
If you are using an OS other than Ubuntu 18.04 LTS, you should edit `ubuntu-18.04` of the last command.
```
sudo apt install xterm xclip libsdl2-2.0-0
git clone https://github.com/Ryu-Miyaki/Fuzz4B
cd Fuzz4B
pip3 install -r requirements.txt -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/
```
<!--
The following systems should be installed before you install Fuzz4B.
- AFL (See [here](https://github.com/google/AFL/blob/master/docs/INSTALL) to install)
- wxPython (Execute `pip3 install wxPython` to install)
- pyperclip (Execute `pip3 install pyperclip` to install)
- xterm (Execute `sudo apt install xterm` to install)
- xclip (Execute `sudo apt-get install xclip` to install)
-->

Ryu Miyaki (e-mail: miyaki AT ertl.jp)
