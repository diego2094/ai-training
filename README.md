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

For the new modules, you will need to have a credit card assigned to your OpenAI account in order to use the embeddings API. Alternatively, you can use Hugging Face, which is a free alternative.

For the OpenAI completions API, `gpt-3.5-turbo` has been used instead of `text-davinci-003`. As a result, in Module 6, Lesson 1, the responses are not exactly the same because the 3.5 model elaborates a bit more on the responses. If you want them to match, you'll need to change `test_cases.csv` to expect the correct response.

In Module 6, Lesson 3, you will be asked to run Grafana. If you downloaded it as suggested on their homepage, you might encounter issues when running it because it's not part of your PATH. If that's the case, here are the steps to follow:

- Edit your `.zshrc` and add `export PATH="$HOME/grafana-v11.5.2/bin:$PATH"`, then apply it in the terminal you are using with source `~/.zshrc`.
- At this point, it will find the `grafana-server` command, but it might still complain about the home path not being set. To fix this, add `export GF_PATHS_HOME="$HOME/grafana-v11.5.2"` to your `.zshrc` and apply it with source `~/.zshrc`.
- However, that might still not be enough to run it just with `grafana-server`; you may need to run it with `grafana server --homepath "$GF_PATHS_HOME"`.
- The solution I found was to create an alias to simplify the command. You can add `alias grafana='grafana server --homepath="$GF_PATHS_HOME"'` to your `.zshrc` and apply it.
- Now, you can run Grafana directly with the command `grafana`.

For this module we used the jarvid-api created for Module5-Lesson1
