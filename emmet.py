# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology 2nd Year
# Filename        : emmet.py
# Description     : main Emmet implementation
# Honor Code      : I have received help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import re                                                                                          # import RegEx im going to use it to search something in the string 

class Emmet:                                                                                       # created a class named Emmet 
    def __init__(self, raw):                                                                       # __init__ method that has the parameter self and raw 
        self.raw = raw                                                                             # takes in the value associated with parameter raw and assign it to raw 
    
    def Emmet_Method(self):                                                                        # created another method called Emmet_Method
        if re.search(r'>\+', self.raw):                                                            # if statement that search the string for a match and;
            return("Error: Unrecognized abbreviation \n")                                          # return an error when it did find the match.
        else:                                                                                      # else statement that will run if it didnt satisfy the preceding conditions
            list_Emmet = self.raw.split('+')                                                       # create another variable name list_Emmet then split the string when it sees in a plus(+)
            storage = ""                                                                           # define another variable that im going to use later
            for i in list_Emmet:                                                                   # for loop that iterate over the list_Emmet 
                if re.search('<|ul|li', i):                                                        # if statement that will findall matches and;
                    return("Error: Unrecognized abbreviation \n")                                  # return if it did find some matches
                elif '>' not in i:                                                                 # elif will run if the previous conditions were'nt true
                    storage += ("<{}> \n</{}> \n".format(i, i))                                    # adds value then assign it to storage 
                else:                                                                              # else statement that will run if it didnt satisfy both the preceding conditions
                    tab_List = i.split('>')                                                        # create a variable named tab_list then split when it sees in greater than (>)
                    begin_Tag = ['\t'*i + '<'+tags+'>' + '\n' for i, tags in enumerate(tab_List)]  # enumerate returns a counter i then multiply tabs based on i. Then concatenate all to tags 
                    end_Tag = ['\t'*i + '</'+tags+'>' + '\n' for i, tags in enumerate(tab_List)]   # same function the difference is that i created it so that the end tag is correct.
                    begin_Tag.extend(reversed(end_Tag))                                            # extends the list begin_tag then reversed the endtag 
                    storage += ''.join(begin_Tag)                                                  # joins begin tag to whatever value storage have 
                expanded_HTML = storage                                                            # join it to the storage 
            return(expanded_HTML)                                                                  # return the variable created 

    def __str__(self):                                                                             # define built in method named __str__ (to string) that will;
        return self.Emmet_Method()                                                                 # represent the return statement of the method Emmet_Method.