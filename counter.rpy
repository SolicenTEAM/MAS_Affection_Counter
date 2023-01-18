
init -990 python in mas_submod_utils:
    Submod(
        author="SAn4es_TV",
        name="Affection Counter",
        description="Показывает счётчик отношений с Моникой",
        version="0.5",
        dependencies={},
        settings_pane="counter_setting_pane",
        version_updates={}
    )

style counter_button:
    background Frame("mod_assets/buttons/generic/idle_bg.png", Borders(5, 5, 5, 5), tile=False)

style counter_button_text:
    color "#fff"

style ncounter_button_text:
    color "#fff"
    
screen drawAff():
    zorder 1000
    
            
    vbox:
        spacing 5
        if store.persistent.aff_counter_use_bg:
            style_prefix "counter"
        else:
            style_prefix "ncounter"
        xpos 0.02

        ypos 0.05
        if store.persistent.aff_counter_enabled:
            if store.persistent.aff_counter_use_dot:
                textbutton  "Привязанность: [_mas_getAffection()]"
            else:
                textbutton  "Привязанность: [str(_mas_getAffection()).split('.')[0]]"
            if store.persistent.aff_counter_use_subaff:
                textbutton "[mas_curr_affection]"
        
            
init 5 python:
    if store.persistent.aff_counter_enabled:
        config.overlay_screens.append("drawAff")


init python in aff_counter:
    import store

    if store.persistent.aff_counter_enabled is None:
        store.persistent.aff_counter_enabled = True
    
    if store.persistent.aff_counter_use_dot is None:
        store.persistent.aff_counter_use_dot = False

    if store.persistent.aff_counter_use_bg is None:
        store.persistent.aff_counter_use_bg = True

    if store.persistent.aff_counter_use_subaff is None:
        store.persistent.aff_counter_use_subaff = True

    
    def toggle_counter():
        from store import persistent
        if persistent.aff_counter_enabled:
            persistent.aff_counter_enabled = False
            return
        else:
            persistent.aff_counter_enabled = True
            return
    
    def toggle_counter_dot():
        from store import persistent
        if persistent.aff_counter_use_dot:
            persistent.aff_counter_use_dot = False
            return
        else:
            persistent.aff_counter_use_dot = True
            return
            
    def toggle_counter_bg():
        from store import persistent
        if persistent.aff_counter_use_bg:
            persistent.aff_counter_use_bg = False
            return
        else:
            persistent.aff_counter_use_bg = True
            return
            
    def toggle_counter_subaff():
        from store import persistent
        if persistent.aff_counter_use_subaff:
            persistent.aff_counter_use_subaff = False
            return
        else:
            persistent.aff_counter_use_subaff = True
            return
    
