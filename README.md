This repository contains a generic template for AI team repositories.
In particular, it gives an example for:
 - having a specific conda environment
 - creating a python module
 - exposing the models via an API
 - exposing the APIs as a flask webservice
 - exposing the demo application via docker

1) Conda environments:

Through the development phase, environments should always be exported as a .yml file:
```
conda activate env_name
conda env export > doc/environment.yml
```

This allows a new user on the repository to recreate the same environment:
```
conda env create -n env_name -f doc/environment.yml
source activate env_name
```

2) Creating a python module + exposing the backend:

This template python module is based on the iris task.  
It features a way to secure model architectures, data paths, ..., and provides a way to expose models with a template API + offers the possibility of exposing it to the world with a flask webservice (backend).
   
In short, if you want to run the backend webservice (port and IP can be specified):
```
cd python/iris/webservice/
python run_backend.py
```
  
If you want to run the front, once the back webservice has been launched,
you need to specify the URL_BACK in front/iris_app/run_front.py, and then run:
```
cd front
python run_front.py
```
  
Once both the backend and the front have been launched, it is possible for a user to access the demo app on the internet via the IP of the host and the port of the front.

3) Docker:

Usually the demo app shouldn't been launched outside a docker container. The reason is that an app is really dependent on the environment (OS, packages (wget, curl, zip, ...), python environments, ...), the environments should always be secured. Docker allows easy deployment and real time monitoring of the app.

To build the app image (container generator) :
```
cd docker/images/iris_app/
bash build_image.sh
```

To launch the app, run :
```
bash run_app.sh
```

You might want to monitor the app by launching:
```
docker logs --follow iris_app
```

You might also want to have a closer look to : docker ps, docker rm, docker stop, docker restart, docker images...


Install Git LFS to handle big files (large file storage)
Download and install the Git command line extension. Once downloaded and installed, set up Git LFS and its respective hooks by running:

git lfs install
You'll need to run this in your repository directory, once per repository.

Select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.

git lfs track "*.psd"
Make sure .gitattributes is tracked

git add .gitattributes
There is no step three. Just commit and push to GitHub as you normally would.

git add file.psd
git commit -m "Add design file"
git push origin master

pip install -U pytest
pip install pytest-cov

4) Check code using pylint tool  

5) Commit code using following tags:
- ADD: new feature
- ENH: enhancement
- REFAC: refactoring
- FIX: bug fix
- MAINT: maintenance, changes based on dependences' updates
- DOC: documentation
- STYLE: coding style
