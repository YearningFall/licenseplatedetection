# Need to install ultralytics and yolo first, then open these files using open folder option in VS Code
# so the program can find the source image
from ultralytics.yolo.engine.model import YOLO

Model = YOLO("best.pt") # Check README.md for best.pt download link, move it into this folder
Result = Model.predict(source='./Source/27.png', show=True, save=True) 
# change file name in source='' to detect plate in that file, don't forget about file type as well (.jpg, .png, .mp4)
# after the program is done, you can find the results in the runs folder