ffmpeg -i elephant.webm -filter:v "crop=1920:1080:0:0" -strict -2 1080p/elephant.mp4 &
ffmpeg -i rhino.webm -filter:v "crop=1920:1080:0:0" -strict -2 1080p/rhino.mp4 &
ffmpeg -i diving.mkv -filter:v "crop=1920:1080:0:0" -strict -2 1080p/diving.mp4 &
ffmpeg -i paris.mkv -filter:v "crop=1920:1080:0:0" -strict -2 1080p/paris.mp4 &
wait
ffmpeg -i venice.mkv -filter:v "crop=1920:1080:0:0" -strict -2 1080p/venice.mp4 &
ffmpeg -i rollercoaster.mkv -filter:v "crop=1920:1080:0:0" -strict -2 1080p/rollercoaster.mp4 &
ffmpeg -i nyc.mkv -filter:v "crop=1920:1080:0:0" -strict -2 1080p/nyc.mp4 &
