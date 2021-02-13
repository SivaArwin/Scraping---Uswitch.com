from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pandas as pd
import xlsxwriter
import time
import _Custom_Exception as CE
import _Config as config
import _EHl_urls 

overlapXpath = "/html/body/div[@id='loaderDiv']"

web_driv = config._WebDriv()

_Mdd_links = config._read_MDD_Urls()
_savePath = config.savePath()

#_regionList = ["Eastern", "East Midlands","London", "MANWEB", "Midlands", "Northern", "NORWEB", "Scottish Hydro", "Scottish Power", "Seeboard", "Southern", "Swalec", "SWEB", "Yorkshire"]


"""
#MainPage #Postcode
postcode = web_driv.find_element_by_xpath("/html/body/main[@class='main']/div/div/div/div[@id='postCodeEntry']/form/fieldset[@class='homepage-cta-container']/div[@class='form-group homepage-cta-input-container']/input[@id='PostCode']")
postcode.send_keys("SS26LU")
CE._Time_to_delay(1)


#Mainpage #Submit button
submit = web_driv.find_element_by_xpath("/html/body/main[@class='main']/div/div/div/div[@id='postCodeEntry']/form/fieldset[@class='homepage-cta-container']/button")
submit.click()
CE._Time_to_delay(10)

#Select Both Gas & Elec
gas_elec_elementXpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[@class='ng-scope']/div[@id='questions-intro']/div[@id='field-compare-type']/div[@class='field-input stacked-radio-buttons']/div/input[@id='compare-type-gas-elec']"
CE._Pass_Through_Me(web_driv,overlapXpath,gas_elec_elementXpath)
CE._Time_to_delay(1)

#Select both same supplier
sameSupplier_elementxpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[@class='ng-scope']/div[@id='questions-intro']/div[@id='field-same-supplier']/div[@class='field-input stacked-radio-buttons']/div/input[@id='comparison-type-same-supplier']"
CE._Pass_Through_Me(web_driv,overlapXpath,sameSupplier_elementxpath)
CE._Time_to_delay(1)

#select tariff
tariffname = web_driv.find_element_by_xpath("/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[@class='ng-scope']/div[@id='section-supply']/span[@id='section-supply-dual']/div[@class='funnel-section question-group-container ng-isolate-scope ng-valid']/div[3]/div[@class='field-input single-radio-button']/select[@id='elecSupplierTariff']")
Select(tariffname).select_by_value("string:44")
CE._Time_to_delay(1)

#select payment method
payment_Method_Xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[@class='ng-scope']/div[@id='section-supply']/span[@id='section-supply-dual']/div[@class='funnel-section question-group-container ng-isolate-scope ng-valid ng-dirty ng-valid-parse']/div[@id='field-energy-payment-type']/div[@class='field-input stacked-radio-buttons']/div[@class='ng-scope']/input[@id='elec-payment-type-1']"
CE._Pass_Through_Me(web_driv,overlapXpath,payment_Method_Xpath)
CE._Time_to_delay(1)


#Select gas usage radio button
gas_button_xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[2]/div[@id='section-usage']/div[@id='gas-usage']/div[@class='field-input expand']/div[@class='radio-gas-usage']/input[@id='gasKWhUsage']"
CE._Pass_Through_Me(web_driv,overlapXpath,gas_button_xpath)
CE._Time_to_delay(3)


#Passing Gas usage
gas_usage_xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[2]/div[@id='section-usage']/div[@id='gas-usage']/div[@class='field-input expand']/div[@class='radio-gas-usage']/div[@class='input-error-container-inline']/input[@id='gasKWhUsage-usageAsKWh']"
gs_usage_res = web_driv.find_element_by_xpath(gas_usage_xpath)
gs_usage_res.send_keys("12000")
CE._Time_to_delay(1)

#select Elec usage radio button
elec_button_xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[2]/div[@id='section-usage']/div[@id='electricity-usage']/div[@class='field-input expand']/div[@class='radio-elec-usage']/input[@id='elecKWhUsage']"
CE._Pass_Through_Me(web_driv,overlapXpath,elec_button_xpath)
CE._Pass_Through_Me(web_driv,overlapXpath,elec_button_xpath) #running this code twice because the elec button is not clicked
CE._Time_to_delay(3)

#Passing Elec usage
elec_usage_xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[2]/div[@id='section-usage']/div[@id='electricity-usage']/div[@class='field-input expand']/div[@class='radio-elec-usage']/div[@class='input-error-container-inline']/input[@id='elecKWhUsage-usageAsKWh']"
elec_usage_res = web_driv.find_element_by_xpath(elec_usage_xpath)
elec_usage_res.send_keys("3100")
CE._Time_to_delay(1)

#Click Submit button #Page2
show_results_button_xpath = "/html/body/div[@class='ng-scope']/div[@class='container-fluid page_funnel-questions ofy-visible current ng-scope ng-isolate-scope']/div/form[@id='current-optilead']/div[@id='section-spending']/div[2]/div[@id='usageSummary']/div[@class='spending-text ng-scope']/button[@id='show-results']"
CE._Pass_Through_Me(web_driv,overlapXpath,show_results_button_xpath)
CE._Pass_Through_Me(web_driv,overlapXpath,show_results_button_xpath) #running this code twice because the elec button is not clicked
CE._Time_to_delay(10)


#Page 3 #Select Show all results .. #Whole of market
#show_all_tariffs_xpath = "/html/body/div[@class='ng-scope']/div[@class='page_funnel-questions container-fluid ofy-visible ng-scope ng-isolate-scope']/div[@class='row wider-margin funnel-columns']/section/div[@class='funnel-filter-sidebar-container']/div[@class='funnel-section ng-isolate-scope']/div[@class='funnel-sidebar-wrapper']/div[@id='section-filters']/form/div[@class='field side-bar-form field-stacked']/ul[2]/li[@class='left-column']/input[@id='Show me all generally available plans']"
#CE._Pass_Through_Me(web_driv,overlapXpath,show_all_tariffs_xpath)
#CE._Time_to_delay(3)
"""

