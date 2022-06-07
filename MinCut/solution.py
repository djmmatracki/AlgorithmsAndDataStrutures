import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    min_cut_1 = cv2.imread("min_cut_seg_1.png", cv2.IMREAD_GRAYSCALE)
    YY, XX = min_cut_1.shape

    scrible_FG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_FG[100:120, 100:120] = 255

    scrible_BG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_BG[0:20, 0:20] = 255

    I = cv2.resize(min_cut_1,(32,32))
    scrible_BG = cv2.resize(scrible_BG,(32,32))
    scrible_FG = cv2.resize(scrible_FG,(32,32))


    hist_FG = cv2.calcHist([I],[0],scrible_FG,[256],[0,256])
    hist_FG = hist_FG/sum(hist_FG)

    hist_BG = cv2.calcHist([I],[0],scrible_BG,[256],[0,256])
    hist_BG = hist_BG/sum(hist_BG)

