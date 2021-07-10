# Python code to convert into dictionary
  
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
      
# Driver Code    
tups = [("Prathusha", 10), ("Rathnakar", 12), ("Pavan", 14), 
     ("Srikanth", 20), ("Sunita", 25), ("Pavitra", 30)]
dictionary = {}
print (Convert(tups, dictionary))
