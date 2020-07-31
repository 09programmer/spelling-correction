
################ follow @09programmer on facebook ################

from textblob import TextBlob                  # install libraries

file=open("programmer.txt", "r+")         # open file in read mode 
a=file.read()                      

print("original text : "+str(a))              #print original text

b=TextBlob(a)                   #convert the data type of textblob                  
print("corrected text : "+str(b.correct())) # print corrected text

file.close()                                           #close file

d=open("programmer.txt","w")             # open file in write mode
d.write(str(b.correct()))                            # update file
d.close()                                              #close file

################ follow @09programmer on facebook ################