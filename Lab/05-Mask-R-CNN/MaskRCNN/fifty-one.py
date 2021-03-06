# !pip install fiftyone

import fiftyone as fo
import fiftyone.zoo as foz

# List available zoo datasets
print(foz.list_zoo_datasets())

#
# Load the COCO-2017 validation split into a FiftyOne dataset
#
# This will download the dataset from the web, if necessary
#
dataset_name = "coco-2017"
# dataset_name = "cityscapes"
dataset = foz.load_zoo_dataset(dataset_name)

# Give the dataset a new name, and make it persistent so that you can
# work with it in future sessions
dataset.name = dataset_name
dataset.persistent = True

# Visualize the in the App
session = fo.launch_app(dataset)