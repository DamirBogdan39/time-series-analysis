import torch

# Path to padded data 
PADDED_PATH = "./padded_lc"

# Path to save preprocesses data
PREPROC_PATH = "./preproc"

# Defining the paths to train, val and test directories

TRAIN_DIR = "./dataset/train/"
VAL_DIR = "./dataset/val/"
TEST_DIR = "./dataset/test/"

# Defining the paths to the directories

TRAIN_DIR_PATH = "./dataset/train"
VAL_DIR_PATH = "./dataset/val"
TEST_DIR_PATH = "./dataset/test"

# Defining the path to the model
MODEL_PATH = "./output/cnp_model.pth"

# Defining batch size 

BATCH_SIZE = 32

# Defining device

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define output path

OUTPUT_PATH = './output/predictions'