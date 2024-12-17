### BUILT-IN IMPORTS ###

import os


#### EXTERNAL IMPORTS ###

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


### SETTINGS ###

DEBUG = bool(os.environ.get('DEBUG', False))


### FUNCTIONS ###

def make_model(resnet_version, num_classes):

    base_model = ResNet50(
        include_top=False,
        weights='imagenet',
        input_tensor=None,
        input_shape=None,
        pooling=None,
        classes=num_classes,
        classifier_activation='softmax'
    )

    base_model.trainable = False

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(1024, activation='relu'),
        Dense(num_classes, activation='softmax')])

    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    if DEBUG:
        print(model.summary())

    return model


def train_model(model, train_dataset, val_dataset, epochs):

    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True,
        verbose=True
    )

    history = model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=epochs,
        callbacks=[early_stopping]
    )

    pass


def save_model(model, params):

    # save model

    pass


def evaluate_model(model, dataset):

    # evaluate model
    # return evaluation

    pass
