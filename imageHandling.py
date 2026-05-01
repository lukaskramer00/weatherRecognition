import pandas 
from pathlib import Path 
import os 

IMAGE_PATH = Path('./data/images')
TRAIN_TEST_SPLIT = 0.7

if not os.path.exists('./data/train'):
    os.mkdir('./data/train')
if not os.path.exists('./data/test'):
    os.mkdir('./data/test')

def createTrainAndTestDatafolder(path: Path) -> None:
    for folder in IMAGE_PATH.iterdir():

        folderSize = len(list(folder.iterdir()))
        trainSize = folderSize * TRAIN_TEST_SPLIT
        os.mkdir('./data/train/' + folder.name) if not os.path.exists('./data/train/' + folder.name) else None
        os.mkdir('./data/test/' + folder.name) if not os.path.exists('./data/test/' + folder.name) else None

        counter = 0
        for image in folder.iterdir(): 
            if counter < trainSize:
                image.copy('./data/train/' + folder.name + '/' + image.name)
            else:
                image.copy('./data/test/' + folder.name + '/' + image.name)
            counter += 1


if __name__ == "__main__":
    createTrainAndTestDatafolder(IMAGE_PATH)