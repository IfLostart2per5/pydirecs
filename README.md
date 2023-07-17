# pydirecs
Some files that process other files, haha


## Notes  
this is a project made for fun. Can be used for production uses? Maybe...


## Objectives
Make python a bit to more closer to C...


## How to run
it need to be runned on terminal... sorry for all IDE's👉👈

```sh
python3 <directive processor>.py file.py
#OR
python <directive processor>.py file.py
#where "file" can be any valid name  of a file
```
# Directives

## include

when it find a `$include("path/to/a/pyfile")` in a code ( or more ), him compile them in a code object and exec it, for example:  

```python
$include("./file1.py")
$include("./file2.py")

print(some_var_from_the_files_above)

#and pratically everything from files above!
```
#### Whats the difference between import and $include?
*2 note  
it's more faster to load local files. Different from import, where the module/file is loaded in memory, as a class, and more, more.. and include... can include files in runtime!

*notes:
1. 
It's too experimental, for example, it can't use python modules, and will give more work to solve name conflicts, so, by precaution, continues to use the classic import ;) this'll serves to cases that is needed for speed and performance to use modular files, okay?

2: it depends from some factors...
