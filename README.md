
# Table of Contents

1.  [Build](#orgf35bce2)
2.  [Launch](#orgc7f8ccd)
3.  [Query](#org1bd2237)
    1.  [`curl`](#org643c71a)
    2.  [Docs](#org7b9aee8)



<a id="orgf35bce2"></a>

# Build

    docker build -t app


<a id="orgc7f8ccd"></a>

# Launch

\#+BEGIN<sub>SRC</sub> bash
docker run -p 8000:8000 app
\#+END<sub>SRC</sub> bash


<a id="org1bd2237"></a>

# Query


<a id="org643c71a"></a>

## `curl`

\#+BEGIN<sub>SRC</sub> bash
curl -X POST <http://localhost:8000/yob> \\
     -H "Content-Type: application/json" \\
     -d '{"age": 40}'
\#+END<sub>SRC</sub> bash


<a id="org7b9aee8"></a>

## Docs

`http://localhost:8000/docs`

