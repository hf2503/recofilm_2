import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
from utils.utils import make_directory




SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
DOCKER_VOLUME = os.path.join(ROOT_DIR, "docker_volume")
make_directory(DOCKER_VOLUME)
model_folder = os.path.join(DOCKER_VOLUME, "model_folder")
make_directory(model_folder)
data_folder = os.path.join(DOCKER_VOLUME, "data")
make_directory(data_folder)
input_data_folder = os.path.join(DOCKER_VOLUME, "inputs")
output_folder = os.path.join(DOCKER_VOLUME, "outputs")
make_directory(output_folder)
unittest_folder = os.path.join(DOCKER_VOLUME, "unittest")
make_directory(unittest_folder)
movie_model_unittest_folder = os.path.join(unittest_folder, "kpi_movie_model")
make_directory(movie_model_unittest_folder)
user_model_unittest_folder = os.path.join(unittest_folder, "kpi_user_model")

#creation du dossier data_unittest_folder
data_unittest_folder = os.path.join(unittest_folder, "test_data")
make_directory(data_unittest_folder)
