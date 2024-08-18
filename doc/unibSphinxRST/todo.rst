
Battle_Std.GetNextMoveTable_Array <- function( ar )
Battle_Std.CheckHanteiAttackExist <- function(code=0)
Battle_Std.SetThrowHitFinalize <- function(code=0, gouin_code=-1, combo_code=-1, miss_code=-1, techmiss_code=-1 )
Battle_Std.CaptureChara_Positioning <- function()
Battle_Std.CheckHanteiDamage <- function()
Battle_Std.GetPP_HitStatus <- function( slot = 0 )
Battle_Std.SetPP_HitStatus <- function( slot = 0 )
Battle_Std.SetPP_ClearHitStatus <- function( slot = -1 )
Battle_Std.DrawPunishAnnounce <- function( anno_flags )


Battle_Std.GetPointStatus_NearEnemy <- function()
Battle_Std.GetNearEnemyMigiAngle <- function()
Battle_Std.GetParentMigiAngle <- function()
Battle_Std.AddToolShift_NoSurinuke <- function(plus_x=0, flag=0)

Battle_Std.GetNoEnemyMukiStageHajiDistance <- function(tbl={})
Battle_Std.SetMuki_PlayerPosition <- function()
Battle_Std.SetMuki_CCharaPosition <- function( tpos )
Battle_Std.JumpFrameID_NoHoldButton_MaskCheck <- function( tbl, buttonMaskCheck=1 )
Battle_Std.SetPattern_NotHoldButton <- function( tbl )// ButtonMask, CheckFrameID, SetPattern, JumpFrameID
Battle_Std.GetHanteiRectArray <- function( pos )
Battle_Std.GetHanteiRect_Player <- function( tbl )
Battle_Std.SetPosition_DamageHanteiRect <- function( tbl={} )
Battle_Std.DrawHitboxChecker <- function()
Battle_Std.DrawPointRepeat <- function()
Battle_Std.DrawPoint <- function( tbl={} )
Battle_Std.DrawRect <- function( tbl={} )
Battle_Std.DrawHanteiRect <- function( rc, color )
Battle_Std.DrawHanteiRect_Outline <- function( rc, color )
Battle_Std.DrawHitBoxes <- function()
Battle_Std.DrawHitBoxes_Outlined <- function()
Battle_Std.MoveEnemyEtcRect <- function( power, _flags=0 )
Battle_Std.array_rand <- function( foo )
Battle_Std.GamePos2ShiftPos <- function( pos )
Battle_Std.DrawBladeEffect <- function( tbl={} ) : (get)
Battle_Std.Call_FootStepSE <- function()
Battle_Std.ScreenEffect <- function( tbl={} ) : (get)
Battle_Std.ScreenEffect_LimitMv <- function( tbl={} )
Battle_Std.DrawIncreaseEffect <- function( tbl={} ) : (get)
Battle_Std.CreateObjectEX <- function( tbl )
Battle_Std.DivHomingTarget <- function( tbl )
Battle_Std.HomingTarget <- function( tbl )
Battle_Std.HomingTarget2 <- function( tbl )
Battle_Std.SetAngle_fromVector <- function()
Battle_Std.ScreenEffect_LimitPat <- function( tbl )
Battle_Std.DrawEffect_LimitPat <- function( tbl )
Battle_Std.NoCansel_NoAttackHit <- function( tbl={} )
Battle_Std.CheckNoCansel <- function()
Battle_Std.EnemyNoAttackHit <- function()
Battle_Std.ThrowMv_CanselRelease <- function( tbl={} )
Battle_Std.SetStatus_AirAtkStatus <- function()
Battle_Std.MoveCode.AddFlag <- function( flag )
Battle_Std.MoveCode.DelFlag <- function( flag )
Battle_Std.MoveCode.CheckFlag <- function( flag )
Battle_Std.MoveCodeEx.AddFlag <- function( pos, flag )
Battle_Std.MoveCodeEx.DelFlag <- function( pos, flag )
Battle_Std.MoveCodeEx.CheckFlag <- function( pos, flag )
Battle_Std.ChangeMoveCodeEx_CheckFlag <- function( pos, flag )
Battle_Std.MvAction.AddFlag <- function( flag )
Battle_Std.MvAction.DelFlag <- function( flag )
Battle_Std.MvAction.CheckFlag <- function( flag )
Battle_Std.GS_AddFlag <- function( flag )
Battle_Std.GS_DelFlag <- function( flag )
Battle_Std.GS_CheckFlag <- function( flag )
Battle_Std.EnemyGS_CheckFlag <- function( flag )
Battle_Std.Core.Push <- function( core )
Battle_Std.Core.FuncPush <- function( core, func )
Battle_Std.SetComboChainMvParam <- function()
Battle_Std.CancelCheck_NormalAtk <- function()
Battle_Std.CallSupport <- function() : (callmvname_ar)
Battle_Std.CallCancelSupport_Effect <- function()
Battle_Std.CallSupport_Effect <- function()
Battle_Std.CheckSt_CancelSupportCall <- function()
Battle_Std.CheckandCall_CancelSupport <- function( _spcost=10000 )
Battle_Std.CheckandCall_NoMotionSupport <- function()
Battle_Std.CheckandCall_GuardCancelSupport <- function()

