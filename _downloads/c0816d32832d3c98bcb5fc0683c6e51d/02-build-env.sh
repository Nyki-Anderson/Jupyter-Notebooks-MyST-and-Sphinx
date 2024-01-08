#! /opt/homebrew/bin/bash
# Run this script in the root directory as follows where <PROJECT_PREFIX> is the absolute path to root directory or the output of pwd command: 
# scripts/02-build-env.sh <PROJECT_PREFIX>

# Environment has been created. Now, we install the necessary packages in it. 
bash ./scripts/01-create-env.sh $1

# Source Miniconda so we can activate the env in the bash script.
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh

# Activate env and install ipykernel
conda activate jupyter
conda install ipykernel

# Link environment to Jupyter
python -m ipykernel install --user --name jupyter --display-name "Jupyter"

# Initialize node.js
npm init