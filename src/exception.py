import sys
import logging


#function to return how the error message should look like with respect to exception
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    lineno=exc_tb.tb_lineno
    error_message="Error occured in python script name [{0}], line number [{1}], error message [{2}]".format(filename,lineno,str(error))
    return error_message

#custom exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        #overding init method. 
        super().__init__(error_message) #inheriting from exception #inheriting parent exception
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    #when exception is raised, it will print the error message.
    def __str__(self):
        return self.error_message 