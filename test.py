import vlc, time, os, random, threading

# Use this one for just a specific folder (in this case, SMT3 Disc 1)

# dir = "/media/sam/Cross_Store/Music/Shin Megami Tensei III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/"

# This dir will catch all of my music

dir2 = "/media/sam/Cross_Store/Music/"
rand = input("Do you want to pick a random track? [y/n] ")
if rand.lower() == 'y':
    # exclude = set(["Windows"])

    fileset = []
    for path, dirs, files in os.walk(dir2):
        dirs[:] = [d for d in dirs if not d == "Windows"]
        for filename in files:
            if filename.endswith(".mp3"):
                fileset.append(os.path.join(path, filename))

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
    while count < len(fileset):
        file = random.choice(fileset)
        print("Now playing: \n" + file)
        p = vlc.MediaPlayer(file)
        p.play()
        time.sleep(1)
        while p.is_playing() == 1:
            if p.is_playing() == 0:
                break
            cmd = input("Do you want to [P]ause, [N]ext Track, or [S]top? Other input will check song completion. ")
            if cmd.lower() == "s":
                break
            elif cmd.lower() == 'p':
                p.pause()
                d = input("Press any key to continue playback, blank to end playback... ")
                #    print(d)
                #    print(len(d))
                if len(d) != 0:
                    p.play()
                    time.sleep(1)
                else:
                    break
            elif cmd.lower() == 'n':
                print("Skipping Track!")
                p.stop()
                count += 1
                continue
            if p.is_playing() == 0:
                break
            pass
        print("Done!")
        p.stop()
        count += 1

    # This is single file mode, and single dir mode as well

    # ranfile = random.choice(os.listdir(dir))
    # file = dir + ranfile
    # p = vlc.MediaPlayer(file)

else:
    p = vlc.MediaPlayer("/media/sam/Cross_Store/Music/Shin Megami Tensei "
                    "III NOCTURNE ORIGINAL SOUNDTRACK [MP3]/Disc 1/1.23 Boss Battle.mp3")
    p.play()
    time.sleep(1)
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
        cmd = input("Do you want to [P]ause or [S]top? Other input will check song completion. ")
        if cmd.lower() == "s":
            break
        elif cmd.lower() == 'p':
            p.pause()
            d = input("Press any key to continue playback, blank to end playback... ")
    #    print(d)
    #    print(len(d))
            if len(d) != 0:
                p.play()
                time.sleep(1)
            else:
                break
        if p.is_playing() == 0:
            break
        pass
    print("Done!")
    p.stop()
