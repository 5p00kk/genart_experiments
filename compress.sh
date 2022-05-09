#!/usr/bin/bash
ffmpeg -i video.mp4 -vcodec libx265 -crf 28 video_comp.mp4
