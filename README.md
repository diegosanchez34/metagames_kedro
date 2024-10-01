# MetaGames Kedro Project

## Overview

This is a Kedro project designed to handle a machine learning case related to the **MetaGames** platform. The main goal is to automate the process of preparing data and training models to improve video game recommendations for users.

## Project Structure

The project includes:

- **Jupyter Notebooks:** Documents containing detailed analysis, visualizations, and explanations of each phase of the process.
- **Process Automation:** Setting up pipelines for data handling and model training.
- **Documentation:** README files and other instructions to facilitate understanding and using the project.

## Setup Instructions

To run this project, follow these steps:

1. **Activate the virtual environment:**

```bash
venv\Scripts\activate
```

2. **Install all necessary dependencies:**

```bash
pip install -r requirements.txt
```

3. **Open the "Technical Report - MetaGames" notebook:**
   Navigate to `kedro-project/notebooks` to access the technical report.

4. **Deactivate the virtual environment when you are done:**

```bash
deactivate
```

## How to Run the Kedro Pipeline

To run your Kedro project, use the following command:

```bash
kedro run
```

This will run all the stages defined in the pipeline.

## How to Test Your Kedro Project

Review the files `src/tests/test_run.py` and `src/tests/pipelines/data_science/test_pipeline.py` for instructions on how to write and run tests. To run the tests, use:

```bash
pytest
```

## Documentation and Resources

For more information on how to use Kedro and work with notebooks, see the [official Kedro documentation](https://docs.kedro.org).

### Notebooks and Kedro

To work with notebooks in your Kedro project, make sure Jupyter is installed:

```bash
pip install jupyter
```

After installation, you can start a local Jupyter server:

```bash
kedro jupyter notebook
```

### Ignoring Notebook Outputs in Git

To automatically remove the contents of output cells before committing to Git, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, add a hook in `.git/config` with:

```bash
nbstripout --install
```

This will be run before any commit.
