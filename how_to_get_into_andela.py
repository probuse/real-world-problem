from blueprint import People, Company, UserGuide
from sys import exit

andela = Company()
user = People()

class Welcome(object):
    "Welcomes our users into the application....."
    def __init__(self, section_map):
        self.section_map = section_map
        
    def begin(self):
        current_section = self.section_map.opening_section() 
              
        while True:
            print "\n\n" + "=" * 65
        
            current_section_name = current_section.enter_section()     
            current_section = self.section_map.next_section(current_section_name)
        
  

class Home(object):
    
    def __init__(self):
        self.user_guide = UserGuide()          
        print "\
            You are welcome.\n\
            Please Enter your name and email addreess to continue.\n"
        self.name = raw_input("Please input your name:\n =>")
        self.email_address = raw_input("Please input your email address:\n =>")  
        self.user_email_address = user.set_email_address(self.email_address)
        
    def start_session(self):
        print self.user_guide.greeting(self.name)
            
    def enter_section(self):
        print " %s thank you for taking time to use our application" % self.name
        return 'andela'
        

class Andela(Company):
    
    def __init__(self):
        self.name = 'Andela'
   
    def enter_section(self):
        print "Here is brief information about %s:" % self.name
        print """
            "We build high-performing engineering teams with the most 
            talented developers from tech hubs across Africa." - Andela  
        """
        print """
            After building these high-performing engineering teams,
            Andela extends engineering teams with 
            world-class software developers. 
        """
        print """
            To get world-class software developers, Andela's 
            recruitment process is extreme.
            CNN called their recruitment process to be harder than
            getting into Harvard.
            But every thing they want in a Developer is someone with
            their values.
            EPIC is the word that describes Andela's values.
        """
        print "Do you want to know what 'EPIC' means?"
        print "Enter y for yes or n for no"
        
        answer = raw_input("> ")
        if answer.lower() == 'y':
            print """\
EPIC stands for Excellence, Passion, Integrity and Collaboration
            """
        elif answer.lower() == 'n':
            print "Alright, we shall just continue.................\n"
        else:
            print "Wrong Entry!!!! Please enter y for yes or n for no"
            
        print 'Andela offers services to so many clients\n'
        print 'Press enter to view some of them'
        user_input = raw_input('....')
        
        andela_clients = andela.set_company_clients(
                            'Microsoft', 
                            'IBM', 
                            'And many other startups'
                            )
        print "These are some of Andela's clients"
        for client in andela_clients:
            print '\t* ', client
        
        print '\nThese clients are some of the biggest companies in the world'
        print 'What kind of services do you think Andela offers to its clients?'
        
        user_reply = raw_input('> ')
        
        andela_products = andela.set_company_products(
            'world-class software developers',
            'mentorship',
            'software development',
            'software maintenance'
            )
        def get_andela_products():
            for product in andela_products:
                print '\t* ',product
            return 'And many more software products and services.'
            
        if user_reply in andela_products:
            print 'You are right and here are some more.\n', get_andela_products()
        else:
            print 'Wrong Answer, but here are their products:\n', get_andela_products()
                                                    
        
        print '\nTo offer services like those to big companies like shown above..'
        print 'Andela needs teams of hardworking employees that deliver on time'
        print '\nHow many employees do you think Andela has?'
        
        andela_employees = andela.set_num_of_employees(400)
        user_guess = int(raw_input('> '))
        
        if user_guess == andela_employees:
            print 'That is right, andela has about %d employees' % user_guess
        else:
            print '%d is close but not right, Andela has %d employees' % (
                                                            user_guess,
                                                            andela_employees
                                                            )
        print 'When do you think Andela was founded?'
        user_response = int(raw_input('> '))
        
        year_founded = andela.set_year_founded(2014)
        
        if user_response == year_founded:
            print 'Correct.'
        else:
            print 'Wrong, Andela was founded in %s' % year_founded
            
        
        andela_investors = andela.set_investors_in_company(
                    'Chan Zuckerberg Initiative',
                    'Google Ventures',
                    'Spark Capital',
                    'Omidyar Network',
                    'Founder Collective',
                    'Learn Capital',
                    'Melo7 Tech',
                    'Arena',
                    'Spark Labs',
                    'Peak Venture',
                    'Summit',
                    'Susa Ventures'
                    )
                    
        def get_andela_funders():
            for funder in andela_investors:
                print '\t* ', funder
            return 'Note: Zuckerberg is founder of Facebook'
                      
        print '\nAndela is also funded by some of the biggest companies in the world.'
        print 'Can you name some?'
        
        user_answer = raw_input('> ')
        
        
        if user_answer in andela_investors or user_answer.lower() == 'facebook':
            print '\nThat is pretty close'
            print 'Here is a detailed list of Investors in Andela.\n', get_andela_funders()
        else:
            print "\nThat's incorrect!!!!"
            print 'Here is a detailed list of Investors in Andela.\n', get_andela_funders()
        
        print '\nTo meet its goals and client\'s needs,' 
        print 'Andela maintains a staff of world-class software developers'
        print 'But how does Andela get these world-class software developers?'
        print 'Do you have any idea?'
         
        user_resp = raw_input('Type y for yes or n for no\n> ')
        
        if user_resp == 'y':
            print '\nTell us about it by typing it here, press Enter after:'
            user_input1 = raw_input('> ')
            print 'Thank you for your response. But here is the detailed process'
            return 'interview'  
        elif user_resp == 'n':
            return 'interview'
        else:
            print 'Wrong entry, Please type in y for yes or n for no.'  
            
        
            exit(0)
        

    
