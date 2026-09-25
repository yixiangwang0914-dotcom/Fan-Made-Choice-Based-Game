################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):

    window:
        id "window"
        background "images/UI_Box1.png"
        yalign 0.925
    
        if who is not None:
        

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    imagebutton:
        idle "gui/hide_idle.png"
        hover "gui/hide_hover.png"
        action HideInterface()
        xalign 0.625
        yalign 0.999


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


default timed_choice_count = 0

screen timed_choice(items, timeout=5.0, timeout_label="bad_ending", max_choices=10, over_limit_label=None, choice_count_variable="timed_choice_count", reset_id=None):
    style_prefix "choice"

    default time_left = timeout
    default last_reset_id = None

    on "show" action SetScreenVariable("time_left", timeout)
    on "replace" action SetScreenVariable("time_left", timeout)

    $ current_reset_id = reset_id or id(items)
    if last_reset_id != current_reset_id:
        $ time_left = timeout
        $ last_reset_id = current_reset_id

    $ limit_label = over_limit_label or timeout_label
    $ current_choices = getattr(renpy.store, choice_count_variable, 0)
    timer 0.1 repeat True action If(
        time_left <= 0.1,
        Jump(timeout_label),
        SetScreenVariable("time_left", max(0.0, time_left - 0.1))
    )

    $ seconds_left = int(time_left + 0.999)

    frame:
        style "timed_choice_countdown"
        hbox:
            spacing 10
            text "剩余时间" style "timed_choice_countdown_text"
            text "[seconds_left]" style "timed_choice_countdown_number"
            text "秒" style "timed_choice_countdown_text"
            if max_choices is not None:
                text "  选择次数 [current_choices]/[max_choices]" style "timed_choice_countdown_text"

    vbox:
        for i in items:
            if max_choices is None:
                textbutton i.caption action i.action
            else:
                $ over_limit = current_choices >= max_choices
                textbutton i.caption action [SetVariable(choice_count_variable, current_choices + 1), If(over_limit, Jump(limit_label), i.action)]

transform breath_hold_cursor(duration, distance):
    xoffset 0
    linear duration xoffset distance

screen breath_hold_round(safe_start=0.2, safe_width=0.25, duration=2.0, round_index=1, total_rounds=5):
    modal True
    zorder 180

    default progress = 0.0

    $ bar_width = 900
    $ bar_height = 46
    $ cursor_width = 8
    $ safe_x = int(bar_width * safe_start)
    $ safe_w = int(bar_width * safe_width)

    key "mouseup_1" action If(safe_start <= progress <= safe_start + safe_width, Return(True), Return(False))
    key "K_SPACE" action If(safe_start <= progress <= safe_start + safe_width, Return(True), Return(False))
    timer 0.02 repeat True action If(
        progress >= 1.0,
        Return(False),
        SetScreenVariable("progress", min(1.0, progress + 0.02 / duration))
    )

    frame:
        style "breath_hold_panel"

        vbox:
            spacing 16
            xalign 0.5

            hbox:
                xalign 0.5
                spacing 24
                text "屏住呼吸" style "breath_hold_title"
                text "[round_index]/[total_rounds]" style "breath_hold_count"

            fixed:
                xysize (bar_width, bar_height)

                add Solid("#080a10dd") xysize (bar_width, bar_height)
                add Solid("#ffffff") xpos safe_x xysize (safe_w, bar_height)
                add Solid("#ff4b4b") ypos -12 xysize (cursor_width, bar_height + 24) at breath_hold_cursor(duration, bar_width - cursor_width)

            text "等红线进入白色区域时点击鼠标" style "breath_hold_hint"


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style timed_choice_countdown is frame
style timed_choice_countdown_text is text
style timed_choice_countdown_number is text
style breath_hold_panel is frame
style breath_hold_title is text
style breath_hold_count is text
style breath_hold_hint is text

