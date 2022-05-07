#!/usr/bin/bash
ffmpeg -i output.mp4 -vcodec libx265 -crf 28 output_comp.mp4