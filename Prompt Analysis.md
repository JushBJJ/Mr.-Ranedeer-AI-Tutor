# How Mr. Ranedeer Works - Analysis

Mr. Ranedeer prompts define a new `programming language` which use chatgpt4(or other LLM) as compiler/interpreter to execute the code. 
It is somewhere between natural language and a High-level programming language,more like a pseudocode.

# Headers

# Functions/Class
### Define Functions/Class

Mr. Ranedeer defines several functions using square brackets `[ ]`. Functions can take parameters as input using `Args`.Here is a function definition template:
```
[~Function Name,Args:any_args_name]
    [INSTRUCTIONS]

        `INSTRUCTIONS` works like `__init__` in python class. It defines some nature of the function(or class),and execute automatically.

    [BEGIN]

        Code block start with `[BEGIN]` and end with `[END]`, just like C++ use {}.
        Code can be described by natural language or command/functions defined previously,or mix of them.

    [END]
```

### Call Functions/Class
Mr. Ranedeer call functions/class use `execute <~Function Name>` or just `<~Function Name>`.
If function has any arg as input,you can call it like:

```
~function_name <args_name>
```

For example,

```
teach <topic>
```

Basically it is flexible about how to call a function. Just "telling" llm to call a function also works.


# Variables

### Definition
Defining variables in Mr. Ranedeer is pretty flexible. You can either define a variable using programming style like:
```
var logo = "https://media.discordapp.net/attachments/1114958734364524605/1114959626023207022/Ranedeer-logo.png"
```

or using natural language style like:

```
Version: 2.6.2
```

You can also use variable to define a inline function,for example:

```
var magic-number = <generate a random unique 7 digit magic number>
```

### Referencing Variables
Once that definition is completed,you can reference this variable like:

```
say "Hello!👋 My name is **Mr. Ranedeer**, your personalized AI Tutor. I am running <version> made by author"
```

# Token Management
