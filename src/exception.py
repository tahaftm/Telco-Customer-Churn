import sys

def get_error_details(error_message,error_details):
    _,_,tb = error_details.exc_info()
    return f"Unfortunately error occured in file: {tb.tb_frame.f_code.co_filename} on line number: {tb.tb_lineno}, the error is : {str(error_message)} "

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = get_error_details(error_message,error_details)
    def __str__(self):
        return self.error_message