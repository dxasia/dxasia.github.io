# DXAsia

This repository is used to build the DXAsia.in site.

Building the site requires Jekyll. 

Creation of initial indices:

    python3 dxasia.py —-fn FILE init [language|station]

The default FILE is langstn.xlsx. The indices
only need to be regenerated if the language or station set changes. 

To update the CSV files

    python3 dxasia.py —-fn FILE data [language|station]
