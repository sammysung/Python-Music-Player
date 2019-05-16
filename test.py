import time
check = ""
go = 0


def clr():
    import subprocess, os
    print("\n"*100)
    cmd = 'clear' if os.name == 'posix' else 'cls'
    subprocess.call(cmd, shell=True)
    # os.system('cls' if os.name == 'nt' else 'clear')


def ctrl():
    import threading, os, tkinter
    from tkinter import filedialog
    # import subprocess
    if os.name == 'nt':
        os.environ['PATH'] += ';C:\\Program Files\\VideoLAN\\VLC'
        # print(os.environ['PATH'])
        # subprocess.call("Start \"\" /b vlc.exe & "
        #                "timeout /T 1 /nobreak >nul & "
        #                "taskkill /IM vlc.exe /F", shell=True)
    rand = input("Do you want to pick a random track? [y/n] \n")
    dir2 = "C:/Users/start/Music"
    if rand.lower() == "y":
        direc = input("Do you want to input the path to your music, or use the default? [y/n]\nDefault: " + dir2 + "\n")
        if direc.lower() == "y":
            root = tkinter.Tk()
            #root.mainloop()
            #root.withdraw()
            dir2 = filedialog.askdirectory()
            root.destroy()
            # dir2 = input("Input the highest level directory you want to scan from: \n")
    one = threading.Thread(target=play, args=(rand, dir2,), name="Player")
    one.start()
    two = threading.Thread(target=menu, name="Menu", daemon=True)
    two.start()
    one.join()
    two.join()


# one.join()
# two.join()
# one.start()
# one.join()
# two.start()
# two.join()


# Use this one for just a specific folder (in this case, SMT3 Disc 1)

# dir = "/media/sam/Cross_Store/Music/Shin Megami Tensei III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/"

# This dir will catch all of my music

def play(rand, dir2):
    import vlc, os, random
    global check
    global go
    #rand = input("Do you want to pick a random track? [y/n] \n")
    if rand.lower() == 'y':
        # exclude = set(["Windows"])

        # Just use the fileset itself for making the files if you don't want to make a randomized list to go backward.

        fileset = []
        for path, dirs, files in os.walk(dir2):
            dirs[:] = [d for d in dirs if not d == "Windows"]
            for filename in files:
                if filename.endswith(".mp3"):
                    fileset.append(os.path.join(path, filename))

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
            #print("Index is %d" % count)
            p = ""
            p = vlc.MediaPlayer(file)
            p.play()
            time.sleep(4)
            re = 0
            while p.is_playing() == 1:
                #    if p.is_playing() == 0:
                #        break

                #    cmd = input("Do you want to [P]ause, [N]ext Track, or [S]top? Other input will check song completion. ")
                if check.lower() == "s":
                    count = le
                    break
                elif check.lower() == "h":
                    p.pause()
                    d = input("Press any key to continue playback, blank to end playback... \n")
                    #print(d)
                    #print(len(d))
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
                    #p.stop()
                    #count += 1
                    #go = 0
                    #continue
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
            #    if p.is_playing() == 0:
            #        break
            clr()
            #print("Done!")
            p.stop()
            count += 1
            if go == 0:
                print("Controls:\n[H]old, [N]ext Track, [P]revious Track, [S]top, [R]estart\nOther input is ignored.")
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
                    time.sleep(3)
                    go = 0
                else:
                    break
            elif check.lower() == 'n':
                break
            if p.is_playing() == 0:
                break
            pass
        print("Done!")
        if go == 0:
            print("Controls:\n[H]old, [N]ext Track, [P]revious Track, [S]top, [R]estart\nOther input is ignored.")
        p.stop()


def menu():
    global check
    global go
    time.sleep(1)
    while True:
        if go == 0:
            check = input("Controls:\n[H]old, [N]ext Track, [P]revious Track, "
                          "[S]top, [R]estart\nOther input is ignored.\n")
            #check = input("\nDo you want to [P]ause, [N]ext Track, or [S]top? "
            #              "Other input will check song completion. \n")
            go = 1
        else:
            continue
        #print("Check is " + check)
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
        else:
            # print("Bad input, try again!")
            go = 0


if __name__ == "__main__":
    ctrl()
