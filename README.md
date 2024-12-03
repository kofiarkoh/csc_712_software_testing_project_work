### ABOUT
This is a project to replicate the result of the openctest paper and apply the tool to run tests of the projects...
Paper: [Testing Configuration Changes in Context to Prevent Production Failures](https://www.usenix.org/conference/osdi20/presentation/sun)

### Requirements
- install the requirements by running `pip install requirements.txt`
### USAGE
- There are two jupyter notebooks. We used `analyze_json_results` to analyzed json logs from [ctest4j](https://github.com/xlab-uiuc/ctest4j) while `analyze_tsv_results` 
was used to analyze the results from the initial version of [openctest](https://github.com/xlab-uiuc/openctest). Both of them have the same under core implementation.