import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emojis_exists(github_api):
    r = github_api.get_emojis()
    assert 'hammer' in r


@pytest.mark.api
def test_emojis_not_exists(github_api):
    r = github_api.get_emojis()
    assert 'blackat' not in r


@pytest.mark.api
def test_get_a_branch(github_api):
    r = github_api.get_branch('OlhaZamota', 'zamota_qa_auto', 'main')
    assert 'name' in r
    assert r['name'] == 'main'


@pytest.mark.api
def test_get_a_branch(github_api):
    r = github_api.get_branch('OlhaZamota', 'zamota_qa_auto', 'no_branch')
    assert r['message'] == 'Branch not found'    
