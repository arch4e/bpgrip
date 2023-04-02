# bpgrip

Blender Painting Utility

## Installation

1. Download this add-on in zip
1. Import to Blender
   * `Edit >> Preferences >> Add-ons >> Install` 
1. Enable `bpgrip` 
1. Setup Keymap
   * `Edit >> Preferences >> Keymap >> 3D View >> ... >> Add New`
   * Change `none` to `bpgrip.set_bbmode`

## Keymap

```
[ Paint in Sculpt Mode ]
Keymap    : 3D View >> Sculpt >> Sculpt (Global)
bl_mode   : Paint
bb_mode   : MIX, ADD, etc...

[ Texture Paint Mode ]
Keymap    : 3D View >> Image Paint >> Image Paint (Global)
bl_mode   : TexDraw
bb_mode   : MIX, ADD, etc...

[ Vertex Paint Mode ]
Keymap    : 3D View >> 3D View >> Vertex Paint >> Vertex Paint (Global)
bl_mode   : Draw
bb_mode   : MIX, ADD, etc...

[ Weight Paint Mode ]
Keymap    : 3D View >> Weight Paint >> Weight Paint (Global)
bl_mode   : Draw
bb_mode   : MIX, ADD, etc...
```

## License

MIT
