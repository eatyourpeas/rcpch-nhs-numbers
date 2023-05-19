
# A python 3.11 module for NHS numbers

Currently it offers:

- NHS number validation
- Unique random NHS number generation

steps for installing for dev purposes:

1. clone the repo
2. create a virtualenv (```python -m pyenv virtualenv 3.11.0 rcpch-nhs-numbers```)
3. ```pip install -e .```

Testing can be done from the command line in the root directory:
```pytest```

## NHS Numbers

NHS numbers are complicated - they are always 10 digits long, do not start with a zero, and must fulfill the modulus 11 algorithm to be valid. This is explained [here](https://www.datadictionary.nhs.uk/attributes/nhs_number.html)

Validation rules are needed in software though nowhere is this offered as an API or as a standardised module. There are several packages on pypi that offer it and there is currently a conversation across UK health tech to have one nhs-number package to rule them all.

This package is designed to be a conversation starter, not the definitive solution. It is a call to arms for NHS data enthusiasts to:

1. Tweak and improve the versions offered here
2. Begin a conversation about what other scope might be included (eg Scotland, Wales and NI)
3. 