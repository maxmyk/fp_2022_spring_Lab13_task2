# fp_2022_spring_Lab13_task2

### **Important! _linkedbst.py_ uses _only 1/10_ of dictionary (_words.txt_)!**

An app that compares time efficiency of BST and standart Python's list.

## Tests for 10,000 random words
- [x] 1. Standart list
- [x] 2. BST using sequential addition
- [x] 3. BST using random addition
- [x] 4. Rebalanced BST using random addition

## Installation

```bash
git clone https://github.com/maxmyk/fp_2022_spring_Lab13_task2
```

## Usage

```bash
cd fp_2022_spring_Lab13_task2
python linkedbst.py
```

## Possible output
```bash
Reading file...
Success.
Creating sample lst...
Success.
Creating working lst...
Success.
Creating Trees...
Success.
Testing time...
        Test1 found/unfound:  1008 8992
        time:  4.346805886998482
        Test2 found/unfound:  1008 8992
        time:  28.76974628899916
        Test3 found/unfound:  1008 8992
        time:  0.06653601399739273
        Rebalancing...
        Success.
        Test4 found/unfound:  1008 8992
        time:  0.053253390004101675
Important information!
If all functions' found/unfound values are the same, they are correct.
Tests represent search time for 10,000 random words in:
        1.(1-st test): standart list
        2.(2-nd test): BST using sequential addition
        3.(3-rd test): BST using random addition
        4.(4-th test): rebalanced BST using random addition
```