Battle_Std.IWEXIST_CallOnePunch <- function()
Battle_Std.UseGRDStock <- function( cost, enemyadd=0 )
Battle_Std.SetHitMuteki <- function( _paramno = 1, _num = 8, _flag=_HitCheckFlag_Head ) : (debug_HitMutekiArray)
Battle_Std.SetHitMutekiParam1 <- function( param={} )
Battle_Std.SetHitMuteki2_Param1 <- function( param={} )
Battle_Std.SetHitCheckFlag <- function( _paramno = 1, _num = 8, _flag=_HitCheckFlag_Head, _defaultflag=0 ) : (debug_HitMutekiArray)

Battle_Std.Atemi.Init <- function( param={} )
Battle_Std.Atemi.Set <- function()
Battle_Std.Atemi.FrameUpdate <- function()

Battle_Std.CheckObjectisYarare <- function( param={} )
Battle_Std.CheckObjectHanteiCross <- function( _hantei, param={} )
Battle_Std.SetVector_ReduceYVecNoLanding <- function( _offydot=0 )
Battle_Std.SetVector_YVecFrameLanding <- function( _frame=22 )
Battle_Std.CheckDamageTiming <- function()
Battle_Std.CheckFrameID <- function( _FrameID )
Battle_Std.CheckDamageTiming_FrameID <- function( _FrameID = 0 )
Battle_Std.GetUpdateFrameID_DamageTiming <- function()
Battle_Std.CheckDamageTiming_ExceptDown <- function()
Battle_Std.CheckDamageTiming_ExceptDownFrameID <- function( _FrameID = 0 )

Battle_Std.AddDamageFlagInterrupt <- function( flag )
Battle_Std.SetKirifudaKaraburiEffect <- function()
Battle_Std.AddBlast_SPSkill <- function()
Battle_Std.BallBound.CallDummy <- function( param={} )
Battle_Std.SetDivKeepVector_AirDashMinHeight <- function( _minHeight = def_POS_AirDashHoseiMinHeight, _safeVec=1 )
Battle_Std.ThrowRelease_SetMuteki <- function( param={} )
Battle_Std.SetEnemyMuteki_Throw <- function()
Battle_Std.MutekiThrowRelease_Init <- function()
Battle_Std.MutekiThrowRelease <- function( param={} )
Battle_Std.AddXPos_NearEnemy <- function( _offx, _minx )
Battle_Std.SnapNearEnemy <- function( _offx, _minx )
Battle_Std.AddXPos_CheckFrontStage <- function( _offx, _minx )


