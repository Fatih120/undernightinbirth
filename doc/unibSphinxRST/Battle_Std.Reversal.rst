Battle_Std.Reversal
-------------------

.. class:: Battle_Std.Reversal

   A class containing reversal-related functions.

   .. function:: SetTime(frame=1)

      Sets the reversal time.

      :param frame: The number of frames for the reversal window. Default is 1.

   .. function:: GetTime()

      Gets the remaining reversal time.

      :return: The remaining reversal time in frames.

   .. function:: CheckTime_DrawInfo(_drawinfo=1)

      Checks if there's remaining reversal time and displays information if true.

      :param _drawinfo: If 1, displays reversal information. Default is 1.
      :return: 1 if there's remaining reversal time, 0 otherwise.

