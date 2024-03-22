from difflib import SequenceMatcher
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from psyanalysis.analysis import diff, nlp
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

def open_training(dat_path) :
  try :
    with open(dat_path, 'r') as file:
      global trainDat
      trainDat = json.load(file)
      print("Training data loaded successfully")
      diff.setDat(trainDat)
      nlp.setDat(trainDat)
      return trainDat
  except Exception as err :
    raise Exception(str(err) + "\nEnsure that your file path to the json training file is correct")
