# Notes

state of boring SUSY in mX and mchi0 space [LL]
Use contour stitching to combine latest from ATLAS and CMS in normal planes
https://github.com/histfitter/histfitter/blob/master/scripts/multiplexContours.py


# Running goals

* A single plot that has the state of the art observed exclusion for
  * gluino vs chi0
  * squark (n-fold degenerate) vs chi0
  * stop vs chi0
  * sleptons?

But there are a lot of model assumptions that go into this. What if we with a low opacity, drew each scenario's muxed contours. So in some way, the darkness of the color tells you how many different kinds of signatures are represented in the exclusion.

# Results to use

Use scraper in this directory to build lists of HEPData results. This also builds folders according to arxiv identifier.

We should manually go through and make sure the paper belongs in this plot, and then download the data (probably CSV?) of the contour and put it in the relevant folder.

* stop->c+chi0 (https://inspirehep.net/literature/2842361)
  * https://www.hepdata.net/record/ins2842361
  * https://www.hepdata.net/record/ins2842361?version=1&table=Contour%204
* Wino from VBF+MET (https://inspirehep.net/literature/2835159)
  * https://www.hepdata.net/record/ins2835159?version=1&table=Observed%20exclusion%20limits%20from%20Figure%208
* Higgsino from photon+b (https://inspirehep.net/literature/2773395)
  * https://www.hepdata.net/record/ins2773395?version=1&table=Exclusion%20contour%204
