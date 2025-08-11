#+TITLE: Template for Dockerized FastAPI

* Build
#+BEGIN_SRC bash
docker build -t app
#+END_SRC 
* Launch
#+BEGIN_SRC bash
docker run -p 8000:8000 app
#+END_SRC bash
* Query
** =curl=
#+BEGIN_SRC bash
curl -X POST http://localhost:8000/yob \
     -H "Content-Type: application/json" \
     -d '{"age": 40}'
#+END_SRC bash
** Docs
=http://localhost:8000/docs=
