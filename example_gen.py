#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example data generation script
"""

import json
import meta
import numpy as np

# Determine output filename (change extension if you want another type)
OUTFILE = meta.get_data_filename(__file__, extension = "json")

# Generate some data to plot
f = lambda x: np.exp(0.5*x)*np.exp(-(x-2)**2)
X = np.arange(-1, 5, 0.1)
Y = f(X)

# Save the data in output file
with open(OUTFILE, 'w') as f:
    json.dump((X.tolist(), Y.tolist()), f)