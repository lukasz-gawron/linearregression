
#!/bin/bash

docker build \
  -f ./Dockerfile \
  -t tensorworks:latest \
  .

  # -v $(pwd)/srccantera1:/root/sources \
  #   -p 8888:8888 \
  # --add-host storage.local:127.0.0.1 \

docker run -it \
  -v $(pwd)/src15:/root/sources \
  -p 6006:6006 \
  tensorworks:latest bash

