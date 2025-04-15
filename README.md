# Project Builder Tool

## Introduction
The PBT is a simple project builder that helps you build the project easily.


## Usage
1. 💡 Class/Classes (Project/Configuration/Classes.json) <br>
This JSON data is located in Project/Configuration/Classes.json that contains all classes:
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

- For the "pattern" field:
   + ⚠️ **Note**: Do not remove "first", "mid" or "last" in the "pattern" field; if you remove one of those, then the builder will not work.

2.  💡 BuildModule (`Project/Configuration/BuildModule.json`) <br>
- This JSON file contains the properties of all the modules in your project.
- "class" field: It identifies the class name in the Classes.json file located in Project/Configuration.
- "name" field: It identifies the name of the module in the allowModuleList.
- ⚠️ **Note**
    + all modules' properties will be contained in `"file"` array.
    + do not skip `input`, `output`, `class` and `name`

3. 💡 allowModuleList (`Project/Configuration/allowModuleList`) <br>
- This file determines which modules are allowed to be built.
 
