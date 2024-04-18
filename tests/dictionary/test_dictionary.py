from dictionary import getDefinition


def test_getDefinition():
    actualDefinition = getDefinition("computer")
    expectedDefinition = "A person employed to perform computations; one who computes."
    assert actualDefinition == expectedDefinition

# Introducing a failing test
def test_getDefinition_failure():
    actualDefinition = getDefinition("bilgisayar")
    expectedDefinition = "A person employed to perform computations; one who computes."
    # Assuming 'bilgisayar' is not defined as such in your dictionary,
    # this assertion would be incorrect and the test will fail.
    assert actualDefinition == expectedDefinition