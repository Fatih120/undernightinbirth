ThrowTech
---------

.. class:: Battle_Std.ThrowTech

   A class containing common throw-related functions.

   .. function:: SetMuteki()

      Makes both the player and the opponent invincible during a throw.

      This function sets invincibility timers for both the player and the opponent during a throw.

   .. function:: SetPos(type=0)

      Stores the positions of the player and the opponent before a throw.

      :param type: 0 for normal throws, 1 for special moves. Default is 0.

   .. function:: CheckTechImpossible(_setCharaFlash=1)

      Checks if the opponent is in a state where they cannot perform a throw escape and applies visual effects.

      :param _setCharaFlash: If 1, applies visual effects for a failed throw escape. Default is 1.
      :return: True if the opponent cannot perform a throw escape, False otherwise.

   .. function:: ShiftOverGamenHajiX()

      Adjusts positions when the opponent is at the edge of the screen to prevent clipping.

   .. function:: SetThrowParam()

      Sets throw parameters for normal throws, including special hit detection coordinates.

   .. function:: DrawThrowEffect(type=0)

      Displays a grab effect at the hit coordinates.

      :param type: 0 for normal throws, 1 for forced throws. Default is 0.

   .. function:: DrawTechEffect()

      Displays visual effects for a successful throw escape.

   .. function:: TechRelease(param={})

      Handles the release process when a throw escape is successful.

      :param param: A dictionary of parameters. Can include 'release_kyori' to specify fixed coordinates after throw escape.

   .. function:: CheckTechCommand()
   
   Checks if a throw escape input has been performed.
   
   :return: True if a throw escape command was input, False otherwise.
   
   This function checks for throw escape inputs during the update of a throw escape move. It considers various conditions such as KO state and throw escape impossibility.
   
   .. function:: CheckTechMissFrame()
   
   Checks if the current frame is a failed throw escape frame.
   
   :return: True if it's a failed throw escape frame, False otherwise.
   
   This function is called by ``Battle_Std.SetThrowHitFinalize()`` to determine if the current frame is a failed throw escape frame.
   
   .. function:: DelThrowMvFlag_NextFrame()
   
   Creates an object to remove the throw attribute flag in the next frame.
   
   .. function:: SetThrowMvFlag()
   
   Sets the throw attribute motion flag.
   
   .. function:: SetThrowMvFlag_AutoDel(frame=0)
   
   Sets the throw attribute motion flag and automatically removes it after a certain time or when the move changes.
   
   :param frame: The number of frames to keep the flag active. Default is 0.