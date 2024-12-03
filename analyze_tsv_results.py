import pandas as pd
import os


def generate_test_summary(project_name):
    all_data = pd.DataFrame()

    for filename in os.listdir(f"./results/{project_name}"):

        if filename.startswith('test_result_') and filename.endswith('.tsv'):
            full_filepath = f'./results/{project_name}/{filename}'
            df = pd.read_csv(
                full_filepath,
                sep='\t', usecols=[0, 1, 2, 3, 4],
                names=['conf_file', 'conf_test', 'a', 'status', 'b'],
                header=None
            )

            # Append the data to all_data DataFrame
            all_data = pd.concat([all_data, df], ignore_index=True)
    num_of_configs = all_data['conf_file'].value_counts().shape[0]
    num_of_tests = all_data['conf_test'].value_counts().shape[0]
    return {
        "num_of_configs": num_of_configs,
        "num_of_tests": num_of_tests
    }

alluxio_results = generate_test_summary("alluxio-core")
print(f"alluxio results")
print(alluxio_results)