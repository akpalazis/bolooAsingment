# Boloo Assigment

This is the end of the assigment

to run:
create an .env file with:
  POSTGRES_USER=xxx
  POSTGRES_PASSWORD=xxxx
  DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5433/mydatabase

Run the DB with:
  docker-compose up --build

install the dependencies of the backend with:
  pip install -r requirements.txt
and run (make sure the db is already running):
  python app.py

install the dependencies of the frontend with:
  npm install in the frontend directory
and run with:
  npm start dev
