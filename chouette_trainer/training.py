import data, model

if __name__ == '__main__':

    resnet_version = '50'
    epochs = 30

    train_dataset, validation_dataset = data.open_train_data()
    num_classes = len(train_dataset.class_names)

    resnet_model = model.make_model(resnet_version, num_classes)
    resnet_model = model.train_model(resnet_model, train_dataset, validation_dataset, epochs)

    params = {
        'resnet_version': resnet_version,
        'epochs': epochs
    }
    model.save_model(resnet_model, params)

    test_dataset = data.open_test_data()
    model.evaluate_model(test_dataset)
