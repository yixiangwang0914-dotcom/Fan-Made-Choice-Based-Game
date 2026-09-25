screen chapter_select():
    tag menu

    add "images/背景/主界面背景/sl_bg.png"
    text "记忆梳理":
        xpos 40
        ypos 28
        size 72
        color "#ffffff"
        outlines [(1, "#000000", 0, 0)]
        font "xiqueyanshu.ttf"

    viewport:
        draggable True
        mousewheel True
        xysize (1920, 1080)
        child_size (6000, 1080)   # 调整宽度以适应所有按钮


        fixed:
            # ===== 第一页按钮（原坐标不变） =====

            # 序章
            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("start"), None)
                xpos 5
                ypos 450
                fixed:
                    xfill True
                    yfill True
                    text "记 第一章":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "寻雁":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "1641年":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35

                vbox:
                    xpos 500
                    ypos 85
                    spacing 10

                    for i in range(15):
                        add Solid("#b8b8b8", xysize=(6, 6))

            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("失败"), None)
                xpos 300
                ypos 700
                fixed:
                    xfill True
                    yfill True
                    text "坏结局":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "雁飞":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35


            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("chapter2"), None)
                xpos 900
                ypos 450
                fixed:
                    xfill True
                    yfill True
                    text "记 第二章":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "雁归":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "1641年":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35

                    hbox:
                        xpos -300
                        ypos 40
                        spacing 10

                        for i in range(20):
                            add Solid("#b8b8b8", xysize=(6, 6))



            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("chapter3"), None)
                xpos 1795
                ypos 450
                fixed:
                    xfill True
                    yfill True
                    text "记 第三章":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "引蝶":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "1641年":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35

                    hbox:
                        xpos -300
                        ypos 40
                        spacing 10

                        for i in range(20):
                            add Solid("#b8b8b8", xysize=(6, 6))

                    vbox:
                        xpos 500
                        ypos 85
                        spacing 10

                        for i in range(15):
                            add Solid("#b8b8b8", xysize=(6, 6))



            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("chapter4"), None)
                xpos 2690
                ypos 450
                fixed:
                    xfill True
                    yfill True
                    text "记 第四章":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "蝶化":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "1641年":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35

                    hbox:
                        xpos -300
                        ypos 40
                        spacing 10

                        for i in range(20):
                            add Solid("#b8b8b8", xysize=(6, 6))

                    vbox:
                        xpos 500
                        ypos -230
                        spacing 10

                        for i in range(15):
                            add Solid("#b8b8b8", xysize=(6, 6))


            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("chapter4_breath_hold_failed"), None)
                xpos 2941
                ypos 200
                fixed:
                    xfill True
                    yfill True
                    text "坏结局":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "蝶散":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35



            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("bad_ending"), None)
                xpos 2045
                ypos 700
                fixed:
                    xfill True
                    yfill True
                    text "坏结局":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "一事无成":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35



            button:
                background Frame("gui/选项/flowchart_data_bg_J.png", 10, 10)
                hover_background Frame("gui/选项/flowchart_data_bg_Y.png", 10, 10)
                hover_sound "audio/界面点击音效/Highlight_New.ogg"
                activate_sound "audio/界面点击音效/Click_New.ogg"
                xsize 650
                ysize 100
                action Confirm("是否载入此章？", Start("chapter5"), None)
                xpos 3585
                ypos 450
                fixed:
                    xfill True
                    yfill True
                    text "记 第五章":
                        size 28
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSansLite.ttf"
                        xpos 180
                        yalign 0.5
                    text "归途":
                        size 70
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "xiqueyanshu.ttf"
                        xpos 280
                        ypos 15
                        kerning -28
                    text "1641年":
                        size 35
                        color "#ffffff"
                        outlines [(0.5, "#000000", 0, 0)]
                        font "SourceHanSerifCN-Bold.otf"
                        xpos 420
                        ypos 35

                    hbox:
                        xpos -300
                        ypos 40
                        spacing 10

                        for i in range(20):
                            add Solid("#b8b8b8", xysize=(6, 6))

                    vbox:
                        xpos 500
                        ypos -230
                        spacing 10

                        for i in range(15):
                            add Solid("#b8b8b8", xysize=(6, 6))






# ========== 右下角返回按钮 ==========
    vbox:
        xalign 0.95
        yalign 1.0
        yoffset -30
        spacing 10
        imagebutton:
            idle "gui/buttons/back_idle.png"
            hover "gui/buttons/back_hover.png"
            action Return()
            hover_sound "audio/界面点击音效/Highlight_New.ogg"
            activate_sound "audio/界面点击音效/Click_New.ogg"
