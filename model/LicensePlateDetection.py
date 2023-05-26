# Need to install ultralytics and yolo first, then open these files using open folder option in VS Code
# so the program can find the source image
from ultralytics.yolo.engine.model import YOLO

Model = YOLO("best.pt")   
Result = Model.predict(source='Driving in Bangkok Thailand 4k.mp4', show=True, save=True) #Display the video
# change file name in source='' to detect plate in that file, don't forget about file type as well
# after the program is done, you can find the results in the - folder