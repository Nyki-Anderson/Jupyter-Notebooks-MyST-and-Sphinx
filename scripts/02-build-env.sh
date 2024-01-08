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
python -m ipykernel install --user --name=jupyter

# Initialize node.js
npm init

# Install ijavascript kernel
npm install ijavascript
ijinstall

# Change to the lib directory for next few steps.
cd $1/lib

# Install xeus-lua kernel which has a dependency on xcanvas. This dependency must be installed from source.
git clone git@github.com:jupyter-xeus/xcanvas.git
cd xcanvas && mkdir build && cd build
cmake -D CMAKE_INSTALL_PREFIX=$CONDA_PREFIX ..
make install

# Go back to the conda_config directory
cd $1/lib

# Install xeus-lua from source
git clone git@github.com:jupyter-xeus/xeus-lua.git
cd xeus-lua && mkdir build && cd build
cmake .. -D CMAKE_PREFIX_PATH=$CONDA_PREFIX -D CMAKE_INSTALL_PREFIX=$CONDA_PREFIX -D CMAKE_INSTALL_LIBDIR=lib