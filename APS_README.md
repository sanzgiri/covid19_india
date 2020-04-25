## Instructions

* App requires t2.medium or higher AWS instance to run

* Create python 3.6 conda environment

* Install following packages
```
pip install pandas numpy scipy
pip install apscheduler flask flask-cors convertdate
pip install requests
pip install plotly
pip install fbprophet
```

* Prepare data, run model, run api service
python covid19_scheduler.py
python covid19_endpoint.py

* Install oracle ojet
```
npm install -g @oracle/ojet-cli
ojet restore
ojet serve
```