Battle_Std.CheckFromtDispCornerDistance <- function( _xkyori=0 )
Battle_Std.CheckBackDispCornerDistance <- function( _xkyori=0 )
Battle_Std.PullEnemy_Etc0xKurai <- function( _frame )
Battle_Std.PullEnemy_Etc1xKurai <- function( _frame )
Battle_Std.PushEnemy_Etc1xKurai <- function( _frame )
Battle_Std.PullEnemy_Etc4xKurai <- function( _frame )
Battle_Std.SetPos_MarkingTarget <- function( _core, _par=5, _dfoy=-150, _miny=0 )
Battle_Std.GetPos_MarkingTarget <- function( _core, _par=5, _dfoy=-150, _miny=0 )
Battle_Std.SetPos_MarkingPlayer <- function( _par=5, _dfoy=-150 )
Battle_Std.SetPos_MarkingEnemy <- function( _par=5, _dfoy=-150 )
Battle_Std.BackScreenBlack_Start <- function( _time=600 )
Battle_Std.BackScreenBlack_Check <- function()
Battle_Std.CheckDownOiuti <- function()
Battle_Std.EnemyDamageFlag_Add <- function( _flag )
Battle_Std.EnemyDamageFlag_Del <- function( _flag )
Battle_Std.EnemyDamageFlag_Check <- function( _flag )
Battle_Std.IsMatchMvNameArray <- function( _ar )
Battle_Std.IsMatchChangeMvNameArray <- function( _ar )
Battle_Std.IsMatchNameArray <- function( _name, _ar )
Battle_Std.CallSkillSoonCache <- function( _frameid, _rest )
Battle_Std.CallSkillSoonCaches <- function( ... )

Battle_Std.CallLoopEndCache_FrameID <- function( _pat, _frameid, _frame=10, _rest=2 )
Battle_Std.CallSamePatLoopEndCache_FrameID <- function( _frameid, _frame=10, _rest=2 )
Battle_Std.AddAirSkillCount <- function( _slot = 0, _val = 1, _mvs = 0 )

Battle_Std.PP_CheckFlag <- function( _PPSlot, _flag )
Battle_Std.PP_AddFlag <- function( _PPSlot, _flag )
Battle_Std.PP_DelFlag <- function( _PPSlot, _flag )
Battle_Std.Val_CheckFlag <- function( _val, _flag )
Battle_Std.Val_AddFlag <- function( _val, _flag )
Battle_Std.Val_DelFlag <- function( _val, _flag )
Battle_Std.LP_AddFlag <- function( _lp, _flag )
Battle_Std.LP_DelFlag <- function( _lp, _flag )
Battle_Std.LP_CheckFlag <- function( _lp, _flag )
Battle_Std.SP_AddFlag <- function( _sp, _flag )
Battle_Std.SP_DelFlag <- function( _sp, _flag )
Battle_Std.SP_CheckFlag <- function( _sp, _flag )
Battle_Std.CreateIgnitionPAni <- function( _pat, _team, _prio, _delay, _type=-1 )
Battle_Std.CheckIgnition <- function( _type )
Battle_Std.CheckDoubleIgnition <- function( _type )
Battle_Std.CheckSubSupportType <- function( _type )
Battle_Std.SetObjectSousaiLv <- function()

Battle_Std.DebWrite_ValTiming <- function( _param ) : (debugwrite)
Battle_Std.GetJumpVectorPar <- function( _start_y_vec )
Battle_Std.AddMoveCode_CSAntenGaesiSkill <- function()
Battle_Std.SetFireBallFlags_InAtemiHitInterrupt <- function( param={} )
Battle_Std.PassPlayerToFireBallMvCode <- function()


Battle_Std.CheckDrawMutekiAnnounce <- function( param={} )
Battle_Std.PosShiftFastVector <- function()
Battle_Std.CheckShieldHoldCommandStrict <- function( checkButtonPos=0 )
Battle_Std.SetShieldSuccessGRDEffect <- function( _type=0 ) // 0:シールド　1:CE
Battle_Std.SetShieldSuccessCancelEffect <- function()
Battle_Std.SetRapidAtkAHosei <- function( hosei=0 )
Battle_Std.CheckDamagedLastUpdate <- function()
Battle_Std.CheckTrainingCharaGaugeMode <- function()
Battle_Std.GetTsRatio <- function()
Battle_Std.GetGRDStockLead <- function()
Battle_Std.CheckChargeCommandActivation_DashF <- function()
Battle_Std.CheckChargeCommandActivation_Assault <- function()














	t.DebugPause <-
	t.DebugButton_4 <-
	t.DebugButton_6 <-
	t.DebugButton_2 <-
