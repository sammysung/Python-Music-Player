import time
check = ""
go = 0


def clr():
    import subprocess
    import os
    print("\n"*100)
    cmd = 'clear' if os.name == 'posix' else 'cls'
    subprocess.call(cmd, shell=True)
    # os.system('cls' if os.name == 'nt' else 'clear')


def ctrl():
    import threading
    import os
    import tkinter
    from tkinter import filedialog
    from pathlib import Path
    import subprocess
    # import queue
    # import multiprocessing

    global check

    # print("CPU count is: %d" % multiprocessing.cpu_count())

    if os.name == 'nt':
        os.environ['PATH'] += ';C:\\Program Files\\VideoLAN\\VLC'
        # print(os.environ['PATH'])
        subprocess.call("Start \"\" /b vlc.exe & "
                        "timeout /T 1 /nobreak >nul & "
                        "taskkill /IM vlc.exe /F", shell=True)
    rand = input("Do you want to pick a random track? [y/n] \n")
    dir2 = str(Path.home())
    dir2 += "/Music"
    if rand.lower() == "y":
        direc = input("Do you want to input the path to your music, or use the default? [y/n]\nDefault: " + dir2 + "\n")
        if direc.lower() == "y":
            # que = queue.Queue()
            # sel = threading.Thread(target=lambda q: q.put(select()), args=(que,), name="Selection Menu")
            # sel.start()
            # sel.join()
            # dir2 = que.get()
            # check = "Done"
        #else:
            # check = "Done"

            root = tkinter.Tk()
            root.wm_attributes('-topmost', 1)
            # root.mainloop()
            root.withdraw()
            root.update()
            dir2 = filedialog.askdirectory(initialdir=dir2)
            root.update()
            root.destroy()
            # dir2 = input("Input the highest level directory you want to scan from: \n")
    # while check != "Done":
    #    pass
    one = threading.Thread(target=play, args=(rand, dir2,), name="Player")
    one.start()
    two = threading.Thread(target=menu, name="Menu", daemon=True)
    two.start()
    one.join()
    two.join()

# Use this one for just a specific folder (in this case, SMT3 Disc 1)

# dir = "/media/sam/Cross_Store/Music/Shin Megami Tensei III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/"


