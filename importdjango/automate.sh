#!/bin/bash

# run media.py in ../cmi
sudo python3 ../cmi/media.py
# run tests
python3 manage.py shell < web_app/test.py 
python3 manage.py shell < web_app/import_csv.py
python3 manage.py shell < web_app/rotate.py

# run the server
python3 manage.py runserver