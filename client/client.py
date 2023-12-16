import socket
import sys
import traceback
from client_custom_exceptions import DisconnectErr, DisconnectRequest
from menu import menu

# from __ import * ruins LSP.
from client_handlers import *

import logging

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
logger.propagate = True


def main(ip: str) -> None:
    """
    main client - handle socket and main loop
    """
    connected = False
    global sock
    sock = socket.socket()
    port = 7777
    try:
        sock.connect((ip, port))
        print(f"Connect succeeded {ip}:{port}")
        connected = True
    except Exception:
        print(f"Error while trying to connect.  Check ip or port -- {ip}:{port}")

    while connected:
        from_user = menu()
        client_args = from_user[-1]
        to_send = protocol_build_request(from_user[:2])
        if to_send == "":
            print("Selection error try again")
            continue
        try:
            handle_msg(sock, to_send, client_args)
        except DisconnectRequest as e:
            break
        except socket.error as err:
            if err.errno == 10053:  # win err 10053: connection was aborted
                print("The server is now closed so cant connect to it")
            else:
                print(f"Got socket error: {err}")
            break
        except Exception as err:
            print(f"General error: {err}")
            print(traceback.format_exc())
            break

    print("Bye")
    sock.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("127.0.0.1")
