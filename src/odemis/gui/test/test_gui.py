# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcstream_frame(wx.Frame):
#!XRCED:begin-block:xrcstream_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcstream_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "stream_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.scrwin = xrc.XRCCTRL(self, "scrwin")
        self.fpb = xrc.XRCCTRL(self, "fpb")
        self.stream_bar = xrc.XRCCTRL(self, "stream_bar")



class xrctext_frame(wx.Frame):
#!XRCED:begin-block:xrctext_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrctext_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "text_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.text_panel = xrc.XRCCTRL(self, "text_panel")
        self.txt_suggest = xrc.XRCCTRL(self, "txt_suggest")
        self.txt_odcbox = xrc.XRCCTRL(self, "txt_odcbox")



class xrcbutton_frame(wx.Frame):
#!XRCED:begin-block:xrcbutton_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcbutton_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "button_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.button_panel = xrc.XRCCTRL(self, "button_panel")



class xrcslider_frame(wx.Frame):
#!XRCED:begin-block:xrcslider_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcslider_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "slider_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.slider_panel = xrc.XRCCTRL(self, "slider_panel")



class xrccairo_frame(wx.Frame):
#!XRCED:begin-block:xrccairo_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrccairo_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "cairo_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.cairo_panel = xrc.XRCCTRL(self, "cairo_panel")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    test_gui_xrc = '''\
<?xml version="1.0" ?><resource class="wxBoxSizer" version="2.5.3.0" xmlns="http://www.wxwidgets.org/wxxrc">
  <object class="wxFrame" name="stream_frame">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxScrolledWindow" name="scrwin">
          <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
              <object class="FoldPanelBar" name="fpb">
                <object class="FoldPanelItem">
                  <label>STREAMS</label>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                  <object class="StreamBar" name="stream_bar">
                    <add_button>1</add_button>
                    <XRCED>
                      <assign_var>1</assign_var>
                    </XRCED>
                  </object>
                </object>
                <spacing>0</spacing>
                <leftspacing>0</leftspacing>
                <rightspacing>0</rightspacing>
                <bg>#4D4D4D</bg>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
              <flag>wxEXPAND</flag>
            </object>
          </object>
          <bg>#A52A2A</bg>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxEXPAND</flag>
        <minsize>400,400</minsize>
      </object>
    </object>
    <size>400,400</size>
    <title>Stream panel test frame</title>
  </object>
  <object class="wxFrame" name="text_frame">
    <object class="wxPanel" name="text_panel">
      <object class="wxBoxSizer">
        <object class="sizeritem">
          <object class="SuggestTextCtrl" name="txt_suggest">
            <size>200,-1</size>
            <value>suggest text field</value>
            <fg>#1E90FF</fg>
            <bg>#A52A2A</bg>
            <style>wxBORDER_NONE</style>
            <XRCED>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <option>0</option>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitIntegerCtrl">
            <size>200,-1</size>
            <value>9</value>
            <min>-10</min>
            <max>10</max>
            <unit>cm</unit>
            <fg>#1E90FF</fg>
            <bg>#A52A2A</bg>
            <style>wxBORDER_NONE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitIntegerCtrl">
            <size>200,-1</size>
            <value>0</value>
            <min>-10</min>
            <max>10</max>
            <unit>μm</unit>
            <fg>#1E90FF</fg>
            <bg>#A52A2A</bg>
            <style>wxBORDER_NONE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="UnitFloatCtrl">
            <size>200,-1</size>
            <value>4.44</value>
            <unit>kg</unit>
            <fg>#1E90FF</fg>
            <bg>#A52A2A</bg>
            <style>wxBORDER_NONE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <orient>wxVERTICAL</orient>
        <object class="sizeritem">
          <object class="wxOwnerDrawnComboBox" name="txt_odcbox">
            <size>200,14</size>
            <content>
              <item>aap</item>
              <item>noot</item>
              <item>mies</item>
            </content>
            <selection>1</selection>
            <fg>#1E90FF</fg>
            <bg>#A52A2A</bg>
            <style>wxBORDER_NONE|wxCB_READONLY</style>
            <XRCED>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="ImageTextToggleButton">
            <label>amaai</label>
            <bitmap>___img_btn_64x48_png</bitmap>
            <hover>___img_btn_64x48_h_png</hover>
            <selected>___img_btn_64x48_a_png</selected>
            <fg>#1A1A1A</fg>
            <style>wxALIGN_CENTRE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="ImageTextToggleButton">
            <label>amaai</label>
            <bitmap>___img_btn_64x24_png</bitmap>
            <hover>___img_btn_64x24_h_png</hover>
            <selected>___img_btn_64x24_a_png</selected>
            <fg>#1A1A1A</fg>
            <style>wxALIGN_CENTRE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
        <object class="sizeritem">
          <object class="ImageTextToggleButton">
            <label>allez</label>
            <bitmap>___img_btn_64x16_png</bitmap>
            <hover>___img_btn_64x16_h_png</hover>
            <selected>___img_btn_64x16_a_png</selected>
            <fg>#1A1A1A</fg>
            <style>wxALIGN_CENTRE</style>
          </object>
          <flag>wxALL|wxALIGN_CENTRE</flag>
          <border>10</border>
        </object>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#A52A2A</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
  </object>
  <object class="wxFrame" name="button_frame">
    <object class="wxPanel" name="button_panel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#A52A2A</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
  </object>
  <object class="wxFrame" name="slider_frame">
    <object class="wxPanel" name="slider_panel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#A52A2A</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
  </object>
  <object class="wxFrame" name="cairo_frame">
    <object class="wxPanel" name="cairo_panel" subclass="test_cairo.CairoPanel">
      <size>400,400</size>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
    <title>Cairo Test</title>
  </object>
