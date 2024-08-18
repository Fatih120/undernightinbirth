
Battle_Std.Atemi
=================

.. function:: void HitInterrupt(dict param={})

   Handles the hit interrupt logic during an attack, including managing invincibility states and sound effects based on the hit status.

   :param dict param: Optional parameters for the hit interrupt behavior, including:
     - `nosound`: Flag to suppress sound effects.
     - `hitstop`: Custom hitstop duration.
     - `e_hitstopAdd`: Additional hitstop to apply to the enemy.
     - `pride`: Pride attribute for checking against enemy types.
     - `noquake`: Flag to suppress camera shake effects.
     - `noeffect`: Flag to suppress visual effects.

