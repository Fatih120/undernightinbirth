Battle_Std
==========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Battle_Std.Atemi
   Battle_Std.JumpStatus
   Battle_Std.Reversal
   Battle_Std.Sousai
   Battle_Std.ThrowTech
   
.. function:: JumpFrameIDEX(_frameID, _pat=-1, _code=-1)

   Performs a frame ID jump with additional pattern and finalize code options.

   :param _frameID: The target frame ID to jump to.
   :param _pat: The pattern to set if different from current. Default is -1 (no change).
   :param _code: The finalize code to set if jump fails. Default is -1 (no finalize).

.. function:: SetPattern_NotEqual(_pat)

   Sets a new pattern only if it's different from the current pattern.

   :param _pat: The new pattern to set.
   :return: 1 if the pattern was changed, 0 if it remained the same.

.. function:: DrawDebugAttackInfo(str)

   Displays debug attack information.

   :param str: The debug string to display.

   This function is used for adjustment and debugging purposes.

.. function:: Create_TechDelayCheckObject(delay=0)

   Creates an object to check for throw escape commands with a delay.

   :param delay: The delay before checking for throw escape commands. Default is 0.


Sound Effect
""""""""""""

.. function:: individual_se_check(target, num, flags)

   Performs individual checks for sound effect playback.

   :param target: The target sound effect information.
   :param num: The sound effect number.
   :param flags: Playback flags.
   :return: A result object containing ret_val and flags.

.. function:: play_se(info, flags)

   Plays a sound effect based on the provided information and flags.

   :param info: Sound effect information.
   :param flags: Playback flags.
   :return: 1 if the sound effect was played, 0 otherwise.

.. function:: PlayerSE_Play(num=0, flags=0)

   Plays and remembers a character sound effect.

   :param num: The sound effect number. Default is 0.
   :param flags: Playback flags. Default is 0.

.. function:: PlayerSE_StopLastPlaySound(_checkMyKo=0)

   Stops the last played sound effect.

   :param _checkMyKo: If 1, checks if the player is KO'd before stopping. Default is 0.

.. function:: TypeSE_Play(tbl)

   Plays a sound effect based on the specified type.

   :param tbl: A table containing sound effect information, including 'type' and optional 'flags'.
   :return: 1 if a sound effect was played, 0 otherwise.

.. function:: TypeSE_AllStop(tbl)

   Stops all sound effects of a specified type.

   :param tbl: A table containing the 'type' of sound effects to stop and optional 'fadetime'.

.. function:: InArrayLastPlaySound(ar)

   Checks if the last played sound effect matches any in the given array.

   :param ar: An array of sound effect numbers to check against.
   :return: 1 if a match is found, 0 otherwise.

.. function:: CreateTechObject(frame=0, gouin=0)

   Creates or updates a throw escape management object.

   :param frame: The initial frame count for throw escape timing. Default is 0.
   :param gouin: If 1, updates the existing throw escape timing. Default is 0.

.. function:: GetTechStatus(_log=1)

   Retrieves the current throw escape status.

   :param _log: If 1, enables debug logging. Default is 1.
   :return: A table containing throw escape status information.

.. function:: CreateTechObject_TechMissStart()

   Creates a throw escape management object in a failed state.

.. function:: GetEnemyCharaNo()

   Retrieves the enemy character's number.

   :return: The enemy character number, or -1 if not available.

.. function:: GetEachCharaNo()

   Retrieves both the player's and enemy's character numbers.

   :return: A table containing 'player' and 'enemy' character numbers.

.. function:: IsDoukyara()

   Checks if the player and enemy are using the same character.

   :return: true if both are using the same character, false otherwise.

.. function:: PlayerisKO()

   Checks if the player is in a KO state.

   :return: true if the player is KO'd, false otherwise.

.. function:: EnemyisKO()

   Checks if the enemy is in a KO state.

   :return: true if the enemy is KO'd, false otherwise.

.. function:: CharaisKO()

   Checks if either the player or enemy is KO'd.

   :return: true if either character is KO'd, false otherwise.

.. function:: RoundisEnd()

   Checks if the round has ended due to KO or time up.

   :return: true if the round has ended, false otherwise.

TODO: Elaborate on the structure of the 'tbl' parameter in TypeSE_Play and TypeSE_AllStop functions.
TODO: Explain the significance of the 'frame' and 'gouin' parameters in CreateTechObject function.
TODO: Describe the contents of the table returned by GetTechStatus function.

.. function:: PlayerisCapture()

   Checks if the player is currently captured.

   :return: true if the player is captured, false otherwise.

.. function:: AttackImpact_StdFunc(info)

   Handles common functionality when an attack impacts.

   :param info: An instance of BMvTbl::MvHitImpactInfo class containing impact information.

   TODO: Elaborate on the structure and contents of the 'info' parameter.

   This function performs various checks and actions based on the attack impact, including:
   
   - GRD increase during Liberate state
   - Handling of guard, bound, capture, and throw states
   - EX and SP skill flags
   - Vorpal state
   - Assault attack handling
   - Counter hit processing
   - Combo point calculations
   - Guard break handling
   - Debug functionality

.. function:: void DamageImpact_StdFunc(dict info)

   Called when an attack connects. It processes the impact of the attack based on various conditions and attributes.

   :param dict info: Information about the attack and its attributes.

   **Attributes and Conditions:**

   - **Guard Attributes:**
     - `StdGuard`: Standard guard possible.
     - `AirGuard`: Air guard possible.
     - `CroGuard`: Crouch guard possible.
     - `Zyodan`: Both standard and crouch guard possible.
     - `Tyudan`: Only standard guard possible.
     - `Gedan`: Only crouch guard possible.
     - `KugaFunou`: Air guard not possible.
     - `GroundGuardFunou`: Ground guard not possible.

   - **Defender States:**
     - `PosisCro`: Defender is crouching.
     - `PosisAir`: Defender is airborne.
     - `PosisStd`: Defender is standing.

   - **Guard Inputs:**
     - `StdGuardInput`: Standard guard input.
     - `CroGuardInput`: Crouch guard input.
     - `AirGuardInput`: Air guard input.
     - `GroGuardInput`: Ground guard input (either standard or crouch).

   - **Attack Flags:**
     - `Nage`: Indicates if the attack is a throw.
     - `Guard`: Indicates if the attack was guarded.
     - `Yarare`: Indicates if the defender is in a hit state (old logic).
     - `NewYarare`: Indicates if the defender is in a hit state (new logic).
     - `Capture`: Indicates if the defender is captured during the hit.

   - **Attack Types:**
     - `DagekiNage`: Indicates if the attack is a strike throw.
     - `DagekiNageNew`: Indicates if the attack is a strike throw (new logic).

   - **Armor Conditions:**
     - `Armor`: Indicates if the defender is using armor to withstand the attack.
     - `ArmorBreak`: Indicates if the attack has armor-breaking properties.

   - **Other Conditions:**
     - `Dage_Syodan`: Indicates the first hit of a strike.
     - `Nage_Syodan`: Indicates the first hit of a throw.
     - `Zenbu_Syodan`: Indicates the first hit of either a strike or throw.
     - `SyodanGuard`: Indicates if the attack was not guarded.
     - `GRDBreak`: Indicates if the attack breaks the guard.

.. function:: GRDBreak_Attack(param={})

   Handles the attacker's side of a GRD break.

   :param param: A table of parameters. Can include 'Nage' and 'NoHosei' flags.

   This function performs the following actions:
   - Multiplies combo points for the attack.
   - Sets flags indicating a GRD break attack occurred.
   - Applies damage modifiers for throws if applicable.
   - Creates visual effects for the GRD break.

.. function:: GRDBreak_Damage(param={})

   Handles the defender's side of a GRD break.

   :param param: A table of parameters. Can include a 'Nage' flag.

   This function performs the following actions:
   - Plays the sound effect for a GRD break.
   - Disables throw escapes for the character.
   - Sets character flash effects.
   - Determines and sets the duration of the GRD break.

.. function:: SetMuki_ReverseEnemy(playertarget=0)

   Sets the character's facing direction opposite to the last attacking enemy.

   :param playertarget: If 1, gets the topmost parent of the attacking character. Default is 0.
   :return: 0 if the character doesn't turn around, undefined otherwise.

.. function:: SetMuki_BoundVectorMuki()

   Sets the character's facing direction based on the current bound vector direction.

   This function adjusts the character's facing during wall bounces or similar situations.


.. function:: GetPSFlag(flag)

   Checks if a specific player status flag is set.

   :param flag: The flag to check.
   :return: True if the flag is set, False otherwise.

.. function:: SetPSFlag(flag)

   Sets a specific player status flag.

   :param flag: The flag to set.

.. function:: DelPSFlag(flag)

   Removes a specific player status flag.

   :param flag: The flag to remove.


.. function:: InitIWExistSkill()

   Initializes the Infinite Worth EXS (IW EXS) skill.

   This function handles various aspects of starting an IW EXS, including:
   - Setting skill counters
   - Adjusting game state (GRD limits, invincibility frames)
   - Setting up visual effects (fade, camera focus)
   - Positioning characters
   - Triggering cut-in animations