t.Convert <-
t.ConvertCharge <-
t.Liberate <-
t.ComboLiberate <-
t.Skill_DyingIWEAtk <-
t.Throw_F <-
t.Dash_F <-
t.Dash_F_Douji <-
t.Dash_B <-
t.Dash_B_Douji <-
t.Jump_F <-
t.Jump_N <-
t.Jump_B <-
t.JumpCancel_F <-
t.JumpCancel_N <-
t.JumpCancel_B <-
t.Assault_Std <-
t.Assault_Air <-
t.Assault_Air <-
	t.GCAttack_Std <-
t.ForwardShift <-
t.Atk_DashStdBandC <-
t.Atk_DashStdC_Normal <-
t.Atk_DashStdB_Normal <-
t.Atk_DashStdC_Direct <-
t.Atk_DashStdB_Direct <-
t.Atk_CroC <-
t.Atk_CroB <-
t.Atk_CroA <-
t.Atk_StdC <-
t.Atk_StdB <-
t.Atk_StdA <-
t.Atk_AirC <-
t.Atk_AirB <-
t.Atk_AirA <-
t.Barrier_Cro <-
t.Barrier_Std <-
t.Barrier_Air <-
t.Crouch <-
t.Walk_F <-
t.Walk_B <-
t.MultiJump_F <- 
t.MultiJump_N <- 
t.MultiJump_B <- 
t.MultiJumpCancel_F <- 
t.MultiJumpCancel_N <- 
t.MultiJumpCancel_B <- 
t.Skill_CircleEX <- 
t.Skill_CircleC <- 
t.Skill_CircleBorC <- 
t.Skill_CircleB <- 
t.Skill_CircleA <- 
t.Skill_41236SP <- 
t.Skill_41236SP <- 
t.Skill_41236SP_ABC <- 
t.Skill_41236EX <- 
t.Skill_41236C <- 
t.Skill_41236BorC <- 
t.Skill_41236B <- 
t.Skill_41236A <- 
t.Skill_63214EX <- 
t.Skill_63214C <- 
t.Skill_63214BorC <- 
t.Skill_63214B <- 
t.Skill_63214A <- 
t.Skill_236EX <- 
t.Skill_236C <- 
t.Skill_236BorC <- 
t.Skill_236B <- 
t.Skill_236A <- 
t.Skill_623EX <- 
t.Skill_623C <- 
t.Skill_623BorC <- 
t.Skill_623B <- 
t.Skill_623A <- 
t.Skill_214EX <- 
t.Skill_214BC <- 
t.Skill_214C <- 
t.Skill_214BorC <- 
t.Skill_214B <- 
t.Skill_214A <- 
t.Skill_421EX <- 
t.Skill_421C <- 
t.Skill_421BorC <- 
t.Skill_421B <- 
t.Skill_421A <- 
t.Skill_0202D <-
t.Skill_0202EX <- 
t.Skill_020202EX <- 
t.Skill_0202C <- 
t.Skill_0202BorC <- 
t.Skill_0202B <- 
t.Skill_0202A <- 
t.Skill_C0202A <- 
t.Skill_C0202B <- 
t.Skill_C0202C <- 
t.Skill_J41236SP <- 
t.Skill_J41236EX <- 
t.Skill_J41236C <- 
t.Skill_J41236BorC <- 
t.Skill_J41236B <- 
t.Skill_J41236A <- 
t.Skill_J63214SP <- 
t.Skill_J63214EX <- 
t.Skill_J63214C <- 
t.Skill_J63214BorC <- 
t.Skill_J63214B <- 
t.Skill_J63214A <- 
t.Skill_J236EX <- 
t.Skill_J236C <- 
t.Skill_J236BorC <- 
t.Skill_J236B <- 
t.Skill_J236A <- 
t.Skill_J623EX <- 
t.Skill_J623C <- 
t.Skill_J623BorC <- 
t.Skill_J623B <- 
t.Skill_J623A <- 
t.Skill_J214EX <- 
t.Skill_J214C <- 
t.Skill_J214BorC <- 
t.Skill_J214B <- 
t.Skill_J214A <- 
t.Skill_J421EX <- 
t.Skill_J421C <- 
t.Skill_J421BorC <- 
t.Skill_J421B <- 
t.Skill_J421A <- 
t.Skill_J0202EX <- 
t.Skill_J0202C <- 
t.Skill_J0202BorC <- 
t.Skill_J0202B <- 
t.Skill_J0202A <- 
t.Atk_Std4A <- 
t.Atk_Std4B <- 
t.Atk_Std4C <- 
t.Atk_Std6A <- 
t.Atk_Std6B <- 
t.Atk_6B_6B <-
t.Atk_Std6C <- 
t.Atk_6C_6C <-
t.Atk_6C_6C_6C <-
t.Atk_Air6A <- 
t.Atk_Air6B <- 
t.Atk_Air6B_Air6B <-
t.Atk_Air6C <- 
t.Atk_Air4A <- 
t.Atk_Air4B <- 
t.Atk_Air4C <- 
t.Atk_Std3B <- 
t.Atk_Cro3B <- 
t.Atk_Std3C <- 
t.Atk_Cro3C <- 
t.Atk_Cro1A <- 
t.Atk_Cro1C <- 
t.Atk_Air2B <- 
t.Atk_Air2C <- 
t.Throw_A <- 
t.Atk_CroAandB <- 
t.Atk_StdAandB <- 
t.DirectSSSkill <-
t.Atk_AirAandB <- 
t.Atk_CroBandC <- 
t.Atk_StdBandC <- 
t.Atk_AirBandC <- 
t.Atk_A_A <- 
t.Atk_B_B <- 
t.Atk_B_B_B <-
t.Atk_C_C <- 
t.Atk_2B_2B <- 
t.Atk_2B_2B_2B <- 
t.Atk_2C_2C <- 
t.Atk_JA_JA <- 
t.Atk_JB_JB <- 
t.Atk_JC_JC <- 
t.Skill_236A_236EX <- 
t.Skill_236A_236C <- 
t.Skill_236A_236BorC <- 
t.Skill_236A_236B <- 
t.Skill_236A_236A <- 
t.Skill_236B_236EX <- 
t.Skill_236B_236C <- 
t.Skill_236B_236BorC <- 
t.Skill_236B_236B <- 
t.Skill_236B_236A <- 
t.Skill_236_236 <- 
t.Skill_236_236_236 <- 
t.Skill_236_236_214 <- 




















	t.DebugPause <-
	t.DebugButton_4 <-
	t.DebugButton_6 <-
	t.DebugButton_2 <-
