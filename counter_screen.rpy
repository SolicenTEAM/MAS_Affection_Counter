screen counter_setting_pane():
    $ submods_screen_tt = store.renpy.get_screen("submods", "screens").scope["tooltip"]
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000

        hbox:
                style_prefix "check"
                box_wrap False
                textbutton _("Включено "):
                    action Function(store.aff_counter.toggle_counter)
                    selected persistent.aff_counter_enabled
                    hovered SetField(submods_screen_tt, "value", ("Включает счётчик привязанности. "))
                    unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)

                textbutton _("Показывать числа после точки"):
                    action Function(store.aff_counter.toggle_counter_dot)
                    selected persistent.aff_counter_use_dot
                    hovered SetField(submods_screen_tt, "value", ("Показывать числа после точки."))
                    unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)