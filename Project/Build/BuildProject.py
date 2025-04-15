#!/bin/python

import json
import os

with open('Project/Configuration/allowModuleList', 'r') as f:
    allowModuleListData = f.read().split('\n')

with open('Project/Configuration/Classes.json', 'r') as f:
    classes = json.load(f)

with open('Project/Configuration/BuildModule.json', 'r') as f:
    buildModule = json.load(f)

with open('Project/Configuration/BuildBase.json', 'r') as f:
    BuildBase = json.load(f)

for i in buildModule['file']:
    input_ = i['input']
    output_ = i['output']
    class_ = i['class']
    name_ = i['name']

    if classes.get(class_) is None:
        print("error (invalidClass) : (Configuration > Classes): invalid class")
        exit(-1)

    d = classes[class_]

    isSkipped = True
    for j in allowModuleListData:
        if name_ == j:
            isSkipped = False
            break

    if isSkipped == False:
        left = ''
        right = ''
        if d['as'] == 'in-out':
            left = input_
            right = output_
        elif d['as'] == 'out-in':
            left = output_
            right = input_

        pattern = d['pattern']
        dCombine = pattern['first'] + left + pattern['mid'] + right + pattern['last']
        os.system(dCombine)

for i in BuildBase['file']:
    input_ = i['input']
    output_ = i['output']
    class_ = i['class']

    if classes.get(class_) is None:
        print("error (invalidClass) : (Configuration > Classes): invalid class")
        exit(-1)

    d = classes[class_]

    left = ''
    right = ''
    if d['as'] == 'in-out':
        left = input_
        right = output_
    elif d['as'] == 'out-in':
        left = output_
        right = input_

    pattern = d['pattern']
    dCombine = pattern['first'] + " " + left + " " + pattern['mid'] + " " + right + " " + pattern['last']
    os.system(dCombine)
