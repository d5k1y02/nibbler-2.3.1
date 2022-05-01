# -*- coding: utf-8 -*-
"""

@author: Desmond Yancey
"""
import os
import numpy as np
from sklearn import tree
from joblib import dump, load
import sys
import tensorflow as tf


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
    tdarr = []
    i = 0
    tdarr = np.zeros(0)
    while(i < 128):
        sarr = np.zeros(8)
        if(arr[i] == 'p'):
            sarr[0] = 1
        elif(arr[i] == 'r'):
            sarr[1] = 1
        elif(arr[i] == 'n'):
            sarr[2] = 1
        elif(arr[i] == 'b'):
            sarr[3] = 1
        elif(arr[i] == 'q'):
            sarr[4] = 1
        elif(arr[i] == 'k'):
            sarr[5] = 1
        i+=1
        if(arr[i]) == 'b':
            sarr[6] = 1
        if(arr[-1] == 1):
            sarr[7] = 1
        i+=1
        tdarr = np.concatenate((tdarr, sarr))
    return tdarr

def main(argv):
    pos = []
    pos.append(np.array(read_position(str(fen_to_array(argv[1])))))
    pos = np.array(pos)
    clf = tf.keras.models.load_model('keras_nn/')
    pred = np.argmax(clf(pos).numpy())
    print(pred)
    # return pred

#print(clf.score(X_test2, y_test))

if __name__ == "__main__":
   main(sys.argv)