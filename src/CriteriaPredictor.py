# -*- coding: utf-8 -*-
"""

@author: Desmond Yancey
"""
import os
import numpy as np
from sklearn import tree
from joblib import dump, load
import sys


# def read_position(file):
#     pos_str = file.read()
#     pos_str = pos_str.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '').replace('\n', ',').replace(' ', '')
#     pos_str = pos_str.strip(',')
#     arr = pos_str.split(',')
#     i = 0
#     j = 1
#     tdarr = np.zeros((8,8,2))
#     for k in range(8):
#         for l in range(8):
#             tdarr[l][k][0] = ord(arr[i])
#             tdarr[l][k][1] = ord(arr[j])
#             i+=2
#             j+=2
#     return tdarr

# def get_labels(file_name):
#     file = open(file_name)
#     labels = []
#     for line in file.readlines():
#         labels.append(line.split(',')[1].strip('\n'))
#     return labels

# def get_positions(path):
#     positions = []
#     for filename in os.listdir(path):
#         with open(path + filename, 'r') as f:
#             positions.append(read_position(f))
#     return positions


# def train_tree_classifier():
#     X_train = np.array(get_positions("./chessdataset/train/"))
#     y_train = get_labels("chess_labels_train.csv")
    

#     d1, d2, d3, d4 = X_train.shape
#     X_train2 = X_train.reshape((d1, d2*d3*d4))
#     clf = tree.DecisionTreeClassifier()
#     clf = clf.fit(X_train2, y_train)
    
#     dump(clf, 'tree.joblib')
#     return 

#X_test = np.array(get_positions("./chessdataset/test/"))
#y_test = get_labels("chess_labels_test.csv")

#d1, d2, d3, d4 = X_test.shape
#X_test2 = X_test.reshape((d1, d2*d3*d4))

#train_tree_classifier()

def fen_to_array(input_fen):
    
    position = [[('e', 'e') for i in range(8)] for j in range(8)] #board[coord1][coord2] = (piece, color)
    fen = input_fen.replace('/', ',')
    fen = fen.replace(' ', ',')
    ranks = fen.split(',')
    k = 0
    for i in range(8):
        for j in ranks[i]:
            if not(j.isdigit()):
                if j.islower():
                    position[i][k] = (j, 'b')
                    k+=1
                else:
                    position[i][k] = (j.lower(), 'w')
                    k+=1
            else:
                k+=int(j)
        k = 0
    return position

def read_position(pos_str):
    pos_str = pos_str.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '').replace('\n', ',').replace(' ', '')
    pos_str = pos_str.strip(',')
    arr = pos_str.split(',')
    i = 0
    j = 1
    tdarr = np.zeros((8,8,2))
    for k in range(8):
        for l in range(8):
            tdarr[l][k][0] = ord(arr[i])
            tdarr[l][k][1] = ord(arr[j])
            i+=2
            j+=2
    return tdarr

def main(argv):
    pos = np.array(read_position(str(fen_to_array(argv[1]))))
    d1, d2, d3 = pos.shape
    pos2 = pos.reshape(1, -1)
    clf = load('tree.joblib')
    pred = clf.predict(pos2)
    print(pred)
    # return pred

#print(clf.score(X_test2, y_test))

if __name__ == "__main__":
   main(sys.argv)