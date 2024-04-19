from dictionary import getDefinition


def test_getDefinition():
    actualDefinition = getDefinition("computer")
    expectedDefinition = "A person employed to perform computations; one who computes."
    assert actualDefinition == expectedDefinition

def test_getDefinition2():
    actualDefinition = getDefinition("cat")
    expectedDefinition = "An animal of the family Felidae:"
    assert actualDefinition == expectedDefinition

