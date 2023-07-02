import os
from datetime import datetime

from python_on_whales import docker

# define test results directory based on current time
test_result_path = "./test_results/"
now = datetime.now()
folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
full_path = os.path.join(test_result_path, folder_name)
os.makedirs(full_path, exist_ok=True)
# push in environnement variable
os.environ["TEST_RESULT_PATH"] = full_path
os.environ['API_URL'] = 'http://api'
os.environ['API_PORT'] = '8000'


# run docker-compose with python library
docker.compose.up(detach=True, build=True)
