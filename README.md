https://github.com/Fatih120/undernightinbirth/assets/18276369/c48ec7f8-b4d9-47eb-8385-b3af4233a222

# Primer on Modding UNI2

For starters, you may use https://github.com/Ekey/UNIB.Data.Tool to unpack the game successfully. Either build it yourself with [CSC.exe included with .NET 4](https://stackoverflow.com/questions/18286855/how-can-i-compile-and-run-c-sharp-program-without-using-visual-studio) and [some elbow grease](https://stackoverflow.com/questions/46320080/c-sharp-unable-to-compile-cs0103-the-name-gutils-does-not-exist-in-the-curre), or download it straight from this repo [right here, pre-built](https://github.com/Fatih120/undernightinbirth/raw/master/uni2unpacker.exe) (or after cloning).

Run the program in a shell ([Command Prompt on Windows](https://www.wikihow.com/Run-a-Program-on-Command-Prompt#Run-Other-Programs)) with `<input> <output>` arguments: Input being the `d` folder, and output being somewhere accessible such as `./d/output`. Don't know what the `d` folder is? Well, that's where the base game folder is, next to `uni2.exe`. Open it via Steam's game Properties -> Local Files -> Browse Local Files. 

After you have unpacked everything, you are ready to sift through and start modding in whatever ways you want.

### Resources

- Tools for graphics and editing data are bundled in this repo, specifically in the [tools directory](https://github.com/Fatih120/undernightinbirth/tree/master/tools). They will be brought up per-basis, but **you should want to get hanteichan_2.1.666.exe** (ignore the scary name).
- To edit `.txt` files without potential issues, use an editor that can properly read and save in the Japanese **SHIFT-JIS** format, [such as NotepadNext](https://github.com/dail8859/NotepadNext/releases/tag/v0.6.4).
- To be able to edit certain files, you should get a hex editor of your choosing, [such as HxD](https://mh-nexus.de/en/downloads.php?product=HxD). [ImHex](https://github.com/WerWolv/ImHex) may also suffice, among others depending on your preference.
- [Audacity v3.0.2 pre-telemetry](https://www.fosshub.com/Audacity-old.html?dwl=audacity-win-3.0.2.exe) for audio editing and getting sample times down.
- This entire repo!
- - Since French Bread and ArcSys explicitly placed taboo on modding the former's games, online circles are typically avoidant of this and information is staggered. By adding findings and opening up issues and discussions on here, hopefully there can be a more accessible and helpful resource to help newcomers.

# To Edit or Add Characters

We are able to set up new characters without modifying the base game's data. You could do this from scratch, but if you're new, you should copy an existing character so you don't have to be worried about requirements and oddities you're unaware of. Alternatively, you can modify existing characters or write over their slots - however, this will require internal edits and copying over mass data. If you'd like the former, read the following - if you'd like the latter, skip below to the "Dereferencing" section.

### The very short of it for copying a character to a new slot:

1. Copy a `chrXXX` character from `./output/data/`. Move it into `./data/` (or create the same folder structure as seems fit).
2. Rename the folder to a new slot greater than 024, such as `025`. Do the same with the files inside using that same number, including the `lst`, `pal`, `txt`s, etc.†
4. Open `chrXXX_mv_0.txt` in your specialized editor. Jump to the end and find the two last written lines - `CHRXXX_MoveTable <- Battle_Std.MakeMoveTable( t, CHRXXX_CommandTable, Def_ChrNo_YYY );` and `__dofile__("./chrXXX_se_category.txt");`. Edit these lines to have your IDs accordingly.
5. Open `chrXXX_0.txt`, and change the references to XXX in the same way. Open `chrXXX_cmd_0.txt`,  and change the references to XXX in the same way. _(Optionally for quick-start?)_ Open the two `chr025_se_*` files and change the references accordingly.
6. Find `./output/script/btl_Define_CharaNew.txt`. Copy it to `./___English/script` or `./script`.
7. Open your copy and append the line `const Def_ChrNo_ChrXXX = XXX;` using the same number you chose. Also add the line `const Def_ChrNo_YYY = XXX;`, with Y preferably being a 3-letter identifier for the character.
8. Find `./output/System/BtlCharaTbl.txt`. Copy it to `./___English/script` or `./script`.
9. Scroll to the bottom and append a `chara_no[XXX]` by templating one of the previous entries, making sure to have `name_short = "chrXXX";` and a unique `order`.

† _You _are_ able to use different naming conventions for certain files to make them easily readable, such as whatever is defined in `chrXXX_0.txt`, but be sure your character loads this way first as I haven't fully figured out what can be changed._

You should now be able to go to training mode and see a new slot, which should be playable with your setup without internal edits. You can make the character accessible on the CSS and in other areas through folders such as `grpdat`'s `CharaColorBar`, `CSel`, `Cockpit`, etc. If you just want to edit this extra slot without the baggage of touching vanilla characters, skip the next section and head down for the guide on character edits and using Hantei-chan.

### Dereferencing for edits

Coming from UNICLR, things are a bit different. After you've dumped all the game assets, you are able to do modifications as a "layered file system" by copying assets to the base directory, next to `uni2.exe`. Common practice in UNICLR was to put everything into an `___English` folder which housed these system folders. For the case of characters, the `data` folder housing all character data simply needs to be moved to the base directory - again, next to `d` and the game executable.

Now, simply trying to edit these copied assets will not result in the game loading these files. Hex edits to certain files in `d` are required to be "dereferenced" or dummied out, since these files tell the game where to look for assets. Within `d`, the file `hexeojmpimrjs` houses links to all the character files and folders within `data`. **Back up this file before you do anything with it.** If your hand needs to be held, you can [get this repo's copy of the dummied file](https://github.com/Fatih120/undernightinbirth/raw/master/tools/GAME/d/hexeojmpimrjs) and replace your copy with it. But for the sake of other `d` files and for reference, open up your hex editor and open the file with it.

![HxD64_2024_0130-173603](https://github.com/Fatih120/undernightinbirth/assets/18276369/25e7eaf0-1074-499b-9be7-f54588d28fec)

You will come across a view like this in your main window. Depending on your knowledge with hex, you will at least see that the ASCII pane to the right shows the names of certain folders within `data`, and scrolling down will sequentially list every file within that directory. As long as the files are properly referenced here, the game will always load the original ingame files. We must break this by simply renaming all references to these files.

![HxD64_2024_0130-173929](https://github.com/Fatih120/undernightinbirth/assets/18276369/9c2d1212-50a4-4c5b-bc96-57fb660b68d9)

In the case of HxD, you should _type to overwrite_, **NOT** delete data. If a prompt warns you're going to change the filesize, cancel and try again. You may now proceed and do this for every file and folder you see, though you _can_ just remove certain files or folders from loading if you want to be selective about it. You may save once finished and proceed to copy any remaining files from your `output` into your workspace `data` folder. If you've applied the file from the repo above, this dummies out **all** of `data`, so you **must** copy/move over all of the outputted `data` folder or the game will crash.

Usually, to add characters, one would go to `System\BtlCharaTbl.txt` and add a definition at the bottom which gives the game an internal ID for them. Then, adding more defines in the first set of values in `script\btl_Define_Chara.txt` (does `script\btl_Define_CharaNew.txt` work too?). Newly added, one can also finally add slots on the CSS using `grpdat\CSel\CSelAnim.ini` (also in `Customize`). Finally, the data would have to be set up for the new character in `data\chr<ID>`, or replacing another character's folder.

As for now, it's hard to test if your changes work when you've copied only vanilla data, so you could try and do things like copy `chr001.cg` and overwrite `chr000.cg` with it and playtest as Hyde to see if anything is wrong. Scroll down towards HA6 Editing to get started on character edits and the like.

# Audio

https://github.com/Fatih120/undernightinbirth/blob/master/AUDIO.md

# Character Structure

     File | Use | Notes
-- | - | -
chrXXX_0.TXT | "Header" File (0) | Declare the name of certain files with this. Allows renaming the HA6, CG and PAT file. Unknown if multiple included files will work. Renamable(?)
chrXXX.HA6 | Hantei6 Pattern (ha6) | Includes all of the basic character data in collections of "patterns", elaborated in the section below - hitboxes, frame data, movement, attack info - lots can be done with this single file and it will have most of your edits. Open this using **Hantei-chan**. **Renamable.**
chrXXX_mv_0.TXT | "Move" Code File (mv) | Includes technical functions that get hooked onto patterns/moves, allowing for elaborate attacks and complex mechanics. The butter to the **HA6**'s bread. UNI2 uses [Squirrel lang](http://squirrel-lang.org/), which is C-like.
chrXXX_cmd_0.TXT | "Command" File (cmd) | Defines what inputs/moves the character can do, along with the Smart Steer definition. Can also have some code that wouldn't belong in mv.
chrXXX_sc_0.TXT | Battle Stats | Defines specific stats like attack/GRD modifiers, and HP.
chrXXX.CG | Character Graphics (cg) | The package holding all of the character's own sprites. Can be extracted or built using the included `cgtool` library in the repo. **Renamable.**
chrXXX.PAL | Palette File (pal) | Colour information for palette selection. Sprites are [Indexed](https://en.wikipedia.org/wiki/Indexed_color) so they must use this for colours. TODO: how to palette
chrXXX.PAT | Pattern File (pat) | Includes all of the character effect graphics and definitions. Must be hex edited to inject (TODO: GUIDE), but use of **ha6chan_pat_editor** can change the "patterns" somewhat.
chrXXX_com_0.txt, chrXXX_com_ranking_0.txt | COM AI Files |
chrXXX_se_category.txt, chrXXX_se_list.txt | Sound Effect Definitions | `./se` |
chrXXX.lst | List File | Useless |
_temp.ha6, _temp.lst | Temp | Useless |
BaseData.lst | Base Data List | `../BaseData.ha6` |

# HA6 Editing

_Note: if you're confused on the three Hanteichan executables, **just focus on v2.1.666 as your main editor**. v2.2.1 includes the ability to copy patterns and data between instances of itself, but is prone to crashing often. pat_editor is not made to edit HA6s._

![Screenshot_20220418_222805](https://user-images.githubusercontent.com/18276369/163865043-1bcfe3e4-d31f-4de2-a9db-e3bf79efac7f.png)

Hantei-chan makes it somewhat easy to modify HA6 (Hantei 6) files to make modifications to UNI2 and other French Bread games. If you would like to edit frame data, box data, effects, attack stats, visuals, and many things far and between, this is what will you get started to bend the Hollow Night to your will.

**Like with all projects, be sure to save often and make backups. A good work ethic will save you from heartaches and lost time. HA6 is a powerful tool, but one that you must get used to and be careful with. There is no typical undoing.**

### File

**New File** - Empty File.
**Close File**  
**Load from .txt...** - Can load a whole character from `chrXXX_0.txt`   
**Load HA6...** - Loads a .HA6 moveset file.  
**Load HA6 and Patch...** -  
**Save** - Save changes. You can use CTRL+S to save quicky.  
**Save as...** - Saves a copy, and `Save`s to it from now on.  
**Load CG...** - Loads the Character Graphic file for a visual of the character.  
**Load parts...** - Loads the .pat file for move effects.  
**Load Palette...** - Loads the .pal file so you can preview colours.  
**Exit** - Close program.  

When you open Hantei-chan, you're also free to use **Preferences** to change the UI colours and other properties. **Tools**, and specifically **Help > Shortcuts** may be of great use to you later.

## Patterns

Patterns are individual animations that are used for every single action a character may make, such as standing still, walking, jumping, blocking, along with their arsenal of attacks - including seperated projectiles and effects. The pattern names within the vanilla characters are in Japanese, though you can inspect what does what by simply examining the frames along with their graphics. Since the characters will share a majority of their default functions also based on `./data/BaseData.HA6`, you can therefore refer to `./script/btl_Define.txt` to view some defined constants starting at Line 1150. For example, you will see that all characters will use Pattern #0 for their idle standing animation, and #1 for their standing A attack animation.

**For a list of all the patterns' uses in UNIB, please refer to [this file on the repo](https://github.com/Fatih120/unib-data/blob/master/patterns.txt).**

When you view or create a pattern, you will see a horizontal slider with arrows to the right of it, indicating the chronological order of the pattern going left to right. This is made up of individual "frames", which you should be familiar with as the fighting game concept (though each frame can have varied lengths of time). It will be important to note that each frame mostly exists in a vacuum, and that every frame will have its own set of parameters. Switching the frame (which you can use the L/R arrow keys for) will change the one that you are editing, and you must account for all the differences between frames. You may click the **Animate** button to preview how the pattern would look in-game, including loops.

From hereon out, we will refer to all the changes in the drop-downs that we can make section-by-section, and inform on what each entry can do.

## Pattern Data

Basic information and definitions on the pattern.

| Label | Function |
|--|--|
| Pattern Name | Personal comment - you can use it to name the pattern. Any name can be used at all, like for naming specials. |
| Code Name | If required, the internal association to be used for this pattern. For example, 6B is not a move that exists on characters by default, so `6B` must be placed as a code name for the move to be available. More examples would be `J4C`, `41236SP`, `236EX_Hit`, 0202A, etc. |
| PSTS, Level, PFLG | Unknown, ignorable.

Hantei-chan lets you copy and paste entire patterns, which is good for editing similar patterns such as variations in specials.

Hantei-chan v2.2.1 will let you copy over other patterns from different open instances of itself, so you can copy over patterns from other characters to edit, but as per the warning above, it is unstable and you should make backups often. Not sure what **Push pattern copy** and **Pop all and paste** are.

## State

![image](https://github.com/Fatih120/undernightinbirth/assets/18276369/66bd405c-4041-4518-8c9e-c354511042fe)

**State** mostly deals with the physical state of the character - whether they can be actionable, have a 2D movement vector, gain special qualities, etc.

### Movement

| Label | Function |
|--|--|
| Movement Flags | Is the motion of this character changing? Flags 1, 2, 5 and 6 are the only ones to be concerned for, where _set_ applies the character's current velocity, while _add_ increments the velocity to what the character already had. For example, setting a character to 1000 will make the frame move the character 1000 units every frame. If the next frame has the _add_ flag with a value of 500, the movement will become 1500. The flags here use the order of Y and X, while the **four values below go X and Y**. Don't get confused.
| Speed | X, Y. Movement Flags required. Sets or adds to the character's speed by this value. Note that Y **positive** means going _downwards_, so for patterns for jumps/going up, you would want a _negative_ Y value. |
| Accel | X, Y. Acceleration, flags required. How many units to add, *each frame*. Applications are - a running start/stop, gravity, a projectile that changes speed, etc. |

#### Flagset 1
Values increase left-to-right, top to bottom. Lots of these are unknown or obsolete. Can be used manually.

| ID | Label | Function |
|--|--|--|
| 0 |  | |
| 1 |  | |
| ... | | |
TODO

#### Flagset 2

| ID | Label | Function |
|--|--|--|
| 0 | Can always EX cancel |  Determines if the frame allows to be stopped by Chain Shift or an EX move. The game will know if it's an EX move and won't allow it to be cancelled by other EX moves.  |
| 1 | UNK2 |
| 2 | Can only Jump Cancel | Obselete.
| 3 | UNK4 |
| 4 | Unknown. | Has been used.
| ... | | |
| 31 | Can't Block | Can't Block |
TODO

#### State Settings
| Label | Function |
|--|--|
| Number of Hits | [Refer to the Attack section](###Attack). |
| ASCF | Unknown |
| Player Can Move | True or False? Is the player able to cancel this frame and do anything at all such as walking around, blocking, etc? Or do they commit to this pattern/frame? |
| State | Is the character Standing, Crouching, or in the Air? Used to determine attack results, air mechanics, etc. |
| Invincibility | What is this character immune to during this frame? |
| Counterhit | Can the character get Counter-Hit during this frame? As a rule of thumb, all _Normals_ will be a _Low Counter_, and all _Specials_ will be a _High Counter_. _No Change_ is typically put for every following frame until _Clear_ enters for the actionable recovery frames. |
| Cancel [Normal/Special] | During and after a hitbox/attack box comes out, can the character cancel into another move? For the most part, _Normals_ will always be cancellable _On Hit_ to anything, while _Specials_ can't be cancelled. EX moves should never cancel. _On Successful Hit_ applies to moves that are NOT blocked - if it is blocked, it's not cancellable.

#### Sine Data
[Sinusoidal](https://en.wikipedia.org/wiki/Sine_wave) information and movement.

| Label | Function |
|--|--|
| Flags | Similar to Movement Flags, 1 being Y and 5 being X. |
| Sinewave | X distance, Y distance, X frequency, Y frequency. Distance = the range of movement, Frequency = speed of oscillation. |
| Phases | X, Y. Starting offset of **frequencies**. |


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

To register an attack, you must fill out:

- "**Number of Hits**" in State data to be 1
- An **Attack Box** using the box window
- Technically optional, but of course you would fill out the **Attack Data**.

A single attack frame will cause 1 hit with its specifications for the length of that frame - it will not attack with the same frame data twice unless you duplicate the frame.

If you need to make a move that has animating attack frames spread across multiple frames, but _don't_ want to have multiple hits to happen, you would set all the **Number of hits** for the frames with attack boxes to **0**. The frame before your first attack frame should have Number of hits set to **1**. Meaning that if you had three attack frames in a row, all their Hit counts would be 0, but the frame right before all of them would be 1. This will make sure that all subsequent attack frames next to each other will count as one hit and won't activate again.

### Attack

Dictate information about an attack for that frame including all active boxes.

### Effects

These cause additional effects to occur, which may also be done in the character's mv file. These can range from playing sounds, modifying the battlers, etc. Refer to https://github.com/Fatih120/undernightinbirth/blob/master/doc/effects.txt for now.

### Conditions

Probably unused.
