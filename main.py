import math
import ffmpeg
import cv2
import numpy as np
import os


def main():
    print("Add a video to the same folder as this file and then input the filename below. (e.g. \"BadApple.mp4\")")
    filepath = input("> ")
    print("\nInput your desired height in pixels.")
    height = int(input("> ")) * 2 + 2
    print("\nInput the duration if you want to trim the video, otherwise leave it blank.")
    duration = input("> ")
    print("\nInput the start coordinates of the canvas.")
    startX = int(input("X: > "))
    startY = int(input("Y: > "))
    startZ = int(input("Z: > "))
    print("Converting video...")

    stream = ffmpeg.input(filepath)

    if duration:
        stream = ffmpeg.trim(stream, duration=duration)

    if os.path.exists("output.mp4"):
        os.remove("output.mp4")

    stream = ffmpeg.filter(stream, 'scale', width=height, height=-2)
    stream = ffmpeg.filter(stream, 'fps', fps=20, round='up')
    stream = ffmpeg.output(stream, 'output.mp4')
    ffmpeg.run(stream)

    print("Video converted successfully, generating animation frames, this may take a while.")

    stream = cv2.VideoCapture('output.mp4')
    frame_count = stream.get(cv2.CAP_PROP_FRAME_COUNT)
    count = 0
    success = 1

    if not os.path.exists("output"):
        os.makedirs("output")

    if not os.path.exists("output/frames"):
        os.makedirs("output/frames")

    tick = open('output/tick.mcfunction', 'a')
    tick.write("execute if score .current frame <= .max frame run scoreboard players add .current frame 1\nexecute if score .current frame > .max frame run scoreboard players set .current frame 0\n")
    tick.close()

    currentPlacement = dict()

    while success:
        success, image = stream.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh_hold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

        blocks = dict()

        file = open('output/frames/frame' + str(count) + '.mcfunction', 'a')

        tick = open('output/tick.mcfunction', 'a')
        tick.write("execute if score .current frame matches " + str(count) + " run function cb:frames/frame" + str(count) + "\n")
        tick.close()

        load = open('output/load.mcfunction', 'w')
        load.write("scoreboard objectives add frame dummy\n\nscoreboard players set .current frame 0\nscoreboard players set .max frame " + str(count))
        load.close()

        for (x, y), pixel in np.ndenumerate(thresh_hold):
            currentBlock = str(math.ceil(math.floor(x + 1) / 3)) + '-' + str(math.ceil(math.floor(y + 1) / 2))

            if not currentBlock in blocks:
                blocks[currentBlock] = []

            if pixel > 255 / 2:
                blocks.get(currentBlock).append("true")
            else:
                blocks.get(currentBlock).append("false")

            if len(blocks.get(currentBlock)) == 6:
                command = "setblock " + str(startX + math.ceil(math.floor(y) / 3)) + " " + str(startY - math.ceil(math.floor(x) / 3)) + " " + str(startZ) + " minecraft:chiseled_bookshelf["
                nbtData = ""
                i = 0

                for line in blocks[currentBlock]:
                    if line == "true":
                        nbtData = nbtData + "slot_" + str(i) + "_occupied=" + line + ","

                    i += 1

                if count == 0 or currentPlacement.get(currentBlock) != nbtData:
                    file.write('# ' + currentBlock + ':\n' + command + nbtData + ']\n\n')
                    currentPlacement[currentBlock] = nbtData

        file.close()
        count += 1

        print(str(count) + "/" + str(int(frame_count)) + " frames processed.")

        if count >= frame_count:
            success = 0

    print("Done, files saved to the \"output\" folder. Move everything into the \"functions\" folder of your datapack!")
    input("Hit enter to close.")


if __name__ == '__main__':
    main()
