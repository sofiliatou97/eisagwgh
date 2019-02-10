import re
def comment_remover(string):
    pattern = r"(\".*?\"|\'.*?\')|(#[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
   
    def _replacer(match):
        if match.group(2) is not None:
            return "" 
        else: 
            return match.group(1) 

    return regex.sub(_replacer, string)

try:
    commentedFile = raw_input("File name: ")
except:
    quit()

fileForProcess = open(commentedFile,"r")
lines = fileForProcess.readlines()
fileForProcess.close()
fileForProcess = open(commentedFile,"w")

fileLines = ''.join(lines)
try:
    fileForProcess.write(comment_remover(fileLines))
except:
    pass
fileForProcess.close()


