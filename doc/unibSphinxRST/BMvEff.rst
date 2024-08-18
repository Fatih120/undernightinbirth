BMvEff
======

.. c:function:: void AttackInfoString_Set(const char* word)

   :param const char* word: The string to display.
   
   Displays Attack Info, which is used for the text pop-ups that display on the sides. This is used for pop-ups such as Vorpal, Chain Shift (UNI), and Reversal, Invincible, Super Armor (MBTL).

.. c:function:: void BGM_Set(int number)

   :param int number: The BGM number to play.

   Sets the BGM.

.. c:function:: int BG_GetNum(void)

   Returns the background number.

.. c:function:: void CockpitSetView(int mode)

   :param int mode: Whether to enable the Cockpit (1 or 0).

   Creates an object that has properties based on the array. Not all of the above properties are needed.

.. c:function:: void CreateObject(int x, int y, int pat, int start_pat, const char* mvname, int flags)

   :param int x: X position of the object.
   :param int y: Y position of the object.
   :param int pat: Sets the pattern based on its number in the HA6.
   :param int start_pat: Sets the object to the given pattern.
   :param const char* mvname: Sets the mv clause based on the name, e.g., ``mvname = "Mv_Startup"``.
   :param int flags: Assigns the object flags.

   Creates an object that has properties based on the array. Not all of the above properties are needed.

.. c:function:: void EraseObjectFlags(int flags)

   :param int flags: The flags that will be erased.

   Erases object flags.

.. c:function:: int GetPointStatus(int2 position)

   :param int2 position: (Description needed)

   (Description needed)

.. c:function:: void PcAfterImage_Clear(void)

   Clears any afterimage effects on the player.

.. c:function:: void PcAfterImage_Set(int type, int range, int delay, int color, int blendmode)

   :param int type: The type of afterimage.
   :param int range: The amount of afterimages that compose the trail.
   :param int delay: The amount of frames of delay between each after effect.
   :param int color: The color of each after effect, which applies a multiply blend onto each afterimage, as well as an alpha value.
   :param int blendmode: Whether or not each afterimage has additive blend (1 or 0).

   Applies a trail of afterimages on the player. Used for dash attacks (UNICLR), Moon Skills (MBTL), and Creeping Edge (UNI2).

.. c:function:: void PcAuraEffect_Clear(void)

   Clears any aura effects on the player.

.. c:function:: void PcAuraEffect_Set(int type, int time, float power, int color, int colorB, int color_chara, int blendmode, int delay)

   :param int type: The type of aura. Type 0's aura has a consistent width. Type 1 creates a pulsing effect.
   :param int time: The amount of frames this effect lasts for.
   :param float power: The strength of the effect, changes the "width" of the aura.
   :param int color: The first color of the aura.
   :param int colorB: The second color of the aura.
   :param int color_chara: The color the character sprite turns to. This appears at the same time colorB fades in.
   :param int blendmode: Whether or not each afterimage has additive blend (1 or 0).
   :param int delay: The amount of frames it takes to fade from color to colorB.

   Adds a color effect to the player's sprite. Does not apply to effects or objects spawned by the player. This is used for various effects such as VORPAL.

.. c:function:: void SetCharaColor(int color, int intime, int time, int outtime, int type)

   :param int color: The color to apply.
   :param int intime: (Description needed)
   :param int time: (Description needed)
   :param int outtime: (Description needed)
   :param int type: (Description needed)

   Adds a color effect to the player's sprite. Does not apply to effects or objects spawned by the player.

.. c:function:: void SetObjectFlags(int flags)

   :param int flags: The flags that will be added.

   Adds object flags.
