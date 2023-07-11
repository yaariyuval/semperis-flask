This repository contains the code for the Python/Flask Codility task which Codility didn't seem to accept.

There are PyTest tests that test the scenarios described in the task.

Additionally, there is a [multi-stage](https://docs.docker.com/build/guide/multi-stage/) Dockerfile that creates a container that runs the tests, or runs the Flask server.

The Docker container uses Python 3.8.5 and Flask 2.1.2 as specified in the Codility task.

Please note that I mocked the save() function, since the described Codility save() function wasn't standard.


Run the tests without using Docker
=======
```
$ pip3 install pytest flask=='2.1.2'
$ python3 -m pytest -v
```

Run the tests as a Docker container (uses pytest)
========
```
$ docker build -t semperis --target test .
$ docker run semperis
```

Run the Flask server as a Docker container
========
```
$ docker build -t semperis --target production .
$ docker run -p 5000:5000 semperis
```

Test using curl
========
Works with both the containerized and non-containerized versions.

```
curl -XPOST http://127.0.0.1:5000/users -H 'Content-Type: application/json' -d '{"name":"My Name","age":38}'
```
