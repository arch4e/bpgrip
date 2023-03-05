# bpgrip

Blender Painting Utility

## Installation

1. Download this add-on in zip
1. Import to Blender
   * `Edit >> Preferences >> Add-ons >> Install` 
1. Enable `bpgrip` 
1. Setup Keymap
   * `Edit >> Preferences >> Keymap >> 3D View >> ... >> Add New`
   * Change `none` to `bpgrip.*`

## Keymap

```
[ Paint in Sculpt Mode ]
Keymap    : 3D View >> Sculpt >> Sculpt (Global)
Identifier: bpgrip.set_bbmode_paint_<mode>

[ Texture Paint Mode ]
Keymap    : 3D View >> Image Paint >> Image Paint (Global)
Identifier: bpgrip.set_bbmode_texdraw_<mode>

[ Vertex Paint Mode ]
Keymap    : 3D View >> 3D View >> Vertex Paint >> Vertex Paint (Global)
Identifier: bpgrip.set_bbmode_draw_<mode>

[ Weight Paint Mode ]
Keymap    : 3D View >> Weight Paint >> Weight Paint (Global)
Identifier: bpgrip.set_bbmode_draw_<mode>
```

## License

MIT

