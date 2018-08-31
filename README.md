# Quantum Computer Environment

This repo contains the environment to run quantum algorithms. You can
run your algorithm simulated or connect to a real quantum chip
on [IBM Q Experience](https://quantumexperience.ng.bluemix.net/qx/).

# Check the full explanation video (GR)
[![Quantum Computers](https://img.youtube.com/vi/rroK2JugvUE/0.jpg)](https://www.youtube.com/watch?v=rroK2JugvUE)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

# Run

Run in root folder,
~~~~
docker-compose build && docker-compose up -d
~~~~

Login to the container,
~~~~
docker exec -it qc /bin/bash -c "TERM=$TERM exec bash"
~~~~

Run
~~~~
python main.py
~~~~

You will see something like
~~~~
Local backends:  ['local_qasm_simulator', 'local_statevector_simulator', 'local_unitary_simulator']
simulation:  COMPLETED
{'00': 512, '11': 512}
~~~~

To stop it
~~~~
exit
docker-compose down
~~~~
# Maintainer
[Thanos Nokas](https://www.linkedin.com/in/thanosnokas)