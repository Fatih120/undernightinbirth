### How do I add jumping attacks?

Make sure that every frame in your attack's State Data has the Airborne state. Make your aerial attack as you like. Then, make sure the final frame ends with "Go To Pattern", while Go To is at 20 so that the character is set to the falling pattern when the move is done. You must also turn on the first Animation Flag, "Land to Pattern?", every frame, and use the Range Tool (or by-hand) to set the Landing Frame to 21. This makes it so that the Landing Frame value is actually saying, "what pattern do we go to when we land?", where 21 is the landing pattern.

#### But what if the attack's on the ground for a while?

Such as for a move that starts grounded? In this case, you can ignore the Animation Flag - properly set each frame's state as Grounded or Aerial, and apply some Movement Vectors right as they're about to take off. You might have to loop the character for while they're in the air, just so that they don't end up standing mid-air once they're done. Add the frames in which the character is landing back on the ground, properly setting their state back to Grounded, and take note of the first frame number in which they're back on the ground (use the number on the bar, not the XX/XX next to it). You are going to use the Range Tool and set every frame's Landing Frame to that value, since they're on the ground on that frame. The pattern should now work in the air and land back down.

### How do I add sprites to my character?

If you need to add more sprites to your character, go back to your sprites folder, and try to add a sprite with a name that won't disrupt your sprite IDs in Hantei-chan. Since your sprites are sorted alphanumerically when creating your CG, you can try prefixing your sprite name with something like "z" (like "z000.png") to make sure the sprite is always packed last. It will probably save you headache down the line.

### How do I make an EX move?

First, make sure you have the move included in your character's cmd file, with an entry such as `Skill_236EX = {},` or whatever type of EX input you'd like your character to have. In Hantei-chan, within your pattern's Code Name, write the input with an "EX" following after (`236EX` in this case). You can now create your EX move, though with one important detail before you test it out - on the very first frame, you need to add a Special Box 1 and a Special Box 2. The top left of these boxes indicate where the EXS superflash effects should spawn, so put them both close to each other somewhere on the character to get the flash to work. Test it out and take any notes on whether you need to pad out the startup of the move as it'll keep going during the flash freeze.

### How do I give a move invincibility?

Simply remove the hurtboxes - click "Delete selected" on the boxes that you want removed on those frames, and also set the State Data to have "Throw Only" Invincibility so that grabs are also prevented from working on the character. Only the hurtboxes really matter, so the invincibility dropdown is really just for throw protection. Just make sure not to remove collision boxes! What's also nice is that the Invincibility text will appear on the screen automatically.

### How do I do a throw or command grab?

### How do I do hitgrabs?

### How do I make a charged (Increase) attack?

### My character's walking speeds aren't changing!

This data is in "script/btl_StdMoveTbl.txt" for some reason. Find the `local type = "歩きベクトル";` section and add something like `chrparam.Param[type][Def_ChrNo_XXX] = [512, 1000, -512,  -1000];` to that table and go from there.

However, this method can be messy and non-modular. Another preferred method is to edit your character's mv file and add the following functions:

```cpp
t.Mv_Walk_F <-
{
    function FrameUpdate_After()
    {   
        BMvTbl.SetVector( { x=1000, flags=_Vector_Normal } );
    }
}

t.Mv_Walk_B <-
{
    function FrameUpdate_After()
    {   
        BMvTbl.SetVector( { x=-880, flags=_Vector_Normal } );
    }
}
```

These are the walk functions, in which you can easily change the x value from here.

### I want to add subtitles to my character!

### How do I make my character talk and appear in the Character Select Screen?

### How do I make my pattern loop a certain amount of times?

On the frame that you want the pattern to go backwards and loop from, enable these animation flags under the Animation Data:

- "Check loop counter"

- "Go to relative offset"

- "Relative end of loop"

Next, set the "End of loop" value to 1 to designate the next frame as your "escape" from the loop (hence, "Relative" end of loop). Then, use "Go to frame" in the drop-down and set the "Go to" to the amount of frames you want to jump backwards for the start of the loop (e.g. "-3").

Before your loop can properly work, go to the frame **before** the frame that starts the loop. This is where you will fill the "Loop N times" field which will make the loop happen as many times as the value you put in. When you're done, test the pattern with the Animate button.

### How does the Rotation system work?

In increments of 10,000 being a full revolution/circle. 2500 is 90 degrees clockwise, 5000 is 180 degrees, and 7500 is 270 degrees.

### I need more help!

It's okay. If you want live help, feel free to drop by (this Discord server)[https://discord.gg/invite/pBrC5KM5b2].





