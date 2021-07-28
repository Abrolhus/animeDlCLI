import mpv
print("vai")
player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
player.play('../testeMpvJsonIpc/v3.mp4')
player.playlist_append('../testeMpvJsonIpc/v2.mp4', title="VAAAAAAI")
#player.loadfile('../testeMpvJsonIpc/v2.mp4', 'append', 'title="VAAAIPFFFF"')
print("vai1")
player.wait_for_property('idle-active')
