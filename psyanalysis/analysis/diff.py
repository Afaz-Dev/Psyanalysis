from difflib import SequenceMatcher
import numpy as np
from psyanalysis.training import data_tables
import json

#Training ==================================================

global trainDat
trainDat = {}


LocalTrainDat = {
  "I" : [],
  "E" : [],
  "S" : [],
  "N" : [],
  "T" : [],
  "F" : [],
  "J" : [],
  "P" : []
}

def setDat(dat) :
  global trainDat
  trainDat = dat


#Basis Analyzing Algorithms ==================================================

#Basis similarity comparison
def similarity_percentage(string1, string2) :
    matcher = SequenceMatcher(None, string1, string2)
    similarity = matcher.ratio() * 100
    return similarity


def compare_messages(msg : str, key : str) :
  sum = 0.00
  dex = 0
  for string in trainDat[key] :
    sum += float(similarity_percentage(string, msg))
    dex += 1

  dex = dex * 100
  return (sum / dex) * 100
