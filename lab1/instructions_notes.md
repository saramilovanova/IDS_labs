### CONDA

- environment

`conda create -m idsev python=3.10`

`conda activate idsev`

`conda remove -m ENV_NAME  --all`

- packages

`conda install pandas`

`conda install -c conda-forge numpy`

`conda config --env --add channels conda-forge`

`conda install xlrd`

`conda config --set solver libmamba`

`conda install ipykernel`

- export

`conda env export`

`conda env export --no-builds`

`conda env export --no-builds > environment.yml`

`pip freeze > requirements.txt`

`conda env create -f environment.yml`



### GIT

git init

git add instructions.txt

git add . #add all

git commit -m "initial commit"

git status

###### create file .gitignore

git clone https://github.com/saramilovanova/IDS_labs.git

git push