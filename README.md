#To Start application:

Press Run 
Press Box URL

#Requirements:

source .venv/bin/activate
pip install --upgrade pip
pip install flask

#To parse the database in the event of adding more countries:

python3 parse_csv.py

#To run the application:

export FLASK_ENV=development
export FLASK_APP=app.py
python3 -m flask run -h 0.0.0.0

#GitHub link
https://github.com/RPaivaniemi/assessment3/tree/main

#Render link
https://assessment3.onrender.com