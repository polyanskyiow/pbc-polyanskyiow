import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pbc.sg.sg import StartGrid, Grid

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

# Verify selenium maxSession count
@pytest.mark.selenium
def test_check_grid():
    driver = webdriver.Firefox()
    driver.get("http://192.168.33.10:4444/grid/console")
    assert "Grid Console" in driver.title
    elem = driver.find_elements_by_xpath("//div[@class='content_detail']//img[contains(@title,'firefox')]")
    assert 5 == len(elem)
    driver.close()
