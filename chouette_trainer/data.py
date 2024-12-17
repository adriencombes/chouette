### BUILD-IN IMPORTS ###

import glob
import os
import shutil


### EXTERNAL IMPORTS ###

import requests
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator


### SETTINGS ###

USERNAME = os.environ.get('CHOUETTE_USERNAME')
PASSWORD = os.environ.get('CHOUETTE_PASSWORD')


### FUNCTIONS ###

def download_train_data(start_date, end_date):

    def download_images(start_date, end_date, tag):

        os.makedirs(f'data/train/{tag}', exist_ok=True)

        params = {
            'start_date': start_date,
            'end_date': end_date,
            'tag': tag
            }

        response = requests.get(
            'https://api.staging.chouette.vision/api/jobs/get-images/',
            auth=(USERNAME, PASSWORD),
            params=params
            )

        url_list = [image['media'] for image in response.json()]
        # attention parfois cette liste est vide (pas de clef 'media')

        for url in url_list:
            image = requests.get(url)
            file_name = f'{url.split("/")[-1].split(".jpg")[0]}' + '.jpg'

            with open(f'data/train/{tag}/{file_name}', 'wb') as file:
                file.write(image.content)
            print(f'{file_name} downloaded')

    for tag in ['vine','grass','ground']:
        download_images(start_date, end_date, tag)


def open_train_data():

    # TODO y'a moyen de factoriser

    # TODO reactiver ça
    # data.clear_cache()
    # download_train_data('2020-01-01', '2021-01-01')

    data_dir = 'data/train'

    seed = 123
    validation_split = 0.3
    img_height = 128
    img_width = 128
    batch_size = 128

    train_dataset = image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        labels='inferred',
        label_mode='categorical',
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    validation_dataset = image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        labels='inferred',
        label_mode='categorical',
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    return train_dataset, validation_dataset

def open_test_data(test_data=False):

    data_dir = 'data/test'

    img_height = 128
    img_width = 128

    test_dataset = image_dataset_from_directory(
        data_dir,
        labels='inferred',
        label_mode='categorical',
        image_size=(img_height, img_width),
    )

    return test_dataset


def clear_cache():

    for directory in glob.glob('data/train/*'):
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f'{directory} removed')
