def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(500)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.pause(500)
    basic.show_icon(IconNames.HEART)
    music.play_melody("G B A G C5 B A B ", 120)
basic.forever(on_forever)
