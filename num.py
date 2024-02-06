def get_categorical_input(prompt):
    """
    Get categorical data input from the user.
    """
    return input(prompt).split(',')

def label_encode_categorical(data):
    """
    Encode categorical data into numeric labels.
    """
    label_mapping = {value: index for index, value in enumerate(set(data))}
    numeric_labels = [label_mapping[value] for value in data]

    return numeric_labels, label_mapping

def main():
    categorical_data = get_categorical_input("Enter categorical data (comma-separated values): ")

    numeric_labels, label_mapping = label_encode_categorical(categorical_data)
    
    print("Numeric Labels:", numeric_labels)
    print("Label Mapping:", label_mapping)

if __name__ == "__main__":
    main()
