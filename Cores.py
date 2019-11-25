import multiprocessing
import os

def CheckCores():
    global cores
    # Used when building Doc2Vec models - 8 means I am running locally on Mac; 16 means I am running on ziggy-dev
    cores = multiprocessing.cpu_count()
    return cores

def FileExists(fname):
    try:
        my_file = open(fname)
        return True
    except IOError:
        return False

def JaccardSimilarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)