.. function:: FinalizeIWExistSkill()

   Finalizes the Infinite Worth EXS (IW EXS) skill.

   This function handles the cleanup after an IW EXS, including:
   - Restoring UI elements
   - Clearing cut-in animations
   - Restoring object rendering
   - Resetting aura states
   - Adjusting BGM

.. function:: IWExistSkill_FinishEffect()

   Applies finishing effects for Infinite Worth EXS skills, including slow motion and camera shake.

.. function:: FinalizeWorthSkill()

   Finalizes Worth skills by erasing cut-in animations.

.. function:: SetEXCutinCameraFocus(stopframe)

   Sets up camera focus for EX skill cut-ins.

   :param stopframe: The duration of the camera focus effect.

.. function:: SetInstantCameraFocus(_frame)

   Sets up an instant camera focus effect.

   :param _frame: The duration of the camera focus effect.

.. function:: SetEXCutinGrp(param={})

   Sets up EX skill cut-in graphics and effects.

   :param param: A table of parameters for customizing the cut-in effect.

.. function:: CallAntenStopObject()

   Creates an object that stops the opponent during the darkening effect.

.. function:: StartExSkill()

   Initializes various aspects of starting an EX skill, including:
   - Setting flags
   - Adding skill counters
   - Applying guarantee corrections
   - Setting SP gauge limits

.. function:: Init_ExistAtkSkill(type=0, stopframe=def_FL_EXCutinStopTime)

   Initializes Exist Attack skills, including camera focus and cut-in effects.

   :param type: The type of Exist Attack skill.
   :param stopframe: The duration of the time stop effect.

.. function:: SetSkillStopTime(stopframe=def_FL_EXCutinStopTime, set_nextf_muteki=0)

   Sets up time stop effects for special skills.

   :param stopframe: The duration of the time stop effect.
   :param set_nextf_muteki: Flag to set invincibility frames after the time stop.

.. function:: Init_Kirifuda()

   Placeholder function for initializing trump card effects.

.. function:: Call_KirifudaEffect()

   Placeholder function for calling trump card effects.

.. function:: UseKirifuda_DelayUpdateTiming()

   Placeholder function for consuming trump card count at a specific timing.

.. function:: GetGRD_AddValue(addgrdval=0)

   Calculates the GRD increase value based on the current GRD stock.

   :param addgrdval: The base value to be adjusted.
   :return: The adjusted GRD increase value.

.. function:: GRD_AddValue(tbl)

   Handles GRD increase, taking into account break states.

   :param tbl: A table containing 'val' (value to add) and 'target' (0 for self, 1 for enemy).

.. function:: SetSpGauge_BarrierFU(tbl)

   Sets SP gauge consumption for barrier skills, adjusting for break states.

   :param tbl: A table containing 'value' (amount to consume).

.. function:: SetSpGauge_ConvertChargeFU(tbl)

   Sets SP gauge consumption for convert charge, adjusting for break states.

   :param tbl: A table containing 'value' (amount to consume).


check chara
""""""""""""

.. function:: CheckPlayerisDamage(_TechisDamage=1)

   Checks if the player is in a damaged state.

   :param _TechisDamage: If 1, considers successful throw escapes as damage.
   :return: True if the player is damaged, False otherwise.

.. function:: CheckPlayerisGuard()

   Checks if the player is in a guard state.

   :return: True if the player is guarding, False otherwise.

.. function:: CheckEnemyisGuard()

   Checks if the enemy is in a guard state.

   :return: True if the enemy is guarding, False otherwise.

.. function:: CheckPlayerisUkemi()

   Checks if the player is in a recovery (ukemi) state.

   :return: True if the player is in recovery, False otherwise.

.. function:: CheckEnemyisUkemi()

   Checks if the enemy is in a recovery (ukemi) state.

   :return: True if the enemy is in recovery, False otherwise.

.. function:: CheckEnemyisDamage(_TechisDamage=1, _CheckUkemiTime=0)

   Checks if the enemy is in a damaged state.

   :param _TechisDamage: If 1, considers successful throw escapes as damage.
   :param _CheckUkemiTime: If 1, considers processing order differences between 1P and 2P (air damage only).
   :return: True if the enemy is damaged, False otherwise.

.. function:: CheckEnemyisAirDamage(_TechisDamage=1)

   Checks if the enemy is in an air damaged state.

   :param _TechisDamage: If 1, considers successful throw escapes as damage.
   :return: True if the enemy is in air damage, False otherwise.

.. function:: CheckEnemyisDamage_ExceptDown()

   Placeholder function for checking enemy damage excluding down states.

   :return: Always returns False.

.. function:: CheckPlayerisBound()

   Checks if the player is in a bound (damaged or guarding) state.

   :return: True if the player is bound, False otherwise.

.. function:: CheckEnemyisBound()

   Checks if the enemy is in a bound (damaged or guarding) state.

   :return: True if the enemy is bound, False otherwise.

.. function:: CheckPlayerisCapture()

   Checks if the player is captured.

   :return: True if the player is captured, False otherwise.

.. function:: CheckEnemyisCapture()

   Checks if the enemy is captured.

   :return: True if the enemy is captured, False otherwise.

.. function:: CheckPlayerisMovable()

   Checks if the player can move.

   :return: True if the player can move, False otherwise.

.. function:: CheckEnemyisMovable()

   Checks if the enemy can move.

   :return: True if the enemy can move, False otherwise.

.. function:: CheckEnemyPosState(_pos)

   Checks the enemy's position state.

   :param _pos: The position state to check.
   :return: The result of the position state check.

.. function:: SwitchNextMoveTable(def, ...)

   Sets the next move based on finalize codes and provided options.

   :param def: Default next move or function.
   :param ...: Variable number of arguments specifying additional move options.

.. function:: SwitchNextMoveTable_NoClearFinCode(def, ...)

   Similar to SwitchNextMoveTable, but doesn't clear the finalize code.

   :param def: Default next move or function.
   :param ...: Variable number of arguments specifying additional move options.

.. function:: SwitchNextMoveTable_Array(ar)

   Sets the next move based on an array of finalize codes and moves.

   :param ar: An array containing default and conditional next moves.

.. function:: GetNextMoveTable_Array(ar)

   Retrieves the next move based on an array of finalize codes and moves.

   :param ar: An array containing default and conditional next moves.
   :return: The selected next move string.

.. function:: CheckHanteiAttackExist(code=0)

   Checks if an attack hitbox exists.

   :param code: Unused parameter.
   :return: 1 if an attack hitbox exists, 0 otherwise.

.. function:: SetThrowHitFinalize(code=0, gouin_code=-1, combo_code=-1, miss_code=-1, techmiss_code=-1)

   Handles throw hit finalization with various conditions.

   :param code: Default finalize code for throws.
   :param gouin_code: Finalize code for forced throws.
   :param combo_code: Finalize code for combo throws.
   :param miss_code: Finalize code for missed throws.
   :param techmiss_code: Unused parameter.
   :return: 1 if throw was successful, 0 otherwise.

   This function handles different throw scenarios, including:
   - Normal throws
   - Forced throws (e.g., during guard)
   - Combo throws
   - Throws during tech miss frames
   It also manages throw escape attempts and updates relevant game state.

.. function:: BoundInit()

   Initializes the bound (hit reaction) state for a character.

   This function handles various aspects of initializing a character's state when they are hit:

   - Processes and displays announcements (e.g., punish, counter)
   - Manages hit voice playback
   - Handles character orientation
   - Sets up vector tables for movement
   - Manages special states like ground fatal, ground bound, and spinning
   - Handles combo point (CP) calculations and adjusts ukemi (recovery) time based on CP
   - Applies special bonuses for certain types of hits or game states (e.g., CVO state)

   Key features:
   - Checks for different types of bound states (ground, air, spinning)
   - Manages character facing direction
   - Handles voice playback for different hit strengths
   - Applies CP-based bonuses to ukemi time
   - Handles special cases like Combo Vorpal (CVO) state

   Note: This function is called during the initialization of a hit reaction and may be triggered multiple times during a combo.

.. function:: BoundUpdate()

   Updates the bound (hit reaction) state for a character.

   This function manages the character's movement vector during a bound state, ensuring proper behavior on the ground.


fireball
""""""""""""

.. function:: InitFireBallStatus(_flags=0)

   Initializes the status for a fireball (projectile) object.

   :param _flags: Initial flags for the fireball status.

.. function:: ClearFireBallStatus()

   Clears the fireball status and releases any associated slot limitations.

.. function:: VanishFireBallStatus()

   Clears the fireball status and marks the object as vanished.

.. function:: GetFireBallStatus()

   Retrieves the current status of a fireball object.

   :return: A table containing various status information about the fireball.

.. function:: GetFireBallFlags(flag)
              CheckFireBallFlags(flag)
              AddFireBallFlags(flag)
              SetFireBallFlags(flag)
              ClearBallFlags(flag)

   A set of functions to manage flags associated with fireball objects.

.. function:: CreateFireBall(t)

   Creates a new fireball object with specified parameters.

   :param t: A table containing various parameters for the fireball creation.
   :return: The created fireball object.

