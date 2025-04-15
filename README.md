# Project Builder Tool

## Introduction
The PBT is a simple project builder that helps you build the project easily.


## Usage
1. 💡 Class/Classes
This JSON data is Project/Configuration/Classes.json that contains all calsses:
```json
{
    "example": { 
        "as": "in-out",
        "pattern" : {
            "first": "echo 'hi, ",
            "mid": "and",
            "last": "!'"
        }
    }
}
```
- For the "as" field:

   + In "in-out" mode, it works like `echo 'hi', (input) and (output) !. The value acts as both input and output`.

   + In "out-in" mode, it works like `echo 'hi', (output) and (input) !. The value first outputs`.
