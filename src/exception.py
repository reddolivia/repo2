import sys
from logger import logging

def error_message_detail(error, error_detail: sys):
    # sys.exc_info() returns (type, value, traceback)
    # We only need the 3rd item (the traceback)
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Pass the sys module to the helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
       # Pass 'e' (the error) and 'sys' (the module)
        raise CustomException(e, sys)  



