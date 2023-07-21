Instructions to Set Up and Run the Code from HW4:

1) Create a new virtual environment:
    Using venv (Python 3 standard library):
        python3 -m venv myenv_yourenv

2) Activate the virtual environment:
    On Windows: yourenv\Scripts\activate
    On macOS and Linux: source yourenv/bin/activate

3) Install the required dependencies:
    pip install -r requirements.txt

4) Run the refactored unittests:
    Make sure you are in the directory containing unittest_dvetriak.py.
    Run the following command: python -m unittest discover -s . -p "test_*"

The unit tests will be executed, and the test results will be displayed in the console.

