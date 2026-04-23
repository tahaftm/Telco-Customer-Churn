import sys

def get_error_details(error_message, sys_mod:sys):
    _,_,tb = sys_mod.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    return f"There is a error in {file_name}, on line number {tb.tb_lineno} and the message is: {str(error_message)}"

class CustomException(BaseException):
    def __init__(self,error_message, sys_module):
        self.error_message = get_error_details(error_message, sys_module)
    def __str__(self):
        return self.error_message