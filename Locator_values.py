class Login_Locators:
    email_xpath = "//*[@id='EmailId']"
    password_xpath = "//*[@id='Password']"
    login_xpath = "//*[@id='divLoginFormLnkBtn']"
    email_id = "EmailId"
    password_id = "Password"
    login_id = "lnkLogin"
    logout = "//a[@id='lnkApplicationLogOut']"
    homebr = "//*[@id='lnkBreadCrumHome']"

    dock_xpath = "//*[@id='divDockingStation']"
    dock_id = "divDockingStation"
    newloc_id = "btnAddLocation"
    newloc_xpath = "//*[@id='btnAddLocation']"
    accord_id = "accordionparent"
    accord_class = "panel-group"
    accord_del_class = "btn btn-sm btn-default pull-right clsdeletelocationgroup"
    loctab = "//*[@id='anchordockstationdetails']"
    apdtab = "//*[@id='anchoraccountsdue']"
    cotab = "//*[@id='anchoraccountcheckedout']"
    bpurtab = "//*[@id='anchoraccountpurchased']"
    loc_text_xpath = "//*[@id='txtLocation']"
    loc_text_id = "txtLocation"
    loc_save_xpath = "//*[@id='btnSaveLocation']"
    loc_save_id = "btnSaveLocation"
    loc_cancel_xpath = "//*[@id='btnCancelLocation']"
    loc_cancel_id = "btnCancelLocation"
    grp_xpath = "//*[@id='divPanel882']/div[2]/button"
    grp_text_xpath = "//*[@id='txtGroup']"
    grp_id = "txtGroup"
    adddock = "// *[ @ id = 'btnAddDockStation'] / span"
    slnum = "//*[@id='txtSerialNumber']"
    subs = "//*[@id='subscrptionList']"
    devloc = "//*[@id='ddlLocation']"
    grpdrp = "//*[@id='ddlGroupName']"
    grpnew = "//*[@id='txtGroupName']"
    grpsave = "//*[@id='btnDropdownSaveGroupName']"
    docname = "//*[@id='txtsecondaryname']"
    wifi = "//*[@id='txtWifiSSID']"
    wifipwd = "//*[@id='txtWifiSSIDPassword']"
    docsave = "//*[@id='btnSave']"
    exploc = "//a[text()='Hubbell Inc']/ancestor::div[@data-parent='#accordionparent']"
    dockst = "//*[@id='divGroupdockstation']/div"
    edtdocsav = "//*[@id='btnEditDockStationSave']"

    delloc = "//*[@id='btnDeleteLocationGroup207']"
    delpop = "//*[@id='btnDeleteLocationGroupOk']"


class preference:
    Prefmenu = "//*[@id='divDashboardSystemPreference']"
    stdtab = "//*[@id='ulpaymentdashboard']/li[1]/a"
    freetab = "//*[@id='ulpaymentdashboard']/li[2]/a"

    usertab = "//*[@id='ulpaymentdashboard']/li[3]/a"
    savebtn = "//*[@id='btnSavePaymentConfiguration']"
    poppay = "//*[@id='btnpaymentsettingexceptcheckedout']"

class Reports:
    repmenu = "//*[@id='divDashboardPayment']"
    timespan = "//*[@id='ddlTimeSpan']"
    transddetails = "//*[@id='headingTwo']"
    usrdts = "//*[@id='headingThree']"

class usradmin:
    usrmenu = "//*[@id='divDashboardUserManagement']"
    addusr = "//*[@id='btnAddUserRole']"
    emailusr = "//*[@id='txtEmailAddress']"
    savbtnusr = "//*[@id='btnAddUser']"





