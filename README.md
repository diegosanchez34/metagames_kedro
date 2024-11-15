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

1. **Create and activate the virtual environment:**

   If you haven't created a virtual environment yet, you can do so by running the following command in your terminal (make sure you're in the project root directory):

   ```bash
   python -m venv venv
   ```

   Then, activate the virtual environment:

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

2. **Install all necessary dependencies:**

   With the virtual environment activated, install the dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to the project folder:**

   Before running the Kedro pipeline, make sure you're inside the `kedro-project` folder. Change to the project directory:

   ```bash
   cd kedro-project
   ```

4. **Run the Kedro pipeline:**

   Now that you are in the `kedro-project` folder, execute the Kedro pipeline with the following command:

   ```bash
   kedro run
   ```

   This will run all the stages defined in the pipeline.

5. **Deactivate the virtual environment when you are done:**

   Once you're done working on the project, deactivate the virtual environment:

   ```bash
   deactivate
   ```

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