.. function:: GetVector_FromAngle(t)

   Calculates a vector based on angle, speed, and time parameters.

   :param t: A table containing angle, speed, and time parameters.
   :return: A vector table with x, y, addx, and addy components.

.. function:: CheckSousai()

   Handles the collision cancellation (sousai) between projectiles or special objects.

   This function checks for collisions between attack hitboxes of different objects and manages the cancellation process, including hit count reduction and flag setting.

.. function:: InitVector()

   Initializes all vector components, including normal, division, bound, and keep vectors. Also resets the X-axis maximum and triangle vectors.

.. function:: InitCharaVector()

   Initializes character vectors while preserving inertia. Useful for ground-based normal and special moves.

.. function:: GetPositionSide()

   Determines the relative position of the player and the opponent.

   :return: 0 if the player is on the left side (1P side), 1 if on the right side (2P side).

.. function:: SetEnemyPosition(tbl)

   Sets the position of the opponent character.

   :param tbl: A table containing position information.
   :return: 1 if successful, 0 if failed to get enemy data.

.. function:: GetEnemyPosition()

   Retrieves the position of the opponent character.

   :return: A table containing the opponent's position, or a default position if retrieval fails.

.. function:: GetPlayerPosition()

   Retrieves the position of the player character.

   :return: A table containing the player's position, or a default position if retrieval fails.

.. function:: GetEnemyVector(tbl)

   Retrieves the vector of the opponent character.

   :param tbl: A table specifying vector retrieval options.
   :return: The opponent's vector, or a default vector if retrieval fails.

.. function:: GetNearEnemyDistance(tbl={})

   Calculates the distance to the nearest enemy, with options for tool coordinates and direction changes.

   :param tbl: A table containing options for distance calculation.
   :return: A table with x and y distances, and an IsDone flag indicating success.

.. function:: GetNearEnemyToolShiftPosition(tbl={})

   Retrieves the opponent's position in tool coordinates.

   :param tbl: A table of options (optional).
   :return: A table containing the opponent's position in tool coordinates.

.. function:: GetPointStatus_NearEnemy()

   Retrieves distance information relative to the nearest enemy.

   :return: A table containing angle and distance information.

.. function:: GetNearEnemyMigiAngle()

   Calculates the angle to the nearest enemy, normalized to right-facing orientation.

   :return: The angle in the range 0.0 to 2.0.

.. function:: GetParentMigiAngle()

   Calculates the angle to the parent object, normalized to right-facing orientation.

   :return: The angle in the range 0.0 to 2.0.

.. function:: AddToolShift_NoSurinuke(plus_x=0, flag=0)

   Adjusts position to prevent passing through opponents on the ground.

   :param plus_x: The amount to shift in the X direction.
   :param flag: Flags for special conditions (e.g., anti-air moves).

.. function:: CheckGamenGai()

   Checks if the character is off-screen.

   :return: 1 if off-screen, 0 otherwise.

.. function:: CheckGamenGaiMuki()

   Checks if the character is off-screen in the direction they're facing.

   :return: 1 if off-screen, 0 otherwise.

.. function:: CheckGamenHaji(offx)

   Checks if the character is at the edge of the screen. (Deprecated)

   :param offx: Offset to check.
   :return: 1 if at the edge, 0 otherwise.

.. function:: GetGamenHajiDistance(tbl={})

   Calculates the distance to the screen edge in the facing direction. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the screen edge.

.. function:: GetHaimenGamenHajiDistance(tbl={})

   Calculates the distance to the screen edge behind the character. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the screen edge behind.

.. function:: GetNearStageHajiDistance(tbl={})

   Calculates the distance to the nearest stage edge. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the nearest stage edge.

.. function:: GetStageHajiDistance(tbl={})

   Calculates the distance to the stage edge in the facing direction. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the stage edge in the facing direction.

.. function:: GetHaimenStageHajiDistance(tbl={})

   Calculates the distance to the stage edge behind the character. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the stage edge behind.

.. function:: GetNoEnemyMukiStageHajiDistance(tbl={})

   Calculates the distance to the stage edge opposite to the enemy's position. (Deprecated)

   :param tbl: A table of options (optional).
   :return: The distance to the stage edge opposite to the enemy.

.. function:: SetMuki_PlayerPosition()

   Sets the character's facing direction towards the player character.

.. function:: SetMuki_CCharaPosition(tpos)

   Sets the character's facing direction towards a specified position.

   :param tpos: The target position.

.. function:: GetParentMvStatus()

   Retrieves the MvStatus of the parent character.

   :return: The parent's MvStatus.

.. function:: GetPlayerMvName()

   Retrieves the MvName of the player character.

   :return: The player's MvName.

.. function:: GetParentMvName()

   Retrieves the MvName of the parent character.

   :return: The parent's MvName.

.. function:: GetParentFrameID()

   Retrieves the FrameID of the parent character.

   :return: The parent's FrameID.

.. function:: GetPlayerMvStatus()

   Retrieves the MvStatus of the player character.

   :return: The player's MvStatus.

.. function:: GetPlayerFrameID()

   Retrieves the FrameID of the player character.

   :return: The player's FrameID.

.. function:: SetPlayerFrameID(frameid=0)

   Sets the FrameID of the player character.

   :param frameid: The FrameID to set.

.. function:: CheckPlayerFireballLimit(num=0)

   Checks the fireball limit for the player.

   :param num: The slot number to check.
   :return: The current fireball count for the specified slot.

.. function:: SetPlayerFireballCount(_slot=0, _num=0)

   Sets the fireball count for a specified slot.

   :param _slot: The slot to set.
   :param _num: The count to set.

.. function:: CCharaVector_GetToolAngle(vec=null)

   Calculates the tool angle from a vector.

   :param vec: The vector to use (uses current vector if null).
   :return: The calculated tool angle.

.. function:: JumpFrameID_NotHoldButton(tbl)

   Jumps to a specified FrameID if a button is not held.

   :param tbl: A table containing mask, checkid, and jumpid.
   :return: The result of the jump operation.

.. function:: JumpFrameID_NotHoldAllButton(tbl)

   Jumps to a specified FrameID if all specified buttons are not held.

   :param tbl: A table containing mask, checkid, and jumpid.
   :return: The result of the jump operation.

.. function:: JumpFrameID_NoHoldButton_MaskCheck(tbl, buttonMaskCheck=1)

   Internal function for handling frame jumps based on button hold states. This function should not be called directly.

   :param tbl: A table containing various parameters for the jump check.
   :param buttonMaskCheck: Determines the button hold check type (1 for any button, 100 for all buttons).
   :return: The result of the jump operation or -1 if no jump occurred.

   Key features:
   - Checks button hold states
   - Handles extend actions
   - Manages frame jumps based on specified conditions
   - Supports reversal actions and IC techniques

   Parameters in 'tbl':
   - flags: Additional control flags
   - mask: Button mask for hold checks
   - checkid: Frame ID(s) to check for jumps
   - jumpid: Frame ID(s) to jump to
   - endid: Frame ID to mark the end of an extend action

   This function is the core implementation for `JumpFrameID_NotHoldButton` and `JumpFrameID_NotHoldAllButton`.
   It should not be used directly in game logic.

.. function:: SetPattern_NotHoldButton(tbl)

   Handles pattern jumps based on button hold states.

   :param tbl: A table containing various parameters for the pattern jump check.
   :return: -1 if no action taken, 1 if a jump occurred due to button not being held.

   Key features:
   - Checks button hold states
   - Manages pattern and frame jumps based on specified conditions
   - Handles extend actions
   - Supports reversal actions and IC techniques
   - Manages cache pre-loading for performance optimization

   Parameters in 'tbl':
   - flags: Additional control flags
   - ButtonMask: Button mask for hold checks
   - CheckFrameID: Frame ID(s) to check for jumps
   - SetPattern: Pattern to set when jumping
   - JumpFrameID: Frame ID(s) to jump to (optional)
   - EndFrameID: Frame ID to mark the end of an extend action (optional)
   - EndGuardFlag: Guard flag to set at the end of an extend action (optional)

   Note: This function should not be called from placed objects as it sets flags on the player.

.. function:: SetCamera_Focus_PlayerPosition(tbl)

   Sets camera focus on the player's position.

   :param tbl: A table containing camera focus parameters.

.. function:: SetCamera_Focus_EnemyPosition(tbl)

   Sets camera focus on the nearest enemy's position.

   :param tbl: A table containing camera focus parameters.
   :return: 0 if enemy retrieval failed, undefined otherwise.

.. function:: GetHanteiRect_Player(tbl)

   Retrieves the hitbox rectangle for the player character.

   :param tbl: A table containing parameters for the hitbox check.
   :return: The hitbox rectangle for the player.

.. function:: SetPosition_DamageHanteiRect(tbl={})

   Adjusts the position of the character based on the hitbox of the enemy.

   :param tbl: A table containing parameters for the position adjustment, including power and distance.

   This function checks the distance to the enemy and adjusts the character's position accordingly, ensuring proper behavior during interactions.

   Note: This function includes checks for ground states and other conditions to prevent unwanted behavior.

.. function:: GetHanteiRectArray(pos)

   Returns the hitbox type based on the specified position.

   :param pos: The position to check (e.g., "頭", "首", "腹", "足").
   :return: An array representing the hitbox type for the specified position.

