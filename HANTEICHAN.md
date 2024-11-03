
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

Typically used to signal when voice clips are played by using the first box with the value of "10".

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

If there is a visual change to a sprite or effect between frames and layers, the method to "blend" (interpolate) between them. For example, if you set an effect to have Alpha 0 (invisibility) on the first frame and Alpha 255 (opaque) on the next, setting interpolation to "Linear" will smoothly cause the graphic to fade in from nothing, whereas setting it to "None" just makes the graphic appear with no buildup. Interpolation can be applied to color and even the X/Y/ROT positioning of assets.

For a better understanding, research [easings](https://doc.starling-framework.org/v1.5/starling/animation/Transitions.html).

- None: No interpolation at all; "hold" frame that appears as-is in Hantei-chan.
- Linear: Smoothly interpolates values from A to B in a linear fashion.
- Slow->Fast: "Eases in" where values from A slowly linger before quickly finishing with B.
- Fast->Slow: "Eases out" where the interpolation immediately speeds away from A while slowing down to B's values.
- Fast Middle: The midpoint of time between A and B is fast compared to the ends which feel slowed down.
- Slow Middle: The midpoint of time between A and B is slow compared to the ends which feel instant.

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

- **Type 3:** When the attack's condition is set on a specific frame, it jumps to the pattern upon successful hit in the first parameter but must start with "10". For example, Shiki Tohno's 623B pattern has this condition on frame 9, so with Type 3 and a first parameter of 10255 (pattern 255 with "10" added in front), it jumps to pattern 255.
