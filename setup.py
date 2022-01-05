import gdown
import os

gdown.download("https://drive.google.com/u/0/uc?id=1NDD54BLligyr8tzo8QGI5eihZisXK1nq&export=download", './model.pth', quiet=False)
os.makedirs("input")
os.makedirs("output")