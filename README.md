*author: Oleksii Polianskyi*

# Python Boot Camp
_____________________________________

##  **Home work 1**

`my_app_tests.fibonacci.py` Function `fib(n)` returns list of `n` fibonacci numbers.

`my_app_tests.numbers_pairs` Function `print_pairs(args)` returns filtered (without duplicates) pairs with specified sum.

`vagrantfile` needs to run virtual invironment.
    `vagrant up`
    `ssh vagrant@192.168.33.10`
    `password: vagrant`
 
 ##  **Home work 2**
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

 ##  **Home work 3**
 
 **Added decorators for:**

- Printing out tested inputs in fib function

- Printing out tested inputs in numbers_pairs function

**Added `app.py` for launching  modules via CLI:**

- Example of command for **fibonacci** module `python app.py fib -n 8`.
Result:
  ```
   arg: "8"
   [0, 1, 1, 2, 3, 5, 8, 13]
    ```

- Example of command for **numbers_pairs** module `python app.py print_pairs -arg 2 7 5 3 1 5 9 8 1`.
Result:
  ```
   arg: "2"
   arg: "7"
   arg: "5"
   arg: "3"
   arg: "1"
   arg: "5"
   arg: "9"
   arg: "8"
   arg: "1"
   set([(2, 8), (5, 5), (1, 9), (3, 7)])

    ```
 ##  **Home work 5**
 
 **Added `ssh_module.py` for launching Selenium grid with node, via ssh, on vagrant VM:**
 
 To run selenium grid execute:
  ```
  python -m my_app_tests.ssh_module
  ```
 
 To verify that grid with node has been launched successfully open `http://192.168.33.10:4444/grid/console` in browser
 
  ##  **Home work 6**
- Project structure has been changed to:
    ```
    .
    ├── Vagrantfile
    ├── app.py
    ├── pbc
    │   ├── __init__.py
    │   ├── func_decorators.py
    │   ├── sg
    │   │   ├── __init__.py
    │   │   ├── conftest.py
    │   │   ├── connections.py
    │   │   ├── sg.py
    │   │   └── test_sel_grid.py
    │   └── tools
    │       ├── __init__.py
    │       ├── fibonacci.py
    │       └── numbers.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        └── tools
            ├── __init__.py
            ├── test_fibonacci.py
            └── test_numbers.py
     ```

- Added tests for setup selenium on the vagrant VM. To run this tests execute:
    ```
    pytest -v -s -m selenium
    ```
##  **Home work 7**
- Selenium grid setup configuration has been updated
- Added test for testing grid config `pbc.sg.test_sel_grid.test_check_grid`.
- Added clean up section to `pbc.sg.conftest`
- Vagrant file was updated

  To run this tests execute:
  ```
  pytest -v -s -m selenium
  ```