# Python-Music-Player
A test music player for learning how to use Python with a (somewhat silly) real world application.

# Usage
Simply call "test.py" using Python 3, like so:

`python3 test.py`

Follow however you have it set up to actually call Python 3.
 
This code does **not** work with Python 2

Command line arguments and a GUI are tentatively planned, but are not
yet available.

At the moment, looks for `.MP3` files exclusively. Also passes over 
directories named "*Windows*" and any sub-directories within them; this is
a personal workaround for my music library, you can remove it if needed.

# Platforms

So far, the x86-64 platforms tested have been:

- Windows 10 (1803) 

- Ubuntu 19.04 

- OSX 10.13.6 

- Windows 8 *(not 8.1, and minimally)* 

These are confirmed working, both from a properly configured PyCharm 
setup and the native terminals/CMD/PowerShell available to each system.

Also, with the proper configuration (info listed down below), you can 
also run this in the Bash on Windows Subsystem environment, if this is
something you want/need.

# Dependencies

You must install the following programs to get this running:

- VLC 

- Python 3 (tested with 3.7.3, specifically)

- Tkinter (part of Python)

# OS Notes

## Linux 

Ensure that you install the `python3-tk` package so you can have the
tkinter directory picking function and eventually (maybe) the whole GUI.

Other than that, the heart of the program was made on Linux, so most
issues have been ironed out to my knowledge.

## OSX

You may have to forgo [Homebrew](https://brew.sh/) python3 installation 
if you have trouble with Tkinter and use the `.pkg` offered from the 
python homepage, though you should try Homebrew first.

You cannot make UI threads in non-main methods for OSX (may be true for 
other OSs as well, I'm not sure), so `select()` is useless here, even if
you'd rather use it.

Tkinter will also crash if you have an open `raw_input` or `input` 
function in a different thread when you call it, so the technique used 
in `menu()` is to get around this.

## Windows

From a fresh boot, you must at least run VLC once to get the library to 
load; there is a Windows-specific command programmed in to open and 
immediately close it to avoid this issue for now.

There is a **LOT** of extra output in the PyCharm terminal for WSAPI 
calls that seemingly failed; these don't affect anything from what I can
tell, and finding info on this issue has been fruitless. If you happen 
to know why this happens or a way to fix it, please let me know!

## Windows Subsystem for Linux

This one is tricky; for starters, follow the Linux notes above, 
you'll need it to run anything.

After that, you've got a lot of work ahead of you; keep in mind that
this version of Linux is not at all intended to have GUI support, and 
future audio support is an afterthought at best.

First off, read through the replies on 
[this askubuntu thread](https://askubuntu.com/questions/993225/whats-the-easiest-way-to-run-gui-apps-on-windows-subsystem-for-linux-as-of-2018)
about the ways around the GUI limitations, and pick what works best for 
you. I personally used VcXsrv (though I tested both), and keep in mind
that you need to start the XLaunch server one way or the other before
you expect any GUI apps to work.

Next, [this great guide here](https://research.wmz.ninja/articles/2017/11/setting-up-wsl-with-graphics-and-audio.html)
was able to get audio working through a server setup on Windows proper 
and a slightly modified version of PulseAudio on the WSL side. If you 
are on Ubuntu 16.04, you can use the PPA method listed, but if you don't
use Ubuntu or updated, you must modify and make PulseAudio from source
in the WSL environment.

Once this all is done, and you have both VcXsrv and PulseAudio running
on Windows proper, you can run the code, which will pass all of the 
misbehaving audio/GUI functions with minimal fuss. You can ignore the 

`shared memfd open() failed: Function not implemented`

message; it is not fatal, and does not hinder playback.