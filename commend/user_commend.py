from common.common_def import COMMEND_LIST


def get_user_commend() -> str:
    while True:
        commend = input('Please input commend: ')
        cmd = commend.lower()
        if cmd not in COMMEND_LIST:
            print(f"{cmd} is not a valid commend")
        else:
            return cmd
        