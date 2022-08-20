# Conversion Dictionary of numbers to Words
conversionDict = {0:"",1:"One ", 2:"Two ", 3:"Three ", 4:"Four ", 5:"Five ", 6:"Six ", 7:"Seven ", 8:"Eight ", 9:"Nine ", 10:"Ten ", 
                11:"Eleven ",12:"Twelve ", 13:"Thirteen ",14:"Fourteen ",15:"Fifteen ",16:"Sixteen ",17:"Seventeen ",18:"Eighteen ",19:"Nineteen ",
                20:"Twenty ",30:"Thirty ",40:"Forty ",50:"Fifty ",60:"Sixty ",70:"Seventy ",80:"Eighty ",90:"Ninety "}

# Logic for solving Tens and Units conversion
def tensAndUnits(numNotation,postText = ""): # numNotation is the integer to convert, postText is a string to add after the number like hundred, thousand, etc
    numNotation = numNotation%100 # Just incase, get only last 2 digits of the number
    if numNotation < 1: # check if number is less than 1
        return ""
    if numNotation<20: #check if number is between 1 and 20
        return conversionDict[numNotation] + postText # Return just that and the post text
    elif numNotation>19:# If number is greater than 20
        return conversionDict[(numNotation//10)*10] + conversionDict[numNotation%10]  + postText # Return Tens part and then the Units part

# Logic for converting entire Number
def NumToWords(numNotation):
    originalNum = numNotation # Save Original Number
    lengthOfNum = len(str(numNotation)) # Get length of Number to check whether number can be converted
    txtString = ""
    if lengthOfNum < 8 and originalNum > 0: # check if number is between Lakhs and Zero
        txtString += tensAndUnits(numNotation//100000,postText="Lakh ") #Function call for Lakhs
        numNotation = numNotation-((numNotation//100000)*100000) #Remove Lakhs part from number
        txtString += tensAndUnits(numNotation//1000,postText="Thousand ") #Function call for Thousands
        numNotation = numNotation-((numNotation//1000)*1000) #Remove Thousands part from number
        txtString += tensAndUnits(numNotation//100,postText="Hundred and ") #Function call for hundreds
        txtString += tensAndUnits(numNotation%100) #Function call for Tens and Units
    if originalNum<=0: # If number is less than 0 just return Zero
        txtString = "Zero"
    return txtString

# import random
# for i in range(50):
#     print(NumToWords(random.randint(0,9999999)))
# while 1:
#     print(NumToWords(int(input("Enter a number to Check: "))))