t.Convert <-
t.ConvertCharge <-
t.Liberate <-
t.ComboLiberate <-
t.Skill_DyingIWEAtk <-
t.Throw_F <-
t.Dash_F <-
t.Dash_F_Douji <-
t.Dash_B <-
t.Dash_B_Douji <-
t.Jump_F <-
t.Jump_N <-
t.Jump_B <-
t.JumpCancel_F <-
t.JumpCancel_N <-
t.JumpCancel_B <-
t.Assault_Std <-
t.Assault_Air <-
t.Assault_Air <-
	t.GCAttack_Std <-
t.ForwardShift <-
t.Atk_DashStdBandC <-
t.Atk_DashStdC_Normal <-
t.Atk_DashStdB_Normal <-
t.Atk_DashStdC_Direct <-
t.Atk_DashStdB_Direct <-
t.Atk_CroC <-
t.Atk_CroB <-
t.Atk_CroA <-
t.Atk_StdC <-
t.Atk_StdB <-
t.Atk_StdA <-
t.Atk_AirC <-
t.Atk_AirB <-
t.Atk_AirA <-
t.Barrier_Cro <-
t.Barrier_Std <-
t.Barrier_Air <-
t.Crouch <-
t.Walk_F <-
t.Walk_B <-
t.MultiJump_F <- 
t.MultiJump_N <- 
t.MultiJump_B <- 
t.MultiJumpCancel_F <- 
t.MultiJumpCancel_N <- 
t.MultiJumpCancel_B <- 
t.Skill_CircleEX <- 
t.Skill_CircleC <- 
t.Skill_CircleBorC <- 
t.Skill_CircleB <- 
t.Skill_CircleA <- 
t.Skill_41236SP <- 
t.Skill_41236SP <- 
t.Skill_41236SP_ABC <- 
t.Skill_41236EX <- 
t.Skill_41236C <- 
t.Skill_41236BorC <- 
t.Skill_41236B <- 
t.Skill_41236A <- 
t.Skill_63214EX <- 
t.Skill_63214C <- 
t.Skill_63214BorC <- 
t.Skill_63214B <- 
t.Skill_63214A <- 
t.Skill_236EX <- 
t.Skill_236C <- 
t.Skill_236BorC <- 
t.Skill_236B <- 
t.Skill_236A <- 
t.Skill_623EX <- 
t.Skill_623C <- 
t.Skill_623BorC <- 
t.Skill_623B <- 
t.Skill_623A <- 
t.Skill_214EX <- 
t.Skill_214BC <- 
t.Skill_214C <- 
t.Skill_214BorC <- 
t.Skill_214B <- 
t.Skill_214A <- 
t.Skill_421EX <- 
t.Skill_421C <- 
t.Skill_421BorC <- 
t.Skill_421B <- 
t.Skill_421A <- 
t.Skill_0202D <-
t.Skill_0202EX <- 
t.Skill_020202EX <- 
t.Skill_0202C <- 
t.Skill_0202BorC <- 
t.Skill_0202B <- 
t.Skill_0202A <- 
t.Skill_C0202A <- 
t.Skill_C0202B <- 
t.Skill_C0202C <- 
t.Skill_J41236SP <- 
t.Skill_J41236EX <- 
t.Skill_J41236C <- 
t.Skill_J41236BorC <- 
t.Skill_J41236B <- 
t.Skill_J41236A <- 
t.Skill_J63214SP <- 
t.Skill_J63214EX <- 
t.Skill_J63214C <- 
t.Skill_J63214BorC <- 
t.Skill_J63214B <- 
t.Skill_J63214A <- 
t.Skill_J236EX <- 
t.Skill_J236C <- 
t.Skill_J236BorC <- 
t.Skill_J236B <- 
t.Skill_J236A <- 
t.Skill_J623EX <- 
t.Skill_J623C <- 
t.Skill_J623BorC <- 
t.Skill_J623B <- 
t.Skill_J623A <- 
t.Skill_J214EX <- 
t.Skill_J214C <- 
t.Skill_J214BorC <- 
t.Skill_J214B <- 
t.Skill_J214A <- 
t.Skill_J421EX <- 
t.Skill_J421C <- 
t.Skill_J421BorC <- 
t.Skill_J421B <- 
t.Skill_J421A <- 
t.Skill_J0202EX <- 
t.Skill_J0202C <- 
t.Skill_J0202BorC <- 
t.Skill_J0202B <- 
t.Skill_J0202A <- 
t.Atk_Std4A <- 
t.Atk_Std4B <- 
t.Atk_Std4C <- 
t.Atk_Std6A <- 
t.Atk_Std6B <- 
t.Atk_6B_6B <-
t.Atk_Std6C <- 
t.Atk_6C_6C <-
t.Atk_6C_6C_6C <-
t.Atk_Air6A <- 
t.Atk_Air6B <- 
t.Atk_Air6B_Air6B <-
t.Atk_Air6C <- 
t.Atk_Air4A <- 
t.Atk_Air4B <- 
t.Atk_Air4C <- 
t.Atk_Std3B <- 
t.Atk_Cro3B <- 
t.Atk_Std3C <- 
t.Atk_Cro3C <- 
t.Atk_Cro1A <- 
t.Atk_Cro1C <- 
t.Atk_Air2B <- 
t.Atk_Air2C <- 
t.Throw_A <- 
t.Atk_CroAandB <- 
t.Atk_StdAandB <- 
t.DirectSSSkill <-
t.Atk_AirAandB <- 
t.Atk_CroBandC <- 
t.Atk_StdBandC <- 
t.Atk_AirBandC <- 
t.Atk_A_A <- 
t.Atk_B_B <- 
t.Atk_B_B_B <-
t.Atk_C_C <- 
t.Atk_2B_2B <- 
t.Atk_2B_2B_2B <- 
t.Atk_2C_2C <- 
t.Atk_JA_JA <- 
t.Atk_JB_JB <- 
t.Atk_JC_JC <- 
t.Skill_236A_236EX <- 
t.Skill_236A_236C <- 
t.Skill_236A_236BorC <- 
t.Skill_236A_236B <- 
t.Skill_236A_236A <- 
t.Skill_236B_236EX <- 
t.Skill_236B_236C <- 
t.Skill_236B_236BorC <- 
t.Skill_236B_236B <- 
t.Skill_236B_236A <- 
t.Skill_236_236 <- 
t.Skill_236_236_236 <- 
t.Skill_236_236_214 <- 








