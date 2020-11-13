#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Steven Macías
# Created Date: 06/11/2020
# =============================================================================

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

OUTPUT_DIR = "/home/steven/workspace/greensteam/nas/steven/Special_Course/SPLIT/"

# time to seconds
def t2s(min, sec):
    return (60*min)+sec

# LEVEL0 = Clean
# LEVEL1 = Slime
# LEVEL2 = Phytoplankton
# LEVEL3 = Zooplankton

video_results={
    "Clean":0,
    "Slime":0,
    "Phytoplankton":0,
    "Zooplankton":0
}
video_files = {
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_1.MP4":
  [
    [40,43, "Clean"],
    [46,50, "Phytoplankton"],
    [56,60, "Phytoplankton"],
    [ t2s(1,29) ,t2s(1,35), "Slime"]
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_2.MP4":
  [
    [t2s(1,6),t2s(1,11), "Clean"],
    [t2s(1,15),t2s(1,17), "Slime"],
    [t2s(1,30),t2s(1,37), "Slime"],
    [t2s(2,9),t2s(2,11), "Phytoplankton"],
    [t2s(2,16),t2s(2,35), "Slime"],
    [t2s(2,57),t2s(3,5), "Slime"],
    [t2s(3,9),t2s(3,14), "Clean"],
    [t2s(3,20),t2s(3,22), "Slime"],
    [t2s(3,20),t2s(3,22), "Slime"],
    [t2s(3,35),t2s(3,36), "Slime"],
    [t2s(3,41),t2s(3,42), "Clean"]
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_4.MP4":
  [
    [t2s(0,17),t2s(0,22), "Phytoplankton"],
    [t2s(0,30),t2s(0,33), "Phytoplankton"],
    [t2s(0,35),t2s(0,37), "Clean"],
    [t2s(0,41),t2s(0,44), "Clean"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_5.MP4":
  [
    [t2s(0,24),t2s(0,32), "Phytoplankton"],
    [t2s(0,35),t2s(0,36), "Clean"],
    [t2s(0,38),t2s(0,44), "Zooplankton"],
    [t2s(1,26),t2s(1,30), "Zooplankton"],
    [t2s(1,38),t2s(1,41), "Phytoplankton"],
    [t2s(1,43),t2s(1,58), "Clean"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_6.MP4":
  [
    [t2s(0,17),t2s(0,22), "Phytoplankton"],
    [t2s(0,27),t2s(0,36), "Slime"],
    [t2s(0,37),t2s(0,39), "Zooplankton"],
    [t2s(0,48),t2s(0,56), "Zooplankton"],
    [t2s(1,9),t2s(1,12), "Zooplankton"],
    [t2s(1,20),t2s(1,22), "Zooplankton"],
    [t2s(1,30),t2s(1,31), "Zooplankton"],
    [t2s(1,43),t2s(1,53), "Slime"],
    [t2s(2,6),t2s(2,8), "Slime"],
    [t2s(2,20),t2s(2,24), "Zooplankton"],
    [t2s(2,35),t2s(2,42), "Zooplankton"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_8.MP4":
  [
    [t2s(0,20),t2s(0,21), "Zooplankton"],
    [t2s(1,18),t2s(1,19), "Zooplankton"],
    [t2s(1,25),t2s(1,26), "Zooplankton"],
    [t2s(1,28),t2s(1,32), "Slime"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_9.MP4":
  [
    [t2s(0,22),t2s(0,32), "Clean"],
    [t2s(0,34),t2s(0,48), "Zooplankton"],
    [t2s(0,52),t2s(1,4), "Clean"],
    [t2s(1,9),t2s(1,10), "Clean"],
    [t2s(1,16),t2s(1,21), "Clean"],
    [t2s(5,1),t2s(5,3), "Slime"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_10.MP4":
  [
    [t2s(5,37),t2s(5,41), "Zooplankton"],
    [t2s(7,3),t2s(8,10), "Clean"],
    [t2s(9,21),t2s(9,22), "Zooplankton"],
  ]
}


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("VydCut Script")
    for file, intervals in video_files.items():
        print(file)
        index=0
        for interval in intervals:
            target = OUTPUT_DIR+file.split("/")[-1].split(".")[0]+"_"+interval[2]+"_CUT"+str(index)+".mp4"
            print("Splitting interval %d from second %s to %s and saving in %s" % (index, str(interval[0]), str(interval[1]), target))
            ffmpeg_extract_subclip(file, interval[0], interval[1], targetname=target)
            index+=1
            video_results[interval[2]]+=1
    print(video_results)
if __name__ == "__main__":
    main()
