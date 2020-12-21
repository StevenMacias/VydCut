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
    "Zooplankton":0,
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
    [t2s(0,41),t2s(0,54), "Clean"],
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
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_7.MP4":
  [
    [t2s(0,20),t2s(0,21), "Zooplankton"],
    [t2s(1,18),t2s(1,19), "Zooplankton"],
    [t2s(1,25),t2s(1,26), "Zooplankton"],
    [t2s(1,28),t2s(1,32), "Slime"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_8.MP4":
  [
    [t2s(0,22),t2s(0,32), "Clean"],
    [t2s(0,34),t2s(0,48), "Zooplankton"],
    [t2s(0,52),t2s(1,4), "Clean"],
    [t2s(1,9),t2s(1,10), "Clean"],
    [t2s(1,16),t2s(1,21), "Clean"],
    [t2s(5,1),t2s(5,3), "Slime"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_1/T1_9.MP4":
  [
    [t2s(5,37),t2s(5,41), "Zooplankton"],
    [t2s(7,3),t2s(8,10), "Clean"],
    [t2s(9,21),t2s(9,22), "Zooplankton"],
  ],
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_1.MP4":
  [
    [t2s(0,26),t2s(0,30), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_2.MP4":
  [
    [t2s(0,19),t2s(0,24), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_4.MP4":
  [
    [t2s(3,34),t2s(3,44), "Clean"],
    [t2s(4,7),t2s(4,10), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_6.MP4":
  [
    [t2s(0,27),t2s(0,35), "Clean"],
    [t2s(0,52),t2s(1,9), "Clean"],
    [t2s(1,18),t2s(1,35), "Clean"],
    [t2s(1,52),t2s(2,18), "Clean"],
    [t2s(2,37),t2s(2,47), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_7.MP4":
  [
    [t2s(0,19),t2s(0,23), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_8.MP4":
  [
    [t2s(1,9),t2s(1,16), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_9.MP4":
  [
    [t2s(0,21),t2s(0,22), "Slime"],
    [t2s(0,34),t2s(0,36), "Slime"],
    [t2s(0,51),t2s(0,56), "Slime"],
    [t2s(1,53),t2s(1,54), "Clean"],
    [t2s(2,5),t2s(2,7), "Clean"],
    [t2s(2,13),t2s(2,14), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_10.MP4":
  [
    [t2s(0,27),t2s(0,29), "Clean"],
    [t2s(0,38),t2s(0,39), "Clean"],
    [t2s(0,45),t2s(0,48), "Clean"],
    [t2s(0,57),t2s(0,58), "Clean"],
    [t2s(1,8),t2s(1,11), "Clean"],
    [t2s(1,16),t2s(1,20), "Clean"],
    [t2s(1,23),t2s(1,26), "Clean"],
    [t2s(1,45),t2s(1,50), "Clean"],
    [t2s(1,54),t2s(2,00), "Clean"],
    [t2s(2,38),t2s(2,40), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_11.MP4":
  [
    [t2s(0,13),t2s(0,18), "Clean"],
    [t2s(1,19),t2s(1,28), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_12.MP4":
  [
    [t2s(0,12),t2s(0,13), "Slime"],
    [t2s(0,17),t2s(0,27), "Slime"],
    [t2s(0,31),t2s(0,39), "Slime"],
    [t2s(0,53),t2s(0,57), "Slime"],
    [t2s(1,5),t2s(1,6), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_13.MP4":
  [
    [t2s(0,12),t2s(0,15), "Clean"],
    [t2s(0,30),t2s(0,32), "Phytoplankton"],
    [t2s(0,55),t2s(1,2), "Clean"],
    [t2s(1,38),t2s(1,42), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_2/T2_15.MP4":
  [
    [t2s(1,2),t2s(1,3), "Phytoplankton"],
    [t2s(1,23),t2s(1,24), "Phytoplankton"],
    [t2s(1,39),t2s(1,40), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_1.MP4":
  [
    [t2s(0,24),t2s(0,44), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_2.MP4":
  [
    [t2s(0,34),t2s(1,8), "Clean"],
    [t2s(1,11),t2s(1,14), "Clean"],
    [t2s(1,33),t2s(1,38), "Clean"],
    [t2s(1,57),t2s(2,12), "Clean"],
    [t2s(2,26),t2s(2,43), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_3.MP4":
  [
    [t2s(0,22),t2s(0,35), "Clean"],
    [t2s(0,50),t2s(1,1), "Clean"],
    [t2s(1,27),t2s(1,32), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_4.MP4":
  [
    [t2s(0,15),t2s(0,18), "Slime"],
    [t2s(0,20),t2s(0,27), "Clean"],
    [t2s(0,33),t2s(0,56), "Clean"],
    [t2s(2,31),t2s(3,5), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_5.MP4":
  [
    [t2s(0,47),t2s(0,51), "Slime"],
    [t2s(0,52),t2s(1,17), "Clean"],
    [t2s(1,19),t2s(1,20), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_6.MP4":
  [
    [t2s(0,40),t2s(0,51), "Clean"],
    [t2s(0,57),t2s(1,8), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_7.MP4":
  [
    [t2s(0,24),t2s(0,51), "Clean"],
    [t2s(0,54),t2s(1,3), "Clean"],
    [t2s(1,11),t2s(1,20), "Clean"],
    [t2s(1,40),t2s(1,50), "Clean"],
    [t2s(2,5),t2s(2,15), "Clean"],
    
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_8.MP4":
  [
    [t2s(0,26),t2s(0,43), "Clean"],
    [t2s(0,49),t2s(1,0), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_9.MP4":
  [
    [t2s(0,33),t2s(0,45), "Clean"],
    [t2s(2,20),t2s(2,36), "Clean"],
    [t2s(2,40),t2s(2,58), "Clean"],
    [t2s(3,13),t2s(3,26), "Clean"],
    [t2s(3,32),t2s(3,38), "Slime"],
    [t2s(3,42),t2s(3,45), "Clean"],
    [t2s(3,47),t2s(3,49), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_10.MP4":
  [
    [t2s(0,11),t2s(0,42), "Slime"], 
    [t2s(0,49),t2s(0,56), "Slime"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_11.MP4":
  [
    [t2s(0,12),t2s(0,26), "Zooplankton"], 
    [t2s(0,38),t2s(0,45), "Zooplankton"], 
    [t2s(0,56),t2s(0,58), "Phytoplankton"], 
    [t2s(1,0),t2s(1,10), "Zooplankton"], 
    [t2s(1,19),t2s(1,30), "Zooplankton"], 
    [t2s(1,31),t2s(1,34), "Phytoplankton"],
    [t2s(1,39),t2s(1,42), "Zooplankton"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_12.MP4":
  [
    [t2s(0,20),t2s(0,21), "Phytoplankton"], 
    [t2s(0,28),t2s(0,35), "Slime"], 
    [t2s(0,39),t2s(0,41), "Phytoplankton"], 
    [t2s(0,45),t2s(0,50), "Phytoplankton"], 
    [t2s(0,52),t2s(0,54), "Slime"], 
    [t2s(0,57),t2s(0,58), "Clean"], 
    [t2s(1,20),t2s(1,30), "Clean"], 
    [t2s(1,39),t2s(1,40), "Phytoplankton"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_13.MP4":
  [
    [t2s(0,30),t2s(0,36), "Clean"], 
    [t2s(0,38),t2s(0,39), "Slime"], 
    [t2s(0,49),t2s(0,52), "Clean"], 
    [t2s(0,54),t2s(1,6), "Slime"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_14.MP4":
  [
    [t2s(0,24),t2s(0,29), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_15.MP4":
  [
    [t2s(0,25),t2s(0,30), "Zooplankton"],
    [t2s(0,34),t2s(0,35), "Zooplankton"],
    [t2s(0,36),t2s(0,39), "Slime"],
    [t2s(0,40),t2s(0,50), "Zooplankton"],
    [t2s(0,55),t2s(0,56), "Zooplankton"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_16.MP4":
  [
    [t2s(0,39),t2s(0,40), "Zooplankton"], 
    [t2s(0,41),t2s(0,42), "Slime"], 
    [t2s(0,43),t2s(0,48), "Zooplankton"], 
    [t2s(0,52),t2s(1,2), "Zooplankton"], 
    [t2s(1,7),t2s(1,13), "Phytoplankton"], 
    [t2s(1,14),t2s(1,19), "Slime"], 
    [t2s(1,24),t2s(1,25), "Slime"],
    [t2s(1,26),t2s(1,33), "Zooplankton"],
    [t2s(1,39),t2s(1,45), "Phytoplankton"],
    [t2s(1,47),t2s(1,51), "Zooplankton"],
    [t2s(1,52),t2s(1,55), "Slime"],
    [t2s(1,56),t2s(2,10), "Zooplankton"],
    [t2s(2,17),t2s(2,19), "Slime"],
    [t2s(2,28),t2s(2,32), "Slime"],
    [t2s(2,46),t2s(2,55), "Phytoplankton"],
    [t2s(3,3),t2s(3,6), "Zooplankton"],
    [t2s(3,7),t2s(3,23), "Slime"],
    [t2s(3,26),t2s(3,31), "Zooplankton"],
    [t2s(4,16),t2s(4,17), "Zooplankton"],
    [t2s(4,36),t2s(4,40), "Zooplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_17.MP4":
  [
    [t2s(1,8),t2s(1,12), "Zooplankton"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_18.MP4":
  [
    [t2s(0,17),t2s(0,30), "Clean"], 
    [t2s(0,32),t2s(0,43), "Clean"], 
    [t2s(0,49),t2s(0,56), "Clean"], 
    [t2s(0,58),t2s(1,1), "Slime"], 
    [t2s(1,6),t2s(1,13), "Slime"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_19.MP4":
  [
    [t2s(0,23),t2s(1,7), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_20.MP4":
  [
    [t2s(0,12),t2s(0,14), "Phytoplankton"],
    [t2s(0,15),t2s(0,22), "Clean"],
    [t2s(0,36),t2s(0,38), "Phytoplankton"],
    [t2s(0,49),t2s(0,52), "Phytoplankton"],
    [t2s(0,53),t2s(1,2), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_21.MP4":
  [
    [t2s(0,10),t2s(0,22), "Clean"],
    [t2s(0,28),t2s(0,40), "Clean"],
    [t2s(0,47),t2s(0,50), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_22.MP4":
  [
    [t2s(0,11),t2s(0,41), "Zooplankton"], 
    [t2s(0,43),t2s(1,8), "Zooplankton"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_24.MP4":
  [
    [t2s(0,30),t2s(1,0), "Clean"],
    [t2s(1,24),t2s(1,35), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_25.MP4":
  [
    [t2s(1,28),t2s(1,35), "Clean"],
    [t2s(2,8),t2s(2,22), "Clean"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_26.MP4":
  [
    [t2s(0,19),t2s(0,25), "Clean"],
    [t2s(0,26),t2s(2,40), "Slime"],
    [t2s(0,54),t2s(1,2), "Slime"],
    [t2s(1,14),t2s(1,18), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_28.MP4":
  [
    [t2s(0,16),t2s(0,54), "Clean"], 
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_29.MP4":
  [
    [t2s(0,16),t2s(0,28), "Clean"], 
    [t2s(0,56),t2s(1,1), "Clean"], 
    [t2s(1,4),t2s(1,7), "Phytoplankton"], 
  ]
   ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_30.MP4":
  [
    [t2s(0,10),t2s(0,14), "Phytoplankton"],
    [t2s(0,36),t2s(0,38), "Phytoplankton"],
    [t2s(0,46),t2s(0,47), "Slime"],
    [t2s(0,48),t2s(0,49), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_31.MP4":
  [
    [t2s(0,9),t2s(0,26), "Slime"],
    [t2s(0,32),t2s(0,34), "Phytoplankton"],
    [t2s(0,44),t2s(0,45), "Slime"],
    [t2s(0,53),t2s(0,55), "Phytoplankton"],
    [t2s(1,16),t2s(1,22), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_32.MP4":
  [
    [t2s(0,26),t2s(0,33), "Clean"],
    [t2s(0,37),t2s(0,40), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/Taarbaek_3/T3_33.MP4":
  [
    [t2s(0,18),t2s(0,25), "Phytoplankton"],
    [t2s(0,29),t2s(0,40), "Clean"],
    [t2s(0,41),t2s(0,43), "Phytoplankton"],
    [t2s(0,48),t2s(0,52), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_1.MP4":
  [
    [t2s(0,29),t2s(0,35), "Clean"]
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_2.MP4":
  [
    [t2s(0,28),t2s(0,33), "Clean"],
    [t2s(1,4),t2s(1,11), "Clean"],
    [t2s(1,18),t2s(1,36), "Clean"],
    [t2s(2,28),t2s(2,50), "Slime"],
    [t2s(3,28),t2s(3,53), "Slime"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_3.MP4":
  [
    [t2s(0,33),t2s(2,3), "Phytoplankton"],
    [t2s(2,31),t2s(2,41), "Zooplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_4.MP4":
  [
    [t2s(0,38),t2s(1,52), "Phytoplankton"]
    
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_5.MP4":
  [
    [t2s(0,35),t2s(2,22), "Phytoplankton"]
    
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_6.MP4":
  [
    [t2s(0,27),t2s(1,5), "Phytoplankton"],
    [t2s(1,8),t2s(1,25), "Zooplankton"],
    
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_7.MP4":
  [
    [t2s(0,20),t2s(0,45), "Phytoplankton"],
    [t2s(0,51),t2s(1,0), "Zooplankton"],
    
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_8.MP4":
  [
    [t2s(0,20),t2s(0,45), "Phytoplankton"],
    [t2s(0,51),t2s(1,0), "Zooplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_9.MP4":
  [
    [t2s(0,40),t2s(2,50), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_10.MP4":
  [
    [t2s(1,0),t2s(2,50), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_11.MP4":
  [
    [t2s(0,32),t2s(1,50), "Phytoplankton"],
  ]
  ,
  "/home/steven/workspace/greensteam/nas/steven/Special_Course/dfds_pearl_1/DFDS_PEARL_1_12.MP4":
  [
    [t2s(0,51),t2s(1,22), "Slime"],
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
