class Opportunity:
    def __init__(self,company=None,title=None,link=None,info=[]):
        self.company = company
        self.title = title
        self.link = link
        self.info = info
    def __str__(self):
        return f"|{self.company}|{self.title}|:\n{self.info}\n{self.link}\n"