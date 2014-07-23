# Branch-Based Configurator

## Overview

This script allows you to create branch-based configuration for your projects (currently only Git is supported).
It uses INI-like syntax to define configurations.
You can specify regex as a branch name:
```
[develop]
API_KEY=@"1111111"
SECRET=@"1111111"

[feature/ipad]
API_KEY=@"222222"
SECRET=@"222222"

[feature/.*]
API_KEY=@"33333"
SECRET=@"33333"
```
Be sure to place sections in order from the most specific to the least specific.
The script will use the first matching section.

## Example

```
python branchconfig.py -p path_to_working_copy -c config.ini -o test.h
```
Using config file from Overview section and assuming that you are on branch feature/test
this command will generate file ```test.h``` with the following contents:

```
/* This file was generated automatically. DO NOT MODIFY IT */
#ifndef __CONFIG_feature_test__
#define __CONFIG_feature_test__
#define API_KEY @"33333"
#define SECRET @"33333"
#endif
```
You can also use script ```configprocessor.py``` if you want manually specify
required section:

```
python configprocessor.py -c config.ini -o test.h -s feature/test
```

## Requirements

Only [GitPython](https://pythonhosted.org/GitPython/0.3.1/tutorial.html) is required.
It can be installed through pip:
```
pip install GitPython
```
