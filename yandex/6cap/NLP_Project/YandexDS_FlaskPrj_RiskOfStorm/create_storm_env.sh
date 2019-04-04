#!/usr/bin/env bash

# Please run it in linux-default terminal, not in Pycharm


conda create --name storm python=3.7 scikit-learn="0.20.1" nltk="3.4" flask="1.0.2" -y
conda activate storm
conda list
conda activate base
