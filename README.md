https://github.com/Fatih120/undernightinbirth/assets/18276369/c48ec7f8-b4d9-47eb-8385-b3af4233a222

# Primer on Modding UNI2

For starters, you may use https://github.com/Ekey/UNIB.Data.Tool to unpack the game successfully. Either build it yourself with [CSC.exe included with .NET 4](https://stackoverflow.com/questions/18286855/how-can-i-compile-and-run-c-sharp-program-without-using-visual-studio) and [some elbow grease](https://stackoverflow.com/questions/46320080/c-sharp-unable-to-compile-cs0103-the-name-gutils-does-not-exist-in-the-curre), or download it straight from this repo [right here, pre-built](https://github.com/Fatih120/undernightinbirth/raw/master/uni2unpacker.exe) (or after cloning). Run the program in a shell with `<input> <output>` arguments, with input being the `d` folder and output being something like `d/output` or wherever you wish. Don't know what the `d` folder is? Well, that's where the base game folder is, next to uni2.exe. Open it via Steam's game Properties -> Local Files -> Browse Local Files. 

After you have unpacked everything, you are ready to sift through and start modding in whatever ways you want.

### Resources

- To .txt files without potential issues, use an editor that can properly read and save in the Japanese SHIFT-JIS format, [such as NotepadNext](https://github.com/dail8859/NotepadNext/releases/tag/v0.6.4).
- To be able to edit quite a few files, you should get a hex editor of your choosing, [such as this one](https://mh-nexus.de/en/downloads.php?product=HxD). [ImHex](https://github.com/WerWolv/ImHex) may also suffice, among others depending on your preference.
- [Audacity v3.0.2 pre-telemetry](https://www.fosshub.com/Audacity-old.html?dwl=audacity-win-3.0.2.exe) for audio editing and getting sample times down.
- Some tools for graphics and editing data are bundled in this repo. They will be brought up per-basis.
- This entire repo! Since French Bread and ArcSys explicitly placed taboo on modding the former's games, online circles are typically avoidant of this and information is staggered. By adding findings and opening up issues and discussions on here, hopefully there can be a more accessible and helpful resource to help newcomers.

# To Edit or Add Characters

Coming from UNICLR, things are a bit different. After you've dumped all the game assets, you are able to do modifications as a "layered file system" by copying assets to the base directory, next to `uni2.exe`. Common practice in UNICLR was to put everything into an `___English` folder which housed these system folders. For the case of characters, the `data` folder housing all character data simply needs to be moved to the base directory - again, next to `d` and the game executable.

Now, simply trying to edit these copied assets will not result in the game loading these files. Hex edits to certain files in `d` are required to be "dereferenced" or dummied out, since these files tell the game where to look for assets. Within `d`, the file `hexeojmpimrjs` houses links to all the character files and folders within `data`. **Back up this file before you do anything with it.** If your hand needs to be held, you can [get this repo's copy of the dummied file](https://github.com/Fatih120/undernightinbirth/raw/master/tools/GAME/d/hexeojmpimrjs) and replace your copy with it. But for the sake of other `d` files and for reference, open up your hex editor and open the file with it.

![HxD64_2024_0130-173603](https://github.com/Fatih120/undernightinbirth/assets/18276369/25e7eaf0-1074-499b-9be7-f54588d28fec)

You will come across a view like this in your main window. Depending on your knowledge with hex, you will at least see that the ASCII pane to the right shows the names of certain folders within `data`, and scrolling down will sequentially list every file within that directory. As long as the files are properly referenced here, the game will always load the original ingame files. We must break this by simply renaming all references to these files.

![HxD64_2024_0130-173929](https://github.com/Fatih120/undernightinbirth/assets/18276369/9c2d1212-50a4-4c5b-bc96-57fb660b68d9)

In the case of HxD, you should _type to overwrite_, **NOT** delete data. If a prompt warns you're going to change the filesize, cancel and try again. You may now proceed and do this for every file and folder you see, though you _can_ just remove certain files or folders from loading if you want to be selective about it. You may save once finished and proceed to copy any remaining files from your `output` into your workspace `data` folder. If you've applied the file from the repo above, this dummies out **all** of `data`, so you **must** copy/move over all of the outputted `data` folder or the game will crash.

Usually, to add characters, one would go to `System\BtlCharaTbl.txt` and add a definition at the bottom which gives the game an internal ID for them. Then, adding more defines in the first set of values in `script\btl_Define_Chara.txt` (does `script\btl_Define_CharaNew.txt` work too?). Newly added, one can also finally add slots on the CSS using `grpdat\CSel\CSelAnim.ini` (also in `Customize`). Finally, the data would have to be set up for the new character in `data\chr<ID>`, or replacing another character's folder.

As for now, it's hard to test if your changes work when you've copied only vanilla data, so you could try and do things like copy `chr001.cg` and overwrite `chr000.cg` with it and playtest as Hyde to see if anything is wrong. Scroll down towards HA6 Editing to get started on character edits and the like.

## BGM Editing

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

# HA6 Editing

![Screenshot_20220418_222805](https://user-images.githubusercontent.com/18276369/163865043-1bcfe3e4-d31f-4de2-a9db-e3bf79efac7f.png)

Hantei-chan makes it somewhat easy to modify HA6 (Hantei 6) files to start working on modifications to UNIB and other French Bread games [note that classic Melty Blood graphics and movesets are roughly 1/3rd the size of modern games]. This document won't go over the technical details of the file format itself - only in the view of Hantei-chan itself. **Be sure to save often and make backups! A good work ethic will save you from heartaches.**

## File

**New File** - Empty File.
**Close File**  
**Load from .txt...**  
**Load HA6...** - Loads a HA6 moveset.  
**Load HA6 and Patch...**  
**Save** - You can use CTRL+S to save quicky.
**Save as...** - Saves a copy which all other saves will replace.
**Load CG...** - Loads the Character Graphic file that lets you have a visual of the edited moveset.  
**Load parts...** - Loads the .pat file for effects.  
**Load Palette...** - Loads the .pal file so you can preview colours.  
**Exit**  

When you open Hantei-chan, you're also free to use **Preferences** to change the UI colours, zooms, and an ugly filter if you wish. **Tools**, and specifically **Help > Shortcuts** may be of great use to you later

# Patterns

Patterns are individual animations that are used for every single action a character may make, such as standing still, walking, jumping, blocking, and their entire attack library including projectiles and effects. The names within the original characters are in Japanese, though you can inspect what does what by referencing a vanilla character (with their graphics if need be). But since the characters will share a majority of their default functions also based on `data/BaseData.HA6`, you can also refer to script/btl_Define.txt to view some defined constants starting at Line 990. For example you will see that all characters will use pattern 0 for their idle standing animation and 1 for their standing A attack animation.

**For a list of all the patterns' uses in UNIB, please refer to [this file on the repo](https://github.com/Fatih120/unib-data/blob/master/patterns.txt).**

When you view or create a pattern, you will see a horizontal slider with arrows to the right of it, indicating the chronological order of the pattern going left to right. This is made up of individual "frames", which you should be familiar with as the fighting game concept. It will be important to note that each frame mostly exists in a vacuum, and that every frame will have its own set of parameters. Switching the frame (which you can use the L/R arrow keys for) will change the one that you are editing, and you must account for all the differences between frames. You may click the **Animate** button to preview how the pattern would look in-game, including loops.

## Pattern Data

### Pattern name
Personal comment to briefly define the pattern. You can use any name you'd like at all, especially for specials.  
### Code name
If required, the internal association to be used for this pattern. For example, since 6B does not exist on every character, it must be manually placed somewhere in the HA6 - the code name would therefore be `6B`. More examples would be `J4C`, `41236SP`, `236EX_Hit`, and other calls.  

**PSTS**, **Level**, and **PFLG** are unknown, but are assumed to be safely ignored.

Hantei-chan lets you copy and paste entire patterns, which is good for editing similar patterns such as variations in specials or other character actions. Also, Hantei-chan is smart. It will let you copy over other patterns from different open instances of itself, so you can copy over patterns from other characters to edit (be sure to save first, though). I do not know the functions of **Push pattern copy** and **Pop all and paste**.

## State

![image](https://github.com/Fatih120/undernightinbirth/assets/18276369/66bd405c-4041-4518-8c9e-c354511042fe)

**State** mostly deals with the physical state of the character, whether they can be actionable, have a movement vector, have special qualities, etc.

### Movement Flags
Is the motion of this character changing? Slots 1, 2, 5 and 6 are the only ones to be concerned for, where _set_ applies the character's current velocity, while _add_ increments the velocity to what the character already had. For example, setting a character to 1000 will make the frame move the character 1000 units every frame. If the next frame has the _add_ flag with a value of 500, the movement will become 1500. The flags use the order of Y and X, while the values below go X and Y. Don't get confused.

### Speed
X, Y. Movement Flags need to be turned on for either-or. Sets or adds to the character's speed by this value. Note that Y **positive** means going _downwards_, so for patterns for jumps, you would want a _negative_ Y value to go up.  

### Accel
X, Y, acceleration. How many units to add each frame. Applications are - a running start/stop, gravity, a projectile that changes speed, etc.  
**Max X Speed** - Prevents _add_ flag or **Accel** from causing X to go over this limit. For example, preventing a running character's acceleration from making them gain enough speed to cross a parallel universe.

### Flagsets
TODO
#### Number of Hits
Will be elaborated in [the Attack section](###Attack).
#### ASCF
Unknown
### Player Can Move
True or False? Is the player able to cancel this frame and do anything at all such as walking around, blocking, etc? Or do they commit to this pattern/frame?  
### State
Is the character Standing, Crouching, or in the Air? Used to determine attack results, air mechanics, etc.  
### Invincibility
What is this character immune to during this frame?  
### Counterhit
Will this character be counterable during this frame? Which kind? As a rule of thumb, all _Normals_ will be a _Low Counter_, and all _Specials_ will be a _High Counter_. No change is usually put for every following frame until _Clear_ enters for the actionable recovery frames.  
### Cancels
During and after a hitbox/attack box comes out, can the character cancel into another move? For the most part, _Normals_ will always be cancellable _On Hit_ to anything, while _Specials_ will only go into other specials _On Hit_ and _Never_ into other normals. EX moves should never cancel. _On Successful Hit_ applies to moves that are NOT blocked, as opposed to any attack that isn't whiffed entirely.
### Sine Flags
Similar to Movement, using only flags 1 and 5 for Y and X.
### Sinewave
X distance, Y distance, X frequency, Y frequency. Distance = the range of movement, Frequency = speed of oscillation.
### Phases
X, Y. Starting offset of **frequencies**. Hope you remembered high school.

The Copy AS and Paste AS buttons let you quickly paste this entire section for easy editing.

## Animation

![image](https://github.com/Fatih120/undernightinbirth/assets/18276369/52e600f6-11bc-4f8f-a6a2-fd986cf9604a)

Animation deals with the visual appearance of the character during that frame, and dictates how the pattern should flow into the next frame, loop, or end.

### Layers

You can have multiple layers in a frame to use graphics with. You can add or delete more with the buttons. Similar to editing the pattern frame, the Layer you select will have all the properties below applied to this layer only. You can remove the extra layers if you won't use anything but the base 0.

### Sprite

The ID number of which sprite to use according to the CG file you're using.

### Use .pat

Using the .pat file instead? For effects.

### X, Y

Visual offset of the character.

### Blend Mode

Display the sprite normally? Or use an additive (brightening) property? Or use a subtractive (darkening) property? Mostly for effects.

### Color

Control the RGB channels, with alpha (transparency) notably included. Can help with Blend Modes.

### Rotate

X, Y, Z. Rotates the sprite. X is a vertical flip. Y is a horizontal flip. Z rotates the sprite clock-wise. Whole integers have the same result, with 0.5 being the exact "flipping" point, so use decimal values. Can make funny 3D-looking effects with this.

### Scale

X, Y. Changes the size in that dimension. For reference, MBAACC characters are roughly 1/3 the size of UNIB characters.

### Layer Priority

How high the current layer should be for this frame. Z-index.

### Rotation keeps scale set by EF

TODO which is EF teehee?

### AFJH

Not sure exactly what it does but this is important for certain moves to work properly and to do some scripts. Standardly, all frame 0s have it enabled. TODO

#### AF Params

TODO

### Frame ID

Give the frame an ID number. Important for editing and timing custom moves or doing certain things such as checking if the direction is held for a dash. TODO

### Animation Flags

Controls other ways the pattern is handled from this point. In order, Land to Pattern? is for aerial states, check loop counter is for moves that loop a certain amount of times, Go to relative offset is used in conjunction with "Go to frame" in the next part, Relative end of loop is a mix of the last two. TODO

### Animation (Goto)

What to do when the frame is done? Go to a different pattern, go to the next chronological frame, jump to a specific frame, or End the pattern? TODO

### Go to

Which Pattern or Frame to go to if using the drop-down's 1st or 3rd option.

### Landing frame

TODO

### Z-priority

TODO

### Loop N-times

TODO

### End of loop

TODO

### Duration

How many frames does this frame last for? Reminder, there are 60 frames in 1 second.

### Interpolation

TODO, I assumed this was for sprite quality but I'm unsure

As before, you can easily copy and paste entire sets of animation data. 

## Tools

Copy current frame when inserting - Disable to insert/append an empty frame instead of duplicating the current one.  
Append Frame - Places another frame at the end of the pattern.  
Insert Frame - Inserts a frame right after the current one.  
Range Tool - You can set a range of frames to paste the colour, mass-set a landing frame, copy/paste frames and paste the visual transformations for. This window can be dragged docked to the rest of the UI.  
Copy Frame   
Paste Frame  
Delete Frame

## Boxes

![image](https://github.com/Fatih120/undernightinbirth/assets/18276369/a1286459-a159-4d09-908c-85a8c51e927f)


### Attack

### Effects

### Conditions
