
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

screen drawAff():
    zorder 1000
    style_prefix "hkb"
    
            
    vbox:
        xpos 0.02

        ypos 0.05
        if store.persistent.aff_counter_enabled:
            if store.persistent.aff_counter_use_dot:
                text "Привязанность: [_mas_getAffection()]"
            else:
                text "Привязанность: [str(_mas_getAffection()).split('.')[0]]"
        
            
init 5 python:
    if store.persistent.aff_counter_enabled:
        config.overlay_screens.append("drawAff")


init python in aff_counter:
    import store

    if store.persistent.aff_counter_enabled is None:
        store.persistent.aff_counter_enabled = True
    
    if store.persistent.aff_counter_use_dot is None:
        store.persistent.aff_counter_use_dot = False

    
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
    
