#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains parameters to be used by plotting scripts to produce visually
consistent plots.
"""

import os

# Define colors to be used in plots
#wine = (110/256,14/256,14/256)
col1 = (156/256,30/256,36/256)
col2 = (35/256,39/256,135/256)
col3 = (203/256,150/256,93/256)

# Define default matplotlib parameters
linewidth = 2.0
plt_settings = {'color' : col1,
                'linewidth' : linewidth}

# Matplotlib style
style = "ggplot"

# Define standard setting for saving plots in various formats
plt_png = {'dpi' : 100}
ext2kwargs = {
              'pdf' : {},
              'png' : plt_png
              }

def get_data_filename(full, extension = None):
    '''Helps a script determine the filename for its corresponding data file.
    For instance 'hest_gen.py' determines that it should use hest_data for its
    output, and 'hest_plot.py' that is should load data from 'hest_data'.'''
    
    filename = full.split(os.sep)[-1]
    old = filename[:-3]
    suffix = old.split("_")[-1]
    if suffix in ["gen", "plot"]:
        new = filename.replace(suffix+".py", "data", 1)
    else:
        raise ValueError("Bad filename")
    
    if extension != None:
        new += "."+extension
    full = full[:-len(filename)]
    return full+new

def get_plot_filename(full, extension = None):
    '''Determines output filename for plotting scripts.'''
    filename = full.split(os.sep)[-1]
    old = filename[:-3]
    new = full[:-len(filename)]+"_".join(old.split('_')[:-1])
    if extension != None:
        new += "."+extension
    return new

if __name__ == '__main__':
    print(get_data_filename())
    str.replace