</resource>'''

    ___img_btn_64x48_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x000\x08\x06\x00\x00\x00\xa1\
K|\x1f\x00\x00\x00\xe3IDATh\xde\xed\xda=
\xc20\x18\xc6\xf1\x90\xc1\x1b8y<\x8f\xa1 \x82\xb37\x10<H\xc7\x0e=H
\xa5\xdd\x13\xe8W\xcc#\xea\xe0\x11\xfa\xfe\x03\x0f\x14:=?\xf2&\x1d\xea\
\xab\xaa\xda\xd5u}k\x9a&\x94d#\x09\xea\xac\xee~Y\x96kJ\xe9\xd4\xf7\xfd\xa1\
m[\x17B\xd8t\xd4Q]\xd5Y\xdd}y8\xc6\x18\xdd8\x8e.\xe7\xec\xb6\xbe\xd4Q]\xd5\
Y\xdd\xfd<\xcf\xfbi\x9a\xde/,E\x9d\xd5\xdd\xaf\xeb\xea\x14k\x00\xdf\xde\
\xde\x19_\xbf\x1d`5\xec\x00k\xb3\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\
\xc00\x80\xf9OaF\x00\x00\x00\x00\xe0\x16\xe0\x16`\x04\x00\x00\x80C\x90C\
\x90\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\xc0
\x00?I\xe5<\x18\xde\x01\x83\x00\x1e\x86\x01\x9e\x1a\x81K\xc9\xbd\xa43\xb4\
\xf3\xbbO\xe7\xf3\x0b\x85s@;\xac\xd7\x8e\xb9\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x48_h_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x000\x08\x06\x00\x00\x00\xa1\
K|\x1f\x00\x00\x00\xe4IDATh\xde\xed\x9a\xbd\x0d\xc20\x18D-\x17l@\xc5x\x8c\
\x01\x12B\xa2f\x03$\xf6Ie)#\xa4\x88\xe2\xc2\xad\xa3\xfc\x18\x1f"\x0d#\xe4\
{\x91\xaeJ\xf5\x9e|\xe7\xc6\xbei\x9aC\x08\xe1\xd1\xb6mWS\x8c\xa4\x13\xb3\
\xd8\xfd\xb2,\xf7\x9c\xf3%\xa5t\x8a1\xbaa\x18v\x1d1\x8aU\xccb\xf7\xe38\x9e\
k\xdc4M\xae\x94\xe2\xf6\xfe\x89Q\xacb\x16\xbbN\xc0q\x9e\xe7\xef\x0fK\x11\
\xb3\xd8\xfd\xba\xaeN\xb1&`\xe3\xf6\xd6\xc0\xff\x83\x00g\xfc\xe3\x04 \xc0\
\xba\x80\xed:\xb0\x1aN\x00\x02\x10\x80\x00n\x01n\x01*\x80\x006\xc0\xec\x06\
0\x82l\x00\x1b@\x05\xa8\x00\x15\xa0\x02T\x00\x01l\x00\x1b@\x05\x10\x80\x00\
\x04p\x0bp\x0bP\x01\x04\xf0D\x86\x272T\xc0\x96\x80hX@\x94\x80\x97a\x01o\
\x8d\xe0\xad\xe6Y\xd3\x1b\xda\xbe\xfe\xc7|\xfd\x00\x1a2

"`R\xa3\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x48_a_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x000\x08\x06\x00\x00\x00\xa1\
K|\x1f\x00\x00\x01\x1bIDATh\xde\xed\x98A\x8a\x83P\x10D\xdbF\xe2J\x10A\x04\
G]\xe9\x05\\x\xa1\x1cc\x06\x86\x81Y\xcf\x0d\x06\xe6pY\x04r\x04\xd1\x9f_\
!\xd9$0\x07\xb0\xaa\xa1\x16\xf9\x8a\xee\xeaV\x1f\x86\xe1\x10\xf5\x1du\x8a
$:\xdd\x99\x0f\x9e\xa6\xe9W\x9e\xe7\xefu]\xbf\xc5\xb2\xb6mw-0\x82\x15\xcc\
`\xf7\xb2,\x8f\xe38\xda4M6\xcf3\x85\xc0
f\xb0{\xd7u\x15\x1e}\xdf[\xd34\x14\x02+\x98\xc1\xeeUUYQ\x14\x16\xdb\xc1\
P!\x84]\x0b\x05V0\x83\xdd\xb3,3w\xdf=\xf8\xb3\xc0|c\x87#I\x92\x18[=\x98\
\xdd\xc8\xcb\xd9Z\xffe\x14\x18\x82\xef\xbf@T\x07\xc8\x00\x19\xa0\x10\xe4\
\x0eA\xdd\x01\xec#\xb0m\x9b1K#\xa0-\xa0SX!\xc8\x1d\x82\xca\x00m\x81@\xdb\
\xfe\xfa\x18\x92\x012@\x06\xe8\x12\xa4_\x83\xba\x04\x95\x01\xba\x04\xd5\
\x01\xfa\x1f\xa0CH\x06\xc8\x00\xadA\xd65\xa8;@#\xa0;\xe0B\xdc\x01\x17\x18\
\xf0\xcb:\xff\x91\xfd\xcf\x97e\xf9\\\xd7\xf5\x27\xbe\xcfD\xecg0G\xf6\x8f\
+\x0d\xb1"$\xa9\x8a`\x0c\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x24_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x18\x08\x06\x00\x00\x00J\
\xb4\xfbD\x00\x00\x00\xbeIDATX\xc3\xed\x98\xb1\x09\xc30\x10E\xc5\x15\xd9\
 U\xc6\xcb\x18\x09\x84@\xeal\x10\xc8 *]x\x10\x19\x8c\xdd\xdaX\xd8Xg}\x88\
!x\x04\xdd/^\xa3\xee=\x9d$\x90x\xefOUU\xbd\xea\xba\x0e\x195B\x803\xdce]\
\xd7\xe74M\xb7\xae\xeb.M\xd3\xb8\x10B\xd1\xc0\x11\xaep\x86\xbb\x8c\xe3x\
\x1d\x86\xc1\xc5\x18]^p)\xa5\xa2\x81#\\\xe1\x0cwY\x96\xe5<\xcfs\xf1\xe2\
G\xe0\x0cw\xd9\x17T\xd5\x14\xbb\xb7X\xdb\xf9#\x0c\xc0\x00\xd6\x03\xe0Y\xb0\
\x0c\x27\x80G\x80G\x80\x13\xc0\x09\xe0%\xc8\x00\x0c\xc0\x00\x0c`8@o8@/\xaa\
\xfa\xb1\xf6\x1b\xf4\xc7\x17\x13\xf0\xc8\xbc3\xad\xa1\x9do\xce\xf7\x0d\
\xd2(\xe7*\xb4/U\x08\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x24_h_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x18\x08\x06\x00\x00\x00J\
\xb4\xfbD\x00\x00\x00\xc3IDATX\xc3\xed\x98\xb1\x09\xc30\x10E\x8f+\xb2A\xaa\
\x8c\x971\x12\x08\x81\xd4\xd9 \x90}\\\x09<\x82\x0bc\x15*ec\xc9\x97\xfb`\
C\xf0\x08\xbe+^\xa3\xeeI\xff\x9f\x84\xb8i\x9aS\x08\xe1\xd5\xb6m\xa7\x88\
\x11:8\xc3\x9dk\xad\xcfq\x1co)\xa5K\x8c\x91\x86a84p\x84+\x9c\xe1\xce9\xe7\
\xabB\xd34\x91.\xd0\xb2,\x87\x06\x8ep\x853\xdc\xb9\x94r\x9e\xe7\xf9\xf0\
\xe2{\xe0\x0cw\xde\x16D\xc4\x14\x9b7[;\xf9=\x18\x82d\x19O\x80W\xc0+`<\x01\
z\x17\x92e<\x01\xe6g\x80\x0fA\xaf\x80\x27\xc0_\x82^\x01\xaf\x80\xe1\x04\
\x88H\xb4\xf6\x19\xf2GD\x02>\x86\x13\xf0\xc5\x06<\x94\xb7\xd2\x1b\x12\xef\
W\xe7\xfb\x0f4a\xf0\xea\xd0Hf\x10\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x24_a_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x18\x08\x06\x00\x00\x00J\
\xb4\xfbD\x00\x00\x00\xe8IDATX\xc3\xed\x941
\x83@\x10E\xc7Q\xb6\x13\x14\x0c\x82Ql<\x80\x857\xca1\x12\x08\x81\xd4\xb9\
A \x87\xb3\x10\xbc\x81\xa8\x9b\xfd!B\xba\xf4\xfe\x1dx\xc5\x96\xef\xef\xcc\
\xd7\xa6i\x8c\xe3\xee\xe8\x1d\x96\x84\xfe\xebl4\x8a\xa2[\x1c\xc7\xe7<\xcf\
\x8fn\xa4,\xcb]\x03G\xb8\xc2\x19\xee\x9a\xa6\xe9\xc9%!m\xdbJ\xd7u\x14\xc0\
\x15\xcep\xd7\xaa\xaa\x0ex\xd4u-EQP\x00W8\xc3]\xb3,\x93$I$\x0cC\xc1Xkw\x0d\
\x06\xaep\x86\xbb\x1ac$\x08\x02Y\xd7\x95
8\xc3]\xb7d\xd8\x02\xd8\xbc\x95Q\xfe7\x04\xdd\xfb\xcd\xffCY\xc3\x9f\xc0\
\xb2,\xc2\x8c\xef\x00\xac\x02\xeb\xef:\xc0\x97 {\x09\xfa\x0d`/A\x02\xec\
\x27@\x1f\x80\x88\x8c\xc2;#6\xe0I\xbc\x01/\x9d\xa6\xe9:\xcf\xf3\xc3\x15\
\xc2@\xd4\xfe\x03\x9c\x9d\xfb\xe5\x0d\xc1<\xb3O\x8b\xf8E\xb6\x00\x00\x00\
\x00IEND\xaeB`\x82'''

    ___img_btn_64x16_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x10\x08\x06\x00\x00\x00\xa6\
