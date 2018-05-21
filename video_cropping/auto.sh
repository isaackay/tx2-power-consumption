ffmpeg -i elephant.webm -filter:v "crop=1224:1224:0:0" -strict -2 cropped/elephant.mp4 &
ffmpeg -i rhino.webm -filter:v "crop=1224:1224:0:0" -strict -2 cropped/rhino.mp4 &
ffmpeg -i diving.mkv -filter:v "crop=1224:1224:0:0" -strict -2 cropped/diving.mp4 &
ffmpeg -i paris.mkv -filter:v "crop=1224:1224:0:0" -strict -2 cropped/paris.mp4 &
wait
ffmpeg -i venice.mkv -filter:v "crop=1224:1224:0:0" -strict -2 cropped/venice.mp4 &
ffmpeg -i rollercoaster.mkv -filter:v "crop=1224:1224:0:0" -strict -2 cropped/rollercoaster.mp4 &
ffmpeg -i nyc.mkv -filter:v "crop=1224:1224:0:0" -strict -2 cropped/nyc.mp4 &