.. function:: ThrowRelease(tbl)

   Handles the release of a throw, managing various parameters related to the throw.

   :param tbl: A table containing parameters for the throw release, including position, frame, and type.

.. function:: ThrowParam_WithHanteiEtc(_pat=0, _frame=0)

   Sets parameters for a throw based on specific hitbox checks.

   :param _pat: The pattern number for the throw.
   :param _frame: The frame number for the throw.
   :return: None.

.. function:: MoveEnemyEtcRect(power, _flags=0)

   Moves the enemy character to a specified position based on various flags.

   :param power: The strength of the movement adjustment.
   :param _flags: Flags controlling movement behavior (e.g., disable X/Y coordinates).

.. function:: array_rand(foo)

   Returns a random element from an array or the element itself if not an array.

   :param foo: The input, which can be an array or a single value.
   :return: A random element if an array, or the original value if not.

.. function:: GamePos2ShiftPos(pos)

   Converts game coordinates to offset coordinates relative to the character's position.

   :param pos: The original game position.
   :return: The converted position.

.. function:: DrawBladeEffect(tbl={})

   Draws a blade effect at a specified position.

   :param tbl: A table containing parameters for the effect, including position and pattern.

.. function:: Call_FootStepSE()

   Calls an object to play a footstep sound effect.

   :return: The created object for the footstep sound effect.

.. function:: ScreenEffect(tbl={})

   Creates a screen-wide effect based on specified parameters.

   :param tbl: A table containing parameters for the effect, including position and pattern.
   :return: The created effect object.

.. function:: ScreenEffect_LimitMv(tbl={})

   Creates a limited movement screen effect based on specified parameters.

   :param tbl: A table containing parameters for the effect.
   :return: The created effect object.

.. function:: DrawIncreaseEffect(tbl={})

   Draws an increase effect at a specified position.

   :param tbl: A table containing parameters for the effect, including position and pattern.

.. function:: CreateObjectEX(tbl)

   Creates an extended object with specified parameters.

   :param tbl: A table containing parameters for the object creation, including position, movement type, and flags.
   :return: The created object.

.. function:: DivHomingTarget(tbl)

   Moves towards a target with specified offsets.

   :param tbl: A table containing parameters for the target, including offsets and frame settings.

.. function:: HomingTarget(tbl)

   Moves towards a target based on specified parameters.

   :param tbl: A table containing parameters for the target, including position and speed settings.

.. function:: HomingTarget2(tbl)

   Adjusts the homing behavior towards a target with additional angle checks.

   :param tbl: A table containing parameters for the target, including position and speed settings.

.. function:: SetAngle_fromVector()

   Sets the angle of the character based on the current movement vector.

.. function:: ScreenEffect_LimitPat(tbl)

   Creates a screen effect that is limited to a specific pattern.

   :param tbl: A table containing parameters for the effect.
   :return: The created effect object.

.. function:: DrawEffect_LimitPat(tbl)

   Draws an effect with limited duration based on a specified pattern.

   :param tbl: A table containing parameters for the effect, including flags and object flags.
   :return: The created effect object.

.. function:: NoCansel_NoAttackHit(tbl={})

   Prevents follow-up attacks if a cancellation did not occur.

   :param tbl: A table containing parameters for the no-cancel behavior, including overwrite and multiplication adjustments.

.. function:: CheckNoCansel()

   Checks if a cancellation has occurred.

   :return: 1 if no cancellation occurred, 0 otherwise.

.. function:: EnemyNoAttackHit()

   Marks the enemy as unable to be followed up after a hit.

   :return: None.

.. function:: ThrowMv_CanselRelease(tbl={})

   Releases a throw if the action was canceled.

   :param tbl: A table containing parameters for the throw release.
   :return: 1 if the throw was released, 0 otherwise.

.. function:: SetStatus_AirAtkStatus()

   Initializes the status for air attacks during jump attacks.

   This function sets various flags and statuses related to air attacks and checks for specific conditions based on the current move status.

.. function:: MoveCode

   A collection of functions for managing movement codes.

   - **AddFlag(flag)**: Adds a specified flag to the movement code.
   - **DelFlag(flag)**: Removes a specified flag from the movement code.
   - **CheckFlag(flag)**: Checks if a specified flag is set in the movement code.

.. function:: MoveCodeEx

   A collection of functions for managing extended movement codes.

   - **AddFlag(pos, flag)**: Adds a specified flag to the extended movement code at the given position.
   - **DelFlag(pos, flag)**: Removes a specified flag from the extended movement code at the given position.
   - **CheckFlag(pos, flag)**: Checks if a specified flag is set in the extended movement code at the given position.

.. function:: ChangeMoveCodeEx_CheckFlag(pos, flag)

   Checks if a specified flag is set in the previous movement code.

   :param pos: The position to check.
   :param flag: The flag to check.
   :return: 1 if the flag is set, 0 otherwise.

.. function:: SetTechReverse(_checkFurimuki=1)

   Sets the throw direction (normal or reverse) based on stick input and character orientation.

   :param _checkFurimuki: If 1, checks for character orientation before determining throw direction. Default is 1.

   This function checks the stick input and character orientation to determine if the throw should be reversed.

.. function:: MvAction.CheckFlag(flag)

   Checks if a specified action code flag is set.

   :param flag: The flag to check.
   :return: 1 if the flag is set, 0 otherwise.

.. function:: GS_AddFlag(flag)

   Adds a specified flag to the global status.

   :param flag: The flag to add.

.. function:: GS_DelFlag(flag)

   Removes a specified flag from the global status.

   :param flag: The flag to remove.

.. function:: GS_CheckFlag(flag)

   Checks if a specified flag is set in the global status.

   :param flag: The flag to check.
   :return: 1 if the flag is set, 0 otherwise.

.. function:: EnemyGS_CheckFlag(flag)

   Checks if a specified flag is set in the enemy's global status.

   :param flag: The flag to check.
   :return: The result of the flag check.

.. function:: Core.Push(core)

   Pushes the character data of the specified core character.

   :param core: The character data to push.
   :return: 1 if successful, 0 if the core character is not done.

.. function:: Core.FuncPush(core, func)

   Pushes the character data of the specified core character and executes a function.

   :param core: The character data to push.
   :param func: The function to execute after pushing.
   :return: The result of the function execution.

.. function:: SmartSteer.ClearCheck()

   Clears the smart steer check based on the command input.

   :return: 1 if cleared, 0 otherwise.

.. function:: SmartSteer.CheckBonus(type=1)

   Checks for bonus conditions based on the specified type.

   :param type: The type of bonus check (1 for standard, 2 for crouch, 3 for air).
   :return: 1 if a bonus condition is met, 0 otherwise.

.. function:: SetComboChainMvParam()

   Sets parameters for combo chain movements based on command input.

   :return: None.

.. function:: CancelCheck_NormalAtk()

   Checks for cancellation conditions when performing a normal attack.

   :return: 1 if cancellation is allowed, 0 otherwise.

.. function:: MvRule_Skill_HitInterrupt()

   Handles hit interruption for skills.

   :return: None.

.. function:: MvRule_Skill_LastUpdate()

   Finalizes the hit interruption for skills.

   :return: None.

.. function:: MvRule_Atk_HitInterrupt()

   Handles hit interruption for attacks.

   :return: None.

.. function:: MvRule_AirAtk_HitInterrupt()

   Handles hit interruption for air attacks.

   :return: None.

.. function:: CallSupport()

   Calls support actions based on specified parameters.

   :return: An array of callable move names.

.. function:: CallCancelSupport_Effect()

   Handles effects for canceling support actions.

   :return: None.

.. function:: CallSupport_Effect()

   Calls effects related to support actions.

   :return: None.

.. function:: GetHPBalance()

   Retrieves the health point balance between the player and the enemy.

   :return: 0 if retrieval failed or a draw, positive if the player is ahead, negative if the enemy is ahead.

.. function:: ComboPoint_Multi(_par)

   Multiplies the current combo point by a specified percentage.

   :param _par: The percentage to multiply the combo point by.
   :return: 1 if successful, 0 if failed.

.. function:: SoundStatus_CheckFlag(_flag)

   Checks if a specified sound status flag is set.

   :param _flag: The flag to check.
   :return: The result of the flag check.

.. function:: SoundStatus_AddFlag(_flag)

   Adds a specified flag to the sound status.

   :param _flag: The flag to add.

.. function:: SoundStatus_DelFlag(_flag)

   Removes a specified flag from the sound status.

   :param _flag: The flag to remove.

.. function:: IWEXIST_CallOnePunch()

   Calls an object to perform a single punch after an IW (Instant Win) activation.

   :return: None.

.. function:: UseGRDStock(cost, enemyadd=0)

   Consumes the player's GRD stock and adds to the enemy's GRD if there is a shortage.

   :param cost: The amount of GRD to consume.
   :param enemyadd: The amount to add to the enemy's GRD if there is not enough stock.
   :return: None.

