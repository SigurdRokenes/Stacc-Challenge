# Stacc-Challenge
 
My solution to the [Stacc code challenge](https://github.com/stacc/stacc-code-challenge-public).

This simple command prompt program takes a 9-digit organisation ID from [Brønnøysundregisteret](https://www.brreg.no/registersok/) as input.
It then finds all the registered leaders utilizing the Stacc API, and checks for matches in the PEP data-set.

### Modules:
core/fetchInfo.py :
gets information from brreg using stacc API. Outputs a dataframe with name and birthdates

core/checkPEP :
Reads pep data-set and contains a method to check for a list of names

core/query.py
Function to utilize stacc api in python.


## Installation (Windows)
### Anaconda (recommended)
1) Install Anaconda3 or Miniconda3
2) Clone this Repo. Navigate to the folder in Terminal (or anaconda prompt if not installed with path).
3) Create virtual environment:
 `conda env create -f requirements.yml`
4) Activate environment and run code:
 `conda activate stacc_code`
 `python main.py`

### Python (not tested)
1) Install Python
2) Install required packages:
 `pip install pandas`
 `pip install requests`
3) Run code:
   `python main.py`

## Usage
Use the command prompt to input a 9-digit number. The command prompt will then show all names being checked and matches.


