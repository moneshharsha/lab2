def one_hot_encoding(categories):
    """
    Perform one-hot encoding on a list of categories.
    """
    unique_categories = sorted(set(categories))  # Sorting for consistent order
    encoded_mapping = {category: [int(category == unique) for unique in unique_categories] for category in categories}
    return encoded_mapping

if __name__ == "__main__":
    categorical_data = ['morning', 'evening', 'night']

    one_hot_encoded_mapping = one_hot_encoding(categorical_data)

    print("Original Categorical Data:", categorical_data)
    print("One-Hot Encoded Mapping:")
    for category, encoding in one_hot_encoded_mapping.items():
        print(f"{category}: {encoding}")
