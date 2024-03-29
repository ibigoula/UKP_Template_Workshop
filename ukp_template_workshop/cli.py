"""CLI interface for ukp_template_workshop project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
##### YOUR CODE HERE #####
import argparse
from ukp_template_workshop import Fibonacci
##########################

def main():  # pragma: no cover

    """
    The main function executes on commands:
    `python -m ukp_template_workshop` and `$ ukp_template_workshop `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ##### YOUR CODE HERE #####

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)

    args = parser.parse_args()

    answer = Fibonacci(args.n)
    print("Answer:", answer.value)
    ##########################