[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/95BWY5mA)

Names: Samuel Calderon Duque and Matias Monsalve Ruiz
Class number: 7309

Operating System: Windows 11 / MacOs Sequoia
Programming Language: Python 3.13
Tools: PyCharm 2024.3.3

Have Python installed, open the IDE of your preference, open the file "dfa_minimization.py", after that run the file. Finally follow the required DFA details and check the output.

The first section of the code "read_input" represents the function that creates an empty list "cases" where we ask for number of cases, number of states, alphabet, final states and transition table.
After that is the function "minimize_dfa" which requires the number of states, alphabet, final states and the transition table. It begins by initializing a table of unordered state pairs, assuming all are initially equivalent. In the first marking phase, any pair where one state is final and the other is not is immediately marked as distinguishable. Then, an iterative marking process follows: for each unmarked pair {p, q}, if any transition leads to a previously marked pair, then {p, q} is also marked. This process continues until a full pass results in no new marks. Finally, unmarked pairs are classified as equivalent. The last part is the "main" function which reads the input from the cases and prints the equivalent states obtained previously.