class Interview(object):
    "Explains the whole interview process"
     
    def enter_section(self):
        print "To get world class-developers..."
        print "Andela's recruitment is extreme and these are the statistics:"
        print "50000+ applicants, six week vetting process, 0.5% acceptance rate"
        
        print "\n\nHow does Andela select world-class software developers?"
        text = open('andela_interview_process.txt')
        print text.read()
        
        print 'Do you think this is extreme?'
        answer = raw_input('Please type in y for yes and n for no.\n> ')
        
        if answer == 'y':
            print '\nHow else can Andela get world-class developers?'
            print 'The selection process has to be this extreme...'
            print 'To get world-class software developers\n'
        elif answer == 'n':
            print '\nThen you must be an extreme person'
            print 'And here is what happens when you join Andela.\n'
        else:
            print 'Wrong entry, make sure you type in y for yes or n for no.'
            
        text1 = open('while_at_andela.txt')
        print text1.read()
        
        print '-'*60
        print 'We can see this is extreme but do you see any other way...'
        print 'Of getting world-class software developers other than this\n?'
        
        reply = raw_input('Please type in y for yes and n for no\n> ')
        if reply == 'y':
            print "\nWhy do you think like that?...press Enter when done typing"
            user_feedback = raw_input('> ')
            user_reply = open('user_feedback.txt','a')
            user_reply.write(user_feedback + '\n')
            print '\nYou can implement that at your own startup.'
            print 'Here it has to be extreme and that is how people grow'
            print 'You will never grow if you don\'t get out of your comfort zone'
            print 'And this prepares you to be a world-class developer'
            print 'A developer who can solve any problem they encounter.'
        elif reply == 'n':
            print 'Then extreme is the way to go'
        else:
            print 'Wrong Entry!!! Please type in y for yes or n for no'
        
        print '\nAnd after that intense recriutment and training......'    
        text2 = open('result_of_training.txt')
        print text2.read()
        
        
        print 'If you think Andela is for you...type "apply" here.'
        user_responce = raw_input('> ')
        if user_responce.lower() == 'apply':
            print 'We have sent you an email of the procedure for applying'
            print 'check your email %s' % user.email_address
            
        exit(0)
    
    

class Selector(object):
    sections = {
        'home' : Home(),
        'andela' : Andela(),
        'interview' : Interview(),
        
    }
    def __init__(self, start_section):
        self.start_section = start_section
        
    def next_section(self, section):
        return Selector.sections.get(section)
    
    def opening_section(self):
        return self.next_section(self.start_section)


start = Selector('home')
home = Welcome(start)
home.begin()