def play(rand, dir2):
    import vlc
    import os
    import random
    global check
    global go
    # rand = input("Do you want to pick a random track? [y/n] \n")
    if rand.lower() == 'y':
        # exclude = set(["Windows"])

        # Just use the fileset itself for making the files if you don't want to make a randomized list to go backward.

        fileset = []
        for path, dirs, files in os.walk(dir2):
            dirs[:] = [d for d in dirs if not d == "Windows"]
            for filename in files:
                if filename.endswith(".mp3"):
                    fileset.append(os.path.join(path, filename))

        # If you do want to go backwards, though, this will shuffle for you, and use the index to control playback.

        # i = 0
        le = len(fileset)
        # lis = []
        lis = fileset
        random.shuffle(lis)

        # This is shuffling "by hand", but it has a lot of repeats possible. Don't use if you don't have to.

        # while i < le:
        #    lis.append(random.choice(fileset))
        #    i += 1

        # This way works well enough if you don't care to be picky with your subdirectories

        # files = [os.path.join(path, filename)
        #         for path, dirs, files in os.walk(dir2):
        #        dirs[:] = [d for d in dirs if not d == "Windows"]
        #         for filename in files
        #         if filename.endswith(".mp3")]
        # file = random.choice(fileset)
        # print("Now playing: \n" + file)
        # p = vlc.MediaPlayer(file)

        count = 0
        re = 0
        file = ''
        print(le)
        while count < le:
            if re == 0:
                # file = random.choice(fileset)
                file = lis[count]
            print("\nNow playing: \n" + file)
            print("Track %d of %d" % (count+1, le))
            #p = ""
            #p = vlc.MediaPlayer(file)

            p = vlc.Instance()
            m = p.media_new(file)
            p = m.player_new_from_media()

            p.play()

            m.parse()
            print("\nSong Info:")
            if m.get_meta(0) is not None:
                print("Title: " + m.get_meta(0))
            else:
                print("Title: None")
            if m.get_meta(1) is not None:
                print("Artist: " + m.get_meta(1))
            else:
                print("Artist: None")
            if m.get_meta(4) is not None:
                print("Album: " + m.get_meta(4))
            else:
                print("Album: None")
            if m.get_meta(4) is not None:
                print("Track: " + m.get_meta(5)+"\n")
            else:
                print("Track: None")

            time.sleep(4)
            re = 0
            while p.is_playing() == 1:
                #    if p.is_playing() == 0:
                #        break

                #cmd = input("Do you want to [P]ause, [N]ext Track, or [S]top? Other input will check song completion. ")
                if check.lower() == "s":
                    count = le
                    break
                elif check.lower() == "h":
                    p.pause()
                    d = input("Press any key to continue playback, blank to end playback... \n")
                    # print(d)
                    # print(len(d))
                    check = ""
                    if len(d) != 0:
                        p.play()
                        time.sleep(1)
                        go = 0
                    else:
                        break
                elif check.lower() == "n":
                    if count == le - 1:
                        print("Already at the end. Playing first track...")
                        count = -1
                        break
                    check = ""
                    print("Skipping Track!")
                    # p.stop()
                    # count += 1
                    # go = 0
                    # continue
                    break
                elif check.lower() == "r":
                    re = 1
                    check = ""
                    count -= 1
                    break
                elif check.lower() == 'p':
                    if count == 0:
                        print("Already at beginning. Playing last track...")
                        count = le - 2
                        break
                    print("Going back one track!")
                    check = ""
                    count -= 2
                    break
                elif check.lower() == 'i':
                    # p.pause()
                    d = input("Enter in the number of the track you want to play.\n"
                              "Example: `201` for the 201st track\n")
                    try:
                        num = int(d)
                        if num > 0 and num < le:
                            num -= 2
                            check = ""
                            count = num
                            go = 1
                            break
                        else:
                            print("Number out of range, try again!")
                            continue
                    except ValueError:
                        print("Not an int, try again!")
                        continue
                    # print(d)
                    # print(len(d))
            #    if p.is_playing() == 0:
            #        break
            clr()
            # print("Done!")
            p.stop()
            count += 1
            if go == 0:
                print("Controls:\n[H]old, [N]ext Track, [P]revious Track, [S]top, [R]estart, [I]ndex"
                      "\nOther input is ignored.")
            go = 0
            time.sleep(1)

    # This is single file mode, and single dir mode as well

    # ranfile = random.choice(os.listdir(dir))
    # file = dir + ranfile
    # p = vlc.MediaPlayer(file)

    else:
        p = vlc.MediaPlayer("/media/sam/Cross_Store/Music/Shin Megami Tensei "
                            "III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/1.23 Boss Battle.mp3")
        p.play()
        time.sleep(3)
        print("\nNow playing: \n/media/sam/Cross_Store/Music/Shin Megami Tensei "
                            "III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/1.23 Boss Battle.mp3")
        # g = p.get_state()
        # print(g)
        # t = p.audio_get_track_count()
        # y = p.audio_get_track()
        # h = p.is_playing()
        # print(t)
        # print(y)
        # print(h)

        while p.is_playing() == 1:
            if p.is_playing() == 0:
                break
            if check.lower() == "s":
                break
            elif check.lower() == 'h':
                p.pause()
                d = input("Press any key to continue playback, blank to end playback... \n")
                check = ""
                #    print(d)
                #    print(len(d))
                if len(d) != 0:
                    p.play()
                else:
                    time.sleep(3)
                    go = 0
                    break
            elif check.lower() == 'n':
                break
            if p.is_playing() == 0:
                break
            pass
        print("Done!")
        if go == 0:
            print("Controls:\n[H]old, [N]ext Track, [P]revious Track, [S]top, [R]estart, [I]ndex"
                  "\nOther input is ignored.")
        p.stop()


def menu():
    import sys
    global check
    global go
    time.sleep(1)
    while True:
        if go == 0:
            print("Controls:\n[H]old, [N]ext Track, [P]revious Track, [S]top, [R]estart, [I]ndex"
                  "\nOther input is ignored.\n", end = ' ')
            sys.stdout.flush()
            check = sys.stdin.readline().rstrip()
            go = 1
        else:
            continue
        # print("Check is " + check)
        time.sleep(0.1)
        if check.lower() == "s":
            print("Outta here!")
            break
        elif check.lower() == "p":
            continue
        elif check.lower() == "h":
            continue
        elif check.lower() == "r":
            continue
        elif check.lower() == "n":
            continue
        elif check.lower() == "i":
            continue
        else:
            # print("Bad input, try again!")
            go = 0


# This method is unused since OSX really does not like UI operations in non-main threads, for whatever reason.
# Might work fine for other OSs, yet to try it.
# Will create the directory picker in its own thread.


def select():
    import tkinter
    from tkinter import filedialog
    root = tkinter.Tk()
    # root.mainloop()
    root.withdraw()
    # root.update()
    dir2 = filedialog.askdirectory()
    # root.update()
    root.destroy()
    return dir2


if __name__ == "__main__":
    ctrl()
