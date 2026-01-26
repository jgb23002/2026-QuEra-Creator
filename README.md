# iQuHACK 2026 - QuEra Creators' Challenge

> Give me an AOD large enough and I can move the atoms of the world. - *John Long, Scientific Software Engineer @ QuEra*

So you fancy taking on QuEra's creators' challenge for iQuHack 2026?! We welcome you with open arms!

Here you will learn all the details about the challenge, and needed to operate QuEra resources for iQuHack 2026. 


## Contents
This repo contains everything you need to get going. Mainly:

- [`challenge.md`](challenge.md) contains the challenge statement, with directions and guidelines
- Inside the `assets` folder you'll find
  - slide decks expanding on the topics from the Friday tutorial, with an intro to neutral-atom quantum computing and including some basic information about error correction
  - guidelines for installation of Manim, for those interested
  - example gifs of different computing processes to help seed ideas for you
  - example of a code for generating an animation of Magic State Distillation using the [Quantum Animation Toolbox](https://github.com/jwaldorf05/quantum-animation-toolbox) (built on a [manim](https://github.com/3b1b/manim) engine)
  

## Coding Infrastructure

In this challenge, you will be using your own tools to generate animations and represent processes of neutral-atom quantum computing. While we at QuEra have sponsored the creation of tools to facilitate this type of workflow in the past (e.g. the [Quantum Animation Toolbox](https://github.com/jwaldorf05/quantum-animation-toolbox)), your are not bound to any specific tool. But if you generate your animations via coding, we do recommend the utilization of `uv` to manage your repo. If you are not familiar with `uv` workflows, here are some directions:


### Using `uv` to start your own project

**1) Create a new project (generates `pyproject.toml`)**
```bash
mkdir my-project && cd my-project
uv init
````

(Optional) pin a Python version for the folder:

```bash
uv python pin 3.11
```


**2) Add packages (updates `pyproject.toml`)**

```bash
uv add numpy pandas        # runtime deps
uv add --dev pytest ruff   # dev deps
```

**3) Install/sync everything into a local `.venv`**

```bash
uv sync
```

**4) Run your code**

activate your environment
```bash
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows PowerShell
```
and start coding!

## Resource Availability and Code of Conduct

There is no access to quantum hardware for this challenge. Development of solutions can use any workflow of preference, including programmatic tools or more manual ones.


## Documentation

This year’s iQuHACK challenges require a write-up/documentation portion that is heavily considered during judging. The write-up is a chance for you to be precise in describing your approach and describing your process, as well as presenting the performance of your solutions. It should clearly explain the process you wanted to depict, the approaches you used, and your implementation. Separate gif or mp4 files for the actual solutions are encouraged.

Make sure to clearly link the documentation into the `README.md` of your own solutions folder and to include a link to the original challenge repository from the documentation!


## Submission

To submit the challenge, do the following:
1. Place all the code you wrote in one folder with your team name under the `team_solutions/` folder (for example `team_solutions/quantum_team`).
2. Create a new entry in `team_solutions.md` with your solution and your documentation. Your solution shuold contain a python script that runs your solution and  a `.pdf` of your presentation slides, and any asset with actual animations. Make sure to add an updated TOML file in case you are using extra packages needed to run your solution.
3. Create a Pull Request from your repository to the original challenge repository
4. Submit the "challenge submission" form as required by iQuHack organization

Project submission forms will automatically close on Sunday at 10am EST and won't accept late submissions.

## Evaluation criteria

This is an artistic creation-focused challenge, but we will try to keep our analysis as objective as possible. To help guide your efforts, here are some points we will take into account when evaluating your work:

- Is the computing process being portrayed in a correct way? Are approximations being clearly stated or are they affecting the understanding of the audience somehow?
- Is the presentation introducing novel elements or ideas on how to portray quantum circuits, atom shuttling, or other processes using neutral-atom quantum computers?
- How extensive have been the creation efforts? How reproducible is the work?
- How polished is the final product?
