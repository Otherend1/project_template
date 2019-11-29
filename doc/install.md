To install the project environment, install conda following dsml_tools/Docs/HOWTO and run:
```
conda env create -n environment_name -f environment.yml
```

To add a submodule, for instance dsml_tools:
```
git submodule add ../../DS-ML/dsml_tools.git externals/dsml_tools
```
Using relative address to our gitlab allows the submodule to work from any location.
/!\ Be carefull to specify external/submodule_name, because moving a submodule can be tricky, regarding git version.

to change submodule version:
```
cd externals/dsml_tools
git checkout commit_hash
cd ../..
git commit
```

Then, the setup after cloning the repo requires to clone the submodule using:
(Use git BASH on windows from l'Oreal network)
```
git submodule init
git submodule update
```

/!\ It is recommended to see the submodules as a shell that we do not modify. /!\
However, when located in external/submodule, we are in another git repo and we can work on this repo, make commits, etc, that will update the submodule (not the current project)

The submodule needs to be added in the path. The easiest seems to be through the __init__.py, see in python/project_name/.
