# Title

A set of examples of unit testing using unittest and pytest

# Folder Description

- **Lesson 1**: contains examples of unit test using python library **unittest**


- **Lesson 2**: Contains examples of unit tests using third party library **pytest**

- **Practical_lesson**: this is what we used to practice together. You can use this folder to play around **pytest**



# Getting Started

1: Clone the entire repo

*on your terminal pass the following command*

```bash
git clone https://github.com/Impact-Africa-Network/Testing-examples/
```

2: Navigate to any of the folders as described on the Folder description section

3: Notes are on the testing101.py file


# Usage

- You will find a set of files namely calc.py where we have most of the calculator functions
- Any file starting with test_filename is where all the test functions are written

# Dependencies

- If you come up a pipfile or pipfile.lock file, this means there are dependencies that were downloaded for the project.
- You can go ahead and install the dependencies using the following command
```bash
pipenv install
```
- Activate your virtual environment 
```bash
pipenv shell
```

- If you dont have pipenv installed, use the following commands
NB: Pipenv helps spin a virtual environment to ensure all dependencies are contained in only the project you are currently working on and not globally

***install pipenv***
```bash
pip install pipenv
```

***install dependencies from the pipfile.lock file***
```bash
pipenv install
```

***activate a new environment***
```bash
pipenv shell
```

- Once the virtual environment is spinned up you can always install any other dependencies and they will be added to the pipfile.lock file
```bash
pipenv install <Package_name>
```
- You can as well exit at any time using exit command
```bash
exit
```

# Running your tests on pytest
***run the following command on your terminal***
```bash
pytest
```

## Author

Kefa Mutuma : [@Boykefa](https://twitter.com/Boykefa)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgments
Shoutout: IAN Devs

## License
[MIT](https://choosealicense.com/licenses/mit/)


