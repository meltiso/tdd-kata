# tdd-kata

# First check

We will create a FizzBuzz class, so our first check consists in checking the class exists and can be tested.

Create the directory structure:

```
fizzbuzz
├── src
│   ├── fizzbuzz.py
└── tests
    └── test_fizzbuzz.py
  ```

Add in `tests/test_fizzbuzz.py`:
 
```
class TestFizzBuzz:
    def test_do_nothing(self):
        assert isinstance(FizzBuzz(), FizzBuzz)
```

Add in `src/fizzbuzz.py`:

```
class FizzBuzz:
    def __init__(self):
        pass
```

Launch pytest:

```
dev@ubuntu:~/Desktop/tdd-kata/fizzbuzz$ pytest
===================================== test session starts ======================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /home/dev/Desktop/tdd-kata/fizzbuzz
plugins: web3-6.1.0
collected 1 item                                                                               

tests/test_fizzbuzz.py F                                                                 [100%]

=========================================== FAILURES ===========================================
_________________________________ TestFizzBuzz.test_do_nothing _________________________________

self = <test_fizzbuzz.TestFizzBuzz object at 0x7f3209e04970>

    def test_do_nothing(self):
>       assert isinstance(FizzBuzz(), FizzBuzz)
E       NameError: name 'FizzBuzz' is not defined

tests/test_fizzbuzz.py:3: NameError
=================================== short test summary info ====================================
FAILED tests/test_fizzbuzz.py::TestFizzBuzz::test_do_nothing - NameError: name 'FizzBuzz' is not defined
====================================== 1 failed in 0.05s =======================================
```

It says `'FizzBuzz' is not defined`. Let's import the module in `/tests/test_fizzbuzz.py`

```
from src.fizzbuzz import FizzBuzz

class TestFizzBuzz:
    def test_do_nothing(self):
        assert isinstance(FizzBuzz(), FizzBuzz)
        
```

Launch `pytest` again:

```
dev@ubuntu:~/Desktop/tdd-kata/fizzbuzz$ pytest
===================================== test session starts ======================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /home/dev/Desktop/tdd-kata/fizzbuzz
plugins: web3-6.1.0
collected 0 items / 1 error                                                                    

============================================ ERRORS ============================================
___________________________ ERROR collecting tests/test_fizzbuzz.py ____________________________
ImportError while importing test module '/home/dev/Desktop/tdd-kata/fizzbuzz/tests/test_fizzbuzz.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_fizzbuzz.py:1: in <module>
    from src.fizzbuzz import FizzBuzz
E   ModuleNotFoundError: No module named 'src'
=================================== short test summary info ====================================
ERROR tests/test_fizzbuzz.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!
======================================= 1 error in 0.10s =======================================
```

It's said `No module named 'src'`. Let's add `tests/__init__.py`:

```
fizzbuzz
├── src
│   ├── fizzbuzz.py
└── tests
    ├── __init__.py
    └── test_fizzbuzz.py
```

Run `pytest` again:

```
dev@ubuntu:~/Desktop/tdd-kata/fizzbuzz$ pytest
===================================== test session starts ======================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /home/dev/Desktop/tdd-kata/fizzbuzz
plugins: web3-6.1.0
collected 1 item                                                                               

tests/test_fizzbuzz.py .                                                                 [100%]

====================================== 1 passed in 0.02s =======================================

```

Now it works! It means there isn't any issue related to modules, imports and dependencies.

