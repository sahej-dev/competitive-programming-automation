# competitive-programming-automation
## Description
A python application to make life easier if you do competitive programming from one of the following places:
- <a href="https://open.kattis.com/"> Kattis </a>
- <a href="https://onlinejudge.org/"> UVa Online judge </a>
- <a href="https://www.codechef.com/"> CodeChef </a> (Not planned to be supported certainly. I don't use codechef much. This might change if i have extra time on my hands or I start using codechef.)

### OS Support:
- Windows
- Linux
- MacOS (NOT TESTED! But it works on linux thanks to bash so probably should work on mac)

I have a ready version of this application with about 75% ish features already implemented, but it's very badly coded and not modular at all.

# Features to be Added:
## Universal
**Universal features are going to be compoatible with each online judge, which will ever be supported by this software.**
- Problem folder setup:
  - A general organization of folder for each problem.
  - This organization is intended to be heavily customizable. Meaning you can have all your solutions and test cases in the same folder or a separate folder for each problem, and for each test case, or anything in between. Basically you can customize it any way you desire to. (This is a hard feature to implement for me, might take a while.)
- Download problem as PDF.
- Download all sample test cases.
- A suite of tools to flexibly compare output with sample test cases and user generated test cases.
- A suite of tools for smooth integration of user generated test cases with the sample test cases.
- Run time measurement on user's PC. I don't know how to simulate the conditions of online judge's server on the users PC to get a similar run time. To do might even be impossible to implement. So maybe... this feature is going to be there. If it is it's probably going to be the last one.

## Kattis
Not anything specific in mind right now. Basically universal features cover all of it.

## UVa
- uDebug integration maybe? This is going to be hard but I am going to give my best.
- uHunt integration (This will open a browser. Sometime later in-app search functionality is intended to be added):
  - Search a problem on uhunt immediately.
  - Search a person on uhunt immediately.
- In app CP4 problem integration:
  - Search for a specific topic from CP4
  - All starred and non starred problems from CP4 to support quickest and easiest set up.
  
**Might add more OJs later if feel like it. This is a perosnal project.**

The version of this project with bad code and limited functionality is going to be available in the "v0.5_alpha" branch. This branch will no longer be supported. Instructions to use that version may or may not be provided.
