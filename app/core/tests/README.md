## Unit tests

Django comes with a test suite of its own, in the tests directory of the code base. It’s our policy to make sure all tests pass at all times.

We appreciate any and all contributions to the test suite!

The Django tests all use the testing infrastructure that ships with Django for testing applications. See Writing and running tests for an explanation of how to write new tests.

## Code coverage

Contributors are encouraged to run coverage on the test suite to identify areas that need additional tests.

When running coverage for the Django tests, the included .coveragerc settings file defines coverage_html as the output directory for the report and also excludes several directories not relevant to the results (test code or external code included in Django).

Source: [Django Documentation](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)

## Integration with coverage.py

Code coverage describes how much source code has been tested. It shows which parts of your code are being exercised by tests and which are not. It’s an important part of testing applications, so it’s strongly recommended to check the coverage of your tests.

Django can be easily integrated with coverage.py, a tool for measuring code coverage of Python programs. First, install coverage.py. Next, run the following from your project folder containing manage.py:

```bash
coverage run --source='.' manage.py test myapp
```

This runs your tests and collects coverage data of the executed files in your project. You can see a report of this data by typing following command:

```bash
coverage report
```

**Note** that some Django code was executed while running tests, but it is not listed here because of the source flag passed to the previous command.

Source: [Django Documentation](https://docs.djangoproject.com/en/dev/topics/testing/advanced/#topics-testing-code-coverage)
