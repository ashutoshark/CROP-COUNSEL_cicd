# handling exception 
# coustom fuction and common for every python projects 
# it can be found in documentation of python exception handling it self 
import sys
import logging

def error_message_detail(error,error_detail:sys):
    file_name=exc_tb.tb_frame.f_code.co_filename
    # it gives us there parameters we are intrested only in last one
    _,_,exc_tb=error_detail.exc_info()
    error_message="Error occured in python script name [{0}] line number[{1}] error message[{3}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
    
class CustomExcepiton(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message    

# testing the excepition handling code
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divided by zero error")
#         raise CustomExcepiton(e,sys)
  