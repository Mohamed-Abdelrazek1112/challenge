import webhandler

class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        # TODO: add your code here
         def Roman(query):
            romanNumeral = (('M',  1000),('CM', 900),('D',  500),('CD', 400),('C',  100),('XC', 90),('L',  50),('XL', 40),('X',  10),('IX', 9),('V',  5),('IV', 4), ('I',  1))
            def NTOROMAN(n):
                n=int(n)
                result = ""
                for num, integer in romanNumeralMap:
                    while n >= integer:
                        result += numeral
                        n -= integer
                return result
            def ROMANTON(string):
                result = 0
                index = 0
                for num, integer in romanNumeralMap:
                    while s[index:index+len(numeral)] == numeral:
                        result += integer
                        index += len(numeral)
                return result
            tokens=query.split(" ")
            for i in range(len(tokens)):
                if tokens[i] not in ["+","*","-","//"]:
                    token = ROMANTON(tokens[i])
            result=0
            for i in range(len(tokens)):
                if tokens[i] in ["+","*","-","//"]:
                    if token[i]=="+":
                        result = token[i-1]+token[i+1]
                    elif token[i]=="-":
                        result = token[i-1]-token[i+1]
                    elif token[i]=="*":
                        result = token[i-1]*token[i+1]
                    else:
                        result = token[i-1]//token[i+1]

            return NTOROOMAN(result)
        return 85
