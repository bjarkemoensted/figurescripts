# figurescripts
Python scripts to generate figures in a visually consistent manner.
Execute runall.py to run all files named <filename>_plot.py to produce plots.
If the boolean GENERATE is set in runall.py, files named <filename>_gen.py will be run first to produce data for plotting.
Settings like matplotlib style, color definitions, etc., are all defined in meta.py to encourage consistency, but can of course be overrided in the individual _plot files.