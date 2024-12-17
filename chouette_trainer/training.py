import data, model

if __name__ == '__main__':

    resnet_version = '50'
    epochs = 25

    train_dataset, validation_dataset = data.open_data(test_data=False)
    num_classes = len(train_dataset.class_names)

    resnet_model = model.make_model(resnet_version, num_classes)
    model.train_model(resnet_model, train_dataset, validation_dataset, epochs)

# save model and params
# model.save_model(model, params)

# delete train data
# data.clear_cache()

# load test data
# data.open_data(test_data=True)
# process test data

# evaluate model
