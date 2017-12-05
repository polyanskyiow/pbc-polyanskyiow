*author: Oleksii Polianskyi*

# Python Boot Camp
_____________________________________

##  **hm1 - Home work 1**

`hm1/fibonacci.py` Function `fib(n)` returns list of `n` fibonacci numbers.

`hm1/numbers_pairs.py` Function `print_pairs(sum, *args)` returns filtered (without duplicates) pairs with specified sum.

`vagrantfile` needs to run virtual invironment.
    `vagrant up`
    `ssh vagrant@192.168.33.10`
    `password: vagrant`
 
 ##  **hm2 - Home work 1**
  **Setup environment**
 1. Install `pip` https://pip.pypa.io/en/stable/installing/ , `pip` is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
     ```
    python get-pip.py
    ```

2. Install `virtualenv` . If `pip` command does not work add path to `pip` to your `PATH` (for Windows something like C:\Python27\Scripts) 
     ```
    pip install virtualenv
    ```
    
 3. Setup virtual environment
      ```
    virtualenv <virtualenv name>
    ```
    
 4. Active `virtualenv` (for Windows)
     ```
    virtualenv <virtualenv name>
    ```
 5. Now you can activate/deactivate your virtual environment from %virtualenv name%\Scripts\
    ```
    activate
    ```
 6. Run `pip install -r requirements.txt`to install packages from requirements.txt
 
 **Unit tests**
 
* for fibonacci tests run `pytest test_fibonacci.py`
* for numbers tests run `pytest test_numbers_pairs.py`