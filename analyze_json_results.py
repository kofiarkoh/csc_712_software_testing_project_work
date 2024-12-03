import json
import os


def extract_json_data(folder_path):
    class_level_params = []
    method_level_params = {}
    num_tests = 0  # number of tests is same as num of files
    num_tests_using_configs = 0

    # Walk through all directories and subdirectories
    for root, _, files in os.walk(folder_path):
        for filename in files:
            # Check for JSON files
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                num_tests += 1
                with open(file_path, 'r') as f:
                    data = json.load(f)

                    # Extract classLevelParams
                    class_level_params.extend(data.get("classLevelParams", []))

                    test_class_uses_configs = bool(data.get("testClassUsesConfigs", []))
                    test_function_uses_configs = False
                    # Extract methodLevelParams and its values
                    for method, params in data.get("methodLevelParams", {}).items():
                        if len(params) > 0:
                            test_function_uses_configs = True
                        if method not in method_level_params:
                            method_level_params[method] = []
                        # Extend the list with values from the current method's parameters
                        method_level_params[method].extend(params)

                    if test_class_uses_configs or test_function_uses_configs:
                        num_tests_using_configs += 1

    return class_level_params, method_level_params, num_tests, num_tests_using_configs


# List of JSON files to read
folder_path = "./flink"  # replace with actual file paths

class_level_params, method_level_params, num_tests, num_tests_using_configs = extract_json_data(folder_path)

configs = []
tests = []
num_tests_with_configs_f = 0  # stores the number of test functions that uses config values
for method, params in method_level_params.items():
    if len(params) > 0:
        num_tests_with_configs_f += 1
    tests.append(method)
    configs.extend(params)

configs = list(set(configs))
tests = list(set(tests))
print("----- APACH FLINK -----")
print(f"Number of Configurations :{len(configs)} ")
print(f"Number of Tests Files Executed :{num_tests}")
print(f"Number of Tests Files Using Configurations {num_tests_using_configs}")