function Battle_Std::CloneCopy( container )
function Battle_Std::MergeTable( tbl, std )
function Battle_Std::InsertTable( tbl, std )
function Battle_Std::GetCommandTableFromTmpl( chr_tbl )
Battle_Std.SetCmdTmplAutoParams <- function( chr_tbl ) : (setDefault)
		val._GetCommandFlags <- function(){ return cmdflags }; // 上記の取得関数
function Battle_Std::GetCmdFromTmpl( tmpl, tmpl_name="" )
function Battle_Std::MakeCommandTable( param={} )
function Battle_Std::GetMoveTableFromTmpl( chr_tbl )
function Battle_Std::GetMvFromTmpl( tmpl, tmpl_name )
		ret.Init <- function() : (tmpl,tmpl_name)
		ret.Init <- function() : (tmpl)
		ret.Update <- function() : (tmpl)
		ret.Update <- function() : (tmpl)
		ret.FrameUpdate <- function() : (tmpl)
		ret.FrameUpdate <- function() : (tmpl)
		ret.Finalize <- function() : (tmpl)
		ret.Finalize <- function() : (tmpl)
		ret.Finalize <- function() : (tmpl)
		ret.HitInterrupt <- function() : (tmpl)
		ret.HitInterrupt <- function() : (tmpl)
		ret.LastUpdate <- function() : (tmpl)
		ret.LastUpdate <- function() : (tmpl)
