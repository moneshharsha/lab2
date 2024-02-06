def get_vector_input(prompt):
    """
    Get vector input from the user.
    """
    return [int(x) for x in input(prompt).split(',')]

def calculate_distance(vector1, vector2, distance_type='euclidean'):
    """
    Calculate the Euclidean or Manhattan distance between two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensionality")

    if distance_type == 'euclidean':
        return sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)) ** 0.5
    elif distance_type == 'manhattan':
        return sum(abs(v1 - v2) for v1, v2 in zip(vector1, vector2))
    else:
        raise ValueError("Invalid distance type. Choose 'euclidean' or 'manhattan'.")

def main():
    vector_a = get_vector_input("Enter vector A values separated by commas: ")
    vector_b = get_vector_input("Enter vector B values separated by commas: ")

    for distance_type in ['euclidean', 'manhattan']:
        result = calculate_distance(vector_a, vector_b, distance_type)
        print(f"{distance_type.capitalize()} Distance: {result}")

if __name__ == "__main__":
    main()
