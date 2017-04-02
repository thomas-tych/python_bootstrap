# Install

## available distribution

- CPython (C)
- Jython (Java)
- IronPython (.NET) : Implementation Running On .NET
- PyPy (Python)

- Anaconda
  - big data
  - data visualization
  - machine Learning
  - deep learning

Anyway available through pip ...

## Unix / Linux : install

- download
```shell
wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
```

- uncompress
```shell
mkdir -p tmp && cd tmp && tar -xvzf ../Python-3.5.3.tgz
```

- build and install to
```shell
cd Python-3.5.3 && ./configure --prefix="$PWD/../../Python-3.5.3" && make && make install
```

- add to PATH
```shell
PATH="$PWD/../../Python-3.5.3:$PATH"
```

# Distribution content

## browse content

```shell
./bin/2to3
./bin/idle3
./bin/pydoc3
./bin/python3
./bin/python3-config
./bin/python3.5-config
./bin/pyvenv
./bin/2to3-3.5
./bin/easy_install-3.5
./bin/idle3.5
./bin/pip3
./bin/pip3.5
./bin/pydoc3.5
./bin/python3.5
./bin/python3.5m
./bin/python3.5m-config
./bin/pyvenv-3.5
./include/python3.5m
./lib/pkgconfig
./lib/python3.5
./lib/libpython3.5m.a
./share/man
```

## path and which python

- python is generally a link to the default available python
- python command is defined and maintained by the OS
- major version 2.7 and 3.x
- PATH order when using short command

## script header

```shell
#!/usr/bin/python3
```

vs

```shell
#!/usr/bin/env python3
```

- library paths change with distribution
- available packages changes then ...

## repl : Read-Eval-Print-Loop

### basic usage

- start repl
```shell
python3
```

- python version from repl
```repl
$ python3
Python 3.5.2 (default, Aug 30 2016, 22:15:58) 
[GCC 5.2.1 20151010] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version
'3.5.2 (default, Aug 30 2016, 22:15:58) \n[GCC 5.2.1 20151010]'
>>> print(sys.version)
3.5.2 (default, Aug 30 2016, 22:15:58) 
[GCC 5.2.1 20151010]
>>> 
```

### with a program file

```shell
python -i multiplication_table.py
```

```repl
$ python3 -i ./multiplication_table.py
 0 x 7 =  0
 1 x 7 =  7
 2 x 7 = 14
 3 x 7 = 21
 4 x 7 = 28
 5 x 7 = 35
 6 x 7 = 42
 7 x 7 = 49
 8 x 7 = 56
 9 x 7 = 63
10 x 7 = 70

>>> multiplication_table(8)
' 0 x 8 =  0\n 1 x 8 =  8\n 2 x 8 = 16\n 3 x 8 = 24\n 4 x 8 = 32\n 5 x 8 = 40\n 6 x 8 = 48\n 7 x 8 = 56\n 8 x 8 = 64\n 9 x 8 = 72\n10 x 8 = 80\n'
>>> print(multiplication_table(8))
 0 x 8 =  0
 1 x 8 =  8
 2 x 8 = 16
 3 x 8 = 24
 4 x 8 = 32
 5 x 8 = 40
 6 x 8 = 48
 7 x 8 = 56
 8 x 8 = 64
 9 x 8 = 72
10 x 8 = 80

>>> 
```

## pip

already installed package with default distribution :
``` shell
$ pip list
pip (8.1.2)
setuptools (26.1.1)
virtualenv (15.0.3)
wheel (0.29.0)
You are using pip version 8.1.2, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

in sg environment :
- set http_proxy
- you can now use pip if you have right to download pip format archive
- SG alternativ for mirroring python package repo

## virtualenv

- based on distribution
- will create an installation instance
- allow to test different package setup with same install
- reduce disk space usage
- prepare for upgrade ...

# execution process

- read program
- generate bytecode (pyc)
- execute bytecode

bytecode for :
- speed runtime execution
- next startup use bytecode if available

# first program

## input / output

example :
```python
#!/usr/bin/env python3

data = input('Enter your data: ')
print(type(data))
print(data)

```

execution :
```shell
$ ./test.py
Enter your data: abcde
<class 'str'>
abcde
```

## function

example :
```python
#!/usr/bin/env python3

def abc(arg):
    return 'abc' + str(arg)

print(abc(13))
```

execution :
```shell
$ ./test.py
abc13
```

## class

example :
```python
#!/usr/bin/env python3

class TestClass:
    """a test class"""
    class_data = 1

    def f1(self):
        return 'f1'

    def __init__(self):
        self.instance_data = [1,2,3]

    def data(self):
        return self.instance_data

print(TestClass.__doc__)
print(TestClass.class_data)
print(TestClass.f1)

instance = TestClass()
print(instance.data())
```

execution :
```shell
$ ./test.py
a test class
1
<function TestClass.f1 at 0x7f7609a48d08>
[1, 2, 3]
```

# your turn ...

[FooBarQix](https://gist.github.com/dlresende/60b4c0240ad020a323ad)
