
./environment.sh
gunicorn -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8080 app.main:app