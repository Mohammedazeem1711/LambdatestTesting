from Basefile import BaseClassMethods


class Test_URL:
    def testURL(self):
        base = BaseClassMethods()
        base.openQAUrl()
        shetpath = "C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\PycharmProjects\\Selenium\\Jumpcharge\\Test_Data.xlsx"
        email = base.readData(shetpath, "Login", 2, 1)
        pawd = base.readData(shetpath, "Login", 2, 2)
        base.with_(email, pawd)
        base.mydock_()
        base.preference()
        base.usrmgmt()




