# [Moved to Gitlab unless Github decides not to be shit](https://gitlab.com/mofatih/undernightinbirth)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://github.com/Fatih120/undernightinbirth/assets/18276369/c48ec7f8-b4d9-47eb-8385-b3af4233a222

Amateur resource to understand the workings of Under Night In-Birth and other French Bread games. 

This repo currently includes a build of Hanteichan labelled v2.2.1. I probably got it from Discord. I **strongly urge** you use this version, or at least not the original Hantei-chan. Some versions were made for only MBAACC in mind, which lacks the ability to do many things introduced in UNIB. There are other builds floating out there, but for the scope of UNIB this one should be functional.

To unpack the game files, [please grab the executable from this repo's release](https://github.com/ucuckic/unist-unpacker/releases). Drop it into the `d` folder in the game's installation folder. Drag and drop every other file into the executable and wait for it to finish. This may take a long time and you will need another 20GB of space because this game is not-at-all optimized for disk space for reasons unknown. After, you will see an `output` directory.

To mod the game, you must create a language folder such as `___English` (three underscores) in the root directory next to `UNIst.exe` and `d`, and then insert files that way copied from the `output` folder. This will "replace" the files loaded on runtime. Character files are located in `data`, and some places of interest are `scripts` and `system`. There will be plenty to explore on your own.

To create a new character, try copying another to edit or set up the file structures the same way, using `data/BaseData.HA6` as a base.

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
