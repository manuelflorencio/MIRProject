import essentia
import os
import json
import csv
from essentia.standard import *
import music21 as mus
from essentia import pool
import numpy as np
import matplotlib.pyplot as plt

inp = '/home/manu/Dropbox/MasterUPF/Asignaturas/2Trim/Music Information Retrieval/MIR Project/evaluation/Dataset/Saarland/Bach_BWV849-01_001_20090916-SMD.mp3'

inpm = '/home/manu/Dropbox/MasterUPF/Asignaturas/2Trim/Music Information Retrieval/MIR Project/evaluation/Dataset/Saarland/Bach_BWV849-01_001_20090916-SMD.mid'

loader = essentia.standard.MonoLoader(filename = inp)
audio = loader()
multip = MultiPitchKlapuri(frameSize=2048, hopSize=441)
f0vec = multip(audio)
time = 0

os.chdir('..')
os.chdir('evaluation')

f = open('dataKlapuri.txt', 'w')
for f0 in f0vec:
	f.write(str(time) + "\t")
	for f0s in f0:
		f.write(str(f0s) + "\t")
	f.write("\n")
	time += 0.01
