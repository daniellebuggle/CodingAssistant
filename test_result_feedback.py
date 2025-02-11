def provide_few_shot_prompt(results, badge, ast_results):
    prompt = f"""
    Here are examples of how you should evaluate test results:
    
    Python Example 1:
    Python Test Results:
    test_empty_list (python_tests.calculate_sum_test.calculate_sum_test.test_empty_list)
    Test an empty list. ... ok
    test_mixed_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_mixed_numbers)
    Test a list with both positive and negative numbers. ... ok
    test_negative_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_negative_numbers)
    Test a list with negative numbers. ... ok
    test_positive_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_positive_numbers)
    Test a list of positive numbers. ... ok
    test_single_element (python_tests.calculate_sum_test.calculate_sum_test.test_single_element)
    Test a list with a single element. ... ok
    test_zeros (python_tests.calculate_sum_test.calculate_sum_test.test_zeros)
    Test a list with all zeros. ... ok
    
    ----------------------------------------------------------------------
    Ran 6 tests in 0.000s
    
    OK
    
    AST Test Results:
    True
    
    Response:
    Great job! You passed all tests and earned the Python For-Loop badge! 
    
    Java Example 1:
    Java Test Results:
    
    Thanks for using JUnit! Support its development at https://junit.org/sponsoring
    
    ╷
    ├─ JUnit Platform Suite ✔
    ├─ JUnit Jupiter ✔
    │  └─ CompareIntegersTest ✔
    │     ├─ testFirstIntegerGreater() ✔
    │     ├─ testNegativeIntegers() ✔
    │     ├─ testEqualIntegers() ✔
    │     ├─ testMixedSignIntegers() ✔
    │     └─ testSecondIntegerGreater() ✔
    └─ JUnit Vintage ✔
    
    Test run finished after 713 ms
    [         4 containers found      ]
    [         0 containers skipped    ]
    [         4 containers started    ]
    [         0 containers aborted    ]
    [         4 containers successful ]
    [         0 containers failed     ]
    [         5 tests found           ]
    [         0 tests skipped         ]
    [         5 tests started         ]
    [         0 tests aborted         ]
    [         5 tests successful      ]
    [         0 tests failed          ]
    
    AST Test Results:
    True
    
    Response:
    Great job! You passed all tests and earned the Java If-Else badge! 🎉
    
    Python Example 2:
    Python Test Results:
    test_factorial_large (python_tests.calculate_factorial_test.calculate_factorial_test.test_factorial_large)
    Test the factorial of a larger number. ... ok
    test_factorial_one (python_tests.calculate_factorial_test.calculate_factorial_test.test_factorial_one)
    Test the factorial of 1. ... ok
    test_factorial_positive (python_tests.calculate_factorial_test.calculate_factorial_test.test_factorial_positive)
    Test the factorial of a positive number. ... ok
    test_factorial_zero (python_tests.calculate_factorial_test.calculate_factorial_test.test_factorial_zero)
    Test the factorial of 0 (special case). ... ok
    test_negative_number (python_tests.calculate_factorial_test.calculate_factorial_test.test_negative_number)
    Test that a negative number raises a ValueError. ... FAIL
    
    ======================================================================
    FAIL: test_negative_number (python_tests.calculate_factorial_test.calculate_factorial_test.test_negative_number)
    Test that a negative number raises a ValueError.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/daniellebuggle/Documents/Trinity/Masters/Dissertation /CodingAssistant/python_tests/calculate_factorial_test.py", line 23, in test_negative_number
        with self.assertRaises(ValueError):
    AssertionError: ValueError not raised
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    FAILED (failures=1)
    
    AST Test Results:
    True
    
    Response:
    You failed the following test(s): `test_negative_number`. Make sure to raise a `ValueError` when a negative number 
    is provided.
    
    Java Example 2:
    Java Test Results:
    
    Thanks for using JUnit! Support its development at https://junit.org/sponsoring
    
    ╷
    ├─ JUnit Platform Suite ✔
    ├─ JUnit Jupiter ✔
    │  └─ PowerCalculatorTest ✔
    │     ├─ testPowerOfNegativeBaseEvenExponent() ✔
    │     ├─ testNegativeExponentThrowsException() ✘ Expected java.lang.IllegalArgumentException to be thrown, but nothing was thrown.
    │     ├─ testPowerOfNegativeBaseOddExponent() ✔
    │     ├─ testPowerOfZeroBase() ✔
    │     ├─ testPowerOfPositiveBaseAndExponent() ✔
    │     ├─ testPowerOfZeroExponent() ✔
    │     └─ testPowerOfOneBase() ✔
    └─ JUnit Vintage ✔
    
    Failures (1):
      JUnit Jupiter:PowerCalculatorTest:testNegativeExponentThrowsException()
        MethodSource [className = 'PowerCalculatorTest', methodName = 'testNegativeExponentThrowsException', methodParameterTypes = '']
        => org.opentest4j.AssertionFailedError: Expected java.lang.IllegalArgumentException to be thrown, but nothing was thrown.
           org.junit.jupiter.api.AssertionFailureBuilder.build(AssertionFailureBuilder.java:152)
           org.junit.jupiter.api.AssertThrows.assertThrows(AssertThrows.java:73)
           org.junit.jupiter.api.AssertThrows.assertThrows(AssertThrows.java:35)
           org.junit.jupiter.api.Assertions.assertThrows(Assertions.java:3128)
           PowerCalculatorTest.testNegativeExponentThrowsException(PowerCalculatorTest.java:49)
           java.base/java.lang.reflect.Method.invoke(Method.java:580)
           java.base/java.util.ArrayList.forEach(ArrayList.java:1597)
           java.base/java.util.ArrayList.forEach(ArrayList.java:1597)
    
    Test run finished after 512 ms
    [         4 containers found      ]
    [         0 containers skipped    ]
    [         4 containers started    ]
    [         0 containers aborted    ]
    [         4 containers successful ]
    [         0 containers failed     ]
    [         7 tests found           ]
    [         0 tests skipped         ]
    [         7 tests started         ]
    [         0 tests aborted         ]
    [         6 tests successful      ]
    [         1 tests failed          ]
    
    AST Test Results:
    True
    
    Response:
    You failed the following test(s): `testNegativeExponentThrowsException()`. Make sure to throw an `IllegalArgumentException` when number provided is negative. 
    
    Python Example 3:
    Python Test Results:
    test_empty_list (python_tests.calculate_sum_test.calculate_sum_test.test_empty_list)
    Test an empty list. ... ok
    test_mixed_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_mixed_numbers)
    Test a list with both positive and negative numbers. ... ok
    test_negative_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_negative_numbers)
    Test a list with negative numbers. ... ok
    test_positive_numbers (python_tests.calculate_sum_test.calculate_sum_test.test_positive_numbers)
    Test a list of positive numbers. ... ok
    test_single_element (python_tests.calculate_sum_test.calculate_sum_test.test_single_element)
    Test a list with a single element. ... ok
    test_zeros (python_tests.calculate_sum_test.calculate_sum_test.test_zeros)
    Test a list with all zeros. ... ok
    
    ----------------------------------------------------------------------
    Ran 6 tests in 0.000s
    
    OK
    
    AST Test Results:
    False
    
    Response:
    You passed all unit tests. Unfortunately, you failed to use the correct coding concept to earn the Python For-Loop 
    badge! 
    
    Java Example 3:
    Java Test Results:
    
    Thanks for using JUnit! Support its development at https://junit.org/sponsoring
    
    ╷
    ├─ JUnit Platform Suite ✔
    ├─ JUnit Jupiter ✔
    │  └─ CompareIntegersTest ✔
    │     ├─ testFirstIntegerGreater() ✔
    │     ├─ testNegativeIntegers() ✔
    │     ├─ testEqualIntegers() ✔
    │     ├─ testMixedSignIntegers() ✔
    │     └─ testSecondIntegerGreater() ✔
    └─ JUnit Vintage ✔
    
    Test run finished after 713 ms
    [         4 containers found      ]
    [         0 containers skipped    ]
    [         4 containers started    ]
    [         0 containers aborted    ]
    [         4 containers successful ]
    [         0 containers failed     ]
    [         5 tests found           ]
    [         0 tests skipped         ]
    [         5 tests started         ]
    [         0 tests aborted         ]
    [         5 tests successful      ]
    [         0 tests failed          ]
    
    AST Test Results:
    False
    
    Response:
    You passed all tests. Unfortunately you failed to use the correct coding concept to earn the Java If-Else badge! 🎉
    
    Now based on the examples above, generate a natural language response in the same format by doing the following:
    Check the student's test results:

    {results}

    and the AST results:
    {ast_results}
    
    Evaluate if they earned the {badge} badge using the unit test results and the AST results. Don't ever include test results.
    """
    return prompt


def provide_zero_shot_prompt(results, badge, ast_results):
    prompt = f"""
    {results}
    These are the unit test results to the code that the student provided. Check to see if they are all correct. 
    
    {ast_results}
    These are the Abstract Syntax Tree test results to the code that the student provided. Check to see if they passed.
    
    If all unit tests are correct and they passed the AST test, you should congratulate them and say they passed all 
    tests, and let them know they earned the {badge} badge. If they failed any test, provide a hint as to where they 
    went wrong by only naming what test(s) failed.
    
    Additionally if they passed all unit tests but failed the AST test, tell them they passed the unit tests but failed 
    to use the correct coding concept to earn the {badge} badge.
    """
    return prompt