#!/usr/bin/env bash

conda create --name riskofstorm python=3.7 scikit-learn="0.20.1" nltk="3.4" flask="1.0.2" -y
pip install dash
pip install dash-daq
conda activate riskofstorm
conda list
conda activate base
