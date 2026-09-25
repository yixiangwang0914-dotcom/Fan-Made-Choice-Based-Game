

#play music "bgm/" loop fadein 5.0
#stop music fadeout 1.0


define eye = ImageDissolve(
    Transform("gui/eye.png", size=(1920, 1080)),
    2.0,
    ramplen=64
)
define ink1 = ImageDissolve(
    Transform("gui/ReInk.png"),
    2.0,
    ramplen=64
)

define ink2 = ImageDissolve(
    Transform("gui/ReInk2.png"),
    4.0,
    ramplen=64
)

define ink3 = ImageDissolve(
    Transform("gui/ReInk3.png"),
    2.0,
    ramplen=64
)

define ink4 = ImageDissolve(
    Transform("gui/Ink.png"),
    2.0,
    ramplen=64
)

define ink5 = ImageDissolve(
    Transform("gui/Ink2.png"),
    2.0,
    ramplen=64
)

define wipe = ImageDissolve(
    Transform("gui/wipe_right.png", size=(1920, 1080)),
    2.0,
    ramplen=64
)

define square = ImageDissolve(
    Transform("gui/square.png", size=(1920, 1080)),
    1.5,
    ramplen=64
)

define circle = ImageDissolve(
    Transform("gui/FadeCircle.png", size=(1920, 1080)),
    2.0,
    ramplen=64
)

transform bg_shake:
    subpixel True
    zoom 1.03
    xalign 0.5
    yalign 0.5
    xoffset 0
    yoffset 0
    linear 0.03 xoffset -18 yoffset 8
    linear 0.03 xoffset 16 yoffset -6
    linear 0.03 xoffset -12 yoffset 5
    linear 0.03 xoffset 10 yoffset -4
    linear 0.03 xoffset 0 yoffset 0
    linear 0.01 zoom 1.0

image thinking = Solid("#00000060", xysize=(1920, 1080))

label flashback1:

    window hide

    scene 红楼 梦
    pause 0.2 

    scene 红楼 妈
    pause 0.2 

    scene 红楼 粥
    pause 0.2 

    scene 红楼 背
    pause 0.2 

    scene 红楼 忘
    pause 0.2 

    scene 红楼 说
    pause 0.2 

    scene 红楼 门
    pause 0.2 

    scene 红楼 香
    pause 0.2 

    scene 红楼 病
    pause 0.2 

    scene 红楼 吐
    pause 0.2 

    scene 红楼 打
    pause 0.2 

    scene 红楼 悔
    pause 0.2 


    window show

    jump sc5


label flashback2:

    window hide

    scene 魂归黄泉
    with eye
    pause 0.2 

    scene 方疯
    pause 0.2 

    scene 方哭
    pause 0.2 

    scene 醉死
    pause 0.2 

    scene 红楼 吐
    pause 0.2 

    scene 红楼 打
    pause 0.2 


    window show

    jump sc8




image chapter_mask = "images/chapter_img_mask2.png"
image chapter_brush = "images/chapter_bg_Y.png"
image chapter_mask_1 = "二十四桥雨无血.png"
image chapter_brush2 = "images/chapter_bg_J.png"

image chapter_title = Text("追雁", size=90, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_title_2 = Text("雁归", size=90, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_title_3 = Text("引蝶", size=90, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_title_4 = Text("蝶化", size=90, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_title_5 = Text("归途", size=90, color="#ffffff", font="fonts/xiqueyanshu.ttf")

image chapter_subtitle = Text("记 第一章", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_subtitle_2 = Text("记 第二章", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_subtitle_3 = Text("记 第三章", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_subtitle_4 = Text("记 第四章", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")
image chapter_subtitle_5 = Text("记 第五章", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")


image chapter_year = Text("1641 崇祯十四年", size=36, color="#ffffff", font="fonts/xiqueyanshu.ttf")

image chapter_image1 = "images/chapter_img1.png"

transform full_screen:
    xysize (1920, 1080)

transform chapter_title_pos:
    xalign 0.24
    ypos 0.4

transform chapter_subtitle_pos:
    xalign 0.13
    ypos 0.428

transform chapter_year_pos:
    xalign 0.40
    ypos 0.43

transform chapter_title_enter:  #重要主标题滑动展示
    xalign -0.2
    ypos 0.4
    linear 1.3 xalign 0.24

transform chapter_subtitle_enter:     #重要副标题滑动展示
    xalign -0.2
    ypos 0.428
    linear 1.3 xalign 0.13

transform chapter_year_enter:     #重要时间标题滑动展示
    xalign -0.2
    ypos 0.43
    linear 1.3 xalign 0.40

transform chapter_scene_pos:
    xpos 0
    ypos 0
    #xysize (640, 900)

transform chapter_brush_pos:
    xpos 0
    ypos 0

label chapter_template_1(bg_image):
    window hide
    show expression bg_image at full_screen  #自己放的图片
    show chapter_image1 at chapter_scene_pos    #章节蒙版
    show chapter_title at chapter_title_enter      #主标题
    show chapter_subtitle at chapter_subtitle_enter  #副标题
    show chapter_year at chapter_year_enter    #时间
    with Dissolve(1.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return

label chapter_template_0(bg_image):
    window hide
    scene black
    pause 1.0
    show expression bg_image at full_screen  #自己放的图片
    with Dissolve(3.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return

label chapter_template_2(bg_image):
    window hide
    show expression bg_image at full_screen  #自己放的图片
    show chapter_image1 at chapter_scene_pos    #章节蒙版
    show chapter_title_2 at chapter_title_enter
    show chapter_subtitle_2 at chapter_subtitle_enter
    show chapter_year at chapter_year_enter
    with Dissolve(1.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return

label chapter_template_3(bg_image):
    window hide
    show expression bg_image at full_screen  #自己放的图片
    show chapter_image1 at chapter_scene_pos    #章节蒙版
    show chapter_title_3 at chapter_title_enter
    show chapter_subtitle_3 at chapter_subtitle_enter
    show chapter_year at chapter_year_enter
    with Dissolve(1.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return

label chapter_template_4(bg_image):
    window hide
    show expression bg_image at full_screen  #自己放的图片
    show chapter_image1 at chapter_scene_pos    #章节蒙版
    show chapter_title_4 at chapter_title_enter
    show chapter_subtitle_4 at chapter_subtitle_enter
    show chapter_year at chapter_year_enter
    with Dissolve(1.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return

label chapter_template_5(bg_image):
    window hide
    show expression bg_image at full_screen  #自己放的图片
    show chapter_image1 at chapter_scene_pos    #章节蒙版
    show chapter_title_5 at chapter_title_enter
    show chapter_subtitle_5 at chapter_subtitle_enter
    show chapter_year at chapter_year_enter
    with Dissolve(1.0)
    pause 3.0
    scene black with Dissolve(1.0)
    return
#

#image chapter_scene_1 = "二十四桥雨无血.png"

