@ECHO OFF
python setup.py install
py -m pip --upgrade pip
pip install -e . --upgrade --no-cache-dir --progress-bar off
