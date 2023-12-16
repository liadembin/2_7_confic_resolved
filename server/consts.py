from typing import Optional, Tuple
SCREEN_SHOT_OUTPUT_DIR = "screenshot_dir"
SEND_SIZE = 1024 * 16
HANDLE_TYPE = Tuple[(str | bytearray), Optional[bool]] | str
GLOBAL_ERROR_CODE = "ERRR"
FILE_NOT_FOUND_ERR = "ERRR~100~File not found"
PREMMISION_DENIED_ERR = "ERRR~200~Premmision denied"
UNKNOWN_ERR = "ERRR~300~Unkown Error"
