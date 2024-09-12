https://github.com/Fatih120/undernightinbirth/assets/18276369/c48ec7f8-b4d9-47eb-8385-b3af4233a222

[![Steam](https://img.shields.io/badge/Steam-231f20?logo=steam)](https://steamcommunity.com/id/Fatih120/)
[![Discord](https://img.shields.io/badge/Discord-220077?logo=discord)](https://discord.com/invite/Cy27FNfQtc)

[<img src="https://img.shields.io/badge/Code-Documentation-brightgreen" height="30">](http://mof.x10.bz/unib)

# Primer on Modding UNI2

For starters, you may use https://github.com/Ekey/UNIB.Data.Tool to unpack the game successfully. Either build it yourself with [CSC.exe included with .NET 4](https://stackoverflow.com/questions/18286855/how-can-i-compile-and-run-c-sharp-program-without-using-visual-studio) and [some elbow grease](https://stackoverflow.com/questions/46320080/c-sharp-unable-to-compile-cs0103-the-name-gutils-does-not-exist-in-the-curre), or download it straight from this repo [right here, pre-built](uni2unpacker.exe) (or after cloning).

Run the program in a shell ([Command Prompt on Windows](https://www.wikihow.com/Run-a-Program-on-Command-Prompt#Run-Other-Programs)) with `<input> <output>` arguments: Input being the `d` folder, and output being somewhere accessible such as `./d/output`. Don't know what the `d` folder is? Well, that's where the base game folder is, next to `uni2.exe`. Open it via Steam's game Properties -> Local Files -> Browse Local Files. 

After you have unpacked everything, you are ready to sift through and start modding in whatever ways you want.

### Resources

- Tools for graphics and editing data are bundled in this repo, specifically in the [tools directory](tools). They will be brought up per-basis, but **you should want to get hanteichan_2.1.666.exe** (ignore the scary name).
- To edit `.txt` files without potential issues, use an editor that can properly read and save in the Japanese **SHIFT-JIS** format, [such as NotepadNext](https://github.com/dail8859/NotepadNext/releases/tag/v0.6.4).
- To be able to edit certain files, you should get a hex editor of your choosing, [such as HxD](https://mh-nexus.de/en/downloads.php?product=HxD). [ImHex](https://github.com/WerWolv/ImHex) may also suffice, among others depending on your preference.
- For editing certain graphics, [Paint.NET](https://getpaint.net) is a fine general-use editor for graphics, in our case, DDS files. It may also keep indexed colour tables. For sprites, the popular [Aseprite](https://github.com/aseprite/aseprite)/[LibreSprite](https://github.com/LibreSprite/LibreSprite) will be useful for editing sprites and their palettes. Tools like [GIMP](https://www.gimp.org/), though more complex, may be used.
- [Audacity v3.0.2 pre-telemetry](https://www.fosshub.com/Audacity-old.html?dwl=audacity-win-3.0.2.exe) for audio editing and getting sample times down.
- This entire repo!
- - Since French Bread and ArcSys explicitly placed taboo on modding the former's games, online circles are typically avoidant of this and information is staggered. By adding findings and opening up issues and discussions on here, hopefully there can be a more accessible and helpful resource to help newcomers.

# To Edit or Add Characters

We are able to set up new characters without modifying the base game's data. You could do this from scratch, but if you're new, you should copy an existing character so you don't have to be worried about requirements and oddities you're unaware of. Alternatively, you can modify existing characters or write over their slots - however, this will require internal edits and copying over mass data. If you'd like the former, read the following - if you'd like the latter, skip below to the "Dereferencing" section.

* _For the following, be SURE to differentiate between your "output" foler and your "working" folder. You COULD use the unpacker to output the files beside the exe, but for the sake of isolating your edited files, I strongly recommend seperating the output data._

### The very short of it for copying a character to a new slot:

1. Copy a `chrXXX` character from `./output/data/`. Move it into `./data/`, creating that folder.
2. Rename the folder to a new slot greater than 024, such as `025`. Do the same with the files inside using that same number, including the `lst`, `pal`, `txt`s, etc.†
4. Open `chrXXX_mv_0.txt` in your specialized editor. Jump to the end and find the two last written lines - `CHRXXX_MoveTable <- Battle_Std.MakeMoveTable( t, CHRXXX_CommandTable, Def_ChrNo_YYY );` and `__dofile__("./chrXXX_se_category.txt");`. Edit these lines to have your IDs accordingly.
5. Open `chrXXX_0.txt`, and change the references to XXX in the same way. Open `chrXXX_cmd_0.txt`,  and change the references to XXX in the same way. _(Optionally for quick-start?)_ Open the two `chr025_se_*` files and change the references accordingly.
6. Find `./output/script/btl_Define_CharaNew.txt`. Copy it to `./___English/script`.
7. Open your copy and append the line `const Def_ChrNo_ChrXXX = XXX;` using the same number you chose. Also add the line `const Def_ChrNo_YYY = XXX;`, with Y preferably being a 3-letter identifier for the character.
8. Find `./output/System/BtlCharaTbl.txt`. Copy it to `./___English/script`.
9. Scroll to the bottom and append a `chara_no[XXX]` by templating one of the previous entries, making sure to have `name_short = "chrXXX";` and a unique `order`.

† _You _are_ able to use different naming conventions for certain files to make them easily readable, such as whatever is defined in `chrXXX_0.txt`, but be sure your character loads this way first as I haven't fully figured out what can be changed._

You should now be able to go to training mode and see a new slot, which should be playable with your setup without internal edits. You can make the character accessible on the CSS and in other areas through folders such as `grpdat`'s `CharaColorBar`, `CSel`, `Cockpit`, etc. If you just want to edit this extra slot without the baggage of touching vanilla characters, skip the next section and head down for the guide on character edits and using Hantei-chan.

### Dereferencing for edits

Coming from UNICLR, things are a bit different. After you've dumped all the game assets, you are able to do modifications as a "layered file system" by copying assets to the base directory, next to `uni2.exe`. Common practice in UNICLR was to put everything into an `___English` folder which housed these system folders. For the case of characters, the `data` folder housing all character data simply needs to be moved to the base directory - again, next to `d` and the game executable.

Now, simply trying to edit these copied assets will not result in the game loading these files. Hex edits to certain files in `d` are required to be "dereferenced" or dummied out, since these files tell the game where to look for assets. Within `d`, the file `hexeojmpimrjs` houses links to all the character files and folders within `data`. **Back up this file before you do anything with it.** If your hand needs to be held, you can [get this repo's copy of the dummied file](tools/GAME/d/hexeojmpimrjs) and replace your copy with it. But for the sake of other `d` files and for reference, open up your hex editor and open the file with it.

![HxD64_2024_0130-173603](https://github.com/Fatih120/undernightinbirth/assets/18276369/25e7eaf0-1074-499b-9be7-f54588d28fec)

You will come across a view like this in your main window. Depending on your knowledge with hex, you will at least see that the ASCII pane to the right shows the names of certain folders within `data`, and scrolling down will sequentially list every file within that directory. As long as the files are properly referenced here, the game will always load the original ingame files. We must break this by simply renaming all references to these files.

![HxD64_2024_0130-173929](https://github.com/Fatih120/undernightinbirth/assets/18276369/9c2d1212-50a4-4c5b-bc96-57fb660b68d9)

In the case of HxD, you should _type to overwrite_, **NOT** delete data. If a prompt warns you're going to change the filesize, cancel and try again. You may now proceed and do this for every file and folder you see, though you _can_ just remove certain files or folders from loading if you want to be selective about it. You may save once finished and proceed to copy any remaining files from your `output` into your workspace `data` folder. If you've applied the file from the repo above, this dummies out **all** of `data`, so you **must** copy/move over all of the outputted `data` folder or the game will crash.

Usually, to add characters, one would go to `System\BtlCharaTbl.txt` and add a definition at the bottom which gives the game an internal ID for them. Then, adding more defines in the first set of values in `script\btl_Define_Chara.txt` (does `script\btl_Define_CharaNew.txt` work too?). Newly added, one can also finally add slots on the CSS using `grpdat\CSel\CSelAnim.ini` (also in `Customize`). Finally, the data would have to be set up for the new character in `data\chr<ID>`, or replacing another character's folder.

As for now, it's hard to test if your changes work when you've copied only vanilla data, so you could try and do things like copy `chr001.cg` and overwrite `chr000.cg` with it and playtest as Hyde to see if anything is wrong. Scroll down towards HA6 Editing to get started on character edits and the like.

# Audio

See: [AUDIO.md](AUDIO.md)

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
chrXXX_se_category.txt, chrXXX_se_list.txt | [Sound Effect Definitions](AUDIO.md) | `./se` |
chrXXX.lst | List File | Useless |
_temp.ha6, _temp.lst | Temp | Useless |
BaseData.lst | Base Data List | `../BaseData.ha6` |

# Character Graphics

If you are making a custom character, adding sprites is obviously essential to being able to put a face to a name. In UNI2, importing sprites to turn them into a **CG file** can either be very simple, or a bit of a pain, depending on things such as if your character already comes from a fighting game, if the sprites are all indexed the same way, and how much you have to modify the sprites without relying on HA6 transformations (it might be a lot, because batch-editing tools like [ImageMagick do NOT seem to do a good job handling sprites and palettes](https://github.com/ImageMagick/ImageMagick/discussions/6705).

### Creating a CG File

For now, this guide will assume you are porting a character from another game and that you have obtained their sprites, all indexed correctly _within a folder_. One important thing to note is that **you should probably not include any "effect" files within this folder**. Things such as fireballs, explosions, trails, glows - anything that doesn't seem to be directly attached to the character (and that may be higher-quality than the regular sprites) - should be isolated for use in **.PAT files**. That is because you will typically be unable to use these sprites within your CG file and they will usually appear very wrong - especially because they tend to not use the palette information in the rest of the sprites. Therefore, they may as well be a waste of space and clutter your sprites.

Sprites will be processed by increasing alphabetical order, and will be ordered as such in the CG file whenever you go to edit them. Because of that, if your sprites aren't already named somehow by number (`Name_000` going up is fine), it may be wise to number them as such, perhaps with [Bulk Rename Utility](https://www.majorgeeks.com/files/details/bulk_rename_utility.html).

If you know that your sprites are smaller than the ones normally found in UNI2, you may want to hold off from doing any pre-processing as stated in the note above. UNI2 can internally scale and turn sprites with HA6 editing. ***However, if you prefer and have been able to find a good method to batch-edit images while keeping their palette info intact, please feel free to share your methods with this repo.***

With that out of the way, you may now grab [the cgtool pack](tools/cgtool.7z) and extract it somewhere. To immediately make a .CG file, simply _drag and drop_ your **folder full of sprites** into the `cgtool_make_cg.bat` file, which should open a command line and process all the images, in turn creating a .CG file in the same directory named after the folder you inputted. You may prefer to open a command line yourself and enter `cgtool -input "FOLDER" -output FOLDER.cg` for the same result. Any errors may result out of non-PNG files being in the folder or some other inconsistency.

If you're familiar with HA6 editing down below, you may test your new CG file within your project and see if it displays using Hantei-chan. If you need to make changes within your folder, do so, and run the tool again to update the CG. However, assuming things have been smooth so far, you'll actually see that the sprites look **grayscale**. This is fine, though it means that you will have to now create a matching palette file (`.pal` file seen in other character folders) to go with your sprites - cgtool does not cause the "default" colour information to be normal by default.

### Modifying a CG File

This section is specifically for editing existing CG packages, such as if you wish to add or edit sprites to an existing character's set. Skip this if you aren't editing them.

Vanilla characters will have their CG files within their respective `data/chrXXX` folders. You're free to copy it over to where you have cgtool or process it right there, where you will now use `cgtool_extract_cg.bat` by dragging and dropping the file, resulting in a new `extracted` folder beside cgtool (you may also do `cgtool -input "chrXXX.cg" -output "extracted"`, optionally setting the output directory).

You will now have access to indexed sprites for your UNI2 character. You are able to reorder or add sprites, and can even remove them if that tickles your fancy. However, do note that as it applies to the previous section, "gaps" in names of sprites will not reflect in HA6 editing - there are no "empty slots" in a CG file, so if you have a "200.png" sprite and the next is "205.png", the file will have "205.png" be registered as ID 201. If you are adding sprites and are scared about messing up the order, simply make sure that your new sprites are last in the folder list. For example, if you've been using nothing but numbers, your "new" sprites could have a leading character - so you can use names such as "New_800", "z_1000", et cetera, and they should always be last in the file, without making changes to the previous sprites.

### Palettes

To create a .pal file for your character, I would recommend [getting these files here](tools/palette) and putting them in a new folder _within_ cgtool's folder - specifically because of `palettehelper.exe`, which will do some work for you. Inside that folder, add a copy of one of your character's sprites and name it "0.png". You can use any sprite you want that is indexed, and you can actually go as far as to make a "sprite sheet" that keeps the colour map for references to make custom paletting easier to visualize. Again, I would recommend LibreSprite for editing these images and for paletting.

![0](https://github.com/Fatih120/undernightinbirth/assets/18276369/0ee32bdd-4e23-496f-91bd-dc354a9fd4e9)

But for now, to make sure that your palettes can load and work to begin with, let's make your job easier by running `pal_dupe_images.py`. This will duplicate 0.png so you have your 41 base colour slots available in the game, which are all referred to with the txt file `TODO: can we pass with less colours? why did they do 41 colours, does 0 = 1?...`. Finally, execute `makePal.bat`, which will run palettehelper and pass the arguments needed where the TXT file lists all the image files to make a .pal for. Your shiny palette file should now come up, so put it into your project, test it out, and you should no longer see any grayscale - just your character in their normal colours.

If you want to already get to filling out the palette information for all the slots, there are several ways to do this. The slowest way is using your palette-editing tool to manually change all the colours. You might be able to cut corners and import the palette information from a sprite with different colours if the structure is the same. Some sprite dumps for other fighting game characters might have palettes laid out for you as seperate PNG files, which will make things very easy for you since you can just copy them to your palette folder and use them.

If you are trying to copy over an old Melty Blood character, you will notice that just using the original pal file will make the character's colour change when they switch sides, due to palettes being "half" or something like that. I have included the [riff2png script](tools/palette/riff2png.py) which will be able to convert the individual pal files [from online sprite rips](https://www.spriters-resource.com/playstation_2/mbaa/), making it easy to copy the output files over to your palette images. Just run the script within those palette directories and it will spit out the images in working order, allowing you to make a true palette, though the last few slots will have to be done by you.

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

**For a list of all the patterns' uses in UNIB, please refer to [this file on the repo](docs/patterns.txt).**

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
| Number of Hits | [Refer to the Attack section](###Attack). The MAXIMUM number of hits the attack does for the duration of the current frame. If it is 2, the attack specified will hit twice on that frame. |
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
