CLI_ARGS=--no-header

MORE_DETAIL=-rA # -r: show extra test summary info. A: show all extra test summary output
LESS_DETAIL=-q # less verbosity
DISABLE_WARNINGS=--disable-pytest-warnings # disable warning summary

run_all_pytests:
	# simplest example
	@echo
	@pytest -rA tests/test_pytest_reusable_components.py --no-header

pytest_fixture_example:
	# fixtures allow you to the same piece of code before every test method
	@echo
	# -k option is used to specify the test case name
	@pytest -k "test_fixture_example" ${CLI_ARGS}

pytestconfig_eg:
	# pytestconfig allows you to provide extra command line args.
	@echo
	@pytest -k "test_pytestconfig_usage" --pytest_example_arg "abc" ${CLI_ARGS} ${MORE_DETAIL}
