#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example plotting script
"""

import json
import meta
import matplotlib.pyplot as plt

# Load data (change extension if you save data in another format)
INFILE = meta.get_data_filename(__file__, extension = "json")
with open(INFILE, 'r') as f:
    X, Y = json.load(f)

# Draw the plot with parameters from meta file
plt.style.use(meta.style)
plt.plot(X, Y, **meta.plt_settings)

# Produce a plot for each of the extension, parameter pairs in meta file.
for ext, kwargs in meta.ext2kwargs.items():
    outfile = meta.get_plot_filename(__file__, extension = ext)
    plt.savefig(outfile, **kwargs)