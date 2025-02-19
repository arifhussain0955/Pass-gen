# importing the necessary module  
import random                       # importing the random module  
  
# defining a function to randomly generate the password  
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
  
    # defining the list of characters that will be used to generate the password  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    # defining an empty password string  
    pass_str = ""  
  
    # creating a loop to randomly select the character from the list and insert it in the password string upto the given length  
    for i in range(len):  
        # using the random.choice() method to select a random character from the list and inserting it in the password string  
        pass_str = pass_str + random.choice(list_of_chars)  
      
    # returning the generated password string  
    return pass_str  
  
# main function  
if __name__ == "__main__":  
    # defining the length of the password  
    len = 8  
    # calling the generate_password() function and storing the returned value in a variable  
    pass_str = generate_password(len)  
    # printing the final result for the users  
    print("A randomly generated Password is:", pass_str)  