style choice_vbox:
    xalign 0.5
    ypos 400
    yanchor 0.5
    spacing -40

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Frame("gui/选项/自然.png", 10, 10)
    hover_background Frame("gui/选项/悬浮.png", 10, 10)
    xsize 1000  # 固定宽度
    ysize 158    # 固定高度
    activate_sound "audio//界面点击音效/点击1.ogg"  # 【关键】点击按钮时播放的音效
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"     # 【关键】鼠标悬停时播放的音效

style choice_button_text is default:
    # properties gui.text_properties("choice_button")
    size 32                 # 文字大小（像素）
    font "SourceHanSerifCN-Bold.otf"  # 字体文件路径
    color "#ffffff"         # 文字颜色（可选）
    hover_color "#ffffff"   # 鼠标悬停时的颜色（可选）
    xalign 0.55              # 水平居中
    yalign 0.48              # 垂直居中

style timed_choice_countdown:
    xalign 0.5
    ypos 120
    xpadding 28
    ypadding 14
    background Frame(Solid("#00000099"), 12, 12)

style timed_choice_countdown_text:
    size 30
    font "SourceHanSerifCN-Bold.otf"
    color "#ffffff"

style timed_choice_countdown_number:
    size 42
    font "SourceHanSerifCN-Bold.otf"
    color "#ffdf6b"

style breath_hold_panel:
    xalign 0.5
    ypos 70
    xpadding 38
    ypadding 24
    background Frame(Solid("#000000aa"), 14, 14)

style breath_hold_title:
    size 34
    font "SourceHanSerifCN-Bold.otf"
    color "#ffffff"

style breath_hold_count:
    size 30
    font "SourceHanSerifCN-Bold.otf"
    color "#ffdf6b"

style breath_hold_hint:
    xalign 0.5
    size 24
    font "SourceHanSerifCN-Bold.otf"
    color "#d7d7d7"

## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():
    zorder 100

    if quick_menu:
        # 获取当前鼠标悬停按钮的提示文本
        $ tooltip_text = GetTooltip()

        hbox:
            style_prefix "quick"
            style "quick_menu"
            spacing 8                     # 按钮之间的间距（像素）
            xalign 1.0      # 水平靠右
            yalign 1.0      # 垂直靠下（底部）

            # 回退
            imagebutton auto "gui/buttons/back_%s.png" action Rollback() tooltip "回退到上一段文本" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 历史
            imagebutton auto "gui/buttons/history_%s.png" action ShowMenu('history') tooltip "查看对话历史" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 快进（注意：右键快进功能已简化，如需保留请参考下方说明）
            imagebutton auto "gui/buttons/skip_%s.png" action Skip() tooltip "快进文本" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 自动
            imagebutton auto "gui/buttons/auto_%s.png" action Preference("auto-forward", "toggle") tooltip "自动前进模式" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 保存
            imagebutton auto "gui/buttons/save_%s.png" action ShowMenu('save') tooltip "保存游戏" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 快存
            imagebutton auto "gui/buttons/quicksave_%s.png" action QuickSave() tooltip "快速保存" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 读取
            imagebutton auto "gui/buttons/quickload_%s.png" action ShowMenu('load') tooltip "读取存档" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"
            # 设置
            imagebutton auto "gui/buttons/prefs_%s.png" action ShowMenu('preferences') tooltip "游戏设置" hover_sound "audio/界面点击音效/鼠标滑动.ogg" activate_sound "audio/界面点击音效/点击1.ogg"

        # 显示悬停提示框（位于按钮上方）
        if tooltip_text:
            frame:
                xalign 0.5                 # 水平居中
                yalign 0.95                # 靠近屏幕底部（按钮上方）
                background Frame("#000000aa", 5, 5)   # 半透明黑色圆角背景
                padding (15, 5)
                text tooltip_text:
                    color "#ffffff"
                    size 20
                    # font "gui/font/YourFont.ttf"  # 可改为你喜欢的字体


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():
    if main_menu and renpy.get_screen("main_menu"):
            fixed:
                # 右上角的设置按钮 (建议也换成 imagebutton)
                hbox:
                    align (1.0, 0.0)
                    xoffset -20
                    yoffset 20

                    imagebutton:
                        idle "gui/button/title_button/title_button_sys_normal.png"     # 普通状态图片
                        hover "gui/button/title_button/title_button_sys_click.png"   # 悬停状态图片
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action ShowMenu("preferences")

                    imagebutton:
                        idle "gui/button/title_button/title_button_exit_normal.png"     # 普通状态图片
                        hover "gui/button/title_button/title_button_exit_click.png"   # 悬停状态图片
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action Quit(confirm=True)   # 退出游戏（弹出确认对话框）

                imagebutton:
                    idle Transform("images/背景/主界面背景/gaokao.png", xsize=272, ysize=86)
                    hover Transform("images/背景/主界面背景/gaokao2.png", xsize=272, ysize=86)
                    hover_sound "audio/界面点击音效/Highlight_New.ogg"
                    activate_sound "audio/界面点击音效/Click_New.ogg"
                    xalign 0.0
                    yalign 0.0
                    xoffset 40
                    yoffset 40
                    action Start("zhufu")

                # 底部水平排列的五个按钮
                hbox:
                    align (0.5, 1.0)
                    spacing 70
                    yoffset -40
                        
                    # 按钮 1: 记忆浮现
                    imagebutton:
                        idle "gui/button/title_button/title_button_start_normal.png"
                        hover "gui/button/title_button/title_button_start_click.png"
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action Start()
                    # 按钮 2: 记忆回响
                    imagebutton:
                        idle "gui/button/title_button/title_button_continue_normal.png"
                        hover "gui/button/title_button/title_button_continue_click.png"
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action ShowMenu("load")
                    # 按钮 3: 记忆梳理
                    imagebutton:
                        idle "gui/button/title_button/title_button_load_normal.png"
                        hover "gui/button/title_button/title_button_load_click #22495.png"
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action ShowMenu("chapter_select")
                    # 按钮 4: 浮光掠影
                    imagebutton:
                        idle "gui/button/title_button/title_button_extra_normal.png"
                        hover "gui/button/title_button/title_button_extra_click #22507.png"
                        hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                        activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                        action ShowMenu("cg_gallery")

                    # 按钮 5: 良田满穗
                    # imagebutton:
                    #     idle "gui/button/title_button/title_button_aonther_normal.png"
                    #     hover "gui/button/title_button/title_button_aonther_click.png"
                    #     hover_sound "audio/界面点击音效/Highlight_New.ogg"      # 鼠标悬停音效
                    #     activate_sound "audio/界面点击音效/Click_New.ogg"   # 点击音效
                    #     action NullAction()

    else:
        # 游戏内菜单：保持原来的垂直布局（不变）
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5
            spacing gui.navigation_spacing

            textbutton _("历史") action ShowMenu("history")
            textbutton _("保存") action ShowMenu("save")
            textbutton _("记忆回响") action ShowMenu("load")
            textbutton _("设置") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("结束回放") action EndReplay(confirm=True)
            else:
                textbutton _("标题菜单") action MainMenu()

            textbutton _("关于") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("帮助") action ShowMenu("help")

            if renpy.variant("pc"):
                textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style high_school_button is navigation_button:
    background None
    hover_background None
    insensitive_background None
    xpadding 0
    ypadding 0

style high_school_button_text is navigation_button_text:
    color "#ffffff"
    hover_color "#dabb3c81"


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu

# 在 screens.rpy 的开头（或任何 init 之前）定义视频
image menu_bg = "images/背景/主界面背景/主页面.png"

#Movie(play="video/menu_bg.webm", loop=True, channel="movie")

screen main_menu():
    tag menu
    
    on "show" action Play("music", "music/BGM/哀鸿_葬花埋香.ogg", fadein=1.0)
    on "hide" action Stop("music", fadeout=1.0)

    add "menu_bg":
        zoom 1.0

    # 暗化层（可选，强度可调）
    #frame:
        #background "#00000060"   # 更淡的黑色
        #xfill True
        #yfill True

    # 添加 Logo 图片（悬浮在暗化层上方）
    # add "gui/splash.png" at truecenter   # 屏幕正中央
    # 或者指定自定义位置：
    #add "gui/splash.png" xalign 1.6 yalign 0.3 zoom 2
    add "gui/button/title_button/字体尾巴/桥.png" xalign 0.185 yalign 0.995 zoom 1
    add "images/背景/主界面背景/毛笔.png" zoom 0.17 xalign 0.006 yalign 0.020
    add "gui/button/title_button/字体尾巴/dialog_menu_explaintext_bg 1.png" xalign 0.185 yalign 0.965 zoom 1
    add "gui/button/title_button/字体尾巴/dialog_menu_explaintext_bg 1.png" xalign 0.815 yalign 0.965 zoom 1

    use navigation

    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

