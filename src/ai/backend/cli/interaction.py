import ipaddress
import os


def ask_host(prompt: str, default: str = "127.0.0.1") -> str:
    try:
        default = default.replace("localhost", "127.0.0.1")
        _ = ipaddress.ip_address(default)
    except ValueError:
        raise ValueError("IP host must be given as 127.0.0.1")

    while True:
        user_reply = input(f"{prompt}(default: {default}): ")
        if user_reply == "":
            user_reply = default
        try:
            _ = ipaddress.ip_address(user_reply)
            break
        except ValueError:
            print("Please input correct host.")
    return user_reply


def ask_number(prompt: str, default: int = 0, min_value: int = 0, max_value: int = 0) -> int:
    try:
        port = default
    except ValueError:
        raise ValueError("Default value must be given as integer")

    while True:
        user_reply = input(f"{prompt}(default: {default}): ")
        if user_reply == "":
            return port
        try:
            if user_reply.isdigit() and min_value <= int(user_reply) <= max_value:
                port = int(user_reply)
                break
        except ValueError:
            print(f"Please input correct number between {min_value}~{max_value}.")
    return port


def ask_string(prompt: str, default: str = "", use_default: bool = True) -> str:
    while True:
        if use_default:
            user_reply = input(f"{prompt}(default: \"{default}\"): ")
            if user_reply == "":
                return default
            return user_reply
        else:
            user_reply = input(f"{prompt}(if you don\'t want, just leave empty): ")
            return user_reply


def ask_string_in_array(prompt: str, default: str = "", choices: list = None):
    if choices is None:
        choices = []
    while True:
        user_reply = input(f"{prompt}(choices: {','.join(choices)}): ")
        if user_reply == "":
            user_reply = default
        if user_reply.lower() in choices:
            break
        else:
            print(f"Please answer in {','.join(choices)}.")
    return user_reply


def ask_file_path(prompt: str):
    while True:
        user_reply = input(f"{prompt}: ")
        if os.path.exists(user_reply):
            break
        print("Please answer a correct file path.")
    return user_reply


def ask_yn(prompt: str = 'Are you sure?', default: str = 'y') -> bool:
    if default == 'y':
        choices = 'Y/n'
    elif default == 'n':
        choices = 'y/N'
    else:
        raise ValueError("default must be given either 'y' or 'n'.")
    while True:
        user_reply = input("{0} [{1}] ".format(prompt, choices)).lower()
        if user_reply == '':
            user_reply = default
        if user_reply in ('y', 'yes', 'n', 'no'):
            break
        else:
            print("Please answer in y/yes/n/no.")
    if user_reply[:1].lower() == 'y':
        return True
    return False


def ask_tf(prompt: str = 'Are you sure?', default: str = 'true') -> bool:
    if default == 't':
        choices = 'T/f'
    elif default == 'f':
        choices = 't/F'
    else:
        raise ValueError("default must be given either 'true' or 'n'.")
    while True:
        user_reply = input(f"{prompt} [{choices}] ").lower()
        if user_reply == '':
            user_reply = default
        if user_reply in ('t', 'true', 'f', 'false'):
            break
        else:
            print("Please answer in t/true/f/false.")
    if user_reply[:1].lower() == 't':
        return True
    return False
