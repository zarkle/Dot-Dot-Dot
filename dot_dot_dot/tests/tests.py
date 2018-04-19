def test_default_behavior_of_home_view(dummy_request):
    """test home view"""
    from ..views.home import home_view
    response = home_view(dummy_request)
    assert isinstance(response, dict)
    assert isinstance(response['data'], list)


def test_not_found(dummy_request):
    """test not found view"""
    from ..views.notfound import notfound_view
    response = notfound_view(dummy_request)
    assert isinstance(response, dict)
    assert response == {}