writer = pd.ExcelWriter(_savePath+'MDD-SE-SD.xlsx', engine='xlsxwriter')

try:
    if(_Mdd_links):
        for driver in range(len(_Mdd_links)):
            web_driv.delete_all_cookies()
            web_driv.get(_Mdd_links[driver])
            CE._Time_to_delay(15)

            Tariff_Name = {}
            #Result Table output
            who = "/html/body/div[@class='ng-scope']/div[@class='page_funnel-questions container-fluid ofy-visible ng-scope ng-isolate-scope']/div[@class='row wider-margin funnel-columns']/section/div[@class='funnel-results-container']/div[@class='funnel-section ng-isolate-scope']/div[@id='section-compare-table']/div[@class='compare-table']/div[@class='compare-table-body']"
            who_res_final_res = web_driv.find_element_by_xpath(who)

            
            '''
            gas = '//*[@id="Gas only"]'
            CE._Pass_Through_Me(web_driv,overlapXpath,gas)
            CE._Time_to_delay(3)
             
            '''

            Ele = '//*[@id="Electricity only"]'
            CE._Pass_Through_Me(web_driv,overlapXpath,Ele)
            CE._Time_to_delay(3)
            
            ## ENQUIRY TARIFFS
            #Supplier Name on Enquiry
            for _supplierName_enquiry in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[1]/div[@class='supplier']/p[contains(@class, 'ng-binding') and contains(@class, 'ng-scope')]"):
                Tariff_Name.setdefault('SupplierName', []).append(_supplierName_enquiry.text)
                #print("Supplier Name ->", _supplierName_enquiry.text )
            print("Fetched Supplier Name Enquire..")    

            #Tariff Name on Enquiry
            for _tarifName_enquiry in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[1]/div[@class='supplier']/p[@class='ng-binding']"):
                #print("tariff name ->", _tarifName_enquiry.text)
                Tariff_Name.setdefault('TariffName',[]).append(_tarifName_enquiry.text) 
            print("Fetched Tariff Name....")

            #Cancellation fees yes or no on apply    
            for cancellation_fees in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[2]/p/span[1]/span"):
                Tariff_Name.setdefault('Cancellationstatus',[]).append(cancellation_fees.text)
                #print("Cancellation >", cancellation_fees.text)
            print("Fetched Cancellation status...!!!")


            #Tariff expiry
            for tariff_expiry in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[2]/p/span[2]/span"):
                Tariff_Name.setdefault('Tariffexpiry',[]).append(tariff_expiry.text)
                #print("Expiry >", tariff_expiry.text)
            print("Fetched Tariff expiry...!!!")


            #annual bill value on apply
            for annual_bill in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[3]/p/span[@class='ng-binding']"):
                Tariff_Name.setdefault('annual_bill',[]).append(annual_bill.text)
                #print("Annual Bills >",annual_bill.text)
            print("Fetched Annual values ...!!!")


            #On Enquiry
            for on_enquiry in who_res_final_res.find_elements_by_xpath("div[contains(@class, 'compare-table-item') and contains(@class, 'compare-cannot-switch')]/fri-result-tariff/div/div[6]/p[@class='ng-binding']"):
                if (on_enquiry.text == "This supplier has not made this plan available through us" ):
                    Tariff_Name.setdefault('Status',[]).append("Enquiry")
                    
                #print("#", on_enquiry.text)
            print("Fetched on Enquiry ...!!!")

	    
	                
            #show Apply only
            show_apply_tariffs_xpath = "/html/body/div[@class='ng-scope']/div[@class='page_funnel-questions container-fluid ofy-visible ng-scope ng-isolate-scope']/div[@class='row wider-margin funnel-columns']/section/div[@class='funnel-filter-sidebar-container']/div[@class='funnel-section ng-isolate-scope']/div[@class='funnel-sidebar-wrapper']/div[@id='section-filters']/form/div[@class='field side-bar-form field-stacked']/ul[1]/li[@class='left-column']/input[@id='Show plans you can switch me to']"
            CE._Pass_Through_Me(web_driv,overlapXpath,show_apply_tariffs_xpath)
            CE._Time_to_delay(3)

            #### APPLY TARIFFS

            print("Fetching on apply tariffs now.......")

            #Supplier Name On Apply #img[@class='supplier-logo ng-scope']
            for SA in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[1]/div[@class='supplier']/img[@class='supplier-logo ng-scope']"):
                Tariff_Name.setdefault('SupplierName',[]).append(SA.get_attribute('alt'))
                #print("Supplier Name >", SA.get_attribute('alt'))
            print("Fetched Supplier Name....!!!")

            #Tariff Name on Apply
            for TA in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[1]/div[@class='supplier']/p[@class='ng-binding']"):
                Tariff_Name.setdefault('TariffName',[]).append(TA.text)
                #print("Tariff Name >",TA.text)
            print("Fetched Tariff Name....!!!")
                
            #Cancellation fees yes or no on apply    
            for cancellation_fees in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[2]/p/span[1]/span"):
                Tariff_Name.setdefault('Cancellationstatus',[]).append(cancellation_fees.text)
                #print("Cancellation fees >", cancellation_fees.text)
            print("Fetched Cancellation status...!!!")

            #Tariff expiry
            for tariff_expiry in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[2]/p/span[2]/span"):
                Tariff_Name.setdefault('Tariffexpiry',[]).append(tariff_expiry.text)
                #print("Expiry >", tariff_expiry.text)
            print("Fetched Tariff expiry...!!!")

            #annual bill value on apply
            for annual_bill in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[3]/p/span[@class='ng-binding']"):
                Tariff_Name.setdefault('annual_bill',[]).append(annual_bill.text)
                #print("Annual Bills >",annual_bill.text)
            print("Fetched Annual values ...!!!")

            #On Apply
            for on_apply in who_res_final_res.find_elements_by_xpath("div/fri-result-tariff/div/div[6]/button"):
                if (on_apply.text == "I WANT THIS PLAN"):
                    Tariff_Name.setdefault('Status',[]).append("Apply")
                
                #print("#", on_apply.text)
            print("Fetched on Apply ...!!!")

            '''
            #Page 3 #Select Show all results .. #Whole of market
            show_all_tariffs_xpath = "/html/body/div[@class='ng-scope']/div[@class='page_funnel-questions container-fluid ofy-visible ng-scope ng-isolate-scope']/div[@class='row wider-margin funnel-columns']/section/div[@class='funnel-filter-sidebar-container']/div[@class='funnel-section ng-isolate-scope']/div[@class='funnel-sidebar-wrapper']/div[@id='section-filters']/form/div[@class='field side-bar-form field-stacked']/ul[2]/li[@class='left-column']/input[@id='Show me all generally available plans']"
            CE._Pass_Through_Me(web_driv,overlapXpath,show_all_tariffs_xpath)
            CE._Time_to_delay(3)
            '''
            

            _df = pd.DataFrame.from_dict(Tariff_Name)
            
            

            #for _region in driver:
            _df.to_excel(writer, sheet_name=str(driver+1), index=False)

            print("Region %d complete" %(driver+1))
            
            


            #tn.to_csv('EHL.csv', index=False, sep=',', encoding='utf-8')
            #print(tn)

        writer.save()
        print("File is ready to use!!!")
        web_driv.close()

except TimeoutException:
    print("Link is broken... Replace new url")
    web_driv.close()