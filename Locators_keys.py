from selenium.webdriver.common.by import By


class Commonkeys:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def findByXpath(self, pathtofind):
        return self.driver.find_element(By.XPATH, pathtofind)

    def findByXPATH(self, pathtofind):
        return self.driver.find_elements(By.XPATH, pathtofind)

    def findByID(self, pathtofind):
        return self.driver.find_element(By.ID, pathtofind)
