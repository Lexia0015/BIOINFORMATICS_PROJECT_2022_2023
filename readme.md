# Projet Bioinformatiques Python Programmation

## Compatibility of the program
The program is compatible with MacOS, Windows, and Unix (Ubuntu and others), as long as you have a **terminal** or an updated version of** Python (3.10.4)**.
It shoud also work on Python 3.9.12.
Please make sure you have the right version of python, or try to update with anaconda (if you're using a Bash terminal).

## How to run the program
```bash
python3 main.py
```

## About the file read_file.py

This file handles the fasta or fasta and gtf/gff file, verifies the files and checks for errors.
This file contains four principal functions:
- The function control() verifies if the selected input files are in the correct format. If not it throws an exception telling the user to use the right file format.
- The function fasta() reads the fasta file and returns the variable that contains the sequence as a string.
- The function read_multiple_fasta() reads the multiple fasta and returns the variable that contains the sequence as a string.
- The function split() takes the start and end position of the gene sequences in the gtf/gff file and extracts these sequences from the fasta file and returns the variable that contains the sequence as a string
- The function erreur() checks if either the fasta file or the gtf/gff file contains errors in the format. It controls if the fasta file is empty, has an ID and if its sequence consists of only the four nucleodides or N. It controls if the gtf/gff file is empty and if each column entries are how they should be. It shows different error messages if the entries are wrong.

## About the graphic_interface.py

This file creates a graphic interface in which the user can insert either the sequence or the fasta file with or without the gtf/gff file and lets him decide what operation he wants to do.
This file contains the interface_tkinter() function that contains following widgets and functions:
- The function select_file_fasta() allows the user to insert a wanted fasta file and that extracts the sequence returned from the fasta() function from the read_fle.py   
- The function select_gtf_gff_fasta() allows the user to insert a wanted gtf/gff file and that extracts the sequence in the fasta file at the positions taken from the gtf file with the split() function from the read_fle.py
- The function validate() converts the sequence from the text window into the wanted RNA or proteine sequence according to the selected combobox command
- The function clean_text() deletes the content of the sequence and results text fields
- The function quit() exits the graphic interface
- The function save_results() saves the results from the scrolled text field as a text file


## About the converter.py

This file converts the sequence into either RNA or protein.
This file contains two functions:
- The function transcription() transscripts the input DNA sequence into RNA
- The function traduction() traducts the RNA into protein sequence


## About the main.py

This file allows the user to choose if he wants to work in the terminal or interface, what file type he wants to use and allows him to choose between transcription, traduction or both.
This can be executed with the main() function that the file contains.

## Requirements
The following installations are required to make the program work.
- First, an updated version of python is needed. The code was written with the version 3.10.1

- Check the version of python in your bash terminal (on an Ubuntu Software)
- Open the right repository to install the following PPA for python 3.10
- Update the system packages
- Check if python version 3.10 is available by running 
- Install python version 3.10
- Since you will have two versions of python, you have to update the alternatives
- If by default python runs the older version, you will have to configure to the new version
- Finally, check the version of your version of python

```bash
python3 --version
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
apt list | grep python3.10
sudo apt-get install python3.10
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.- 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
sudo update-alternatives --config python3
python3 -V
```

- Additionally, you will need the following libraries to execute the program

### Install the numpy librairy
### Install the tkinter librairy
### Install the pandas librairy
### Install the pathlib librairy

```bash
pip install numpy
pip3 install tk
pip install pandas
pip install pathlib
```

## Authors and acknowledgment
Made by **CAMPOS FERREIRA Andreia and NICOLAUS Franziska**, Students in Master Degree 1 Bio-Informatics.


## License
Open source project.