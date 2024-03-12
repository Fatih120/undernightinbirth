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
}
