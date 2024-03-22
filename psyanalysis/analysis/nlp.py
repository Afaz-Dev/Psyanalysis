from difflib import SequenceMatcher
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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

#NLP Analysis ==================================================

def analyze_similarity(message1, message2) :
  tfidf_vectorizer = TfidfVectorizer()
  tfidf_matrix = tfidf_vectorizer.fit_transform([message1, message2])

  similarity_matrix = cosine_similarity(tfidf_matrix)
  similarity_score = similarity_matrix[0][1]

  similarity_percentage = similarity_score * 100

  return similarity_percentage

def analyze_arrays(messages1, messages2) :
  history1 = " ".join(messages1)
  history2 = " ".join(messages2)

  tfidf_vectorizer = TfidfVectorizer()

  tfidf_matrix = tfidf_vectorizer.fit_transform([history1, history2])
  similarity_matrix = cosine_similarity(tfidf_matrix)

  similarity_score = similarity_matrix[0][1]

  similarity_percentage = similarity_score * 100

  return similarity_percentage

def analyze_message(message, key) :
  datarr = []
  try :
    datarr = trainDat[key]
  except KeyError :
    return "Key not found"

  try :
    perc = analyze_arrays(datarr, [message])
    return perc
  except Exception as err :
    return "Error: " + str(err)

def analyze_dat(messageArr, key) :
  datarr = []
  try :
    datarr = trainDat[key]
  except KeyError :
    return "Key not found"

  try :
    perc = analyze_arrays(datarr, messageArr)
    return perc
  except Exception as err :
    return "Error: " + str(err)

#MBTI Analysis ==================================================
