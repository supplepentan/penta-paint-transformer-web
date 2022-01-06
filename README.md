# Setting
```
git clone https://github.com/supplepentan/penta-paint-transformer.git
cd penta-paint-transformer
pyenv local 3.8.6
python -m venv venv
venv/scripts/activate
python -m pip install -U pip setuptools
python -m pip install -r requirements.txt
python -m pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
python setup.py
```
# Try
## Launch the local-server, and acces to localhost
```
uvicorn main:app --reload
access to "httpl//localhost8080"
```
# Deveropment
## Backend
FastAPI
## Forntend
Vue.js3: Type of Typescript and yarn.

# Original
https://arxiv.org/abs/2108.03798