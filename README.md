# VAR NAMER

This was a small project that was used for research purposes looking into variable name feedback using LLMs

`studentCodeGenerator.py` and `variableFeedbackGenerator.py` were used to generate synthetic student code and variable name feedback using LLMs respectively.

`feedbackCoding.py` is a program that made rating LLM responses more easier by displaying it's output into a better format.

## How to Use VarNamer

```sh
# clone this repository
git clone git@github.com:Kot6603/var-namer.git

# change directory to the cloned repository
cd var-namer

# activate the virtual environment
python3 -m venv venv
source venv/bin/activate # sorry windows users...

# install dependencies - hopefully these are the only ones
pip install dotenv
pip install openai
```

### Coding

```sh
# run the coding program
python3 feedbackCoding.py
```

This will start the program which will output each sample (in random order) in the following output:
```
[iteration]/200 == problem_id [problem_id] ==>

[problem]

---
[question]
---
[list of feedbacks]
[mapping of old -> new variables]

Actionability: [user input]
Correctness (Prior): [user input]
Correctness (After): [user input]
Justification: [user input]
```
