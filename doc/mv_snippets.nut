///////////////////////////////////////////////////////////////////////
// Random Startup Animation                                          //
// -- Randomly one of two startup animations to play during a match. //
///////////////////////////////////////////////////////////////////////

t.Mv_Startup <- // The code name of the intro animation
{
	function Init_After() // After Initializing
    {
        local rand = BMvEff.Random_Limit(2); // Randomize a value from 1 to 2
        switch(rand) // Conditional
        {
        case 1: // If rand = 1
            BMvEff.AttackInfoString_Set({ word = "1" }); // Personal debug, show rand = 1
            BMvTbl.SetPattern(50); // Default Startup Pattern ID
            break; // Finish
        case 2: // If rand = 2
            BMvEff.AttackInfoString_Set({ word = "2" }) // Personal debug, show rand = 2
            BMvTbl.SetPattern(51); // Alternate Startup Pattern ID
            break; // Finish
        }  
    }
} // this was working before but now it's not? did i do something on my end or...

///////////////////////////////////////////////////////////////////////
// System Mechanics Resize Band-Aid Fix                              //
// -- CGs that are small and are scaled up in-game can seemingly     //
// break and be set to 1x scale with unknown cause. If your          //
// character does this, you can use these temporary workarounds.     //
// They are ugly, but they set and reset the scales for such moves.  //
///////////////////////////////////////////////////////////////////////

t.Mv_Liberate <- // Veil Off
{ 
    function Init_After() // When it starts
    {
        BMvTbl.SetScale( { x=60000, y=60000 } ); // 600.00 %
    }
}
t.Mv_Liberate_End <-
{
    function Finalize_After() // When it finishes
    {
        BMvTbl.SetScale( { x=10000, y=10000 } ); // Set back to 100.00 %
    }
}
// This example is for Veil Off. There are several other system mechanics
// this issue applies to, such as CCVO, shield, etc. You may compress them.
t.Mv_ComboLiberate <- { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } }
t.Mv_ComboLiberate_End <- { function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
t.Mv_Barrier_Std <- { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
t.Mv_Barrier_Cro <- { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
t.Mv_Barrier_Air <- { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
// t.Mv_Convert <-             { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
// t.Mv_Convert_Modori <-      { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
// t.Mv_Convert_Modori_Land <- { function Init_After() { BMvTbl.SetScale( { x=60000, y=60000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
// t.Mv_Guard <- { function Init_After() { BMvTbl.SetScale( { x=66000, y=66000 } ); } function Finalize_After() { BMvTbl.SetScale( { x=10000, y=10000 } ); } }
// Not sure if Barriers do it right and I'm sure I'm missing some but I haven't experienced this anymore so I'll see if someone else brings it up again.
// If you end up being bigger after certain moves (which I need to TODO), another bandaid is to include this function in t.Mv_Standby:
t.Mv_Standby <-
{
	function Init_After()
	{
		BMvTbl.SetScale( { x=10000, y=10000 });
	}
}