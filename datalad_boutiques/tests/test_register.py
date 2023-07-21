from datalad.tests.utils_pytest import assert_result_count


def test_register():
    import datalad.api as da
    assert hasattr(da, 'boutiques')
    assert_result_count(
        da.boutiques(),
        1,
        action='demo')

