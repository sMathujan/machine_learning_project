## Start Machine Learning Project

### Software and Account Requirement

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda environment
```
conda create -p venv python==3.7 -y
```

Activating virtual environment
```
conda activate venv/
```
OR
```
conda actuvate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```
OR
```
git add <file_name>
```
> Note: To ignore file or folder from git, we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all version maintain by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku, we need 3 information
1. HEROKU_EMAIL = siva.mathu1997@gmail.com
2. HEROKU_API_KEY = 14df0c9f-c216-4e09-982d-1f6f7aa1c5a1
3. HEROKU_APP_NAME = ml-regresser-app


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker images
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 52b382f30a86
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```


```
python setup.py install
```

Install ipykernal
```
pip install ipykernal  or  pip install jupyter
```