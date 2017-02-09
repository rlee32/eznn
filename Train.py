#!/usr/bin/env python



def split_data(data_original, training_fraction, test_fraction):
    """
    Splits data into a training, validation, and test sets.
    """
    validation_fraction = 1-training_fraction-test_fraction
    if validation_fraction < 0:
        total = training_fraction + test_fraction
        training_fraction /= total
        validation_fraction = 0
        test_fraction /= total

    # Deep copy
    data = data_original[:]
    random.shuffle(data)

    n_data = len(data)
    n_training = int(training_fraction*n_data)
    n_validation = int(validation_fraction*n_data)
    n_test = int(test_fraction*n_data)
    new_total = n_training + n_validation + n_test
    diff = n_data - new_total
    n_training += diff

    training_data = data[:n_training]
    validation_data = data[n_training:-n_test]
    test_data = data[-n_test:]

    return (training_data, validation_data, test_data)

def get_neural_network_data(vault_path):
    dat_files = get_all_dat_files(vault_path)
    all_instances = [ read_feature_vector(vault_path+"/"+x, 25) \
        for x in dat_files ]
    # Transform data
    feature_transform = read_scale_data("feature_scaling.dat")
    result_transform = read_scale_data("result_scaling.dat")
    transform_instances(all_instances, feature_transform, result_transform)
    (training_data_, validation_data_, test_data_) = \
        split_data(all_instances, 0.6, 0.2)
    training_data = [ numpy_instance(x) for x in training_data_ ]
    validation_data = [ numpy_instance(x) for x in validation_data_ ]
    test_data = [ numpy_instance(x) for x in test_data_ ]
    return (training_data, validation_data, test_data)


if __name__ == "__main__":
    # Tests.