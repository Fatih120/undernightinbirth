#### Binary

Any file that isn't an easily editable text file. Typically requires use of tools or [hex editing](#Hex), such as [PAT](#PAT) files.

#### CG

"Character Graphic" files. These contain all the image data used for a character in the form of [indexed, paletted](#Palette) [sprites](#Sprite). They don't contain the palettes themselves.

The sprites in CGs use incremental IDs for use in [Hantei-chan](#Hantei-chan) that are sorted in alphanumeric order within the folder you're converting. This means that if you're converting sprites into CG but have added files in the middle of your directory, some of the sprites may shift their ID. This may end up being an issue if you need to add sprites while making a character.

For example, let's say you have PNGs with the filenames "A", "B", and "C". These would internally have the IDs of 0, 1 and 2 respectively. If you now edited the set to have "A", "Aasdw", "B", and "C", these would now have the IDs of 0, 1, 2, and 3, meaning Aasdw stole B's slot and the rest of the images are now 1 higher, which would be a problem if you were already using those sprites. You can circumvent this by adding sprites to the end of the CG by using prefixes such as "z" which will likely take up new IDs.

#### DDS

Microsoft's DirectDraw Surface image files. They're usually for textures in other games, but are strangely used for nearly *everything* in UNI2 - perhaps because they work better with GPUs. Most of the menus rely on DDS files, and so do character effects. However, they're almost always stored within a [PAT](#PAT) file and tend to require [hex editing](#Hex) to replace.

They can have several compression types not unlike PNGs, however, due to how [FB](#French Bread) operates, a lot of these are bloated, uncompressed images that use DXT5 (specifically B8G8R8A8 / Linear A8R8G8B8) format. On one hand, it explains why the game can be compressed to an impressively-small size using [CompactGUI](https://github.com/IridiumIO/CompactGUI "CompactGUI"), but on the other hand, it makes it easier to replace textures with PAT files without worrying about filesize offsets. In fact, compressed DDS textures can be a roadblock as UNI2 seems to change how they load.

Two programs that can easily export DDS graphics are [GIMP](https://www.gimp.org/ "GIMP") and [Paint.NET](https://www.getpaint.net/ "Paint.NET").

#### French Bread

The developers of UNI2. Not to be confused with ArcSys who only publishes and provides ports. Usually shortened to FB.

#### HA6

Hantei (Animation) v6 File. This file type is a binary that contains moveset or animation data for characters and visual effects, which also includes attack and hitbox data. Is the main piece of data needed for characters to carry out actions, including state data, animation data, attack data, and manipulative effects. HA6 are the bones whereas the [Mv data](#Mv) is the meat. They don't contain any graphics, but typically link to other [CG](#CG) and [PAT](#PAT) files, and can carry up to 999 [patterns](#Pattern).

They can be opened and viewed with any fork of [Hantei-chan](#Hantei-chan).

#### Hantei

The code name for [French Bread](#French Bread)'s data system for how characters interact with the game and other characters. Usually the word itself will refer to [HA6](#HA6) data, and there's not much of a differentiation, but it's worth nothing that Hantei data is very engrained to the point of being used since early Melty Blood, and convoluted [Mv](#Mv) functions can call for it.

"Hantei" might come from the Judo word regarding judgement, or might mean nothing.

#### Hantei-chan

An open-source editor for [HA6](#HA6) files. It provides an interface to edit a character's moveset, including all their [patterns](#Pattern) and data. Characters can be entirely made within it, and it will load [CGs](#CG), [PATs](#PAT), and [Palettes](#Palette) just fine.

Due to the nature of a niche game and differing needs, there are several seperate to the program done by different contributors.

#### Hex

Hexadecimal - particularly in reference to [hex dumps](https://en.wikipedia.org/wiki/Hex_dump "hex dumps") and [hex editing](https://en.wikipedia.org/wiki/Hex_editor "hex editing").

When this is brought up, it's in regards to opening a file in it's raw state, especially when some formats such as [PATs](#PAT) are [binary](#Binary) files. You'll have to do some hex editing if you want to surgically replace files or edit particular data that you can't with regular tools, and may be aided with use of debuggers and the such that are out of the scope of the glossary.

#### Part

A "piece" of a texture when editing [PAT](#PAT) files. Parts are chosen with X/Y + W/H data with a few other parameters which then let you use and manipulate them for [PAT patterns](#Pattern).

#### PAT

"P Animation" data file. Not to be confused with "[patterns](#Pattern)" when "pats" are mentioned. PATs are always used as graphic data for images, effects and other UIs where indexed character [sprites](#Sprite) are not. They contain [DDS](#DDS) files and lots of binary data that dictate the appearance, animations, and ["parts"](#Part) of graphics, among other things. Characters will use them for their visual effects, and most menu elements are using a .pat file.

Character and effect PATs can usually be opened with [pani edit](#pani edit) to create effects, while a majority of system PATs require [hex editing](#Hex) or using scripts to manipulate.

#### pani edit

A [PAT](#PAT) editor, mostly for character effects. It lets you add [DDS](#DDS) files and arrange [parts](#Part) for them to create dynamic, fluid animations, which are then referenced by the [HA6](#HA6) file.

#### Pattern
- The name for an animation entry in an [HA6](#HA6) file, which can be a character's move data and/or animations using PAT patterns - see the next bullet.
- A single finalized "sprite" within a [PAT](#PAT) file. A bit of a misnomer compared to HA6: this would be more of a "frame" than a full "pattern" as several of these will sequentially animate in a list. Patterns here can be comprised of many put-together [parts](#Part). Each pattern can be interpolated across each other.

#### Sprite

A sprite is an image used to represent a character. In most cases, we're talking about a PNG file that is "indexed", which means that each pixel on the picture doesn't have its own color, but instead references an index of a limited palette of colors. This explains how character sprites can have several palettes (or color sets), because the same sprite can have different colors without changing the sprite data itself.

Non-indexed images such as [DDS](#DDS) used for effects are not included in this terminology. We use sprite when we want to talk about how a character itself looks or talk about the files they use, which in the case of UNI2, uses a pixellated/dot style.

Sprite IDs may also be mentioned when using [Hantei-chan](#Hantei-chan) to choose which sprite appears during a [Frame](#Frame)

#### Palette

A set of colors used for a character to have several different color options. Please refer to [Sprite](#Sprite). In UNI2, characters will have a ".pal" file to display properly, which has a list of color information. We can convert a set of PNG images that each have a different indexed palette into this format.

#### Frame

This can have several meanings based on the context:

- Ingame, 1/60th of a second. The game only "updates" every frame, so this timing is used to explain temporal concepts such as frame data.
- A frame of a [pattern](#Pattern) (made up of several frames) within [Hantei-chan](#Hantei-chan), which can last a certain amount of *time* frames. A frame here will contain a single [sprite](#Sprite) and have individual properties.
- The outer bounds or "canvas" of an image - if it's a [DDS](#DDS) made up of several images, for example, this could be used to define the "frame" of a single [part](#Part).
