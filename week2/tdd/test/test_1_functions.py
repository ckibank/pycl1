# Write an add function with 2 parameters
# Write a divide function with 2 parameters

import time
import pytest
import functions as fn

def test_add():
  assert fn.add(1,2) == 3

# fixtures
def test_with_conf_fix(numbers_to_add):
  assert fn.add(numbers_to_add[0], numbers_to_add[1]) == 12
  # pass

# parameterizing functions
@pytest.mark.parametrize(
  "param1, param2, result",
  [
    (1,2,3),
    (.1,.2,.3),
    (5,6,11)
  ]
)
def test_param_add(param1, param2, result):
  assert fn.add(param1, param2) == pytest.approx(result)


@pytest.mark.slow
def test_slow_test():
  time.sleep(1)
  assert True

@pytest.mark.skip(reason="This is expected to fail")
def test_skip_add():
  assert fn.add(4, *7) == 11

# write test to check divide function