.. function:: SetHitMuteki(_paramno=1, _num=8, _flag=_HitCheckFlag_Head)

   Sets invincibility status based on specified parameters.

   :param _paramno: The parameter number to check.
   :param _num: The specific value to check against.
   :param _flag: The hit check flag to set.
   :return: 1 if invincibility was set, 0 otherwise.

.. function:: SetHitMutekiParam1(param={})

   Sets invincibility parameters based on the specified conditions.

   :param param: A table of parameters for invincibility settings.
   :return: 1 if successful, 0 otherwise.

.. function:: SetHitMuteki2_Param1(param={})

   Sets invincibility parameters for multiple flags based on the specified conditions.

   :param param: A table of parameters for invincibility settings.
   :return: 1 if successful, 0 otherwise.

.. function:: SetHitCheckFlag(_paramno=1, _num=8, _flag=_HitCheckFlag_Head, _defaultflag=0)

   Sets hit check flags based on the specified parameters.

   :param _paramno: The parameter number to check.
   :param _num: The specific value to check against.
   :param _flag: The hit check flag to set.
   :param _defaultflag: The default flag to set if specified.
   :return: None.

.. function:: SetThrowEnemyMuteki(_mutekiframe=0)

   Sets invincibility for the enemy during a throw.

   :param _mutekiframe: The duration of invincibility.
   :return: None.

.. function:: SetCaptureCharaMuteki(_mutekiframe=0)

   Sets invincibility for the captured character.

   :param _mutekiframe: The duration of invincibility.
   :return: None.

.. function:: GetFrameIDStatus()

   Retrieves the FrameID status, adjusting for frame updates.

   :return: The adjusted FrameID.

.. function:: GetUpdateFrameID(_mvs=0)

   Retrieves the updated FrameID, adjusting for frame updates.

   :param _mvs: The move status to check (optional).
   :return: The updated FrameID.

.. function:: GetUpdateParam0(_mvs=0)

   Retrieves the updated Param0 value, adjusting for frame updates.

   :param _mvs: The move status to check (optional).
   :return: The updated Param0 value.

.. function:: GetUpdateParam1(_mvs=0)

   Retrieves the updated Param1 value, adjusting for frame updates.

   :param _mvs: The move status to check (optional).
   :return: The updated Param1 value.

.. function:: GetUpdateParam2(_mvs=0)

   Retrieves the updated Param2 value, adjusting for frame updates.

   :param _mvs: The move status to check (optional).
   :return: The updated Param2 value.

.. function:: GetUpdateParam3(_mvs=0)

   Retrieves the updated Param3 value, adjusting for frame updates.

   :param _mvs: The move status to check (optional).
   :return: The updated Param3 value.

.. function:: JumpStatus.Set(flag)

   Sets the jump status flag.

   :param flag: The flag to set.
   :return: None.

.. function:: JumpStatus.Add(flag)

   Adds a specified flag to the jump status.

   :param flag: The flag to add.
   :return: None.

.. function:: JumpStatus.Del(flag)

   Removes a specified flag from the jump status.

   :param flag: The flag to remove.
   :return: None.

.. function:: JumpStatus.Check(flag)

   Checks if a specified jump status flag is set.

   :param flag: The flag to check.
   :return: 1 if the flag is set, 0 otherwise.

.. function:: CheckObjectisYarare(param={})

   Checks if an attack hitbox has hit the object, including projectile interactions.

   :param param: A table of parameters for the check.
   :return: Flags indicating the result of the check (e.g., hit or cancel).

.. function:: CheckObjectHanteiCross(_hantei, param={})

   Checks if an attack hitbox has intersected with an object, used for handling projectile interactions.

   :param _hantei: The type of hitbox to check against.
   :param param: Additional parameters for the check.
   :return: 1 if the hitbox intersects, otherwise 0.

.. function:: SetVector_ReduceYVecNoLanding(_offydot=0)

   Adjusts the vertical vector to converge without landing.

   :param _offydot: The offset in Y to apply.
   :return: None.

.. function:: SetVector_YVecFrameLanding(_frame=22)

   Sets the vertical vector to land at a specified frame.

   :param _frame: The frame at which to land.
   :return: None.

.. function:: CheckDamageTiming()

   Checks if an attack hits at the right timing.

   :return: 1 if the timing is correct, otherwise 0.

.. function:: CheckFrameID(_FrameID)

   Checks if the current FrameID matches the specified FrameID or any in an array.

   :param _FrameID: The FrameID or array of FrameIDs to check against.
   :return: 1 if a match is found, otherwise 0.

.. function:: CheckDamageTiming_FrameID(_FrameID=0)

   Checks if the current FrameID matches the specified FrameID and if the damage timing is correct.

   :param _FrameID: The FrameID to check against.
   :return: 1 if both conditions are met, otherwise 0.

.. function:: GetUpdateFrameID_DamageTiming()

   Retrieves the updated FrameID if the damage timing is correct.

   :return: The updated FrameID if timing is correct, otherwise 0.

.. function:: CheckGuardTiming()

   Checks if a guard action occurred at the right timing.

   :return: 1 if the timing is correct, otherwise 0.

.. function:: CheckGuardTiming_FrameID(_FrameID=0)

   Checks if the current FrameID matches the specified FrameID and if the guard timing is correct.

   :param _FrameID: The FrameID to check against.
   :return: 1 if both conditions are met, otherwise 0.

.. function:: CheckHitTiming()

   Checks if a hit occurred during the action.

   :return: 1 if a hit occurred, otherwise 0.

.. function:: CheckAnyHitTiming()

   Checks if any hit occurred, including during atemi (counter) actions.

   :return: 1 if any hit occurred, otherwise 0.

.. function:: CheckHitTiming_FrameID(_FrameID=0)

   Checks if the current FrameID matches the specified FrameID and if the hit timing is correct.

   :param _FrameID: The FrameID to check against.
   :return: 1 if both conditions are met, otherwise 0.

.. function:: CheckSousaiHitTiming()

   Checks if a canceling hit occurred during an attack.

   :return: 1 if a hit occurred, otherwise 0.

.. function:: CheckCatchedTiming_FlagHit()

   Checks if a hit occurred when a character was caught.

   :return: 1 if a hit occurred, otherwise 0.

.. function:: AddDamageFlagInterrupt(flag)

   Adds a damage flag during a hit interrupt.

   :param flag: The flag to add.
   :return: 1 if the flag was added, otherwise 0.

.. function:: SetKirifudaKaraburiEffect()

   Sets the effect for a missed special move.

   :return: None.

.. function:: SetEnemyMuteki_Throw()

   Sets invincibility for the enemy during a throw.

   :return: None.

.. function:: SetDivKeepVector_AirDashMinHeight(_minHeight=def_POS_AirDashHoseiMinHeight, _safeVec=1)

   Sets the vector to ensure a minimum height during an air dash.

   :param _minHeight: The minimum height to maintain.
   :param _safeVec: A flag to indicate safe vector handling.
   :return: 1 if adjustments were made, otherwise 0.

.. function:: CheckFrameUpdateTiming()

   Checks if the current frame is updated and not in a landing state.

   :return: 1 if the timing is correct, otherwise 0.

.. function:: AddXPos_CheckBackStage(_offx, _minx)

   Adjusts the position to ensure the character does not get too close to the back stage edge.

   :param _offx: The offset to apply to the X position.
   :param _minx: The minimum distance to maintain from the back stage edge.
   :return: None.

.. function:: AddXPos_CheckFromtCorner(_offx, _minx)

   Adjusts the position to ensure the character does not get too close to the front stage edge.

   :param _offx: The offset to apply to the X position.
   :param _minx: The minimum distance to maintain from the front stage edge.
   :return: None.

.. function:: SetXPos_BackCorner(_offx=0)

   Sets the character's position to the back corner of the stage with an optional offset.

   :param _offx: The offset to apply to the X position.
   :return: None.

.. function:: SetXPos_FrontCorner(_offx=0)

   Sets the character's position to the front corner of the stage with an optional offset.

   :param _offx: The offset to apply to the X position.
   :return: None.

.. function:: CheckEnemyDistance(_xkyori)

   Checks the distance to the enemy and returns 1 if within the specified range.

   :param _xkyori: The distance threshold to check against.
   :return: 1 if the enemy is within range, otherwise 0.

.. function:: CheckEnemyDistance2(_xmin, _xmax)

   Checks if the enemy's distance is within a specified range.

   :param _xmin: The minimum distance threshold.
   :param _xmax: The maximum distance threshold.
   :return: 1 if within range, otherwise 0.

.. function:: GetEnemyDistanceStatus(_xmin, _xmax)

   Returns the distance status relative to the enemy.

   :param _xmin: The minimum distance threshold.
   :param _xmax: The maximum distance threshold.
   :return: 0 if retrieval fails, -4 if too close, -6 if too far, 1 if within range.

.. function:: GetEnemyDistance()

   Retrieves the distance to the enemy.

   :return: The distance to the enemy, or 0 if the enemy is not found.

.. function:: CheckFrontStageDistance(_xkyori=0)

   Checks if the distance to the front stage edge is within a specified threshold.

   :param _xkyori: The distance threshold to check against.
   :return: 1 if within range, otherwise 0.

.. function:: CheckBackStageDistance(_xkyori=0)

   Checks if the distance to the back stage edge is within a specified threshold.

   :param _xkyori: The distance threshold to check against.
   :return: 1 if within range, otherwise 0.

