# --- ペイントプロセスの作成 ---
from inference import run_inference
import os 
import shutil

# 画像指定
input_img = 'yui.jpg'
 
# outputフォルダーリセット
if os.path.isdir('output'):
    shutil.rmtree('output')
 
# name取得
name = input_img[:-4]
 
# プロセス作成
run_inference(input_path='input/'+input_img,
              model_path='model.pth',
              output_dir='output/', # whether need intermediate results for animation.
              need_animation=True,  # resize original input to this size. None means do not resize.
              resize_h=None,        # resize original input to this size. None means do not resize.
              resize_w=None,
              serial=True)          # if need animation, serial must be True.