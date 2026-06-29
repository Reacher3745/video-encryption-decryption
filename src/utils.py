import random
import numpy as np

def per_sub(pt , pbox , sbox):
    pt = np.array(pt).flatten().tolist()
    pt1 = pt.copy()
    for i in range(5):
        for k in range(64):
            pt1[k] = pt[pbox[k]]
            pt1[k] = sbox[pt[k]]
            
    return np.array(pt1).reshape(8,

def permute(pt , pbox):
    pt = np.array(pt).flatten().tolist()
    pt1 = pt.copy()
    for k in range(64):
        pt1[k] = pt[pbox[k]]
    return np.array(pt1).reshape(8,8)
    
def sub(pt , sbox):
    pt = np.array(pt).flatten().tolist()
    pt1 = pt.copy()
    for k in range(64):
        pt1[k] = sbox[pt[k]]
    return np.array(pt1).reshape(8,8)
    
def diffusion(frame , key):
    eframe = frame.copy()
    for ch in range(3):
        for i in range(256):
            for j in range(256):
                eframe[i ,j , ch] = (frame[i,j,ch] ^ key[i , j , ch])
    return eframe 

def permuteinv(pt, pbox):
    pt = np.array(pt).flatten().tolist()
    pt1 = pt.copy()
    for k in range(64):
        pt1[pbox[k]] = pt[k]
    return np.array(pt1).reshape(8,8)
        
def subinv(pt, sbox):
    pt = np.array(pt).flatten().tolist()
    pt1 = pt.copy()
    for k in range(64):
        pt1[k] = sbox.index(pt[k])
    return np.array(pt1).reshape(8,8)
