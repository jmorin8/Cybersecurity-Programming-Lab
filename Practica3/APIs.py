import getpass
import requests
import json 
import re

# Email Verifier
def email_Verify(*vars):
    
    url= f"https://api.hunter.io/v2/email-verifier?email={mail}&api_key={apiKey}"

    request = requests.get(url) 
    response_dict = json.loads(request.content)
    
    email = response_dict['data']['email']
    email_status = response_dict['data']['status']

    print("\n[*] Verifying email..")
    if email_status == "valid":
        print(f'[*] Email {email} is a proffesional account')
        email_Count(email)
    
    elif email_status == "webmail":
        print(f'[*] Email {email} is a web-mail')
    
    else:
        print('[*]Not a valid email\n[*]Quiting...')



# Email Count 
# show how many adresses are for the domain
def email_Count(var):
    url = "https://api.hunter.io/v2/email-count?domain="
    
    getDomain = re.search(r"@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})", str(var)) # search for all after @ (incluiding it) in the email
    domain = getDomain.group()
    
    new_url= f"{url}+{domain[1:]}"

    req = requests.get(new_url)
    res_dict = json.loads(req.content)

    total_mails = res_dict['data']['total']
    personal = res_dict['data']['personal_emails']
    generic = res_dict['data']['generic_emails']

    executive_department = res_dict['data']['department']['executive']
    IT_department = res_dict['data']['department']['it']
    finance_department = res_dict['data']['department']['finance']
    sales_department = res_dict['data']['department']['sales']
    legal_department = res_dict['data']['department']['legal']
    marketing_department = res_dict['data']['department']['marketing']

    print(f"[*] We found {total_mails} emails where {personal} are personal emails and {generic} are generic emails\n[*] Emails found by department:\n\tExecutive : {executive_department}\n\tIT : {IT_department}\n\tFinance : {finance_department}\n\tSales : {sales_department}\n\tLegal : {legal_department}\n\tMarketing : {marketing_department}")
    


def other_API(var):
    print(f'\nThis function will test another API with email-->{var}')



if __name__=="__main__":
    mail=input("Write an email: ")
    apiKey=getpass.getpass("API-key: ") # 
    
    email_Verify(mail,apiKey)

