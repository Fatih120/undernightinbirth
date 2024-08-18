BMvTbl
======

.. function:: void CBtlInfo(void)

   Collects info about the current battle.

.. function:: int CBtlInfo.GetSelectBgm(void)

   Returns the current BGM number. -2 is Off / MUTE.

.. function:: bool CBtlInfo.IsSelectBgm(void)

   Whether the current playing BGM was player-chosen.
   
   :return: 0 or 1.

.. function:: void CBtlInfo.SetSelectBgm(int number)

   Sets the BGM.

   :param int number: BGM ID

.. function:: int GetMuki(void)

   Returns the facing direction of the object as either -1 or 1 (facing left and right respectively).

.. function:: int GetMvRoundStatus(void)

   Returns the round status.

.. function:: void GetMvRoundStatus.CharaMoveMode(void)

   

.. function:: int GetMvRoundStatus.Round(void)

   Gets the current round number.
   
   :return: Round number beginning from 0 as Round 1.

.. function:: bool GetMvRoundStatus.isDown(void)

   

.. function:: bool GetMvRoundStatus.isFinalRound(void)

   Returns if the current round is the final round in the form of a bool.

.. function:: bool GetMvRoundStatus.isKO(void)

   

.. function:: bool GetMvRoundStatus.isLoseRound(void)

   

.. function:: bool GetMvRoundStatus.isMyKO(void)

   

.. function:: bool GetMvRoundStatus.isWinRound(void)

   

.. function:: int GetMvStatus(void)

   Returns the status data of the current object's movetable.

.. function:: void GetMvStatus.CallCount(void)

   

.. function:: void GetMvStatus.DataPattern(void)

   

.. function:: int GetMvStatus.FrameID(void)

   Returns the Frame ID of the current object.

.. function:: bool GetMvStatus.isLanding(void)

   Returns a bool for the isLanding state.

.. function:: void GetMvStatus.MvCount(void)

   

.. function:: int GetMvStatus.Param0(void)

   Returns the current value of Param0.

.. function:: int GetMvStatus.Param1(void)

   Returns the current value of Param1.

.. function:: int GetMvStatus.Param2(void)

   Returns the current value of Param2.

.. function:: int GetMvStatus.Param3(void)

   Returns the current value of Param3.

.. function:: int GetMvStatus.CharaNo(void)

   Returns the character ID number.

.. function:: int GetPlayerSide(void)

   Returns which side the character is in, ie port number, as chosen before Character Selection.
   
   :return: 0 for Player 1, 1 for Player 2.
   
.. function:: int GetSelectColor(void)

   Returns the ID of the character's chosen Color number.
   
.. function:: void SetMuki(int direction)

   :param int direction: ``_Direction_Left``, ``_Direction_Right``, ``_Direction_Auto``, ``_Direction_Reverse``

   Sets the facing direction of the object.

.. function:: void SetPattern(int pattern)

   Immediately sets the object's current pattern.
	
   :param int pattern: ID of the pattern. Move Code as a string can be used instead.
