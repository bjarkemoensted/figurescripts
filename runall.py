#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runs a number of external scripts to generate plotting data and produce plots
that are visually consistent.
Runs all files in containing folder that end in *_gen.py to generate data.
Runs all files ending in *_plot.py to produce plots from said data.
"""

from __future__ import print_function
import os
from glob import glob
from subprocess import Popen
from time import sleep

DEVNULL = open(os.devnull, 'w')

GENERATE = True  # Whether to generate data from scratch
PLOT = True  # Whether to do plots

def print_section(msg):
    print("\n"+42*'-'+"\n"+msg+"\n"+42*'-')

# Get absolute path to current directory
thisfile = os.path.realpath(__file__)
_here = os.path.dirname(thisfile)

def run_async(script_list):
    '''Asynchronously executes input list of python scripts.'''
    # Map of filenames to processes
    fn2p = {fn : Popen(["python", fn], stdout = DEVNULL) for fn in script_list}
    print("Running %d processes" % len(fn2p))
    # Try/catch because we must kill remaining procs if there's trouble
    try:
        while len(fn2p) > 0:
            done = []  # List of procs completed in this loop iteration
            for fn, p in fn2p.items():
                # Get the status of the processs
                status = p.poll()
                if status == None:
                    continue  # It's still running
                elif status == 0:
                    # Yay, it's done.
                    print(fn.split(os.sep)[-1], "completed successfully")
                    done.append(fn)
                else:
                    print(fn, "failed with exit code", status)
                #
            # Remove completed jobs from dictionary
            for fn in done:
                del fn2p[fn]
            # Sleep so we don't hog a CPU core checking progress
            sleep(1)
        #
    except:
        print_section("Exception occurred. Killing remaining %d processes."
                      % len(fn2p))
        # If exception occurs, kill remaining jobs
        for p in fn2p.values():
            p.kill()
        # then reraise exception
        raise

# Generate data for plots
genfiles = glob(os.path.join(_here, '*_gen.py'))
if GENERATE:
    print_section("Generating data")
    run_async(genfiles)

# Generate plots from data
plotfiles = glob(os.path.join(_here, '*_plot.py'))
if PLOT:
    print_section("Generating plots")
    run_async(plotfiles)

print_section("Finished running %d scripts." 
              % (GENERATE*len(genfiles)+PLOT*len(plotfiles)))