# style main_menu_frame:
#     xsize 560
#     yfill True

#     background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -40
    xmaximum 1600
    yalign 1.0
    yoffset -40

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。可使用屏幕标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。此屏幕旨在与一个或多个子
## 屏幕同时使用，这些子屏幕将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    if title == "__memory_recall_title":
        add "gui/button/title_button/title_button_continue_normal.png":
            xpos 100
            ypos 70
    elif title == "__cg_gallery_title":
        add "gui/button/title_button/title_button_extra_normal.png":
            xpos 100
            ypos 70
    else:
        label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 60
    top_padding 240

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 380
    yfill True

style game_menu_content_frame:
    left_margin 50
    right_margin 40
    top_margin 20

style game_menu_viewport:
    xsize 1450

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 20

style game_menu_label:
    xpos 100
    ysize 240
    yoffset -20

style game_menu_label_text:
    size 100
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60


style cg_gallery_label is gui_label
style cg_gallery_label_text is main_menu_title


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此屏幕没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义屏
## 幕。

screen about():

    tag menu

    ## 此 use 语句将 game_menu 屏幕包含到了这个屏幕内。子级 vbox 将包含在
    ## game_menu 屏幕的 viewport 内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## gui.about 通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"), mode="save")


screen load():

    tag menu

    use file_slots("__memory_recall_title", mode="load")


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5
                yoffset -80

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) 给出 1 到 9 之间的数字。
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("上传同步"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("下载同步"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 100
    ypadding 6
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"

style slot_button_text:
    properties gui.text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(" ", scroll="viewport"):

        vbox:
            xoffset 30

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        xoffset 18

                        add "gui/hua_button.png":
                            xpos 0
                            yoffset 30

                        hbox:
                            xoffset 80
                            spacing 35
                            yoffset 50

                            imagebutton:
                                idle "gui/chuuangkou_button.png"
                                hover "gui/chuuangkouhover_button.png"
                                selected_idle "gui/chuuangkouhover_button.png"
                                selected_hover "gui/chuuangkouhover_button.png"
                                hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                                activate_sound "audio/界面点击音效/点击1.ogg"
                                action Preference("display", "window")

                            imagebutton:
                                idle "gui/quanpin_button.png"
                                hover "gui/quanpinhover_button.png"
                                selected_idle "gui/quanpinhover_button.png"
                                selected_hover "gui/quanpinhover_button.png"
                                hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                                activate_sound "audio/界面点击音效/点击1.ogg"
                                action Preference("display", "fullscreen")

                        add "gui/xuanxiang_button.png":
                            xpos 0
                            yoffset 100

                        hbox:
                            spacing 35
                            xoffset 80
                            yoffset 100

                            imagebutton:
                                idle "gui/quanbu_button.png"
                                hover "gui/quanbuhover_button.png"
                                selected_idle "gui/quanbuhover_button.png"
                                selected_hover "gui/quanbuhover_button.png"
                                hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                                activate_sound "audio/界面点击音效/点击1.ogg"
                                action Preference("skip", "toggle")

                            imagebutton:
                                idle "gui/yidu_button.png"
                                hover "gui/yiduhover_button.png"
                                selected_idle "gui/yiduhover_button.png"
                                selected_hover "gui/yiduhover_button.png"
                                hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                                activate_sound "audio/界面点击音效/点击1.ogg"
                                action Preference("after choices", "toggle")

            null height (4 * gui.pref_spacing)

            hbox:
                box_wrap True

                vbox:
                    xoffset 18
                    yoffset 50

                    add "gui/wenzi_button.png":
                        xpos 0
                        yoffset 75

                    hbox:
                        xoffset 80
                        spacing 10
                        yoffset 75

                        text _("慢"):
                            yalign 0.5
                            color "#ffffff"
                            outlines [(0.5, "#000000", 0, 0)]

                        bar:
                            value Preference("text speed")
                            xsize 500
                            ysize 40
                            left_bar "gui/slidebar.png"
                            right_bar "gui/slidebar.png"
                            thumb "gui/slidebox0.png"
                            hover_thumb "gui/slidebox.png"

                        text _("快"):
                            yalign 0.5
                            color "#ffffff"
                            outlines [(0.5, "#000000", 0, 0)]

                    text _("自动前进时间"):
                        xpos 0
                        yoffset 135
                        size 28
                        color "#ffffff"
                        outlines [(1, "#000000", 0, 0)]

                    hbox:
                        xoffset 80
                        spacing 10
                        yoffset 150

                        text _("慢"):
                            yalign 0.5
                            color "#ffffff"
                            outlines [(0.5, "#000000", 0, 0)]

                        bar:
                            value Preference("auto-forward time")
                            xsize 500
                            ysize 40
                            left_bar "gui/slidebar.png"
                            right_bar "gui/slidebar.png"
                            thumb "gui/slidebox0.png"
                            hover_thumb "gui/slidebox.png"

                        text _("快"):
                            yalign 0.5
                            color "#ffffff"
                            outlines [(0.5, "#000000", 0, 0)]

                vbox:
                    xoffset -30
                    yoffset -250

                    if config.has_music:
                        add "gui/bgm_button.png":
                            xpos -100

                        hbox:
                            xoffset 35
                            yoffset -10

                            text _("小"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                            bar:
                                value Preference("music volume")
                                xsize 480
                                ysize 40
                                left_bar "gui/slidebar.png"
                                right_bar "gui/slidebar.png"
                                thumb "gui/slidebox0.png"
                                hover_thumb "gui/slidebox.png"

                            text _("大"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                    if config.has_sound:

                        add "gui/se_button.png":
                            xpos -92
                            yoffset 50

                        hbox:
                            xoffset 35
                            yoffset 40

                            text _("小"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                            bar:
                                value Preference("sound volume")
                                xsize 480
                                ysize 40
                                left_bar "gui/slidebar.png"
                                right_bar "gui/slidebar.png"
                                thumb "gui/slidebox0.png"
                                hover_thumb "gui/slidebox.png"

                            text _("大"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        add "gui/voice_button.png":
                            xpos -92
                            yoffset 135

                        hbox:
                            xoffset 35
                            yoffset 125

                            text _("小"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                            bar:
                                value Preference("voice volume")
                                xsize 480
                                ysize 40
                                left_bar "gui/slidebar.png"
                                right_bar "gui/slidebar.png"
                                thumb "gui/slidebox0.png"
                                hover_thumb "gui/slidebox.png"

                            text _("大"):
                                yalign 0.5
                                color "#ffffff"
                                outlines [(0.5, "#000000", 0, 0)]

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        button:
                            xoffset 500
                            yoffset 135
                            action Preference("all mute", "toggle")
                            xpadding 5
                            ypadding 5
                            background Frame("#000", 2, 2)
                            hover_background Frame("#fff", 2, 2)
                            selected_background Frame("#fff", 2, 2)
                            hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                            activate_sound "audio/界面点击音效/点击1.ogg"

                            text _("全部静音"):
                                color "#ffffff"
                                hover_color "#000000"
                                selected_color "#000000"
                                size 20

            null height (2 * gui.pref_spacing)

            hbox:
                spacing 80
                xalign 0.5

                textbutton _("关于") action ShowMenu("about") style "prefs_footer_button"
                textbutton _("帮助") action ShowMenu("help") style "prefs_footer_button"
                textbutton _("退出游戏") action Quit(confirm=True) style "prefs_footer_button"

    add "gui/button/my_icon.png" zoom 1.2 xpos 20 ypos -5

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style prefs_footer_button is navigation_button
style prefs_footer_button_text is navigation_button_text

style prefs_footer_button:
    background None
    hover_background None
    selected_background None
    xpadding 22
    ypadding 0

style prefs_footer_button_text:
    font gui.navigation_button_text_font
    size 54
    color "#8d8d8d"
    hover_color "#ffffff"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    outlines [(1, "#00000080", 0, 0)]

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style radio_button:
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style check_button:
    hover_sound "audio/界面点击音效/鼠标滑动.ogg"

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 4

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 300

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 20

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 900


## CG 库屏幕 ########################################################################
##
## 显示已解锁的CG集合

screen cg_gallery():

    tag menu
    
    style_prefix "cg_gallery"

    python:
        gallery_unlocked = unlocked_cgs
        if not gallery_unlocked:
            gallery_unlocked = getattr(persistent, "unlocked_cgs", []) or []
        gallery_rows = max(1, (len(gallery_cgs) + 1) // 2)

    use game_menu("__cg_gallery_title", scroll="viewport"):

        grid 2 gallery_rows:
            spacing 30
            xalign 0.5

            for cg in gallery_cgs:
                button:
                    xsize 500
                    ysize 375
                    
                    if cg["id"] in gallery_unlocked:
                        add Transform(cg["path"], fit="contain") xalign 0.5 yalign 0.5
                        action Call("view_cg", cg_path=cg["path"], cg_name=cg["name"])
                    else:
                        frame:
                            background "#1a1a1a"
                            xfill True
                            yfill True
                            text "？" xalign 0.5 yalign 0.5 size 80 color "#666666"
                        action NullAction()

            if len(gallery_cgs) % 2:
                null width 500 height 375


screen cg_view_display(cg_path, cg_name):

    modal True

    frame:
        background "#000000"
        xysize (1920, 1080)
        
        vbox:
            xalign 0.5
            yalign 0.5

            add cg_path xalign 0.5 yalign 0.5

        hbox:
            xalign 0.5
            yalign 1.0
            yoffset -40
            spacing 20

            textbutton _("关闭"):
                action Return()


## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for i, h in enumerate(_history_list):

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                if i < len(history_voice_paths) and history_voice_paths[i]:
                    text "🔊" style "history_voice"

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_voice is gui_text

style history_voice:
    xalign 0.95
    yalign 0.0
    size 28
    color "#a0a0ff"

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("键盘")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("上一页")
        text _("回退至先前的对话。")

    hbox:
        label _("下一页")
        text _("向前至后来的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://doc.renpy.cn/zh-CN/self_voicing.html}机器朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 16

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 500
    right_padding 40

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        background Frame("gui/confirm/frame.png")
        align (0.5, 0.5)
        padding (0, 0, 0, 0)

        vbox:
            xalign .5
            yalign .5
            spacing 45

            frame:
                background Frame("gui/confirm/message_bg.png", 10, 10)
                xalign 0.5
                xsize 750
                ysize 90
                padding (0, 0, 0, 0)

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5
                    yalign 0.5

            hbox:
                xalign 0.5
                spacing 35

                imagebutton:
                    action yes_action
                    auto "gui/confirm/yes_%s.png"
                    hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                    activate_sound "audio/界面点击音效/点击1.ogg"

                imagebutton:
                    action no_action
                    auto "gui/confirm/no_%s.png"
                    hover_sound "audio/界面点击音效/鼠标滑动.ogg"
                    activate_sound "audio/界面点击音效/点击1.ogg"

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 12

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## 对话气泡屏幕 ######################################################################
##
## 对话气泡屏幕用于以对话气泡的形式向玩家显示对话。对话气泡屏幕的参数与 say 屏幕
## 相同，必须创建一个 id 为 what 的可视控件，并且可以创建 id 为 namebox、who 和
## window 的可视控件。
##
## https://doc.renpy.cn/zh-CN/bubble.html#bubble-screen

#screen ctc(arg=None):

#    zorder 100

#    if arg:
#       add arg

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 900

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 680

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1740

style pref_vbox:
    variant "small"
    xsize 800

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 1200
