import sys
import traceback

class CustomException(Exception):
    """Custom Exception class to provide detailed error messages."""

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(str(error_message))
        self.error_message = self._get_error_message(error_message, error_detail)

    def _get_error_message(self, error: Exception, error_detail: sys) -> str:
        """Extracts error details such as filename, line number, and full traceback."""
        exc_type, exc_obj, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        # Capture full traceback
        full_traceback = traceback.format_exc()

        return f"Error in script [{file_name}] at line [{line_number}]: {error}\nFull Traceback:\n{full_traceback}"

    def __str__(self):
        return self.error_message
