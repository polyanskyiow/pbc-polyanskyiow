import pytest
import requests


from pbc.sg.sg import StartGrid, Grid
from pbc.sg.page import GridPage, PythonPage
from requests import RequestException

# Initial test
@pytest.mark.selenium
def test_sg_sm(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert 2 == int(ssh_client.execute('pgrep java | wc -l'))

# Same test , but nothing will be done because selenium has already been downloaded, and  hub with node is running
# You will see this in the output
@pytest.mark.selenium
def test_sg_sm2(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert 2 == int(ssh_client.execute('pgrep java | wc -l'))


@pytest.mark.selenium
def test_requests(ssh_client ):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    try:
        response = requests.get('http://192.168.33.10:4444/grid/console')
        assert response.status_code == 200
        assert 5 == str(response.text).count('/grid/resources/org/openqa/grid/images/firefox.png')
    except RequestException as a:
        print 'Request failed.'
        raise a


# Verify selenium maxSession count
@pytest.mark.selenium
def test_check_grid(web_driver):
    grid_page = GridPage(web_driver)
    grid_page.open()
    assert True is grid_page.is_title_matches()
    assert True is grid_page.is_node_count_matches()


@pytest.mark.selenium
def test_pycon(web_driver):
    pycon_page = PythonPage(web_driver)
    pycon_page.open()
    assert True is pycon_page.is_title_matches()
    pycon_page.search_for('pycon')
    pycon_page.screenshot('pycon.png')