// Battle_Std::MakeMoveTable　※キャラのMvから呼ばれる
function Battle_Std::MakeMoveTable( t, cmd, _ChrNum = 0 )
function Battle_Std::ErrorCheckMoveTable( mvlist )
function Battle_Std::MakeMoveTmpl( t, mvlist, _ChrNum )
				mv_tmpl.Init_Std <- function() : (preParam, skillType, smart_stear)
				mv_tmpl.Init_Std <- function() : (preParam, skillType, smart_stear)
			mv_tmpl.FrameUpdate_Std <- function() : (preParam)
			mv_tmpl.Start_Std <- function() : (preParam)
			mv_tmpl.Finalize_Std <- function() : (preParam)
			mv_tmpl.GetFinalizeCode_Std <- function()
			mv_tmpl.LastUpdate_Std <- function() : (preParam)
			mv_tmpl.HitInterrupt_Std <- function() : (preParam)
			mv_tmpl.Init_Std <- function() : (pat, landObj, atkObj)
			mv_tmpl.Finalize_Std <- function()
			mv_tmpl.Init_Std <- function()
			mv_tmpl.Finalize_Std <- function()
				mv_tmpl.Init_Std <- function() : (preParam)
				mv_tmpl.Start_Std <- function() : (preParam)
				mv_tmpl.FrameUpdate_Std <- function() : (preParam)
				mv_tmpl.Finalize_Std <- function()
				mv_tmpl.GetFinalizeCode_Std <- function()
				t[mvname].FB_Sousai <- function() : (fb_params)
				t[mvname].FB_FirstHitTiming <- function() : (fb_params)
				t[mvname].FB_HitTiming <- function() : (fb_params)
				t[mvname].FB_DamageTiming <- function() : (fb_params)
				t[mvname].FB_GuardTiming <- function() : (fb_params)
				t[mvname].FB_LandTiming <- function() : (fb_params)
				t[mvname].FB_Wall <- function() : (fb_params)
				t[mvname].FB_Blocked <- function() : (fb_params)
				t[mvname].FB_AtkCountZero <- function() : (fb_params)
				t[mvname].FB_ParentChange <- function() : (fb_params)
				t[mvname].Init_Std <- function() : (fb_params)
				t[mvname].Init_Std <- function() : (fb_params, nochange_landmv)
			t[mvname].Update_Std <- function() : (fb_params)
			t[mvname].FrameUpdate_Std <- function() : (fb_params)
			t[mvname].HitInterrupt_Std <- function() : (fb_params)
			t[mvname].Finalize_Std <- function()
			t[mvname].LastUpdate_Std <- function()
				t[mvname].Init_Std <- function() : (flag_sousaicheck)
				t[mvname].Init_Std <- function() : (flag_sousaicheck, nochange_landmv)
			t[mvname].Update_Std <- function() : (flag_blockedcheck)
			t[mvname].FrameUpdate_Std <- function() : (flag_sousaicheck,flag_landcheck,flag_wallcheck,flag_ceilcheck,flag_ex_skill,flag_parentchangecheck)
			t[mvname].HitInterrupt_Std <- function() : (flag_hitcheck, flag_sousaicheck, flag_damagecheck, flag_guardheck, flag_ex_skill, noEXSLimit)
			t[mvname].Finalize_Std <- function() : (far)
				t[mvsousai_name].Init_Std <- function() : ()
				t[mvsousai_name].Finalize_Std <- function()
				t[mvhit_name].Init_Std <- function() : ()
				t[mvhit_name].HitInterrupt_Std <- function()
				t[mvhit_name].Finalize_Std <- function()
				t[mvdamage_name].Init_Std <- function() : ()
				t[mvdamage_name].Finalize_Std <- function()
				t[mvguard_name].Init_Std <- function() : ()
				t[mvguard_name].Finalize_Std <- function()
				t[mvland_name].Init_Std <- function() : (noset_vec)
				t[mvland_name].Finalize_Std <- function()
				t[mvwall_name].Init_Std <- function() : ()
				t[mvwall_name].Finalize_Std <- function()
				t[mvceil_name].Init_Std <- function() : ()
				t[mvceil_name].Finalize_Std <- function()
				t[mvblocked_name].Init_Std <- function() : ()
				t[mvblocked_name].Finalize_Std <- function()
				t[mvparentchange_name].Init_Std <- function() : ()
				t[mvparentchange_name].Finalize_Std <- function()
