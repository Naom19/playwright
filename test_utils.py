import utils


def test_root():
    utils.root_25
    print("Testing for 25...")
    root_25 = utils.root(25)
    print("...got ", root_25)
    assert root_25 == 5