.. function:: GetFrontStageDistance()

   Returns the distance to the front stage edge.

   :return: The distance to the front stage edge.

.. function:: GetBackStageDistance()

   Returns the distance to the back stage edge.

   :return: The distance to the back stage edge.

.. function:: GetNearStageDistance()

   Returns the distance to the nearest stage edge.

   :return: The distance to the nearest stage edge.

.. function:: CheckFromtCornerDistance_with_RoundEnd(_xkyori=0)

   Checks the distance to the front corner considering round end conditions.

   :param _xkyori: The distance threshold to check against.
   :return: The result of the distance check.

.. function:: CheckBackCornerDistance_with_RoundEnd(_xkyori=0)

   Checks the distance to the back corner considering round end conditions.

   :param _xkyori: The distance threshold to check against.
   :return: The result of the distance check.

.. function:: CheckFromtCornerDistance(_xkyori=0)

   Checks if the distance to the front corner is within a specified threshold.

   :param _xkyori: The distance threshold to check against.
   :return: 1 if within range, otherwise 0.

.. function:: CheckBackCornerDistance(_xkyori=0)

   Checks if the distance to the back corner is within a specified threshold.

   :param _xkyori: The distance threshold to check against.
   :return: 1 if within range, otherwise 0.

.. function:: GetFrontCornerDistance()

   Returns the distance to the front corner of the screen.

   :return: The distance to the front corner.

.. function:: GetBackCornerDistance()

   Returns the distance to the back corner of the screen.

   :return: The distance to the back corner.

.. function:: GetCeilCprnerDistance()

   Returns the distance to the ceiling of the stage.

   :return: The distance to the ceiling.


.. function:: PullEnemy_HanteiCross(_frame=100, _src=[_Hantei_Etc, 0, 1], _dst=[_Hantei_Kurai, 0, -1])

   Pulls the enemy towards the character based on hitbox intersection.

   :param _frame: The frame duration for the pull effect.
   :param _src: The source hitbox for the check.
   :param _dst: The destination hitbox for the check.
   :return: None.

.. function:: PushEnemy_HanteiCross(_frame=100, _src=[_Hantei_Etc, 0, 1], _dst=[_Hantei_Kurai, 0, -1])

   Pushes the enemy away from the character based on hitbox intersection.

   :param _frame: The frame duration for the push effect.
   :param _src: The source hitbox for the check.
   :param _dst: The destination hitbox for the check.
   :return: None.

.. function:: PullEnemy_Etc0xKurai(_frame)

   Pulls the enemy based on special hitbox type 0.

   :param _frame: The frame duration for the pull effect.
   :return: None.

.. function:: PullEnemy_Etc1xKurai(_frame)

   Pulls the enemy based on special hitbox type 1.

   :param _frame: The frame duration for the pull effect.
   :return: None.

.. function:: PushEnemy_Etc1xKurai(_frame)

   Pushes the enemy based on special hitbox type 1.

   :param _frame: The frame duration for the push effect.
   :return: None.

.. function:: PullEnemy_Etc4xKurai(_frame)

   Pulls the enemy based on special hitbox type 4.

   :param _frame: The frame duration for the pull effect.
   :return: None.

.. function:: SetPos_MarkingTarget(_core, _par=5, _dfoy=-150, _miny=0)

   Sets the position of a marking target based on specified parameters.

   :param _core: The target character data.
   :param _par: The parameter for marking.
   :param _dfoy: The offset in Y position.
   :param _miny: The minimum Y position to maintain.
   :return: None.

.. function:: GetPos_MarkingTarget(_core, _par=5, _dfoy=-150, _miny=0)

   Retrieves the position of a marking target based on specified parameters.

   :param _core: The target character data.
   :param _par: The parameter for marking.
   :param _dfoy: The offset in Y position.
   :param _miny: The minimum Y position to maintain.
   :return: The position of the marking target or 0 if not found.

.. function:: SetPos_MarkingPlayer(_par=5, _dfoy=-150)

   Sets the position of the marking player based on specified parameters.

   :param _par: The parameter for marking.
   :param _dfoy: The offset in Y position.
   :return: None.

.. function:: SetPos_MarkingEnemy(_par=5, _dfoy=-150)

   Sets the position of the marking enemy based on specified parameters.

   :param _par: The parameter for marking.
   :param _dfoy: The offset in Y position.
   :return: None.

.. function:: BackScreenBlack_Start(_time=600)

   Starts a black screen effect for a specified duration.

   :param _time: The duration of the black screen effect.
   :return: None.

.. function:: BackScreenBlack_Check()

   Checks the status of the black screen effect.

   :return: None.

.. function:: CheckDownOiuti()

   Checks for downed state interactions.

   :return: 0 if no interactions are found.

.. function:: EnemyDamageFlag_Add(_flag)

   Adds a damage flag to the enemy.

   :param _flag: The flag to add.
   :return: None.

.. function:: EnemyDamageFlag_Del(_flag)

   Removes a damage flag from the enemy.

   :param _flag: The flag to remove.
   :return: None.

.. function:: EnemyDamageFlag_Check(_flag)

   Checks if a specified damage flag is set for the enemy.

   :param _flag: The flag to check.
   :return: 0 or 1 based on the flag status.

.. function:: IsMatchMvNameArray(_ar)

   Checks if the current move name matches any in the specified array.

   :param _ar: The array of move names to check against.
   :return: 1 if a match is found, otherwise 0.

.. function:: IsMatchChangeMvNameArray(_ar)

   Checks if the previous move name matches any in the specified array.

   :param _ar: The array of move names to check against.
   :return: 1 if a match is found, otherwise 0.

.. function:: CallSkillSoonCache(_frameid, _rest)

   Calls a skill action with a specified frame ID and remaining duration.

   :param _frameid: The frame ID for the skill.
   :param _rest: The remaining duration for the skill action.
   :return: None.

.. function:: SetVorpalPattern(_pat=0)

   Sets the Vorpal pattern if the GRD condition is met.

   :param _pat: The pattern to set.
   :return: 1 if the pattern was set, 0 otherwise.

.. function:: SetVorpalAtkEffect()

   Sets the effect for Vorpal attacks.

   :return: None.

.. function:: EnemyGRD_Minus(_val, _drainval=0, _useflag=0)

   Reduces the enemy's GRD by a specified amount and adds to their drain value.

   :param _val: The amount to reduce from the enemy's GRD.
   :param _drainval: The amount to drain from the enemy's GRD.
   :param _useflag: The flag indicating the type of drain.
   :return: None.

.. function:: EnemyGRD_Drain(_val, _useflag=0)

   Drains a specified amount of GRD from the enemy.

   :param _val: The amount to drain from the enemy's GRD.
   :param _useflag: The flag indicating the type of drain.
   :return: None.

.. function:: LP_Rebagatya_Init(_LP0=0, _LP1=1, _LP2=2)

   Initializes the LP (button press) counters.

   :param _LP0: The LP counter for button presses.
   :param _LP1: The LP counter for the last button pressed.
   :param _LP2: The LP counter for the last stick movement.
   :return: None.

.. function:: LP_Rebagatya_Update(_LP0=0, _LP1=1, _LP2=2)

   Updates the LP counters based on button and stick inputs.

   :param _LP0: The LP counter for button presses.
   :param _LP1: The LP counter for the last button pressed.
   :param _LP2: The LP counter for the last stick movement.
   :return: None.

.. function:: DrawDebugRect(param={})

   Draws a debug rectangle at a specified position.

   :param param: A table containing parameters for the rectangle, including position.
   :return: None.

.. function:: DrawDebugRectPos(pos)

   Draws a debug rectangle at the specified position.

   :param pos: The position to draw the rectangle at.
   :return: None.

.. function:: SupSt_AddFlag(flag)

   Adds a specified flag to the support character's status.

   :param flag: The flag to add.
   :return: None.

.. function:: SupSt_DelFlag(flag)

   Removes a specified flag from the support character's status.

   :param flag: The flag to remove.
   :return: None.

.. function:: SupSt_CheckFlag(flag)

   Checks if a specified flag is set in the support character's status.

   :param flag: The flag to check.
   :return: 1 if the flag is set, 0 otherwise.

.. function:: SetPP_JumpStartHeight()

   Sets the jump start height based on the character's current position.

   :return: None.


.. function:: SupportSetMuki(_flag=_Direction_Auto)

   Aligns the support character and its parent to face the specified direction.

   :param _flag: The direction to face, defaults to automatic direction.
   :return: None.

.. function:: LP_Rebagatya_Check(param={})

   Checks the LP (button press) counters against a list of thresholds.

   :param param: A table containing parameters for the check, including the LP slot and a list of thresholds.
   :return: The level of LP achieved based on the thresholds.

.. function:: SetHosyoHosei(_val=100)

   Sets the minimum guarantee adjustment value for combo damage.

   :param _val: The new guarantee adjustment value.
   :return: None.

.. function:: SetHosyoHosei_Multi(_par)

   Multiplies the minimum guarantee adjustment value for combo damage.

   :param _par: The percentage to multiply the current guarantee adjustment value by.
   :return: None.

