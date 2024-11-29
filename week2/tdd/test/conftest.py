import pytest

@pytest.fixture
def numbers_to_add():
  paramaters = [10,2]
  print("~~~~~ Ran param setup")
  return paramaters

@pytest.fixture(scope="module", autouse=True)
def mod_setup_teardown(request):
  print("***** Started auto fixture")
  yield
  print("***** END auto fixture")