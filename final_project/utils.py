def count_outliers(df, threshold=1.5):
    """
    Count outliers in a DataFrame using the IQR method.

    Parameters:
    - df: DataFrame
        The input DataFrame.
    - threshold: float, optional (default=1.5)
        Multiplier for the IQR. Data points beyond this threshold are considered outliers.

    Returns:
    - outlier_counts: dict
        Dictionary containing counts of outliers for each column.
    """
    outlier_counts = {}

    # Loop through each column in the DataFrame
    for column in df.columns:
        # Calculate the first and third quartiles
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        # Calculate the IQR (Interquartile Range)
        IQR = Q3 - Q1

        # Define the lower and upper bounds for outliers
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        # Count the outliers in the current column
        column_outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column].count()
        
        # Store the count in the dictionary
        outlier_counts[column] = column_outliers

    return outlier_counts