\xe7y)\x00\x00\x00\xa8IDATX\x09\xe5\xcf!
\x84\x00\x14E\xd1\x97\\\xb7\xc8\x8822\x06\xc1 \x18\x04A\x055\xd8D\x8c\x06\
\x17"\x08n\xe2\xcd\xffa61/\x9cr\xdb\xc5\xbe\xef\xc1q\x1c\xaf\xf3</C\x11\
\x97?\xfb;\xd6uM\xb6m\xe3\xb2,\x9c\xa6\x89\xe38\xfe5\xf4W\xf6wXx\xe6y\
\xe60\x0cR\xfc\xd9\xdf\xd1\xf7=]\xd7uR~\xdfh\xdb\x96\xca\xd04\x0d\x95\xa1\
\xaek*CUUT\x86\xb2,\xa9\x0cEQP\x19\xf2<\xa72dYFeH\xd3\x94\xca\x10\xc7\xf1\
c(\xeaA\x14E\x89\xa1\xa87\xc20\x0c\xcc\xc7\xdc\x86"\xfc\xd5\x9f\x83/\xd1\
_\x1b\x05\xb1\xa2\xee\xdc\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x16_h_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x10\x08\x06\x00\x00\x00\xa6\
\xe7y)\x00\x00\x00\xa7IDATX\x09\xe5\xcf!
\x84P\x00\x84\xe1I\x9e|AX\x10\xc4 \x18\x0c\x06\x83\xc1 \x18T\xd0`\x111\
\x09\x1eAX\xf0\x12\xb3o\xc2^bg\xe0+\xd3~\x1c\xc7\x11\x9d\xe7\xf9\xba\xae\
\xeb\x0eh\xe2V\xb3\xda\xb1m[\xbc\xef;\xd7u\xe5\xb2,\x9c\xe7\xf9\xaf\xa9\
Q\xadjV;\xc2\xf1\xe8\x9c\xa6\xc9\x8a\x9a\xd5\x8eq\x1c)\xc30X\xf9u\xa3\xef\
{:C\xd7ut\x86\xb6m\xe9\x0cM\xd3\xd0\x19\xea\xba\xa63TUEg(\xcb\x92\xceP\x14\
\x05\x9d!\xcfs:C\x96eO@S\x0f\xd24\x8d\x03\x9az#I\x92(\xd0>\x01M\xa8U\x8b\
\xbe1g\xd4-J\xc4\xa7\xc7\x00\x00\x00\x00IEND\xaeB`\x82'''

    ___img_btn_64x16_a_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00@\x00\x00\x00\x10\x08\x06\x00\x00\x00\xa6\
\xe7y)\x00\x00\x00\xdbIDATX\xc3\xed\xd51
\x83@\x10\x85\xe1q\x90\xed,\x14\x82\xe8\x8a\xcd\xda\xdbx\xa3\x1c#\x81\x10\
H\x9d\x1b\x04r8\x0b\xc1\x0b\x88\xa8\x9by\x12C\x8a\x9c\xc0I\xf17\xdb}\xb3\
\xb3,WUe\xa4\x9b\xd4J^I\xed\xdbl8\x0c\xc3k\x14E\xa74Mm\x9e\xe7d\xad\xdd\
u0\xc2
3\xec\x1c\xc7\xf1Q&Au]S\xd34*\x82\x15f\xd8\xb9(\x8a\x83s\x8e\xca\xb2\xa4\
,\xcbT\x04+\xcc\xb0s\x92$$\xeb@A\x10\xd0\xb2,4\xcf\xf3\xae\x83\x11V\x98\
agc\xcc\x07\xaf)\x98a\xe7\xed`\xef7\xffk\x13\x10k\xc4\x0f\x81\xb5\xe2\xb7\
\xd6\x01L\xd3\xa4\xb2u\x00\xff\x27\xa0\xfd\x09x\xef\xd5}\x81[\xb0c\x03z\
\xc5\x1b\xd0c\x03\x1e\x98\x84\xd2\x9e<\x0c\xc3e\x1c\xc7\xbbL\xa3St\xf3\x1d\
\xccb?\xbf\x00\x06\x94x\xf4\xde\xb3\xdf\x9a\x00\x00\x00\x00IEND\xaeB`\x82'''

    wx.MemoryFSHandler.AddFile('XRC/test_gui/test_gui_xrc', test_gui_xrc)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x48_png', ___img_btn_64x48_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x48_h_png', ___img_btn_64x48_h_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x48_a_png', ___img_btn_64x48_a_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x24_png', ___img_btn_64x24_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x24_h_png', ___img_btn_64x24_h_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x24_a_png', ___img_btn_64x24_a_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x16_png', ___img_btn_64x16_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x16_h_png', ___img_btn_64x16_h_png)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_btn_64x16_a_png', ___img_btn_64x16_a_png)
    __res.Load('memory:XRC/test_gui/test_gui_xrc')

