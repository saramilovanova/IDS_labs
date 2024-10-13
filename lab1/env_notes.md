## Vanilla python + pip

- Make an environment
`python -m venv .venv`

- Activate the environment
`.venv\Scripts\activate`

At the begging of the command line you should see the name of the
environment in brackets e.g. ` (.venv) C:\Users\user\project> `.

- Install a package (or multiple) into the environment
`pip install ipykernel pandas matplotlib scikit-learn`

- Install packages from requirements.txt
`pip install -r requirements.txt`

- Export the list of installed packages
`pip freeze > requirements.txt`

- Deactivate the environment
`deactivate`

## Conda

- Make an environment
`conda create -n myenv`

(You can specify the python version with `python=3.8`)

- Activate the environment
`conda activate myenv`

- Install a package (or multiple) into the environment
`conda install ipykernel pandas matplotlib scikit-learn`

You can specify the conda forge channel with `-c conda-forge`,
or specify it as the default `conda config --env --add channels conda-forge`

- Deactivate the environment
`conda deactivate`

- Export the list of installed packages
`conda env export --no-builds > environment.yml`

- Create an environment from a file
`conda env create -n myenv2 -f environment.yml`

- Deactivate the environment
`conda deactivate`

- Remove the environment
`conda env remove -n myenv`


## Astral uv
A very fast drop-in replacement for pip, written in rust.
Download uv from https://docs.astral.sh/uv/getting-started/installation/.

- Make an environment
`uv venv`

Name can be specified using `uv venv myenv`

A Python version can be requested using `uv venv --python 3.11`. This requires the specified
Python version to be available on the system, if unavailable, uv will download it.

- Activate the environment
`.venv\Scripts\activate`

- Install a package (or multiple) into the environment
`uv pip install ipykernel pandas matplotlib scikit-learn`

- Install packages from requirements.txt
`uv pip install -r requirements.txt`

- Export the list of installed packages
`uv pip freeze > requirements.txt`

- Deactivate the environment
`deactivate`
