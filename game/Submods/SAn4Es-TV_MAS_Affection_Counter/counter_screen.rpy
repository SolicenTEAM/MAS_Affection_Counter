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

                textbutton _("Числа после точки"):
                    action Function(store.aff_counter.toggle_counter_dot)
                    selected persistent.aff_counter_use_dot
                    hovered SetField(submods_screen_tt, "value", ("Показывать числа после точки."))
                    unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)

                textbutton _("Фон"):
                    action Function(store.aff_counter.toggle_counter_bg)
                    selected persistent.aff_counter_use_bg
                    hovered SetField(submods_screen_tt, "value", ("Показывать фон."))
                    unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)

                textbutton _("Уровень отношений"):
                    action Function(store.aff_counter.toggle_counter_subaff)
                    selected persistent.aff_counter_use_subaff
                    hovered SetField(submods_screen_tt, "value", ("Показывать показатель уровня отношений."))
                    unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)