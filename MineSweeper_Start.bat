py gui_Intro.py
PAUSE

pytest
PAUSE

flake8 --exclude ./venv/ --max-line-length=150 --ignore=F405,E401,F403,E125,E501,E115,E501,E302
PAUSE