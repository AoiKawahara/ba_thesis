import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# Google Driveのマウント
from google.colab import drive
drive.mount('/content/drive')

def Histogram_Computation(Image):
    Image_Height = Image.shape[0]
    Image_Width = Image.shape[1]
    Image_Channels = Image.shape[2]

    Histogram = np.zeros([256, Image_Channels], np.int32)

    for x in range(0, Image_Height):
        for y in range(0, Image_Width):
            Histogram[int(Image[x, y, 0] * 1.4), 0] += 1 # Hが0〜179なので1.4倍して0〜255にする
            for c in range(1, Image_Channels): # SとV
                Histogram[Image[x, y, c], c] += 1

    return Histogram

def Compute_Variance(Histogram):
    variances = []
    for c in range(Histogram.shape[1]):
        channel_values = Histogram[:, c]
        mean = np.sum(channel_values * np.arange(256)) / np.sum(channel_values)
        variance = np.sum(((np.arange(256) - mean) ** 2) * channel_values) / np.sum(channel_values)
        variances.append(variance)
    return variances

def main():
    folder_path = ''
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # ファイルの絶対パスを取得
        file_path = os.path.join(folder_path, file_name)

        # 画像を読み込む
        Input_Image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2HSV)

        # ヒストグラムの計算
        Histogram = Histogram_Computation(Input_Image)

        # # 計算結果の表示
        # for i in range(0, Histogram.shape[0]):
        #     for c in range(0, Histogram.shape[1]):
        #         print("Histogram[", i, ", ", c, "]: ", Histogram[i, c])

        # 分散を計算
        variances = Compute_Variance(Histogram)

        # 分散を表示
        print("Hチャンネルの分散: ", variances[0])
        print("Sチャンネルの分散: ", variances[1])
        print("Vチャンネルの分散: ", variances[2])

        # ヒストグラムのプロットと保存
        Plot_Histogram(Histogram, file_name)

def Plot_Histogram(Histogram, file_name):
    plt.figure()
    plt.title("Color Image Histogram")
    plt.xlabel("Intensity Level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(Histogram[:,0],'h')
    plt.plot(Histogram[:,1],'s')
    plt.plot(Histogram[:,2],'v')
    plt.savefig(f"")

if __name__ == '__main__':
    main()