.. function:: SetSpHosyoHosei(param={})

   Sets the guarantee adjustment based on the specified parameters, considering various conditions like dying state and Vorpal status.

   :param param: A table containing parameters for the adjustment.
   :return: 1 if successful, 0 if already set.

.. function:: CallSkillSoonCaches(...)

   Reserves FrameIDs for the current pattern based on the specified parameters.

   :param ...: A variable-length argument list containing FrameID and duration pairs.
   :return: None.

.. function:: CallSoonCaches_noFrameID(...)

   Reserves the current pattern without specifying FrameIDs.

   :param ...: A variable-length argument list containing duration pairs.
   :return: None.

.. function:: CallSkillSoonCaches_AnoterPat(_patstr, ...)

   Reserves FrameIDs for a different pattern based on the specified parameters.

   :param _patstr: The pattern string to use for the reservation.
   :param ...: A variable-length argument list containing FrameID and duration pairs.
   :return: None.

.. function:: CallSkillLandCache_Param2(_param2, _frameid, _rest=4)

   Reserves a FrameID in the cache if the specified Param2 matches.

   :param _param2: The parameter to check against.
   :param _frameid: The FrameID to reserve.
   :param _rest: The remaining duration for the reservation.
   :return: None.

.. function:: CallAddSkillCache(_patstr, _rest)

   Reserves an additional skill action based on the specified pattern and duration.

   :param _patstr: The pattern string for the additional skill.
   :param _rest: The remaining duration for the reservation.
   :return: None.

.. function:: CallLoopEndCache_FrameID(_pat, _frameid, _frame=10, _rest=2)

   Reserves a loop end FrameID for the specified pattern.

   :param _pat: The pattern to reserve.
   :param _frameid: The FrameID to reserve.
   :param _frame: The frame duration for the reservation.
   :param _rest: The remaining duration for the reservation.
   :return: None.

.. function:: CallSamePatLoopEndCache_FrameID(_frameid, _frame=10, _rest=2)

   Reserves a loop end FrameID for the current pattern.

   :param _frameid: The FrameID to reserve.
   :param _frame: The frame duration for the reservation.
   :param _rest: The remaining duration for the reservation.
   :return: None.

.. function:: AddAirSkillCount(_slot=0, _val=1, _mvs=0)

   Adds a count for air skills after a specified number of frames.

   :param _slot: The slot to increment.
   :param _val: The value to add to the count.
   :param _mvs: The move status to check (optional).
   :return: 1 if the count was added, otherwise 0.


.. function:: SupportAtk_EscapeFinalize()

   Finalizes the escape action for support attacks.

   :return: None.

.. function:: SupportAtk_Init()

   Initializes the support attack parameters.

   :return: None.

.. function:: SupportAtk_DamageFinalize()

   Finalizes the damage calculations for support attacks.

   :return: None.


.. function:: CheckTuigeki()

   Checks if the timing is appropriate for a follow-up attack.

   :return: 1 if the timing is correct for a follow-up, otherwise 0.

.. function:: CheckDagekiMuteki()

   Checks if the character is in a state of "hit invincibility".

   :return: 1 if in a hit invincibility state, otherwise 0.

.. function:: CheckAirAtkFsiki()

   Checks the conditions for an air attack and updates guard flags accordingly.

   :return: None.


.. function:: CallFreezObject()

   Calls an object to freeze the game state temporarily.

   :return: None.



.. function:: GetJumpVectorPar(_start_y_vec)

   Calculates the jump height as a percentage from start to landing.

   :param _start_y_vec: The starting Y vector value.
   :return: A percentage value representing the jump height.

.. function:: AddMoveCode_CSAntenGaesiSkill()

   Checks if the last action was a chain shift and sets the corresponding flag.

   :return: None.

.. function:: CSAntenGaesi_NoAttackHit()

   Prevents follow-up attacks if the last action was a chain shift.

   :return: None.

.. function:: CSAntenGaesi_DamageHosei(_zyozanHosei=70, _uwagakiHosei=70)

   Applies damage adjustments based on the chain shift status.

   :param _zyozanHosei: The adjustment value for the first hit.
   :param _uwagakiHosei: The adjustment value for subsequent hits.
   :return: None.

.. function:: PassBeforeMoveCodeEx(_pos, _flag)

   Passes the previous move code and adds a flag if conditions are met.

   :param _pos: The position to check.
   :param _flag: The flag to add.
   :return: 1 if the flag was added, otherwise 0.

.. function:: CopyBeforeMoveAction()

   Copies the previous move action to the current action.

   :return: None.

.. function:: SetKezurareDamage(_dmg_val)

   Applies damage to the player if not in a guard state.

   :param _dmg_val: The amount of damage to apply.
   :return: None.

.. function:: CheckMainisDamage()

   Checks for damage state in the main character.

   :return: None.

.. function:: CheckMainisBound()

   Checks if the main character is in a bound state.

   :return: None.



.. function:: PassHitMoveCodes()

   Passes hit-related move codes for follow-up actions. This function is used to maintain the state of various hit-related flags and conditions during attacks.

   :return: None.

.. function:: PassLandMoveCodes()

   Passes landing-related move codes for follow-up actions. This function is used to maintain the state of various landing-related flags and conditions.

   :return: None.

.. function:: CheckEnableFlag_AssaultAirA()

   Checks if the conditions to enable Assault Air A are met.

   :return: 1 if conditions are met, otherwise 0.

.. function:: CheckEnableFlag_AssaultAirB()

   Checks if the conditions to enable Assault Air B are met.

   :return: 1 if conditions are met, otherwise 0.

.. function:: CheckEnableFlag_AssaultAirC()

   Checks if the conditions to enable Assault Air C are met.

   :return: 1 if conditions are met, otherwise 0.

.. function:: CheckParamFlags(paramNum, checkFlag, _mvs=0)

   Checks if a specified parameter contains a certain flag.

   :param paramNum: The parameter number to check (0-3).
   :param checkFlag: The flag to check for.
   :param _mvs: The move status to check (optional).
   :return: 1 if the flag is found, otherwise 0.

.. function:: SetBothCharaInStagePosition()

   Adjusts the position of both characters relative to the stage edges.

   :return: None.

.. function:: GetCreatePosition(pos)

   Converts a world position to a relative position based on the character's current position.

   :param pos: The world position to convert.
   :return: The relative position.

.. function:: GetHitEffectAngle(info, base_angle=0)

   Calculates the hit effect angle based on the specified parameters.

   :param info: The hit information.
   :param base_angle: The base angle to consider.
   :return: The calculated angle.

.. function:: GetPoint(param={})

   Retrieves the hitbox's top-left coordinates based on the specified parameters.

   :param param: A table containing parameters for the hitbox check.
   :return: A table containing the x and y coordinates.

.. function:: SetInActiveEffect()

   Triggers an effect that indicates the character is inactive.

   :return: None.

.. function:: DrawInActiveEffect()

   Draws an effect indicating the character is inactive.

   :return: None.


.. function:: SetNoMovableMove()

   Sets the character to a state where they cannot move or cancel actions.

   :return: None.


.. function:: Achievement_Unlock(slot, training_ok=0)

   Unlocks an achievement based on the specified slot. If `training_ok` is set to 0, achievements from training or tutorial modes cannot be unlocked.

   :param slot: The slot number of the achievement to unlock.
   :param training_ok: A flag indicating if training achievements can be unlocked (default is 0).
   :return: None.

.. function:: CharaAchievement_Increment(slot, name="")

   Increments the achievement count for the specified character and slot. Can handle both character and slot arrays.

   :param slot: The slot number or array of slot numbers to increment.
   :param name: An optional name for debugging purposes.
   :return: None.

.. function:: CharaBattleActivity_Increment(slot, str)

   Increments the battle activity count for the specified character and slot.

   :param slot: The slot number for the activity.
   :param str: A string describing the activity.
   :return: None.

.. function:: CharaBattleActivity_Calc(tbl={})

   Performs calculations related to the character's battle activity based on the provided parameters.

   :param tbl: A table containing parameters for the calculation.
   :return: None.

.. function:: CharaBattleActivity_Count(str)

   Returns the count of a specific battle activity for the current character.

   :param str: The name of the activity to check.
   :return: The count of the specified activity.

.. function:: EnemyCharaBattleActivity_Increment(slot, str)

   Increments the battle activity count for the enemy character.

   :param slot: The slot number for the enemy activity.
   :param str: A string describing the activity.
   :return: None.

.. function:: EnemyCharaBattleActivity_Calc(tbl={})

   Performs calculations related to the enemy's battle activity based on the provided parameters.

   :param tbl: A table containing parameters for the calculation.
   :return: None.

.. function:: EnemyCharaBattleActivity_Count(str)

   Returns the count of a specific battle activity for the enemy character.

   :param str: The name of the activity to check.
   :return: The count of the specified activity.

.. function:: SetFromNoCancelFlag()

   Sets a flag indicating that the character cannot cancel actions if they are in a specific state.

   :return: None.


.. function:: ClearHitStatus_SetChangeMv()

   Clears the hit status and sets the move to a change state.

   :return: None.


