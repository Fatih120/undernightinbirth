//goes in ___English\script\

const Def_Dbg_LocalDebugMode	=	1;	// function on/off for debugging in local environment

//I think this tries to load scripts from the folder specifid in the comment.
//But I'm not totally sure. Interestingly, enabling this causes the battle loop to freeze
//up, similarly to how it would do it with a character's erroneous mv file in CLR.
//(Loops and creates clones of itself, pressing buttons resets idle anim, speed fluc, etc)
//Maybe it needs a little something?
const Def_Dbg_LocalDebugScriptPath	= 0; // "./___NotProject/LocalDebug/";

// Debug message output related
// I think these are useless without the debugging environment(?), as a console is needed.
const Def_Dbg_DebugMessage		=	1;	// Debug console output
const Def_Dbg_LocalAnnounce	=	1;	// Local debug announcements
const Def_DbgMes_PlaySE		=	1;	// SE playback

const Def_Dbg_KeyLog1P		=	1;	// 1Pkey display
const Def_Dbg_KeyLog2P		=	1;	// 2Pkey display

const Def_Dbg_DebugButtonMode	=	1;	// whether E button is debug button or not - 0:unused , 1:increase gauge,  2:pause opponent , 3:for tremo(?), 4:disappear from screen, 5:force win,  6:make opponent roll over at 0 damage, 6:check voice, 7:check stage


const Def_Dbg_DebugGauge		=	1;	// Display temporary gauge

const Def_Dbg_WriteCommandList	=	1;	// generate command list file when loading character
const Def_Dbg_NoPlayUpsetSE		=	1;	// do not play "irritating" SEs (VORPAL and taunts)

const Def_Dbg_SmartSteerLog		=	1;	// Smart steer
const Def_Dbg_KoukaFrameLog		=	1;	// Display hard difference frames
const Def_Dbg_ComboChanceLog	=	1;	// Followup availability
const Def_Dbg_InterruptedLog	=	1;	// Gap display (1P•2P)
const Def_Dbg_TotalFrameLog		=	1;	// Frame data (1P•2P)
const Def_Dbg_ComboSPKouritu	=	1;	// Gauge efficiency
const Def_Dbg_TmplMoveLog		=	1;	// Tmpl auto-gen action log
const Def_Dbg_PotentialLog		=	1;	// Potential Log
const Def_Dbg_SkillThrowLog		=	1;	// Special Move throw log
const Def_Dbg_TechHitLog		=	1;	// Throw log
const Def_Dbg_DoujiDelayLog		=	1;	// sim. press grace log?
const Def_Dbg_BoundBlastLog		=	1;	// Bound Blast Log
const Def_Dbg_AirAtkFlag		=	1;	// Jump attack flag log
const Def_Dbg_RoundStatus		=	1;	// Round info log
const Def_Dbg_AirCountLog		=	1;	// flag change log for air special moves (0-7), air dash, and 2-step jump (8-9)
const Def_Dbg_BattleDamageLog	=	1;	// Battle damage efficiency log
const Def_Dbg_HitMutekiLog		=	1;	// Invincibility frame log
const Def_Dbg_MoveCodeStatus	=	1;	// Display Mv flags, etc. on game screen during battle
const Def_Dbg_MoveListStatus	=	1;	// display list of Mv's in battle on game screen
const Def_Dbg_MoveZokuseiStatus	=	1;	// display attribute information on game screen
const Def_Dbg_MvValStatus		=	1;	// Display the flags of Mvs in battle as numbers
const Def_Dbg_BtlGRDAssist		=	1;	// display GRD and TS warnings on game screen during battle
const Def_Dbg_AllMoveAddCommand	=	1;	// treat all moves as add commands so you can do more with them
const Def_Dbg_ViewComboEfficient=	1;	// Display combo recipes and efficiency
const Def_Dbg_DebugButtonMenu	=	1;	// Make the debug button open the debug menu
const Def_Dbg_AchiveMessage		=	1;	// Display Achievement and Activity Log
const Def_Dbg_CommandAssist		=	1;	// Simplify and automate certain operations
