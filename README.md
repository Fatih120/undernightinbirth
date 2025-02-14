https://github.com/Fatih120/undernightinbirth/assets/18276369/c48ec7f8-b4d9-47eb-8385-b3af4233a222

[![Steam](https://img.shields.io/badge/Steam-231f20?logo=steam)](https://steamcommunity.com/id/Fatih120/)
[![Discord](https://img.shields.io/badge/Discord-220077?logo=discord)](https://discord.com/invite/Cy27FNfQtc)

[<img src="https://img.shields.io/badge/Code-Documentation-brightgreen" height="30">](http://mof.x10.bz/unib)


# Contents

- [README](README.md)
- [FAQ](FAQ.md)
- [GLOSSARY](GLOSSARY.md)
- [HANTEICHAN](HANTEICHAN.md)
- [AUDIO](AUDIO.md)
- [CONTRIBUTING](CONTRIBUTING.md)
- [Character Repo](https://github.com/UnderNightInBirth/Characters)

## Video Series

[![PRIMER](https://img.youtube.com/vi/uV6T4MC23zo/maxresdefault.jpg)](https://www.youtube.com/watch?v=uV6T4MC23zo&list=PL28iAGlfgcCXCme17jHTZQDqbEAgG7Igx)

# Primer on Modding UNI2

For starters, you may use https://github.com/Ekey/UNIB.Data.Tool to unpack the game successfully. Either build it yourself with [CSC.exe included with .NET 4](https://stackoverflow.com/questions/18286855/how-can-i-compile-and-run-c-sharp-program-without-using-visual-studio) and [some elbow grease](https://stackoverflow.com/questions/46320080/c-sharp-unable-to-compile-cs0103-the-name-gutils-does-not-exist-in-the-curre), or download it straight from this repo [right here, pre-built](uni2unpacker.exe) (or after cloning).

Run the program in a shell ([Command Prompt on Windows](https://www.wikihow.com/Run-a-Program-on-Command-Prompt#Run-Other-Programs)) with `<input> <output>` arguments: Input being the `d` folder, and output being somewhere accessible such as `./d/output`. Don't know what the `d` folder is? Well, that's where the base game folder is, next to `uni2.exe`. Open it via Steam's game Properties -> Local Files -> Browse Local Files. 

After you have unpacked everything, you are ready to sift through and start modding in whatever ways you want.

### Resources

- Tools for graphics and editing data are bundled in this repo, specifically in the [tools directory](tools). They will be brought up per-basis, but **you should want to get hanteichan_2.1.666.exe** (ignore the scary name).
- To edit `.txt` files without potential issues, use an editor that can properly read and save in the Japanese **SHIFT-JIS** format, [such as NotepadNext](https://github.com/dail8859/NotepadNext/releases/tag/v0.6.4).
- To be able to edit certain files, you should get a hex editor of your choosing, [such as HxD](https://mh-nexus.de/en/downloads.php?product=HxD). [ImHex](https://github.com/WerWolv/ImHex) may also suffice, among others depending on your preference.
- For editing certain graphics, [Paint.NET](https://getpaint.net) is a fine general-use editor for graphics, in our case, DDS files. It may also keep indexed colour tables. For sprites, the popular [Aseprite](https://github.com/aseprite/aseprite)/[LibreSprite](https://github.com/LibreSprite/LibreSprite) will be useful for editing sprites and their palettes. Tools like [GIMP](https://www.gimp.org/), though more complex, may be used.
- [Audacity v3.0.2 pre-telemetry](https://www.fosshub.com/Audacity-old.html?dwl=audacity-win-3.0.2.exe) for audio editing and getting sample times down.
- This entire repo!
- - Since French Bread and ArcSys explicitly placed taboo on modding the former's games, online circles are typically avoidant of this and information is staggered. By adding findings and opening up issues and discussions on here, hopefully there can be a more accessible and helpful resource to help newcomers.

# To Edit or Add Characters

We are able to set up new characters without modifying the base game's data. You could do this from scratch, but if you're new, you should copy an existing character so you don't have to be worried about requirements and oddities you're unaware of. Alternatively, you can modify existing characters or write over their slots - however, this will require internal edits and copying over mass data. If you'd like the former, read the following - if you'd like the latter, skip below to the "Dereferencing" section.

* _For the following, be SURE to differentiate between your "output" foler and your "working" folder. You COULD use the unpacker to output the files beside the exe, but for the sake of isolating your edited files, I strongly recommend seperating the output data._

### The very short of it for copying a character to a new slot:

1. Copy a `chrXXX` character from `./output/data/`. Move it into `./data/`, creating that folder.
2. Rename the folder to a new slot greater than 024, such as `025`. Do the same with the files inside using that same number, including the `lst`, `pal`, `txt`s, etc.†
4. Open `chrXXX_mv_0.txt` in your specialized editor. Jump to the end and find the two last written lines - `CHRXXX_MoveTable <- Battle_Std.MakeMoveTable( t, CHRXXX_CommandTable, Def_ChrNo_YYY );` and `__dofile__("./chrXXX_se_category.txt");`. Edit these lines to have your IDs accordingly.
5. Open `chrXXX_0.txt`, and change the references to XXX in the same way. Open `chrXXX_cmd_0.txt`,  and change the references to XXX in the same way. _(Optionally for quick-start?)_ Open the two `chr025_se_*` files and change the references accordingly.
6. Find `./output/script/btl_Define_CharaNew.txt`. Copy it to `./___English/script`.
7. Open your copy and append the line `const Def_ChrNo_ChrXXX = XXX;` using the same number you chose. Also add the line `const Def_ChrNo_YYY = XXX;`, with Y preferably being a 3-letter identifier for the character.
8. Find `./output/System/BtlCharaTbl.txt`. Copy it to `./___English/script`.
9. Scroll to the bottom and append a `chara_no[XXX]` by templating one of the previous entries, making sure to have `name_short = "chrXXX";` and a unique `order`.

† _You _are_ able to use different naming conventions for certain files to make them easily readable, such as whatever is defined in `chrXXX_0.txt`, but be sure your character loads this way first as I haven't fully figured out what can be changed._

You should now be able to go to training mode and see a new slot, which should be playable with your setup without internal edits. You can make the character accessible on the CSS and in other areas through folders such as `grpdat`'s `CharaColorBar`, `CSel`, `Cockpit`, etc. If you just want to edit this extra slot without the baggage of touching vanilla characters, skip the next section and head down for the guide on character edits and using Hantei-chan.

### Dereferencing for edits

Coming from UNICLR, things are a bit different. After you've dumped all the game assets, you are able to do modifications as a "layered file system" by copying assets to the base directory, next to `uni2.exe`. Common practice in UNICLR was to put everything into an `___English` folder which housed these system folders. For the case of characters, the `data` folder housing all character data simply needs to be moved to the base directory - again, next to `d` and the game executable.

Now, simply trying to edit these copied assets will not result in the game loading these files. Hex edits to certain files in `d` are required to be "dereferenced" or dummied out, since these files tell the game where to look for assets. Within `d`, the file `hexeojmpimrjs` houses links to all the character files and folders within `data`. **Back up this file before you do anything with it.** If your hand needs to be held, you can [get this repo's copy of the dummied file](tools/GAME/d/hexeojmpimrjs) and replace your copy with it. But for the sake of other `d` files and for reference, open up your hex editor and open the file with it.

![HxD64_2024_0130-173603](https://github.com/Fatih120/undernightinbirth/assets/18276369/25e7eaf0-1074-499b-9be7-f54588d28fec)

You will come across a view like this in your main window. Depending on your knowledge with hex, you will at least see that the ASCII pane to the right shows the names of certain folders within `data`, and scrolling down will sequentially list every file within that directory. As long as the files are properly referenced here, the game will always load the original ingame files. We must break this by simply renaming all references to these files.

![HxD64_2024_0130-173929](https://github.com/Fatih120/undernightinbirth/assets/18276369/9c2d1212-50a4-4c5b-bc96-57fb660b68d9)

In the case of HxD, you should _type to overwrite_, **NOT** delete data. If a prompt warns you're going to change the filesize, cancel and try again. You may now proceed and do this for every file and folder you see, though you _can_ just remove certain files or folders from loading if you want to be selective about it. You may save once finished and proceed to copy any remaining files from your `output` into your workspace `data` folder. If you've applied the file from the repo above, this dummies out **all** of `data`, so you **must** copy/move over all of the outputted `data` folder or the game will crash.

Usually, to add characters, one would go to `System\BtlCharaTbl.txt` and add a definition at the bottom which gives the game an internal ID for them. Then, adding more defines in the first set of values in `script\btl_Define_Chara.txt` (does `script\btl_Define_CharaNew.txt` work too?). Newly added, one can also finally add slots on the CSS using `grpdat\CSel\CSelAnim.ini` (also in `Customize`). Finally, the data would have to be set up for the new character in `data\chr<ID>`, or replacing another character's folder.

As for now, it's hard to test if your changes work when you've copied only vanilla data, so you could try and do things like copy `chr001.cg` and overwrite `chr000.cg` with it and playtest as Hyde to see if anything is wrong. Scroll down towards HA6 Editing to get started on character edits and the like.

# Audio

See: [AUDIO.md](AUDIO.md)

# Character Structure

     File | Use | Notes
-- | - | -
chrXXX_0.TXT | "Header" File (0) | Declare the name of certain files with this. Allows renaming the HA6, CG and PAT file. Unknown if multiple included files will work. Renamable(?)
chrXXX.HA6 | Hantei6 Pattern (ha6) | Includes all of the basic character data in collections of "patterns", elaborated in the section below - hitboxes, frame data, movement, attack info - lots can be done with this single file and it will have most of your edits. Open this using **Hantei-chan**. **Renamable.**
chrXXX_mv_0.TXT | "Move" Code File (mv) | Includes technical functions that get hooked onto patterns/moves, allowing for elaborate attacks and complex mechanics. The butter to the **HA6**'s bread. UNI2 uses [Squirrel lang](http://squirrel-lang.org/), which is C-like.
chrXXX_cmd_0.TXT | "Command" File (cmd) | Defines what inputs/moves the character can do, along with the Smart Steer definition. Can also have some code that wouldn't belong in mv.
chrXXX_sc_0.TXT | Battle Stats | Defines specific stats like attack/GRD modifiers, and HP.
chrXXX.CG | Character Graphics (cg) | The package holding all of the character's own sprites. Can be extracted or built using the included `cgtool` library in the repo. **Renamable.**
chrXXX.PAL | Palette File (pal) | Colour information for palette selection. Sprites are [Indexed](https://en.wikipedia.org/wiki/Indexed_color) so they must use this for colours. TODO: how to palette
chrXXX.PAT | Pattern File (pat) | Includes all of the character effect graphics and definitions. Must be hex edited to inject (TODO: GUIDE), but use of **ha6chan_pat_editor** can change the "patterns" somewhat.
chrXXX_com_0.txt, chrXXX_com_ranking_0.txt | COM AI Files |
chrXXX_se_category.txt, chrXXX_se_list.txt | [Sound Effect Definitions](AUDIO.md) | `./se` |
chrXXX.lst | List File | Useless |
_temp.ha6, _temp.lst | Temp | Useless |
BaseData.lst | Base Data List | `../BaseData.ha6` |

# Character Graphics

If you are making a custom character, adding sprites is obviously essential to being able to put a face to a name. In UNI2, importing sprites to turn them into a **CG file** can either be very simple, or a bit of a pain, depending on things such as if your character already comes from a fighting game, if the sprites are all indexed the same way, and how much you have to modify the sprites without relying on HA6 transformations (it might be a lot, because batch-editing tools like [ImageMagick do NOT seem to do a good job handling sprites and palettes](https://github.com/ImageMagick/ImageMagick/discussions/6705).

### Creating a CG File

For now, this guide will assume you are porting a character from another game and that you have obtained their sprites, all indexed correctly _within a folder_. One important thing to note is that **you should probably not include any "effect" files within this folder**. Things such as fireballs, explosions, trails, glows - anything that doesn't seem to be directly attached to the character (and that may be higher-quality than the regular sprites) - should be isolated for use in **.PAT files**. That is because you will typically be unable to use these sprites within your CG file and they will usually appear very wrong - especially because they tend to not use the palette information in the rest of the sprites. Therefore, they may as well be a waste of space and clutter your sprites.

Sprites will be processed by increasing alphabetical order, and will be ordered as such in the CG file whenever you go to edit them. Because of that, if your sprites aren't already named somehow by number (`Name_000` going up is fine), it may be wise to number them as such, perhaps with [Bulk Rename Utility](https://www.majorgeeks.com/files/details/bulk_rename_utility.html).

If you know that your sprites are smaller than the ones normally found in UNI2, you may want to hold off from doing any pre-processing as stated in the note above. UNI2 can internally scale and turn sprites with HA6 editing. ***However, if you prefer and have been able to find a good method to batch-edit images while keeping their palette info intact, please feel free to share your methods with this repo.***

With that out of the way, you may now grab [the cgtool pack](tools/cgtool.7z) and extract it somewhere. To immediately make a .CG file, simply _drag and drop_ your **folder full of sprites** into the `cgtool_make_cg.bat` file, which should open a command line and process all the images, in turn creating a .CG file in the same directory named after the folder you inputted. You may prefer to open a command line yourself and enter `cgtool -input "FOLDER" -output FOLDER.cg` for the same result. Any errors may result out of non-PNG files being in the folder or some other inconsistency.

If you're familiar with HA6 editing down below, you may test your new CG file within your project and see if it displays using Hantei-chan. If you need to make changes within your folder, do so, and run the tool again to update the CG. However, assuming things have been smooth so far, you'll actually see that the sprites look **grayscale**. This is fine, though it means that you will have to now create a matching palette file (`.pal` file seen in other character folders) to go with your sprites - cgtool does not cause the "default" colour information to be normal by default.

### Modifying a CG File

This section is specifically for editing existing CG packages, such as if you wish to add or edit sprites to an existing character's set. Skip this if you aren't editing them.

Vanilla characters will have their CG files within their respective `data/chrXXX` folders. You're free to copy it over to where you have cgtool or process it right there, where you will now use `cgtool_extract_cg.bat` by dragging and dropping the file, resulting in a new `extracted` folder beside cgtool (you may also do `cgtool -input "chrXXX.cg" -output "extracted"`, optionally setting the output directory).

You will now have access to indexed sprites for your UNI2 character. You are able to reorder or add sprites, and can even remove them if that tickles your fancy. However, do note that as it applies to the previous section, "gaps" in names of sprites will not reflect in HA6 editing - there are no "empty slots" in a CG file, so if you have a "200.png" sprite and the next is "205.png", the file will have "205.png" be registered as ID 201. If you are adding sprites and are scared about messing up the order, simply make sure that your new sprites are last in the folder list. For example, if you've been using nothing but numbers, your "new" sprites could have a leading character - so you can use names such as "New_800", "z_1000", et cetera, and they should always be last in the file, without making changes to the previous sprites.

### Palettes

To create a .pal file for your character, I would recommend [getting these files here](tools/palette) and putting them in a new folder _within_ cgtool's folder - specifically because of `palettehelper.exe`, which will do some work for you. Inside that folder, add a copy of one of your character's sprites and name it "0.png". You can use any sprite you want that is indexed, and you can actually go as far as to make a "sprite sheet" that keeps the colour map for references to make custom paletting easier to visualize. Again, I would recommend LibreSprite for editing these images and for paletting.

![0](https://github.com/Fatih120/undernightinbirth/assets/18276369/0ee32bdd-4e23-496f-91bd-dc354a9fd4e9)

But for now, to make sure that your palettes can load and work to begin with, let's make your job easier by running `pal_dupe_images.py`. This will duplicate 0.png so you have your 41 base colour slots available in the game, which are all referred to with the txt file `TODO: can we pass with less colours? why did they do 41 colours, does 0 = 1?...`. Finally, execute `makePal.bat`, which will run palettehelper and pass the arguments needed where the TXT file lists all the image files to make a .pal for. Your shiny palette file should now come up, so put it into your project, test it out, and you should no longer see any grayscale - just your character in their normal colours.

If you want to already get to filling out the palette information for all the slots, there are several ways to do this. The slowest way is using your palette-editing tool to manually change all the colours. You might be able to cut corners and import the palette information from a sprite with different colours if the structure is the same. Some sprite dumps for other fighting game characters might have palettes laid out for you as seperate PNG files, which will make things very easy for you since you can just copy them to your palette folder and use them.

If you are trying to copy over an old Melty Blood character, you will notice that just using the original pal file will make the character's colour change when they switch sides, due to palettes being "half" or something like that. I have included the [riff2png script](tools/palette/riff2png.py) which will be able to convert the individual pal files [from online sprite rips](https://www.spriters-resource.com/playstation_2/mbaa/), making it easy to copy the output files over to your palette images. Just run the script within those palette directories and it will spit out the images in working order, allowing you to make a true palette, though the last few slots will have to be done by you.