.. function:: ExtendTiming()

   Extends the timing for certain actions.

   :return: None.

   
   
.. function:: SetJumpCtrlVector(param={})

   Adjusts the jump control vector based on the specified parameters for jumping mechanics.

   :param param: A table containing parameters such as max, min, and plus for the jump control.
   :return: None.

.. function:: SetVector_SeachJump(param={})

   Adjusts the jump power based on the distance to the enemy, enhancing jump capabilities when needed.

   :param param: A table containing parameters for the jump adjustment.
   :return: None.

.. function:: AddVector_TargetXLen(param={})

   Adjusts the character's X velocity based on the distance to the enemy, slowing down if close and speeding up if far.

   :param param: A table containing parameters for the velocity adjustment.
   :return: None.

.. function:: SetFireBallFlags_InAtemiHitInterrupt(param={})

   Sets flags related to fireball interactions during a successful counter hit.

   :param param: A table containing parameters for the hit status.
   :return: None.

.. function:: CheckParentIsSkill()

   Checks if the parent character is executing a skill.

   :return: 1 if the parent is executing a skill, otherwise 0.

.. function:: PassPlayerToFireBallMvCode()

   Passes relevant move codes from the player to the fireball.

   :return: None.

.. function:: PassAddSkillMoveCodes()

   Passes additional skill move codes for follow-up actions.

   :return: None.

.. function:: SetSpecialEXSLimit_Enemy(exs_limit=70)

   Sets a limit on the enemy's EX skill gauge.

   :param exs_limit: The limit value for the EX skill gauge.
   :return: 1 if the limit was successfully set, otherwise 0.


.. function:: GetStickHold_FurimukiReverse()

   Checks the stick input and reverses the direction if the character is supposed to turn.

   :return: The adjusted stick input value.

.. function:: CheckCharaIsSPActionProduction()

   Checks if either the player or the enemy character is currently executing a special action.

   :return: 1 if either character is executing a special action, otherwise 0.

.. function:: CheckEnemyIsSPActionProduction()

   Checks if the enemy character is currently executing a special action.

   :return: 1 if the enemy is executing a special action, otherwise 0.

.. function:: CheckPlayerIsSPActionProduction()

   Checks if the player character is currently executing a special action.

   :return: 1 if the player is executing a special action, otherwise 0.

.. function:: CheckExSpecialCancel()

   Checks if an EX special cancel is possible based on the current move state.

   :return: 1 if cancel is possible, otherwise 0.

.. function:: SetDamageMutekiFrame(_frame=60)

   Sets a temporary invincibility frame when the character takes damage.

   :param _frame: The duration of the invincibility frame.
   :return: None.

.. function:: CheckLastDamageCharaIsPlayer()

   Checks if the last character that dealt damage was the player.

   :return: 1 if the last damage was dealt by the player, otherwise 0.

.. function:: EnemyDamageFlag_DelayAdd(flags)

   Adds a delay to the enemy's damage flags.

   :param flags: The flags to add.
   :return: None.

.. function:: EnemyDamageFlag_DamageOnlyDelayAdd(flags)

   Adds a delay to the enemy's damage flags, only for damage-related flags.

   :param flags: The flags to add.
   :return: None.

.. function:: RecoverDoubleExHohoHosei()

   Adjusts the damage scaling for double EX skills to prevent excessive damage reduction.

   :return: None.

.. function:: InitRecover()

   Initializes the recovery state for the character after a hit.

   :return: None.

.. function:: CallSystemHereYouAre()

   Displays a "YOU" message for the player during network battles.

   :return: None.

.. function:: Play_SubtitleVoice(_se, _delay=120)

   Plays a subtitle voice line with an optional delay.

   :param _se: The sound effect ID to play.
   :param _delay: The delay before playing the sound effect (default is 120).
   :return: None.



.. function:: SetSkillMvChipDamage()

   Sets the chip damage value for a skill move. The damage is calculated as 1/8 of the attack power.

   :return: None.

.. function:: EXSLimit_EXSkillObject()

   Applies a limit to the gauge increase during the execution of an EX skill.

   :return: None.

.. function:: CallEXSkillAntenEffect(param={})

   Calls the effect for an EX skill during a transition, managing visual effects and invincibility states.

   :param param: A table containing parameters for the effect.
   :return: None.

.. function:: CallVorpalEXSChaege(_fra=25, _val=100)

   Charges the Vorpal gauge during specific conditions.

   :param _fra: The frame duration for the charge (default is 25).
   :param _val: The value to add to the gauge (default is 100).
   :return: None.

.. function:: GetGuardMuki(pl=0)

   Retrieves the expected guard direction based on the character's position and the enemy's position.

   :param pl: 0 for the player, 1 for the enemy.
   :return: The expected guard direction (1 for left, -1 for right).

.. function:: CheckExtraTraining()

   Checks if the character is currently in extra training mode.

   :return: The value of the extra training gauge, or 0 if not in extra training.

.. function:: EnableExtraTrainingMode()

   Checks if the extra training mode is enabled.

   :return: 1 if enabled, otherwise 0.

.. function:: InvalidateObjectMixupInit_SetLP(lp_slot=0)

   Initializes the mix-up state for the specified LP slot based on the enemy's guard direction.

   :param lp_slot: The LP slot to set (default is 0).
   :return: None.

.. function:: InvalidateObjectMixupUpdate_SetLP(lp_slot=0)

   Updates the mix-up state for the specified LP slot based on the enemy's guard direction.

   :param lp_slot: The LP slot to update (default is 0).
   :return: None.

.. function:: CheckDrawMutekiAnnounce(param={})

   Checks if a muteki (invincibility) announcement should be drawn based on the character's actions.

   :param param: A table containing parameters for the check.
   :return: None.

.. function:: PosShiftFastVector()

   Adjusts the character's position to prevent passing through the enemy when moving too fast.

   :return: None.

.. function:: CheckSPTuigekiDamage()

   Checks if the character can deal damage during a follow-up attack based on the enemy's state.

   :return: 1 if conditions are met, otherwise 0.


.. function:: CheckShieldHoldCommandStrict(checkButtonPos=0)

   Checks if the shield hold command is being executed strictly based on the specified button position.

   :param checkButtonPos: The button position to check against (default is 0).
   :return: 1 if the command is valid, otherwise 0.


Character Flash Effects
""""""""""""""""""""""""

.. function:: SetCharaFlash_Ukemi()

   Sets a green character flash effect for successful ukemi (recovery).

.. function:: SetCharaFlash_ConvertCharge()

   Sets a dark blue character flash effect during convert charge.

.. function:: SetCharaFlash_Counter()

   Sets a red character flash effect for counter hits.

.. function:: SetCharaFlash_Armor()

   Sets a red character flash effect when withstanding attacks with armor.

.. function:: SetCharaFlash_TechMiss()

   Sets a red character flash effect for failed throw escapes.

.. function:: SetCharaFlash_TechSuccessInit()

   Sets a white character flash effect for successful throw escapes.

.. function:: SetCharaFlash_FaultGuardSPInit()

   Sets a red character flash effect for failed guard special inputs.

.. function:: SetCharaFlash_ShieldAtkInit()

   Sets a light red character flash effect for shield attacks.

.. function:: SetCharaFlash_GuardSPCommand(time=10)

   Sets a green character flash effect for guard special command inputs.

.. function:: SetCharaFlash_GuardCansel()

   Sets a white character flash effect for guard cancel activations.

.. function:: SetCharaFlash_GRDJudgeFlash()

   Sets a light purple character flash effect for GRD judge wins or draws.

.. function:: SetCharaFlash_LiberateInit()

   Sets a white character flash effect for Liberate activation.

.. function:: SetCharaFlash_PotentialFlash()

   Sets a light purple character flash effect for Potential activation.

Aura Effects
""""""""""""

.. function:: PcAfterImage_DashAtkInit()

   Initializes afterimage effect for dash attacks.

.. function:: PcAfterImage_EXSkillInit()

   Initializes afterimage effect for EX skills.

.. function:: PcAfterImage_DoudgeInit()

   Initializes after image effect for dodges (Creeping Edge).

.. function:: PcAuraEffect_LiberateInit(isCelestial=false)

   Initializes aura effect for Liberate state.

.. function:: PcAuraEffect_CutinInit()

   Initializes aura effect for cut-in animations.

.. function:: PcAuraEffect_ConvertCharge()

   Initializes aura effect for convert charge.

.. function:: GRDJudgeWinEffect_Init(isCelestial=false)

   Initializes aura effect for GRD judge wins.

.. function:: PcAuraEffect_CommonAuraSet(flag)

   Sets a temporary aura effect based on provided parameters.

.. function:: PcAuraEffect_CommonAuraEnd()

   Clears current aura effects and flags.

.. function:: PcAuraEffect_AllAuraEnd()

   Clears all aura effects and sets the aura management end flag.

.. function:: PcAuraEffect_AuraCheck()

   Checks and updates aura effects based on the current game state.

   This function is called periodically by the aura management system to handle various aura effects, including GRD judge wins and Liberate states.

.. function:: PcAuraEffect_Clear()

   Clears all aura effects.

.. function:: ClearAuraFlag()

   Clears all persistent aura flags.