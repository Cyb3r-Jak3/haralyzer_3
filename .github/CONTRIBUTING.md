# CONTRIBUTING

## How to contribute

---

Thanks for reading this because I are always looking to collaborate with other people to see their ideas.

To get started fork the repo and make a branch with an accurate name for the changes you are making. Once you have made the changes to your liking open a pull request and I will look it over.

## Getting Started
---

Follow to code below to get the repo cloned

```bash
git clone https://github.com/Cyb3r-Jak3/haralyzer_3.git
cd haralyzer_3
# Highly recommend creating a virtualenv before continuing
pip install -r requirements-dev.txt
```

## Documentation
---

All changes should be documented using restructuredText both with docstring and in [docs](../docs) for readthedoc. If you need help with it then please let me know.


## Testing
---

All new changes should have tests cases when possible. New changes should also not break existing tests. Other tools that are used are [bandit](https://bandit.readthedocs.io/en/latest/), [black](https://github.com/psf/black), [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://www.pylint.org/.

### Running tests locally

This project has a [tox](https://tox.readthedocs.io/en/latest/) file so you are to run the tests locally. To use install tox and run it using `tox`. 