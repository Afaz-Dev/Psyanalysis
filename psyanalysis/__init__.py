"""
A simple string psychological analysis and pattern finding module. Good for comparing message similarity and determining personality probability between users.
"""

from difflib import SequenceMatcher
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from psyanalysis.training import data_tables
import json


__version__ = "1.0.1"
