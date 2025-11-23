# Project Title

Deterministic Turing Machine Simulator in python (with numpy, pandas, and requests)     
# Overview of the Project

This project implements a Deterministic Turing Machine (DTM) in Python that simulates how a theoretical Turing Machine reads, writes, and moves along a tape according to transition rules.

To satisfy project requirements, the implementation integrate three external Python modules:

numpy → for tape representation

pandas → for storing the transition tables

requests → to demonstrate external for data fetching (mock information)

The simulator perfroms a sample operation called Unary Increment, where the input tape (e.g., "111")  transformed by appending one extra "1".
# Features

 Simulates deterministic Turing Machine behavior
 -Tape stored using a numpy array
 -Transition functions stores in a pandas DataFrame
 -Uses requests module for external information retrieval
 -Step-by-step execution using step()
 -Full simulation using run()
 -Works for any custom transition table
 -Clean OOP-based design

#Technologies / Tools Used
Tool / Module	Purpose
Python 3	Core programming
numpy	Tape storage & dynamic resizing
pandas	Structured transition table
requests	Fetch TM info (dummy API)
VS Code	IDE used for development
GitHub	Version control & submission
# Steps to Install & Run the Project
1️. Clone the Repository
git clone <your-repository-link>
cd turing-machine-simulator

2️. Install Required Modules
pip install numpy pandas requests

3️. Run the Project
python machine.py

Expected Output:
Info: Requests module used: No internet, but code works!
Final Tape: 1111
Final State: qf
Transition Table:
  state symbol write move next
0    q0      1     1    R   q0
1    q0      _     1    N   qf
# Instructions for Testing

You can test the Turing Machine by modifying the tape input inside machine.py.

Example:
tm = TuringMachine(
    tape_str="1111",
    blank="_",
    initial_state="q0",
    final_states={"qf"},
    transition_fn=transition_df
)
