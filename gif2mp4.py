# conda activate lightninh
import moviepy.editor as mp

clip = mp.VideoFileClip(
    r"C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20.gif"
)
clip.write_videofile(
    r"C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20.mp4"
)

clip.close()

# mp4を 横幅320に合わせた 10fpsのgifに変換
# https://qiita.com/wMETAw/items/fdb754022aec1da88e6e
#!ffmpeg -i "C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20.mp4" -vf scale=320:-1 -r 10 "C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20_conv.gif"
#!ffmpeg -i "C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20.mp4" -vf scale=1033:-1 -r 10 "C:\Users\81908\Pictures\lightweight-gan\mydog_like_img_256\68000step\generated-03-01-2021_12-42-20_conv2.gif"
