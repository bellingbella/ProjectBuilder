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
- for "as", if you use "in-out" mode then it'll likes `echo 'hi', (input) and (output) !'` and if you use "out-in" mode then  it'll likes `echo 'hi',  (output) and  (input) !`
- 
