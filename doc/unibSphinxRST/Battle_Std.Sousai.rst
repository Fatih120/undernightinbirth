Battle_Std.Sousai
==================

Cancel State

Initialization Functions
-------------------------


.. function:: Sousai.Init(_etcHantei=0)

   Initializes the cancellation status for a specified hitbox type.

   :param _etcHantei: Additional parameters for the initialization.
   :return: None.

.. function:: Sousai.Init_NoHitFlag(_etcHantei=0)

   Initializes the cancellation status without hit flags for a specified hitbox type.

   :param _etcHantei: Additional parameters for the initialization.
   :return: None.

.. function:: Sousai.Init_NoGedan(_etcHantei=0)

   Initializes the cancellation status without ground hit flags for a specified hitbox type.

   :param _etcHantei: Additional parameters for the initialization.
   :return: None.

.. function:: Sousai.Init_BallTarget(_etcHantei=0)

   Initializes the ball target for cancellation status.

   :param _etcHantei: Additional parameters for the initialization.
   :return: None.

Setting Functions
------------------

.. function:: Sousai.Set(_etcHantei=0)

   Sets the attack catch flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the setting.
   :return: None.

.. function:: Sousai.Erase(_etcHantei=2)

   Erases the attack catch flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the erasure.
   :return: None.

.. function:: Sousai.Set_NoHitFlag(_etcHantei=0)

   Sets the attack catch flags without hit flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the setting.
   :return: None.

.. function:: Sousai.Set_NoGedan(_etcHantei=0)

   Sets the attack catch flags without ground hit flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the setting.
   :return: None.

.. function:: Sousai.Set_BallTarget(_etcHantei=0)

   Sets the attack catch flags specifically for projectiles.

   :param _etcHantei: Additional parameters for the setting.
   :return: None.

Erasing Function
-----------------

.. function:: Sousai_Erase(_etcHantei=2)

   Erases the cancel state for the enemy character.

   :param int _etcHantei: Optional parameter for additional behavior.

Frame Update Functions
-----------------------

.. function:: Sousai.FrameUpdate(_etcHantei=0)

   Updates the frame for the specified hitbox type.

   :param _etcHantei: Additional parameters for the update.
   :return: None.

.. function:: Sousai.FrameUpdate_NoHitFlag(_etcHantei=0)

   Updates the frame without hit flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the update.
   :return: None.

.. function:: Sousai.FrameUpdate_NoGedan(_etcHantei=0)

   Updates the frame without ground hit flags for the specified hitbox type.

   :param _etcHantei: Additional parameters for the update.
   :return: None.

.. function:: Sousai.FrameUpdate_BallTarget(_etcHantei=0)

   Updates the frame for projectile targets.

   :param _etcHantei: Additional parameters for the update.
   :return: None.

.. function:: Sousai.HitInterrupt(param={})

   Handles the hit interrupt during a cancellation, managing various parameters related to the hit.

   :param param: A table containing parameters for the hit interrupt, including sound options and hit stop duration.
   :return: An instance of `AtemiHitStatus` if a hit occurred, otherwise 0.