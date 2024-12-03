### ABOUT
This is a project to replicate the result of the openctest paper and apply the tool to run tests of the projects...
Paper: [Testing Configuration Changes in Context to Prevent Production Failures](https://www.usenix.org/conference/osdi20/presentation/sun)

### Requirements
- install the requirements by running `pip install requirements.txt`
### USAGE
- Clone the repository by running `git clone git@github.com:kofiarkoh/csc_712_software_testing_project_work.git`
- There are two python files. We used `analyze_json_results.py` to analyzed json logs from [ctest4j](https://github.com/xlab-uiuc/ctest4j) while `analyze_tsv_results.py` 
was used to analyze the results from the initial version of [openctest](https://github.com/xlab-uiuc/openctest). Both of them have the same under core implementation.
- To analyze the results, run `python analyze_json_results.py`.
- To analyze the tsv results, run `python analyze_json_results.py`