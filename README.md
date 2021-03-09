# FastAPI

This repository is the example I've been using for my quick talk at [Clermont'ech API Hour #47](https://www.clermontech.org/api-hours/api-hour-47.html).
Slides are available at: https://docs.google.com/presentation/d/1DtpLMC59WfuuPMpW9ZvoU50SEd8i_D5jOyZILfuze_s/edit?usp=sharing

This repository can be used as an example to bootstrap your FastAPI project. It uses a SQLite database and a full dump is available (in the `dump.sql` file).

# Install

### Create a virtual environment

```bash
$ python3 -m venv .venv
```

###  Source your virtual environment

```bash
$ source .venv/bin/activate
```

### Install the dependencies

```bash
$ pip install -r requirements.txt
```

### Import the DB

```bash
$ ./import.sh
```

### Launching the app 🚀

```bash
$ uvicorn app.main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [76014] using statreload
INFO:     Started server process [76016]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Enjoy!

URLs to access endpoints are available at:
- Swagger URL : http://127.0.0.1:8000/docs
- Redoc : http://127.0.0.1:8000/redoc

# Licence

No specific license for this project, feel free to fork it and start developing using this (great!) framework. Happy coding!