function Battle_Std::MakeCmdArray( tbl ) //CMD形式の配列を返す
function Battle_Std::MakeStdCombo( cmdtmpl, ar, type=0 /*0:立ち 1:しゃがみ 2:空中 */ )
					cmdtmpl[cmdname[j]].CmdLastFunc <- function() : (i,usepp)
Battle_Std.MakeMv.TechWait <- function( tbl={} )
Battle_Std.MakeMv.LastCharaAnimeEnd <- function( clear_vector = 0 )
Battle_Std.MakeMv.SetCaptureCharaAnime <- function( tbl )
	tmpl.Init <- function() : (animation, set_NextAniCache)
	tmpl.FrameUpdate <- function() : (tbl, set_NextAniCache)
	tmpl.Finalize <- function()
Battle_Std.MakeMv.SetCaptureCharaAnime <- function( tbl )
	tmpl.Init <- function() : (animation, set_NextAniCache)
	tmpl.Update <- function() : (tbl, set_NextAniCache)
	tmpl.Finalize <- function()
Battle_Std.WriteCommandList <- function( param={} )
Battle_Std.AddHitEffects <- function( std, _ChrNo=0 )
	std.Mv_Eff_Hit_Guard <- function( info )
	std.Mv_Eff_Hit_GuardEx <- function( info )
	std.Mv_Eff_Hit_GuardLimit <- function( info ) {}; // ガード間引き
	std.Mv_Eff_Hit_GuardExLimit <- function( info ) {}; // ガード間引き
	std.Mv_Eff_Hit_Counter <- function( info ) {};
	std.Mv_Eff_Sousai <- function( info )
Battle_Std.MakeFireBallTmpl <- function( param={} )
	retMv.Init_After <- function() : (mvParam)
	retMv.FrameUpdate_After <- function() : (mvParam)
		retMv.LandTiming <- function() : (mvParam)
		retMv.HitTiming <- function() : (mvParam)
		retMv.Sousai <- function() : (mvParam)
		retMv.Blocked <- function() : (mvParam)
		retMv.ParentChange <- function() : (mvParam)
	