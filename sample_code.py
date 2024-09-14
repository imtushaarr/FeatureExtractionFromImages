import os
import random
import pandas as pd


def predictor(image_link, category_id, entity_name):
    '''
    Call your model/approach here
    '''
    # TODO: Replace with actual prediction logic
    return "" if random.random() > 0.5 else "10 inch"


if __name__ == "__main__":
    DATASET_FOLDER = '/Users/tushargupta/Documents/PyCharm/model/dataset'

    # Define file paths
    test_file = os.path.join(DATASET_FOLDER, 'test.csv')
    output_file = os.path.join(DATASET_FOLDER, 'test_out.csv')

    try:
        # Load test data
        test = pd.read_csv(test_file)

        # Validate necessary columns
        required_columns = ['image_link', 'group_id', 'entity_name']
        if not all(col in test.columns for col in required_columns):
            raise ValueError(f"Test CSV file must contain the columns: {required_columns}")

        # Apply predictor function
        test['prediction'] = test.apply(
            lambda row: predictor(row['image_link'], row['group_id'], row['entity_name']), axis=1)

        # Save predictions to CSV
        test[['index', 'prediction']].to_csv(output_file, index=False)
        print(f"Predictions saved to {output_file}")

    except FileNotFoundError:
        print(f"File not found: {test_file}")
    except pd.errors.EmptyDataError:
        print(f"File is empty: {test_file}")
    except pd.errors.ParserError:
        print(f"Error parsing the CSV file: {test_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
