'''
You have been tasked with gathering some qualitative metrics regarding a simple text search auto-complete feature. 
You'll be given a set of documents, each having a title and a body of text.
You can assume text and queries are comprised of A-Z characters. In documents, words are separated by a space; there is no other whitespace.

Every word in the documents can be assigned a numeric score. The score is defined as follows:

Each occurrence in the title: 10
Each occurrence in the body: 1

Note that the scores should be computed across all documents.

For example, given two documents

           | Title     | Body
---------------------------------------------------
Document A | ANIMALS   | ANT ANTELOPE CAMEL CAT DOG
Document B | DOG FACTS | FURRY FURRY LOYAL

ANIMALS has a score of 10, because it appears once in a document's title
CAT has a score of 1, because it appears once in a document's body
DOG has a score of 11, because it appears once in a docurnent's body, and once in a document's title
FURRY has a score of 2, because it appears twice in a document's body

You'll then be given a set of user queries, each a string with no whitespace. 
For each query, compute the highest score among all the words that could be auto-completed from it. 
For instance, among the set of words above, the query 'AN' could be auto-completed into ANIMALS, ANT, and ANTELOPE. If no such words exist, the score is 0.

For example, given these following queries:

AN would output 10, because it can auto-complete into ANIMAL (which has a higher score than ANT and ANTELOPE)
DO would output 11, because it can auto-complete into DOG
FUR would output 2, because it can auto-complete into FURRY
ELEPH would output 0, because it cannot auto-complete into any of the words

'''

'''
The obvious data structure to write an autocomplete feature is a Trie. 
But, in this solution I wanted to take advantage of Python's powerful dictionaries to accomplish the same task. 
For every query, a temporary dictionary is created that stores each word from the documents that would autocomplete the query, mapped to the score it gives.
The final step is simple: pick the highest score among all autocompletes for that query.
'''

# helper function for input formatting
# splits the documents (strings separated by whitespace) into a list of individual strings
def splitter(listToSplit):
    
    # turns the documents into array of sublists of individual strings
    splitlist = []
    for item in listToSplit:
        splitlist.append((item.split(' ')))
    
    # last step to "flatten" all sublists into one list of strings
    itemsList = []
    for sublist in splitlist:
        itemsList.extend(sublist)
        
    return itemsList

# helper function to reset "found" dictionary for every query
def resetFound(titlesList, bodiesList):
    
    # fill a dictionary with the words in the documents
    found = {}
        
    for i in titlesList:
        found[i] = 0
        
    for j in bodiesList:
        if (j not in found):
            found[j] = 0
        
    return found

# main function -- retrieve the highest score you could get by autocompleting each query
def getAutocompleteScores(documentTitles, documentBodies, queries):
    
    scores = []
   
    titlesList = splitter(documentTitles)
    bodiesList = splitter(documentBodies)
        
    for query in queries:    # loop through every query, check for matches in documents and titles
        
        found = resetFound(titlesList, bodiesList)
        lenquery = len(query)
    
        for title in titlesList:   # check titles and look for matches to the current query
            
            lentitle = len(title)
            i = 0
            
            while (i < lenquery and i < lentitle):

                if (query[i] != title[i]):   # no match, break
                    break
                    
                while (query[i] == title[i]):   # found a match
                    
                    if (i == lenquery-1 or i == lentitle-1):
                        found[title] += 10
                        i = float('inf')
                        break
                    i+=1
           
        for body in bodiesList:      # check bodies and look for matches to the current query
            
            lenbody = len(body)
            i = 0
            
            while (i < lenquery and i < lenbody):   # found a match
                 
                if (query[i] != body[i]):   # no match, break
                    break
                    
                while (query[i] == body[i]):
                    
                    if (i == lenquery-1 or i == lenbody-1):
                        found[body] += 1
                        i = float('inf')
                        break
                    i+=1
    
        
        bestscore = 0    # retrieve the best score for this query
        
        for result in found:
            if (found[result] > bestscore):
                bestscore = found[result]
                
        scores.append(bestscore)
        
    return scores
    

# This example outputs: [11, 10, 0, 10, 1]

# Why? These are the highest scores for each query:

# power == 1 == the autocompleted "power" appears once in the Bodies
# auto == 11 == "autocomplete" yields the best score, and it appears once in the Titles and once in the Bodies (10+1)
# Python == 10 == Python appears once in the Titles, gives a score of 10. It can also be completed into Pythonista, but this only gives you 1 point, so we don't pick this
# Java == 0 == Java isn't found in Titles or Bodies
# trie == 10 == appears once in the Titles
# deb == 2 == the autocompleted "debug" appears twice in the Bodies

print(getAutocompleteScores(["Python is the way", "autocomplete", "no trie"], ["power of dictionaries", "debug", "Pythonista", "autocomplete", "debug"], 
                            ["pow", "auto", "Python", "Java", "trie", "deb"]))
