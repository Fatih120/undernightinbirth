# BGM Additions

To add or replace a song (for battle) in UNI2, you must grab:
- `Bgm/bgm.txt` (The file that defines the music the game will load)
- `grpdat/CSel/bgmselect.txt` (The file for changing the available songs in CSS or Training)
Copy these to your `___English` folder keeping the directory structure.

**[You can just grab this preassembled 7z from the repo if you didn't want to unpack the game, and just edit songs.](https://github.com/Fatih120/undernightinbirth/raw/master/tools/CustomBGM.7z)** Just place the `___English` folder into your game's install folder, next to uni2.exe.

1. To add a new song, add your [OGG file](https://xiph.org/vorbis/) (use [foobar2000](https://www.foobar2000.org/) or [Audacity v3.0.2 pre-telemetry](https://www.fosshub.com/Audacity-old.html?dwl=audacity-win-3.0.2.exe) to convert your own music) to the `Bgm` directory with your `bgm.txt`.
2. Open `Bgm/bgm.txt` with your text editor (it will be gibberish if you use notepad, but it may not matter, but for the best scroll up and use something like NotepadNext).
   - If you just want to replace a character's theme entirely, just find their entry among the first 25 BGMs using the table below this guide as correspondance, without doing the copypasting in the next bullet.
   - You will come across sections in the format of `[BGM_001]`, followed by File, IsLoop, and LoopPos. Copy an entire block of these four lines and append it somewhere. For battle, it's best to rename BGM_XXX starting from ID 30 - so `[BGM_030]`.
   - The `File =` line dictates which OGG to use. If your file was `my_song.ogg` in the folder, put `File = my_song` - do NOT include the `.ogg` extension or it won't work!
   - `IsLoop` defines if the song is looping or not. You will definitely want to keep this to `1` or else the song will play only once.
   - `LoopPos` defines the position in the song that the song will loop back towards once it's done, so that means your song should've NOT had an outtro and just cuts off. The point here is in Seconds with decimal values being milliseconds (Audacity can show you this position along the bottom rack).
   - Save the file. Your song will be registered in the game next time it is run. If you just wanted to replace a character's song, you can skip step 3 unless you want to rename it nonetheless.
3. Open `grpdat\CSel\bgmselect.txt`. You will see a series of: `[ID]`, `num`, and `name`. Copy and append one of these to the bottom like last time.
   - `[ID]` is the slot number in which the song appears in the Character Select Screen or in Training Mode. It's best to set it to the next last number (`[26]` in our newly-made case) as you'd have to edit all the other IDs to rearrange your song into the middle.
   - `num` is which BGM number this song uses. From Step 2, you've seen the `BGM_XXX` tag - XXX is the number you wish to use here (without leading 0s). For 30 example, you would put `num = 30`.
   - `name` is the string that appears ingame - or, the name that shows when you select the song. You likely see other entries list `<x> (<y>)` values - these are variables that are defined elsewhere in vanilla for localization purposes. Don't worry about that, as you can just set the name in plain English to whatever you would like to use. For example, just use `name = My Cool Song (Character)`

That should be all. Open your game and check to see your new cool song that's ready to use.
![image](https://github.com/Fatih120/undernightinbirth/assets/18276369/6694b680-aeaf-49be-adfb-1da1c6b3673b)


```000 = Hyde
001 = Linne
002 = Waldstein
003 = Carmine
004 = Orie
005 = Gordeau
006 = Merkava
007 = Vatista
008 = Seth
009 = Yuzuriha
010 = Hilda
011 = Eltnum
012 = Nanase
013 = Byakuya
014 = Akatsuki
015 = Chaos
016 = Wagner
017 = Enkidu
018 = Londrekia
019 = Tsurugi
021 = Mika
022 = Kaguya
023 = Kuon
024 = Phonon
```
