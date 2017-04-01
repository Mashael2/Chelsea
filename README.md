# Chelsea
Homework Assignment 7 Group Project  
Authors: [Micheal Brewer](https://github.com/omega-wyd) and [Macheala] 
CS 3030 &ndash; Hugo Valle


## Task 1
## Script usage

`Chelsea_task1_hw7.py` calls `./Chelsea_task1_module1_hw7.py` script to verify the information it is passed

```python3
$ python3 Chelsea_task1_hw7.py
```

With the names of our scripts, this can be run as

```python3
$ python3 Chelsea_task1_hw7.py
```

## What each file does

- The `Chelsea_task1_hw7.py` is the file that is called and ran. it will open a url file to retrieve a `.csv` file. It will then sort 
  each line and match it to its corresponding open or closed value. Then it calls module `Chelsea_task1_module1_hw7.py` def `doors()` to 
  use the info to verify if a door is open or closed.
  
- The `Chelsea_task1_module1_hw7.py` takes the args (H1, LD, RD, CL, ML, LI, LO, RI, RO,  GS) and checks the position of each to determine
  if the doors are open or closed. It then returns the status of the doors. 
