
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal(),

keys = [
    Key([mod], "a", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "d", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "s", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "w", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "a", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "d", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "s", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "w", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "a", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "s", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "w", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "k", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "k", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus='#999999', border_normal='#333333', border_width=3, margin=9, border_on_single=True),
    layout.Max(border_focus='#ffffff', border_normal='#cccccc', border_width=3, margin=9),
]

widget_defaults = dict(
    font="monospace",
    fontsize=16,
    padding=9,
    foreground='#ffffff',
    active='#ffffff',
    inactive='#333333',
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                # widget.Battery(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            24,
            border_width=[3, 0, 3, 0],
            border_color=["#333333", "#333333", "#333333", "#333333"]
            ),
        # x11_drag_polling_rate = 60,
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "archQzen"
