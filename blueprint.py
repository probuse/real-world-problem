class People(object):
    "A template for a person associated with a company"
    first_name = 'someone'
    second_name = 'like you'
    user_name = 'Mr. Robot'
    email_address = 'someonelikeyou@company.com'
    
    
    def __init__(self):
        self.user_name = self.user_name
        self.email_address = self.email_address
        
    def set_user_name(self, name):
        " Sets user name"
        self.user_name = name
        return self.user_name
        
    def set_email_address(self, email_address):
        self.email_address = email_address
        return self.email_address
        
    
class Company(object):
    "A template for all companies"
    
    company_name = "company"
    year_founded = 1888
    num_of_employees = 0
    company_clients = ['Truth', 'Selfless']
    company_products = []
    company_networth = '$0'
    IPO_date = '1/1/1900'
    company_values = {} # value : meaning
    investors_in_company = []
    
    def __init__(self):
        self.company_name = self.company_name
        self.year_founded = self.year_founded
        self.num_of_employees = self.num_of_employees
        self.company_clients = self.company_clients
        self.company_values = self.company_values
        self.company_products = self.company_products
        self.company_networth = self.company_networth
        self.IPO_date = self.IPO_date
        self.investors_in_company = self.investors_in_company
        
    def set_company_name(self, name_of_company):
        "sets and returns name of company"
        self.company_name = str(name_of_company)
        return self.company_name
        
    def set_year_founded(self, year):
        "Sets and returns year company was founded"
        self.year_founded = year
        return self.year_founded
        
    def set_num_of_employees(self, employee):
        "Adds an employee to employees of the company, returns new employee # "
        new_num_of_employees = self.num_of_employees + employee
        self.num_of_employees = new_num_of_employees
        return self.num_of_employees
        
    def set_company_clients(self, *args):
        self.company_clients = args
        return self.company_clients
        
    def set_company_products(self, *args):
        self.company_products = args
        return self.company_products       
        
    def set_company_values(self, **kwargs):
        "Sets and returns a dictionary containing values of company and\
        what each value means "
        if kwargs == {}:
            print 'No company values set.'
        self.company_values = kwargs
        return self.company_values
            
        
    def set_IPO_date(self, date=None, month=None ,year=None):
        "sets Date of IPO"
        if date == None and month == None and year == None:
            return "Still a private entity"
        else:
            IPO_date = "%s/%s/%s" % (date, month, year)
            self.IPO_date = IPO_date
            return self.IPO_date
            
    def set_investors_in_company(self, *args):
        self.investors_in_company = args
        return self.investors_in_company
        
         
    
class UserGuide(object):
        
    def greeting(self, name):
        return " Howdy, %s" % name

