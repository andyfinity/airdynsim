# airdynsim
Originally intended to drive a 6-dof aircraft simulator, this set of scripts now simply solves a special set of matrices.  The matrices are based on page 932 in the book Mechanics of Flight (second edition) by Warren Phillips.

**This software is still in alpha development.**  Not all features are properly implemented.

## Required
* Python 3.3 or newer (might work on 2.7)
* pint (used for unit checking during development) 
* numpy (used for the solver)
* scipy (also used for the solver)

## How to use
After installing required packages, simply run `python3 solver.py`.  To change aircraft parameters, only change values in `equations.py`.  All other files only have equations and should not be edited. 

## Installation
### Ubuntu or Debian
    sudo apt-get install python3.3 python3-pip
    sudo pip3 install pint
    sudo pip3 install numpy
    sudo pip3 install scipy

### OS X
*TODO*

### Windows
*TODO*

## License
This code is released under the [GPLv3 license](https://www.gnu.org/licenses/gpl.html).