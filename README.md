# Chiseled bookshelf animations
A fun little project to generate Minecraft pixel art animations using the new block "chiseled bookshelf" and data packs. Check out the demo [here](https://www.reddit.com/user/Rezzorex/comments/yysbsb/bad_apple_recreated_with_minecraft_chiseled/).

![image](https://user-images.githubusercontent.com/73910894/202816365-5e2820d9-0bf1-4ab9-a2a0-d6cb478faf2f.png)

## Required python packages

[ffmpeg-python](https://pypi.org/project/ffmpeg-python/)
>pip install ffmpeg-python

[opencv-python](https://pypi.org/project/opencv-python/)
>pip install opencv-python

[numpy](https://pypi.org/project/numpy/)
>pip install numpy

## Usage instructions
1. Make sure you have the latest version of [python](https://www.python.org/downloads/) installed.
2. Open a command Window by pressing <kbd>⊞ Win</kbd> + <kbd>r</kbd> and then enter "cmd" and hit <kbd>Enter</kbd>. Install all of the required python packages by pasting each of the commands from above. 
3. Download the [code](https://github.com/Rezzorex/ChiseledBookshelfAnimations/archive/refs/heads/main.zip) and extract the files into a folder. Add the video you want to convert to that same folder.
4. Open the "main.py" file and a window should pop up. Follow the instructions on screen and then wait until the program has finished. There should now be a new folder called "output".
5. Copy the files from the output folder into your data packs "functions" folder. If you don't already have a data pack you can use the data pack template available with the download. If you do simply paste the files into "data/cb/functions".
6. Create a Minecraft world with the "update_1_20" data pack enabled. (You need to do this before generating the world, it can't be done after)
7. Add the generated data pack to your world and it should appear at the cords you specified.

To restart the animation you can run the command "/scoreboard player set .current frame 0"

## Note:
The data packs generated currently only works on snapshot 22w46a or later with the "update_1_20" data pack enabled.
