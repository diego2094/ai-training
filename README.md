# Building Intelligent Pipelines with LLMs: The JARVID Blueprint

This project provides datasets and solutions for the "Building Intelligent Pipelines with LLMs: The JARVID Blueprint" training.

You will find solutions for every lesson in all modules, along with datasets that you can use for each lesson.

Additionally, it includes utilities that you can use to generate datasets on your own.

## Try it out

As mentioned above, two datasets are already provided with the data needed to test all the lesson solutions. For the first module, you will need an `employees.db` file. A Python script called `csv-to-db-py` is provided to generate this file from the CSV data. Simply run `python csv-to-db-py` to generate it.
For the third lesson of the second module, a large dataset is required. We have provided one as part of this repository, but there's also a Python script that you can run to generate a new one with as many rows as you'd like. To do so, set the number of rows you want to generate in `generate_large_dataset.py` and run the script with `python generate_large_dataset.py`.

To begin testing the solutions, a `requirements.txt` file is included with all the dependencies you need for these modules. Run `pip install -r requirements.txt` to install them.

Then, you can run the solutions using Python to check the results for each of them.

For the first module, you will need to:

- Generate the `employees.db` file as mentioned above.
- Create an AWS account if you don't already have one and add your credentials to `~/.aws/credentials` (or manually export the environment variables into your console).

For the second module, you will need to:

- Have the large dataset ready. You can use the one provided or generate one using `generate_large_dataset.py`.
- For the PySpark part of the third lesson in the second module, you will need to have Java installed.

For the new modules you will need to have a credit card assign to your OpenAI account in ourder to use the embeddings API. Otherwise, you can use HuggingFace which is a free alternative.
