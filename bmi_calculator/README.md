# BMI Calculator

This project calculates BMI of people, whose data stored in json file.

# Requirements:

    Python 3.x

## Prerequisites

Use python on windows cmd prompt
Use python3 on linux terminal

### Install libraries

```bash
pip install tabulate
```

# File structure:

```
└───bmi_calculator
    │   bmi_main.py
    │   README.md
    │
    ├───example
    │       BMI.log
    │       bmi_example.py
    │       input.json
    │
    ├───lib
    │       bmi_lib.py
    │       logging_conf.py
    │
    └───test
            bmi_test.py
```

# Run Example design

Run bmi_example.py to understand the basic flow of this app.

```python3
python bmi_example.py # windows
python3 bmi_example.py # linux
```

## Expected Example design output

```
Running example design ...

 count_by_bmi_category:

 BMI_category        Count
----------------  -------
Moderately_obese        3
Normal                  2
Overweight              1

 count_by_bmi_risk:

 BMI_risk      Count
----------  -------
Medium            3
Low               2
Enhanced          1

 Successfully ran example design

 Execution time: <your_execution_seconds> seconds

```

# Running Tests

To run test, run following command

## On windows

Command format:
python bmi_test.py <input_json_file> <height_col_name> <weight_col_name>

### Example

    python bmi_test.py input.json HeightCm WeightKg

## On Linux

Command format:
python3 bmi_test.py <input_json_file> <height_col_name> <weight_col_name>

### Example

    python3 bmi_test.py input.json HeightCm WeightKg
