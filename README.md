### 安装相应的环境

#### Linux
```
$ sudo apt install git cmake build-essential libpng-dev
$ git clone https://git.code.sf.net/p/zint/code zint
$ mkdir build
$ cd build
$ cmake ..
$ make
$ sudo make install
```

#### MacOS
```
# 安装brew 已安装可以忽略
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
$ brew update
$ brew install zint
```
  
